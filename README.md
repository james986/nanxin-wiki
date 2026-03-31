# 南芯微 Wiki 脚手架

这个目录已经整理成一个可独立迁走的新仓库骨架，适合直接用于 `南芯微-wiki` 首版建设。

## 当前状态

- 已改为中文单站配置，入口文件为 `mkdocs.yml`
- 已保留现有 MkDocs Material 主题、首页模板、自定义样式和 Markdown hook
- 已改为单站 GitHub Pages 部署工作流
- 已移除双语站部署流程、语言切换器、统计与旧站社交入口
- 已将首页改成新项目占位文案

## 使用步骤

1. 在 GitHub 新建一个空仓库。
2. 将本目录全部内容复制到新仓库根目录。
3. 当前仓库地址和 Pages 地址已经预填为：
   - `https://james986.github.io/nanxin-wiki/`
   - `https://github.com/james986/nanxin-wiki`
4. 本地验证构建：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs build -f mkdocs.yml
```

5. 推送到 GitHub 主分支。
6. 进入 GitHub 仓库设置：
   - `Settings -> Pages`
   - `Build and deployment` 选择 `GitHub Actions`
7. 等待 `.github/workflows/deploy.yml` 执行完成，然后访问站点。

## 建议的删减顺序

1. 先确认保留栏目清单
2. 先删 `mkdocs.yml` 里的 `nav`
3. 再删除 `docs_zh/` 中对应文档和资源
4. 最后清理首页入口、交叉链接和品牌信息

## 已知情况

- 当前正文内容仍大量保留原模板资料，后续需要按栏目逐步删减。
- 部分正文、数据文件和下载资源里仍包含原品牌或原外链，这一轮没有做全站替换。
- 若后续改为自定义域名，需要同时更新 `mkdocs.yml` 中的 `site_url`。
