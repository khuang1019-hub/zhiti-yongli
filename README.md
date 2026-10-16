# 智体用例

面向中国企业的智能体真实落地目录

静态站 MVP：企业智能体真实落地用例目录 + 周刊意向占位 +「废标速查」最小 Demo。

## 本地预览

无需构建工具。任选其一：

```bash
# 方式 A：Python
cd /workspace/zhiti-yongli
python3 -m http.server 8765
# 浏览器打开 http://127.0.0.1:8765/

# 方式 B：直接打开
# 用浏览器打开 index.html（部分浏览器对 fetch 本地 JSON 有限制，Demo 建议用方式 A）
```

可预览入口：

| 页面 | 路径 |
|------|------|
| 首页 | `index.html` |
| 用例目录 | `cases/index.html` |
| 单条用例 | `cases/<id>.html` |
| 废标速查 Demo | `demo/feibiao.html` |
| 关于 | `about.html` |

当前用例数：**18**

## 重新生成页面

用例数据在 `build.py` 与 `data/cases.json`。修改 `build.py` 中 `CASES` 后：

```bash
python3 build.py
```

## 部署到 Vercel

1. 将本目录推到 GitHub 仓库（可只推 `zhiti-yongli/` 为仓库根，或配置 Root Directory）。
2. [vercel.com](https://vercel.com) Import 该仓库。
3. Framework Preset 选 **Other**；Build Command 留空；Output Directory 填 `.`（若仓库根即本站）。
4. Deploy 后绑定域名。

## 部署到 GitHub Pages

1. 仓库 Settings → Pages → Source: Deploy from branch。
2. Branch 选 `main`，folder `/ (root)` 或 `/docs`（若你把静态文件放进 docs）。
3. 若站点在子目录，注意 `cases/`、`assets/` 相对路径已按相对链接写好，一般可直接用。

也可使用 Action `peaceiris/actions-gh-pages` 发布。

## 站名

正式采用：**智体用例**（候选「Agent用例港」未采用，因中英混排较长）。

副标题：面向中国企业的智能体真实落地目录

## milo 运维清单草稿

### 每日（约 15–30 分钟）

- [ ] 扫一遍微信公众号 / 厂商博客 / IDC·信通院转载，是否有新的可溯源 Agent 案例
- [ ] 检查站点与 Demo 页是否可打开（若已部署：生产 URL 探活）
- [ ] 回复赞助 / 投稿意向（若邮箱或表单已接通）

### 每周（约 1–2 小时）

- [ ] 新增 ≥1 条合格用例（有 URL、字段齐全）；更新 `build.py` → 跑生成 → 部署
- [ ] 写周刊草稿：3 条精选 + 1 条踩坑/风险（Klarna 类「回潮」也可写）
- [ ] 抽查 2 条旧用例链接是否失效
- [ ] 废标 Demo：收集 1 份真实公开招标 PDF 做回归（仍标注人工复核）
- [ ] 看赞助位询盘，更新定价占位文案

### 双周 / MVP 后

- [ ] 接入真实邮件订阅（Resend / 邮件服务商）替换本地示意
- [ ] 废标：服务端解析 PDF（按次计费）
- [ ] 搜索与标签（行业/角色）可分享 URL
- [ ] 中英来源分级标记（一手新闻稿 / 二手研究报告）

## 已知缺口

- 订阅与赞助仅为前端占位，未接后端
- 废标上传不解析真实文件，仅内置样例
- 部分中国案例来自 IDC 摘要，客户全称或细节有限（已在风险中注明）
- 未收录「内部知本策研」真实素材（按原则暂缺）
- 无障碍与 SEO 仅基础 meta，未做 sitemap

## 目录结构

```
zhiti-yongli/
  index.html
  about.html
  assets/style.css
  assets/app.js
  cases/index.html
  cases/*.html
  demo/feibiao.html
  demo/sample-tender.txt
  demo/sample-tender.json
  data/cases.json
  build.py
  README.md
```
