(function () {
  function isFiniteNumber(v) {
    return typeof v === "number" && Number.isFinite(v);
  }

  function flattenValues(datasets) {
    var out = [];
    for (var i = 0; i < datasets.length; i++) {
      var data = (datasets[i] && datasets[i].data) || [];
      for (var j = 0; j < data.length; j++) {
        var n = Number(data[j]);
        if (isFiniteNumber(n)) out.push(n);
      }
    }
    return out;
  }

  function LiteChart(ctxOrCanvas, config) {
    this.ctx = ctxOrCanvas && ctxOrCanvas.canvas ? ctxOrCanvas : ctxOrCanvas.getContext("2d");
    this.canvas = this.ctx.canvas;
    this.type = (config && config.type) || "line";
    this.data = (config && config.data) || { labels: [], datasets: [] };
    this.options = (config && config.options) || {};

    this._onResize = this.update.bind(this);
    window.addEventListener("resize", this._onResize);
    this.update();
  }

  LiteChart.prototype._resizeCanvas = function () {
    var canvas = this.canvas;
    var rect = canvas.getBoundingClientRect();
    var width = Math.max(320, Math.floor(rect.width || (canvas.parentElement && canvas.parentElement.clientWidth) || 800));
    var height = Math.max(180, Math.floor(rect.height || (canvas.parentElement && canvas.parentElement.clientHeight) || 260));
    var dpr = window.devicePixelRatio || 1;

    if (canvas.width !== Math.floor(width * dpr) || canvas.height !== Math.floor(height * dpr)) {
      canvas.width = Math.floor(width * dpr);
      canvas.height = Math.floor(height * dpr);
      this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    return { width: width, height: height };
  };

  LiteChart.prototype._drawAxes = function (ctx, area, xTitle, yTitle) {
    ctx.save();
    ctx.strokeStyle = "#BFC5D2";
    ctx.lineWidth = 1;

    ctx.beginPath();
    ctx.moveTo(area.left, area.bottom);
    ctx.lineTo(area.right, area.bottom);
    ctx.moveTo(area.left, area.top);
    ctx.lineTo(area.left, area.bottom);
    ctx.stroke();

    ctx.fillStyle = "#5f6368";
    ctx.font = "12px system-ui, -apple-system, Segoe UI, Arial";

    if (xTitle) {
      var tw = ctx.measureText(xTitle).width;
      ctx.fillText(xTitle, area.left + (area.right - area.left - tw) / 2, area.bottom + 24);
    }
    if (yTitle) {
      ctx.save();
      ctx.translate(area.left - 34, area.top + (area.bottom - area.top) / 2);
      ctx.rotate(-Math.PI / 2);
      ctx.fillText(yTitle, -ctx.measureText(yTitle).width / 2, 0);
      ctx.restore();
    }

    ctx.restore();
  };

  LiteChart.prototype._drawGrid = function (ctx, area, yMin, yMax) {
    ctx.save();
    ctx.strokeStyle = "#E6E9F0";
    ctx.fillStyle = "#8B93A6";
    ctx.lineWidth = 1;
    ctx.font = "11px system-ui, -apple-system, Segoe UI, Arial";

    var ticks = 5;
    for (var i = 0; i <= ticks; i++) {
      var ratio = i / ticks;
      var y = area.bottom - ratio * (area.bottom - area.top);
      var val = yMin + ratio * (yMax - yMin);

      ctx.beginPath();
      ctx.moveTo(area.left, y);
      ctx.lineTo(area.right, y);
      ctx.stroke();

      var label = val.toFixed(2);
      ctx.fillText(label, area.left - ctx.measureText(label).width - 8, y + 4);
    }

    ctx.restore();
  };

  LiteChart.prototype._drawLine = function (ctx, area, points, color) {
    if (!points.length) return;

    ctx.save();
    ctx.strokeStyle = color || "#1A73E8";
    ctx.lineWidth = 1.5;
    ctx.beginPath();

    for (var i = 0; i < points.length; i++) {
      var p = points[i];
      if (i === 0) ctx.moveTo(p.x, p.y);
      else ctx.lineTo(p.x, p.y);
    }

    ctx.stroke();
    ctx.restore();
  };

  LiteChart.prototype._drawLegend = function (ctx, datasets, area) {
    ctx.save();
    ctx.font = "12px system-ui, -apple-system, Segoe UI, Arial";

    var x = area.left;
    var y = area.top - 10;

    for (var i = 0; i < datasets.length; i++) {
      var ds = datasets[i] || {};
      var label = ds.label || "Data " + (i + 1);
      var color = ds.borderColor || "#1A73E8";

      ctx.fillStyle = color;
      ctx.fillRect(x, y - 8, 10, 10);

      ctx.fillStyle = "#4B5563";
      ctx.fillText(label, x + 14, y);
      x += 14 + ctx.measureText(label).width + 14;

      if (x > area.right - 120) {
        x = area.left;
        y += 16;
      }
    }

    ctx.restore();
  };

  LiteChart.prototype.update = function () {
    var ctx = this.ctx;
    var size = this._resizeCanvas();
    var width = size.width;
    var height = size.height;

    ctx.clearRect(0, 0, width, height);

    var labels = (this.data && this.data.labels) || [];
    var datasets = (this.data && this.data.datasets) || [];

    var xTitle = this.options && this.options.scales && this.options.scales.x && this.options.scales.x.title && this.options.scales.x.title.text;
    var yTitle = this.options && this.options.scales && this.options.scales.y && this.options.scales.y.title && this.options.scales.y.title.text;

    var area = {
      left: 56,
      top: 38,
      right: width - 16,
      bottom: height - 36
    };

    if (area.right <= area.left || area.bottom <= area.top) return;

    var values = flattenValues(datasets);
    var yMin = values.length ? Math.min.apply(null, values) : 0;
    var yMax = values.length ? Math.max.apply(null, values) : 1;

    if (yMin === yMax) {
      yMin -= 1;
      yMax += 1;
    }

    var pad = (yMax - yMin) * 0.12;
    yMin -= pad;
    yMax += pad;

    this._drawAxes(ctx, area, xTitle, yTitle);
    this._drawGrid(ctx, area, yMin, yMax);
    this._drawLegend(ctx, datasets, area);

    var n = Math.max(labels.length, 1);

    for (var i = 0; i < datasets.length; i++) {
      var ds = datasets[i] || {};
      var data = ds.data || [];
      var points = [];

      for (var j = 0; j < data.length; j++) {
        var v = Number(data[j]);
        if (!isFiniteNumber(v)) continue;

        var xr = n > 1 ? j / (n - 1) : 0;
        var yr = (v - yMin) / (yMax - yMin);

        points.push({
          x: area.left + xr * (area.right - area.left),
          y: area.bottom - yr * (area.bottom - area.top)
        });
      }

      this._drawLine(ctx, area, points, ds.borderColor);
    }
  };

  LiteChart.prototype.destroy = function () {
    window.removeEventListener("resize", this._onResize);
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
  };

  window.Chart = LiteChart;
})();
