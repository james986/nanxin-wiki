# 宏用法说明：
# - pdf_line(href, title=None, size="56px")
#   示例：{{ pdf_line("/uart-servo/datasheet/pdf/HA8-U25-M.pdf", "HA8-U25-M", "48px") }}
#   【作用】渲染“分隔线 + PDF 图标下载块”。
#   参数说明：
#     - 第 1 个参数：PDF 地址（用相对路径./pdf/xxx.pdf）
#     - 第 2 个参数：title（鼠标悬停提示）
#     - 第 3 个参数：尺寸（我固定了 48px，不要动先）
#
# - fig_center(src, caption, width="500px")
#   示例：{{ fig_center("/uart-servo/datasheet/image/U25特性曲线.png", "T-N 特性曲线", "500px") }}
#   【作用】渲染“居中图片 + 标题说明”块。
#   参数说明：
#    - 第 1 个参数：图片地址（用相对路径./images/xxx.png）
#    - 第 2 个参数：图片标题说明
#    - 第 3 个参数：图片宽度（不要动）
#
# - fig_indent(src, alt, offset="3em")
#   示例：{{ fig_indent("/uart-servo/software/images/xxx.png", "软件界面", "3em") }}
#   【作用】渲染“与正文缩进对齐的图片”块（右侧满幅，左侧按 offset 缩进）。主要用于软件界面截图等。
#   参数说明：
#     - 第 1 个参数：图片地址（用相对路径./images/xxx.png）
#     - 第 2 个参数：图片替代文字（alt）
#     - 第 3 个参数：左侧缩进（默认 3em）
#
# - fig_indent_adjustable(src, alt, width="50%", offset="3em")
#   示例：{{ fig_indent_adjustable("/uart-servo/software/images/xxx.png", "局部截图", "50%", "3em") }}
#   【作用】渲染“与正文缩进对齐 + 宽度可调 + 带边框”的图片块。适合竖图、局部截图、需要手动统一视觉大小的图片。
#   参数说明：
#     - 第 1 个参数：图片地址（用相对路径./images/xxx.png）
#     - 第 2 个参数：图片替代文字（alt）
#     - 第 3 个参数：图片显示宽度比例或尺寸（如 50% / 100% / 36rem）
#     - 第 4 个参数：左侧缩进（默认 3em）
#
# - github_download_table(protocol, version, github_url, download_url, icon_size="28px")
#   示例：{{ github_download_table("UART/RS-485 全系列", "v1.1.9.286", "https://github.com/servodevelop/servo-uart-rs485-sdk", "./data/Develop-US-1.1.9.286.zip", "28px") }}
#   【作用】渲染“软件信息与下载”表格（GitHub 图标链接 + 下载按钮）。
#   参数说明：
#     - 第 1 个参数：protocol，适用协议文字
#     - 第 2 个参数：version，当前版本
#     - 第 3 个参数：github_url，GitHub 仓库地址
#     - 第 4 个参数：download_url，下载链接地址（用相对路径./data/xxx.zip）
#     - 第 5 个参数：icon_size，图标尺寸（默认 28px）

from pathlib import Path
from markupsafe import Markup, escape


def _css_size(size):
    if size is None:
        return "56px"
    if isinstance(size, (int, float)):
        return f"{int(size)}px"
    return str(size)

def _size_attr(size_css):
    if isinstance(size_css, str) and size_css.endswith("px"):
        return size_css[:-2]
    return size_css


def define_env(env):
    site_dir = str(env.conf.get("site_dir", "site")).replace("\\", "/")
    site_dir_parts = [p for p in site_dir.split("/") if p]
    base_prefix = ""
    if "site" in site_dir_parts:
        idx = site_dir_parts.index("site")
        if idx + 1 < len(site_dir_parts):
            base_prefix = "/" + "/".join(site_dir_parts[idx + 1 :])

    @env.macro
    def pdf_line(href, title=None, size="56px"):
        size_css = _css_size(size)
        safe_href = escape(href)
        title_attr = f' title="{escape(title)}"' if title else ""
        return Markup(
            f'''
<div style="--pdf-size:{size_css}; display: flex; align-items: center; gap: 16px; margin: -16px 0 12px;">
  <div style="flex: 1; height: 1px; background-color: var(--md-default-fg-color--lighter); opacity: 0.5; transform: scaleY(0.5); transform-origin: center;"></div>
  <a href="{safe_href}" download{title_attr} style="display: inline-flex; align-items: center; justify-content: center; width: var(--pdf-size); height: var(--pdf-size); padding: 0; background: transparent; border: 0; box-shadow: none; text-decoration: none; outline: none;">
    <img src="/assets/icons/pdf.svg" alt="PDF" style="width: 100%; height: 100%; display: block; border: none !important; box-shadow: none !important; outline: none !important; background: transparent !important; border-radius: 0 !important; cursor: pointer !important; transition: transform 0.2s ease;" onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 4px 10px rgba(0,0,0,.12)';" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none';">
  </a>
</div>
'''
        )

    @env.macro
    def fig_center(src, caption, width="500px"):
        width_css = _css_size(width)
        safe_src = escape(src)
        safe_caption = escape(caption)
        return Markup(
            f'''
<div style="text-align: center; margin-bottom: 20px;">
  <img src="{safe_src}"
       style="width: {width_css} !important; height: auto !important; display: inline-block;">
  <div style="margin-top: 10px; font-weight: bold; font-size: 14px;">
    {safe_caption}
  </div>
</div>
'''
        )

    @env.macro
    def fig_indent(src, alt, offset="3em"):
        offset_css = str(offset) if offset is not None else "3em"
        safe_src = escape(src)
        safe_alt = escape(alt)
        return Markup(
            f'''
<div style="margin: 12px 0; box-sizing: border-box; text-align: right; width: calc(100% - {offset_css}); margin-left: {offset_css};">
  <img src="{safe_src}" alt="{safe_alt}" style="display: block !important; width: 100% !important; max-width: none !important; height: auto !important; margin-left: auto !important; margin-right: 0 !important;">
</div>
'''
        )

    @env.macro
    def fig_indent_adjustable(src, alt, width="50%", offset="3em"):
        offset_css = str(offset) if offset is not None else "3em"
        width_css = _css_size(width)
        safe_src = escape(src)
        safe_alt = escape(alt)
        is_full_width = width_css.strip() == "100%"
        outer_margin = "0" if is_full_width else "12px 0"
        outer_align = "right" if is_full_width else "left"
        inner_wrapper_open = (
            '<div style="display: inline-block; vertical-align: top; padding: 0; line-height: 0; '
            'font-size: 0; border: 0; box-shadow: none; outline: none; background: transparent; overflow: hidden;">'
            if is_full_width
            else ""
        )
        inner_wrapper_close = "</div>" if is_full_width else ""
        img_width = "100%" if is_full_width else width_css
        img_max_width = "none" if is_full_width else "100%"
        img_margin = (
            "margin: 0 !important;"
            if is_full_width
            else "margin-left: 0 !important; margin-right: auto !important;"
        )
        return Markup(
            f'''
<div style="margin: {outer_margin}; box-sizing: border-box; text-align: {outer_align}; width: calc(100% - {offset_css}); margin-left: {offset_css};">
  {inner_wrapper_open}
    <img src="{safe_src}" alt="{safe_alt}" style="display: block !important; width: {img_width} !important; max-width: {img_max_width} !important; height: auto !important; {img_margin} border: 1px solid var(--md-default-fg-color--lighter) !important; box-shadow: none !important; outline: none !important; vertical-align: top; padding: 0 !important; background: transparent !important; box-sizing: border-box !important;">
  {inner_wrapper_close}
</div>
'''
        )

    @env.macro
    def github_download_table(protocol, version, github_url, download_url, icon_size="28px"):
        size_css = _css_size(icon_size)
        size_attr = _size_attr(size_css)
        safe_version = escape(version)
        safe_github = escape(github_url)
        safe_download = escape(download_url)
        github_icon_html = (
            f'<a href="{safe_github}" title="GitHub 仓库" aria-label="GitHub" '
            f'style="display:inline-flex;align-items:center;justify-content:center;vertical-align:middle;'
            f'width:{size_css};height:{size_css};line-height:0;transition:transform 0.15s ease, box-shadow 0.15s ease;'
            f'border-radius:6px;" onmouseover="this.style.transform=\'translateY(-2px)\';this.style.boxShadow=\'0 4px 10px rgba(0,0,0,.12)\';" '
            f'onmouseout="this.style.transform=\'translateY(0)\';this.style.boxShadow=\'none\';"><img src="/assets/icons/github.svg" '
            f'data-light="/assets/icons/github.svg" data-dark="/assets/icons/github-dark.svg" width="{size_attr}" height="{size_attr}" '
            f'alt="GitHub" style="display:block;width:{size_css} !important;height:{size_css} !important;max-width:{size_css} !important;'
            f'max-height:{size_css} !important;" onload="(function(img){{var root=document.documentElement;var body=document.body;'
            f'var getScheme=function(){{var s=\'\';try{{var p=localStorage.getItem(\'__palette\');if(p){{var obj=JSON.parse(p);'
            f'if(obj&&obj.color&&obj.color.scheme){{s=obj.color.scheme;}}}}}}catch(e){{}}if(!s){{s=root.getAttribute(\'data-md-color-scheme\');}}'
            f'if(!s&&body){{s=body.getAttribute(\'data-md-color-scheme\');}}if(!s){{s=root.dataset.mdColorScheme;}}if(!s&&body){{s=body.dataset.mdColorScheme;}}'
            f'return s;}};var isDark=function(){{var s=getScheme();var dark=false;if(s===\'slate\'){{dark=true;}}else if(s===\'dark\'){{dark=true;}}'
            f'if(!s&&window.matchMedia){{dark=window.matchMedia(\'(prefers-color-scheme: dark)\').matches;}}return dark;}};'
            f'var setSrc=function(){{var target=isDark()?img.dataset.dark:img.dataset.light;if(img.getAttribute(\'src\')!==target){{img.setAttribute(\'src\',target);}}}};'
            f'setSrc();if(!img._fsObservers&&window.MutationObserver){{var list=[];var makeObs=function(node){{if(!node){{return;}}'
            f'var obs=new MutationObserver(function(){{setSrc();}});obs.observe(node,{{attributes:true,attributeFilter:[\'data-md-color-scheme\']}});'
            f'list.push(obs);}};makeObs(root);makeObs(body);img._fsObservers=list;}}if(window.matchMedia){{var mq=window.matchMedia(\'(prefers-color-scheme: dark)\');'
            f'if(mq.addEventListener){{mq.addEventListener(\'change\',setSrc);}}else if(mq.addListener){{mq.addListener(setSrc);}}}}}})(this)"></a>'
        )

        # protocol 为空时输出三列表格（版本 / GitHub / 下载）
        if protocol is None or str(protocol).strip() == "":
            return Markup(
                f'''
| 版本 | GitHub | 开发资源包 |
| :---: | :---: | :---: |
| <span class="no-wrap">{safe_version}</span> | {github_icon_html} | [点击下载]({safe_download}){{ .fs-download-btn }} |
'''
            )

        safe_protocol = escape(protocol)
        return Markup(
            f'''
| 适用协议 | 版本 | GitHub | 开发资源包 |
| :---: | :---: | :---: | :---: |
| <span class="no-wrap">{safe_protocol}</span> | <span class="no-wrap">{safe_version}</span> | {github_icon_html} | [点击下载]({safe_download}){{ .fs-download-btn }} |
'''
        )
