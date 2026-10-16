import html
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 智体用例 static site."""
import json
import os
from pathlib import Path

ROOT = Path("/workspace/zhiti-yongli")
CASES_DIR = ROOT / "cases"
ASSETS = ROOT / "assets"
DEMO = ROOT / "demo"

for d in [ROOT, CASES_DIR, ASSETS, DEMO]:
    d.mkdir(parents=True, exist_ok=True)

SITE_NAME = "智体用例"
TAGLINE = "面向中国企业的智能体真实落地目录"
BRAND_SUB = "公开可溯源 · 可分享 · 可订阅周刊意向"

CASES = [
  {
    "id": "zhaogang-tencent-adp",
    "title": "找钢网：企微入口数字员工做询价报价与比价",
    "industry": "钢铁贸易 / B2B",
    "role": "销售、采购、内勤",
    "stack": "腾讯云 ADP / Claw、企业微信、交易/ERP/TMS/财务 Workflow",
    "summary": "在企业微信统一入口接入「数字员工」：Agent 理解口语化询价与多意图提问，Workflow 严格调用业务系统完成查货配单、报价生成与采购比价。公开报道称售前找货报价人效提升约 10–20 倍；比价从近 1 小时缩短到几分钟。",
    "steps": [
      "员工在企微提问或客户群出现询价消息",
      "Agent 识别意图，抽取品名/规格/材质/数量/到货地",
      "开放意图走 Agent，严谨步骤走 Workflow 调交易/ERP 等系统",
      "生成报价单或比价表，销售/采购确认后发送",
      "商机状态提醒与询价转化复盘"
    ],
    "risks": "行业黑话与非标规格解析误差；报价需人工确认防错报；系统权限与审计需可追踪。",
    "featured": True,
    "source_name": "腾讯云开发者社区 / IDC 案例观察 / 腾讯云 ADP 方案页",
    "source_url": "https://developer.cloud.tencent.com/article/2715405",
    "source_urls": [
      "https://developer.cloud.tencent.com/article/2715405",
      "https://adp.tencent.com/solutions/trading",
      "https://www.idc.com/resource-center/blog/%E4%BC%81%E4%B8%9A-agent-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E8%A7%82%E5%AF%9F%EF%BC%9A%E7%AE%97%E5%A5%BD%E5%BD%93%E4%B8%8Broi%EF%BC%8C%E5%B8%83%E5%B1%80%E7%BB%84%E7%BB%87%E9%95%BF%E6%9C%9F%E8%BD%AC/"
    ]
  },
  {
    "id": "laiyiifen-volcengine",
    "title": "来伊份×火山引擎：200+智能体进门店巡检与补货",
    "industry": "零售连锁",
    "role": "门店运营、督导、供应链、审批流负责人",
    "stack": "火山引擎 HiAgent、豆包大模型、现有数字化中台",
    "summary": "创建 500+ 智能体，其中 200+ 落地：AI 巡检覆盖近 3000 家门店，AI 补货覆盖 1500+ 门店；智能审批耗时降低约 70%；飞单识别准确率公开披露约 95%。采用「1+N+X」矩阵与数据/能力分级治理。",
    "steps": [
      "核心系统上云并部署统一 AI 中台（HiAgent）",
      "业务侧成立智能提升组，按开店/运店/商品等域建 Agent",
      "巡检 Agent 多模态识别陈列/物料/空置与异常交易",
      "补货 Agent 按门店特征生成差异化补货清单",
      "审批 Agent 智能提醒与自动审批，关键节点保留人工"
    ],
    "risks": "加盟门店执行一致性；误报飞单影响一线信任；敏感数据五级分级与 Agent 五级能力边界需持续治理。",
    "featured": True,
    "source_name": "中国日报网（鲁网转载）",
    "source_url": "https://cn.chinadaily.com.cn/a/202608/21/WS6a880312a3105d3d7a27c416.html",
    "source_urls": [
      "https://cn.chinadaily.com.cn/a/202608/21/WS6a880312a3105d3d7a27c416.html"
    ]
  },
  {
    "id": "laiyiifen-ai-cs",
    "title": "来伊份：在线客服 AI 助手独立处理约七成咨询",
    "industry": "零售 / 消费者服务",
    "role": "客服、会员运营",
    "stack": "在线客服 AI 助手（公司投资者关系披露）",
    "summary": "上市公司投资者关系活动披露：在线客服 AI 助手可独立处理约 73.95% 咨询量，问题解决时效较 2024 年提升至披露口径下的显著改善（材料中并提 92.7% 相关时效表述）。与门店/供应链 Agent 体系并行。",
    "steps": [
      "全渠道接入在线咨询",
      "AI 助手优先应答标准问题",
      "复杂/投诉类转人工",
      "知识沉淀与问题解决时效追踪"
    ],
    "risks": "公开披露为投资者沟通口径，需与内部运营报表交叉验证；客服体验与「人可随时介入」边界需明确（参考行业 Klarna 教训）。",
    "featured": False,
    "source_name": "上海来伊份投资者关系活动记录表（东财 PDF）",
    "source_url": "https://pdf.dfcfw.com/pdf/H22_AN202606121823509283_1.pdf",
    "source_urls": [
      "https://pdf.dfcfw.com/pdf/H22_AN202606121823509283_1.pdf",
      "https://www.gelonghui.com/news/5019529"
    ]
  },
  {
    "id": "klarna-openai-cs",
    "title": "Klarna：AI 客服助理承接约三分之二会话",
    "industry": "金融科技 / 消费信贷",
    "role": "客户服务",
    "stack": "OpenAI 驱动的 AI assistant（公司新闻稿）",
    "summary": "上线首月约 230 万次会话、承接约 2/3 客服聊天；解决时间从约 11 分钟降至不足 2 分钟；重复问询下降约 25%。后续公开报道显示公司强调保留真人通道并调整「过度 AI 化」策略——是「可量化成效 + 人工兜底」双重教材。",
    "steps": [
      "全球多市场接入 AI 助理（多语言）",
      "处理退款/退货/支付/争议等高频工单",
      "满意度与一次解决率对标人工",
      "保留转人工选项，并按业务反馈调整人机配比"
    ],
    "risks": "体验与品牌口碑风险；过度裁员后回潮用人；成本节省与客服总成本需分项看，避免只报分子。",
    "featured": True,
    "source_name": "Klarna 官方新闻稿",
    "source_url": "https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/",
    "source_urls": [
      "https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/",
      "https://www.customerexperiencedive.com/news/klarna-says-ai-agent-work-853-employees/805987/"
    ]
  },
  {
    "id": "statefarm-copilot-studio",
    "title": "State Farm：受治理的 Copilot Studio Agent 规模化",
    "industry": "保险",
    "role": "HR、核保、内容与翻译、IT 平台团队",
    "stack": "Microsoft Copilot Studio、Power Platform、SharePoint、Entra ID",
    "summary": "41 个通过风险评估的生产构建；Power Platform 内 3000+ Agent 身份。Ask HR 政策 Agent 减轻人工答疑；核保准则检索 Agent 上线 30 天内成为第二常用；营销翻译周转从约 12 个月压到约 24 小时。强调治理与人工问责先行。",
    "steps": [
      "负责任 AI 工坊 + 阶梯式建设（个人→团队→部门→企业）",
      "风险与合规审批路径清晰后再进生产",
      "知识类 Agent（HR/核保手册）优先",
      "目录化复用连接器与入职/离职方案",
      "规划向跨系统编排与行动型 Agent 演进"
    ],
    "risks": "知识库过时导致误导；核保等关键决策必须人责；规模化后 Agent 身份与权限治理成本上升。",
    "featured": True,
    "source_name": "Microsoft Customer Stories",
    "source_url": "https://www.microsoft.com/en/customers/story/26947-state-farm-microsoft-power-platform",
    "source_urls": [
      "https://www.microsoft.com/en/customers/story/26947-state-farm-microsoft-power-platform",
      "https://adoption.microsoft.com/zh-cn/agent-transformation-stories/"
    ]
  },
  {
    "id": "fujitsu-m365-copilot",
    "title": "富士通：约 10 万席 Copilot，服务台初响自动化约 75%",
    "industry": "IT 服务 / 综合科技",
    "role": "服务台、全体知识工作者",
    "stack": "Microsoft 365 Copilot、企业内部 Fujitra 转型网络",
    "summary": "从 7500 席试点扩至约 10 万席；有权限员工中使用率曾报超 90%。服务台年询约 30 万，AI Agent 承接约 75% 的初响与分诊，员工更多投入知识质量与准确率改进。",
    "steps": [
      "小规模跨部门试点验证价值",
      "分阶段扩容席位与接入系统",
      "服务台初响/分诊 Agent 上线",
      "以 Copilot 为入口连接专业 Agent 与业务系统"
    ],
    "risks": "客户现场/高安全环境无法覆盖；依赖知识内容质量；自动化分诊错误会放大工单路由成本。",
    "featured": False,
    "source_name": "Microsoft Customer Stories",
    "source_url": "https://www.microsoft.com/en/customers/story/27449-fujitsu-limited-microsoft-365-copilot",
    "source_urls": [
      "https://www.microsoft.com/en/customers/story/27449-fujitsu-limited-microsoft-365-copilot"
    ]
  },
  {
    "id": "sanofi-bedrock-concierge",
    "title": "赛诺菲 Concierge：全球员工 Agent 入口（AWS Bedrock）",
    "industry": "医药 / 生物制药",
    "role": "研发、制造供应、职能横向团队",
    "stack": "Amazon Bedrock、自建 Concierge、Agent Hub 编排层",
    "summary": "2026Q1：周活约 5 万、月活约 7.2 万、累计约 1100 万次对话、正面反馈约 90%；调查称约 90.5% 员工节省常规任务时间。Concierge 作为发现与编排入口，连接检索、回写与流程自动化专业 Agent。",
    "steps": [
      "自建、可换模型、多区域部署降延迟",
      "从生产力助手升级为数字网关",
      "建设 Agent Hub 连接专业 Agent",
      "社区超级用户分享工作流，持续扩能力（含 AgentCore）"
    ],
    "risks": "制药数据敏感与合规；幻觉导致错误决策；遗留应用千万级导航替代需权限与审计严密。",
    "featured": False,
    "source_name": "AWS Case Study",
    "source_url": "https://aws.amazon.com/solutions/case-studies/sanofi-bedrock-case-study/",
    "source_urls": [
      "https://aws.amazon.com/solutions/case-studies/sanofi-bedrock-case-study/"
    ]
  },
  {
    "id": "pwc-google-agents",
    "title": "PwC×Google Cloud：全球 250+ 企业级 Agent 组合",
    "industry": "专业服务（多行业模板）",
    "role": "咨询交付、客户行业运营团队",
    "stack": "Google Cloud、PwC agent ecosystem",
    "summary": "2025-10 宣布 EMEA 新增 100+ 企业就绪 Agent，全球组合超 250。覆盖金融合规/AML、制造质检与供应链例外、能源运维、公共服务分诊、零售需求与退货异常等。欧洲医疗网络 Limbach 在 34 个站点推进行政与科研侧 Agent，并强调 EU AI Act 对齐培训。",
    "steps": [
      "按行业打包可复用 Agent 能力",
      "与客户共创用例并治理先行",
      "站点级推广（采购、市场等跨站点 Agent）",
      "培训三件套：基础、现场、专家论坛"
    ],
    "risks": "模板与客户流程落差；跨境数据与 AI Act 合规；「企业就绪」需客户侧数据与权限配套。",
    "featured": False,
    "source_name": "PwC 新闻稿",
    "source_url": "https://www.pwc.com/gx/en/news-room/press-releases/2025/scales-global-ai-agent-ecosystem.html",
    "source_urls": [
      "https://www.pwc.com/gx/en/news-room/press-releases/2025/scales-global-ai-agent-ecosystem.html"
    ]
  },
  {
    "id": "bank-360-cs-credit",
    "title": "某银行×360：客服与信贷初审智能体（信通院报告收录）",
    "industry": "银行",
    "role": "客服、信贷审批",
    "stack": "360 企业级智能体方案（报告案例，客户名公开材料未全称）",
    "summary": "中国信通院联合 360 等发布的企业级智能体研究报告（2026）收录案例：客服智能体上线后人工客服投入降约 15%、满意度升约 20%；信贷审批辅助结合材料、内部政策与评级模型做智能初审，周期由约 7 天缩至约 3 天。",
    "steps": [
      "客服场景承接高频标准问询",
      "信贷材料与政策/评级模型辅助初审",
      "人工复核终审与责任边界",
      "以人效与周期等 KPI 验收"
    ],
    "risks": "公开报道为二手转述，银行全称与审计口径需再核原报告；信贷决策合规与可解释性要求高。",
    "featured": False,
    "source_name": "信息主管网（转述信通院×360 报告）",
    "source_url": "https://www.cio360.net/show-616-104901-1.html",
    "source_urls": [
      "https://www.cio360.net/show-616-104901-1.html"
    ]
  },
  {
    "id": "qingdao-port-baidu",
    "title": "青岛港×百度伐谋：配载算法迭代 Agent",
    "industry": "港口物流",
    "role": "算法/运营优化团队",
    "stack": "百度伐谋 Agent（IDC 案例精选披露）",
    "summary": "IDC「中国企业级 Agent 最佳实践与案例精选」观察：用 Agent 持续优化青岛港配载算法，算法迭代周期缩短 50% 以上，从数周压到小时级。",
    "steps": [
      "将配载优化目标与约束结构化",
      "Agent 辅助实验/迭代算法方案",
      "用生产指标验证效果",
      "缩短迭代闭环"
    ],
    "risks": "港口安全与调度强约束；效果依赖数据质量；公开材料为 IDC 摘要，细节需企业侧确认。",
    "featured": False,
    "source_name": "IDC 企业 Agent 最佳实践观察",
    "source_url": "https://www.idc.com/resource-center/blog/%E4%BC%81%E4%B8%9A-agent-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E8%A7%82%E5%AF%9F%EF%BC%9A%E7%AE%97%E5%A5%BD%E5%BD%93%E4%B8%8Broi%EF%BC%8C%E5%B8%83%E5%B1%80%E7%BB%84%E7%BB%87%E9%95%BF%E6%9C%9F%E8%BD%AC/",
    "source_urls": [
      "https://www.idc.com/resource-center/blog/%E4%BC%81%E4%B8%9A-agent-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E8%A7%82%E5%AF%9F%EF%BC%9A%E7%AE%97%E5%A5%BD%E5%BD%93%E4%B8%8Broi%EF%BC%8C%E5%B8%83%E5%B1%80%E7%BB%84%E7%BB%87%E9%95%BF%E6%9C%9F%E8%BD%AC/"
    ]
  },
  {
    "id": "hangzhou-bank-ant",
    "title": "杭州银行×蚂蚁数科：多 Agent 营销策略生成",
    "industry": "银行零售/对公经营",
    "role": "客户经营、产品与策略团队",
    "stack": "蚂蚁数科多 Agent（客户洞察/产品分析/营销策略）",
    "summary": "IDC 案例观察：基于多个 Agent 处理客户洞察、产品分析与营销策略，项目测算策略生成时间从天级缩短到分钟级。可与杭州银行公开的智能展业体系表述交叉阅读。",
    "steps": [
      "客户洞察 Agent 汇总画像与信号",
      "产品分析 Agent 匹配可售产品",
      "策略 Agent 生成营销方案",
      "人工合规校验后触达与复盘"
    ],
    "risks": "金融营销合规与适当性；分钟级产出需质检；IDC 为摘要口径。",
    "featured": False,
    "source_name": "IDC 企业 Agent 最佳实践观察",
    "source_url": "https://www.idc.com/resource-center/blog/%E4%BC%81%E4%B8%9A-agent-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E8%A7%82%E5%AF%9F%EF%BC%9A%E7%AE%97%E5%A5%BD%E5%BD%93%E4%B8%8Broi%EF%BC%8C%E5%B8%83%E5%B1%80%E7%BB%84%E7%BB%87%E9%95%BF%E6%9C%9F%E8%BD%AC/",
    "source_urls": [
      "https://www.idc.com/resource-center/blog/%E4%BC%81%E4%B8%9A-agent-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E8%A7%82%E5%AF%9F%EF%BC%9A%E7%AE%97%E5%A5%BD%E5%BD%93%E4%B8%8Broi%EF%BC%8C%E5%B8%83%E5%B1%80%E7%BB%84%E7%BB%87%E9%95%BF%E6%9C%9F%E8%BD%AC/",
      "https://www.shobserver.com/sgh/detail?id=1749968"
    ]
  },
  {
    "id": "guosheng-jinzhiwei",
    "title": "国盛证券×金智维：运维 CMDB 查询进工单秒级处置",
    "industry": "证券 / IT 运维",
    "role": "运维、值班工程师",
    "stack": "金智维 RPA/Agent 与 CMDB、工单系统",
    "summary": "IDC 案例：将证券运维中的 CMDB 查询接入工单与自动处置流程，查询时间从数天级缩短到秒级，减少人工翻查与等待。",
    "steps": [
      "工单触发或自然语言查询",
      "连接 CMDB 检索配置与依赖",
      "自动处置流程执行可脚本化步骤",
      "异常升级人工"
    ],
    "risks": "自动变更的生产风险；权限与双人复核；公开材料为 IDC 摘要。",
    "featured": False,
    "source_name": "IDC 企业 Agent 最佳实践观察",
    "source_url": "https://www.idc.com/resource-center/blog/%E4%BC%81%E4%B8%9A-agent-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E8%A7%82%E5%AF%9F%EF%BC%9A%E7%AE%97%E5%A5%BD%E5%BD%93%E4%B8%8Broi%EF%BC%8C%E5%B8%83%E5%B1%80%E7%BB%84%E7%BB%87%E9%95%BF%E6%9C%9F%E8%BD%AC/",
    "source_urls": [
      "https://www.idc.com/resource-center/blog/%E4%BC%81%E4%B8%9A-agent-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E8%A7%82%E5%AF%9F%EF%BC%9A%E7%AE%97%E5%A5%BD%E5%BD%93%E4%B8%8Broi%EF%BC%8C%E5%B8%83%E5%B1%80%E7%BB%84%E7%BB%87%E9%95%BF%E6%9C%9F%E8%BD%AC/"
    ]
  },
  {
    "id": "china-spring-defan",
    "title": "中国弹簧×得帆：计划物流采购排产做成 Skills",
    "industry": "制造",
    "role": "计划、物流、采购、质量",
    "stack": "得帆平台 Skills + 企业业务系统连接",
    "summary": "IDC 案例：把计划物流、采购、排产和质量整改等流程整理为 Skills，连接业务系统协助员工处理任务，整体效率公开口径提升约 70%–80%。业务人员参与定义与验收。",
    "steps": [
      "梳理高频业务流程为 Skills",
      "连接 ERP/MES 等系统",
      "业务人员提供样例与验收标准",
      "上线后按任务闭环迭代"
    ],
    "risks": "制造现场例外多；Skills 覆盖不足时体验差；效率百分比为案例口径，跨厂不可直接对比。",
    "featured": False,
    "source_name": "IDC 企业 Agent 最佳实践观察",
    "source_url": "https://www.idc.com/resource-center/blog/%E4%BC%81%E4%B8%9A-agent-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E8%A7%82%E5%AF%9F%EF%BC%9A%E7%AE%97%E5%A5%BD%E5%BD%93%E4%B8%8Broi%EF%BC%8C%E5%B8%83%E5%B1%80%E7%BB%84%E7%BB%87%E9%95%BF%E6%9C%9F%E8%BD%AC/",
    "source_urls": [
      "https://www.idc.com/resource-center/blog/%E4%BC%81%E4%B8%9A-agent-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E8%A7%82%E5%AF%9F%EF%BC%9A%E7%AE%97%E5%A5%BD%E5%BD%93%E4%B8%8Broi%EF%BC%8C%E5%B8%83%E5%B1%80%E7%BB%84%E7%BB%87%E9%95%BF%E6%9C%9F%E8%BD%AC/"
    ]
  },
  {
    "id": "laiyi-tech-order",
    "title": "来也科技：电子元器件分销商订单处理人效重构",
    "industry": "电子元器件分销",
    "role": "订单处理团队",
    "stack": "来也科技自动化/Agent 方案（IDC 披露）",
    "summary": "IDC 案例：帮助某电子元器件分销商处理订单，订单处理团队从约 20 人减至 1 人负责监管与异常复核，大量订单由自动化/Agent 完成。",
    "steps": [
      "标准化订单录入与校验规则",
      "自动处理主流订单路径",
      "异常单人工复核",
      "持续沉淀例外规则"
    ],
    "risks": "客户名为「某」，公开可溯源到 IDC 摘要级别；人员编制变化需考虑业务波动与合规劳务安排。",
    "featured": False,
    "source_name": "IDC 企业 Agent 最佳实践观察",
    "source_url": "https://www.idc.com/resource-center/blog/%E4%BC%81%E4%B8%9A-agent-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E8%A7%82%E5%AF%9F%EF%BC%9A%E7%AE%97%E5%A5%BD%E5%BD%93%E4%B8%8Broi%EF%BC%8C%E5%B8%83%E5%B1%80%E7%BB%84%E7%BB%87%E9%95%BF%E6%9C%9F%E8%BD%AC/",
    "source_urls": [
      "https://www.idc.com/resource-center/blog/%E4%BC%81%E4%B8%9A-agent-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E8%A7%82%E5%AF%9F%EF%BC%9A%E7%AE%97%E5%A5%BD%E5%BD%93%E4%B8%8Broi%EF%BC%8C%E5%B8%83%E5%B1%80%E7%BB%84%E7%BB%87%E9%95%BF%E6%9C%9F%E8%BD%AC/"
    ]
  },
  {
    "id": "jahwa-workbuddy-logistics",
    "title": "上海家化×WorkBuddy：物流对账月度分析从 2 人天到 15 分钟",
    "industry": "日化 / 消费品",
    "role": "供应链运营、财务、品牌营销",
    "stack": "腾讯 WorkBuddy 企业版、Skill 沉淀、Python 脚本、资料库",
    "summary": "上海家化 2026 年 4 月联合腾讯智慧零售试点 WorkBuddy，报道称已覆盖九大部门、平均提效超 4.5 倍。供应链物流对账涉及天猫/京东/抖音等 7 类原始账单、18 个月约 6000 万行数据：运营经理把月度处理步骤拆解交给 WorkBuddy 生成 Python 脚本，用历史数据反复验证并把问题沉淀为 Skill，月度账单分析从 2 人天缩到 15 分钟，单项最高提效约 150 倍，整套月度工作压缩到 20 分钟内。",
    "steps": [
      "业务骨干把月度对账拆成可描述的处理步骤",
      "WorkBuddy 按步骤生成 Python 处理脚本",
      "用 18 个月历史账单持续验证结果",
      "把发现的口径问题与例外沉淀为 Skill",
      "其他部门复用 Skill，扩到看板、周报、调研分析"
    ],
    "risks": "指标为媒体报道转述企业方口径；脚本口径错误会批量放大，需保留历史回测与人工抽检；Skill 跨部门复用要管住数据权限。",
    "featured": True,
    "source_name": "扬子晚报扬眼（腾讯新闻转载），2026-08-27",
    "source_url": "https://news.qq.com/rain/a/20260827A0991A00",
    "source_urls": [
      "https://news.qq.com/rain/a/20260827A0991A00"
    ]
  },
  {
    "id": "desay-sv-ai-indeed",
    "title": "德赛西威×实在智能：218 条需求筛出 60+ 自动化场景，年省 4.3 万小时",
    "industry": "汽车电子 / 制造",
    "role": "财务、采购计划、跟单仓储、HR",
    "stack": "实在智能数字员工（RPA+Agent）、OCR、合同智能审核、飞书/网银/财务系统",
    "summary": "德赛西威数字化转型 CMO 在实在智能大会上分享：先梳理 218 条需求并分流，约七成（152 条）为自动化类；从研发生产、采购计划、跟单仓储、财务人事四类高频场景切入。批量开票人工 8 分钟、数字员工 30 秒。规模化后 60 余个场景自动化，年节省 4.3 万小时（目标 4.2 万），效率提升 396%，管理响应时间缩短 50%。",
    "steps": [
      "调研加工作坊梳理需求，分流为自动化、AI 叠加、回系统优化",
      "按规则清晰、高频、跨系统优先挑场景",
      "单场景（批量开票）先验证",
      "数字员工上岗后按指标复盘",
      "场景库沉淀后复制推广，配权限边界与操作日志审计"
    ],
    "risks": "来源为供应商官网发布的客户演讲整理，属厂商渠道；多数场景偏 RPA 式流程自动化，智能体成分需按场景甄别；指标为企业自报。",
    "featured": False,
    "source_name": "实在智能官网新闻（德赛西威 CMO 大会分享整理），2026-10-13",
    "source_url": "https://www.ai-indeed.com/aboutNews/32499.html",
    "source_urls": [
      "https://www.ai-indeed.com/aboutNews/32499.html"
    ]
  },
  {
    "id": "asurion-copilot-invoice",
    "title": "Asurion：发票异常处理 Agent，免人工处理率从不足 20% 升到 70%+",
    "industry": "保险 / 设备保障服务",
    "role": "财务应付（AP）",
    "stack": "Microsoft Copilot Studio、Power Automate、Dynamics 365 Finance 发票采集",
    "summary": "Asurion 每年约 3 万张直接采购订单发票、约九成带至少一个异常，免人工处理率一度跌破 20%。团队把 Copilot Studio Agent 嵌进 Power Automate 流程：发票进入错误状态时由 Agent 按既定规则修正料号、订单号等再回流入账。约一周做出验证，上线首周北美/南美供应商提升到 55% 以上，后续达到 70% 以上，目标 85%。",
    "steps": [
      "发票采集识别出错误状态的数据",
      "Power Automate 抽取相关字段路由给 Agent",
      "Agent 按确定性指令修正外部料号、订单号等",
      "后续流程重处理，完整发票进入财务系统",
      "按供应商与区域逐步扩展，规划分录与对账场景"
    ],
    "risks": "来源为微软客户案例，厂商渠道；场景是确定性规则修正，需最小权限、尽量只读和人工复核节点；MCP 能力仍在 QA。",
    "featured": False,
    "source_name": "Microsoft Customer Stories，2026-10-08",
    "source_url": "https://www.microsoft.com/en/customers/story/27456-asurion-insurance-services-microsoft-copilot-studio",
    "source_urls": [
      "https://www.microsoft.com/en/customers/story/27456-asurion-insurance-services-microsoft-copilot-studio"
    ]
  },
  {
    "id": "cornerstone-bedrock-dataops",
    "title": "Cornerstone：多 Agent 数据库故障诊断，从 45 分钟缩到 10 分钟",
    "industry": "企业软件 / SaaS",
    "role": "DataOps、SRE",
    "stack": "Amazon Bedrock、Strands Agents 多 Agent 编排",
    "summary": "Cornerstone OnDemand 的 DataOps 团队过去每次数据库事故要花最多 45 分钟手工查系统视图、对日志再跨团队交接。其 Orion AI 多 Agent 系统按领域分工协同，诊断时间降到 10 分钟（约 78%），手工生命周期步骤减少约 70%，冗余告警中位数降 65%。三人团队用六个月交付。",
    "steps": [
      "告警进入后路由到对应领域的专职 Agent",
      "Agent 查询系统视图与日志、汇总诊断",
      "混合路由：常见问题走固定路径，复杂问题交多 Agent 协同",
      "会话级记忆加实时指标直取，避免用过期数据",
      "结果同步给 SRE，过滤重复告警"
    ],
    "risks": "来源为 AWS 机器学习博客（与客户联合署名），厂商渠道；涉及生产数据库，需限定只读与操作审批；指标为企业自报。",
    "featured": False,
    "source_name": "AWS Machine Learning Blog，2026-10-07",
    "source_url": "https://aws.amazon.com/blogs/machine-learning/how-cornerstone-ondemand-cut-database-diagnosis-by-78-with-amazon-bedrock/",
    "source_urls": [
      "https://aws.amazon.com/blogs/machine-learning/how-cornerstone-ondemand-cut-database-diagnosis-by-78-with-amazon-bedrock/"
    ]
  },
]

assert len(CASES) >= 12

CSS = r"""
:root {
  --bg: #0b1220;
  --bg2: #121a2b;
  --card: #162033;
  --line: #243049;
  --text: #e8eefc;
  --muted: #9aa8c7;
  --accent: #3d8bfd;
  --accent2: #22c55e;
  --warn: #f59e0b;
  --danger: #ef4444;
  --radius: 14px;
  --shadow: 0 10px 30px rgba(0,0,0,.35);
  --max: 1080px;
  --font: "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0; font-family: var(--font); background: linear-gradient(180deg,#0b1220 0%,#0e1628 40%,#0b1220 100%);
  color: var(--text); line-height: 1.65; min-height: 100vh;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.wrap { width: min(var(--max), calc(100% - 2rem)); margin: 0 auto; }
.site-header {
  position: sticky; top: 0; z-index: 20; backdrop-filter: blur(10px);
  background: rgba(11,18,32,.82); border-bottom: 1px solid var(--line);
}
.nav { display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: .9rem 0; flex-wrap: wrap; }
.brand { display: flex; align-items: center; gap: .7rem; color: var(--text); text-decoration: none; font-weight: 700; }
.brand-mark {
  width: 34px; height: 34px; border-radius: 10px; display:grid; place-items:center;
  background: linear-gradient(135deg,#3d8bfd,#22c55e); color:#041018; font-size: .85rem;
}
.nav-links { display:flex; gap: .9rem; flex-wrap: wrap; align-items:center; }
.nav-links a { color: var(--muted); font-size: .95rem; }
.nav-links a:hover, .nav-links a.active { color: var(--text); }
.btn {
  display:inline-flex; align-items:center; justify-content:center; gap:.4rem;
  border:1px solid var(--line); background: var(--card); color: var(--text);
  padding: .65rem 1rem; border-radius: 999px; font-weight: 600; cursor: pointer;
}
.btn:hover { border-color: var(--accent); text-decoration: none; }
.btn-primary { background: linear-gradient(135deg,#2f6fed,#3d8bfd); border-color: transparent; }
.btn-ghost { background: transparent; }
.hero {
  padding: 3.2rem 0 2rem; display:grid; gap: 1.4rem;
}
.badge {
  display:inline-flex; gap:.4rem; align-items:center; width:fit-content;
  padding:.35rem .7rem; border-radius:999px; border:1px solid var(--line);
  background: rgba(61,139,253,.1); color:#b9d3ff; font-size:.85rem;
}
.hero h1 { margin:0; font-size: clamp(1.8rem, 4vw, 2.7rem); line-height:1.2; }
.hero .lead { color: var(--muted); font-size: 1.08rem; max-width: 46rem; }
.hero-actions { display:flex; gap:.8rem; flex-wrap:wrap; }
.grid { display:grid; gap: 1rem; }
.grid-3 { grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); }
.grid-2 { grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
.card {
  background: var(--card); border:1px solid var(--line); border-radius: var(--radius);
  padding: 1.15rem 1.2rem; box-shadow: var(--shadow);
}
.card h3 { margin: .2rem 0 .5rem; font-size: 1.05rem; }
.muted { color: var(--muted); }
.section { padding: 1.6rem 0 2.2rem; }
.section h2 { margin: 0 0 .4rem; font-size: 1.45rem; }
.section .desc { color: var(--muted); margin: 0 0 1.1rem; }
.meta { display:flex; flex-wrap:wrap; gap:.45rem; margin: .6rem 0; }
.tag {
  font-size: .78rem; color:#c9d7f5; background:#1b2740; border:1px solid var(--line);
  padding: .18rem .5rem; border-radius: 999px;
}
.tag.green { color:#bbf7d0; background:#12301f; }
.tag.orange { color:#fde68a; background:#3a2a12; }
.case-card h3 a { color: var(--text); }
.case-card p { margin: .4rem 0; color: var(--muted); font-size: .94rem; }
.source { font-size: .85rem; margin-top: .7rem; }
.footer {
  border-top:1px solid var(--line); padding: 1.6rem 0 2.4rem; color: var(--muted); font-size: .9rem;
}
.footer .row { display:flex; justify-content:space-between; gap:1rem; flex-wrap:wrap; }
.form { display:grid; gap: .7rem; }
input, textarea, select {
  width:100%; padding: .75rem .9rem; border-radius: 10px; border:1px solid var(--line);
  background:#0f1728; color: var(--text); font: inherit;
}
label { font-size: .9rem; color: var(--muted); }
.note {
  border-left: 3px solid var(--warn); background: rgba(245,158,11,.08);
  padding: .8rem 1rem; border-radius: 0 10px 10px 0; color: #fde68a; font-size: .92rem;
}
.danger-note {
  border-left: 3px solid var(--danger); background: rgba(239,68,68,.08);
  padding: .8rem 1rem; border-radius: 0 10px 10px 0; color: #fecaca; font-size: .92rem;
}
.ok-note {
  border-left: 3px solid var(--accent2); background: rgba(34,197,94,.08);
  padding: .8rem 1rem; border-radius: 0 10px 10px 0; color: #bbf7d0; font-size: .92rem;
}
.kv { display:grid; grid-template-columns: 110px 1fr; gap: .35rem .8rem; margin: .8rem 0; }
.kv dt { color: var(--muted); }
.kv dd { margin: 0; }
ol.steps { padding-left: 1.2rem; }
ol.steps li { margin: .35rem 0; }
.upload-box {
  border: 1.5px dashed #35507a; border-radius: var(--radius); padding: 1.2rem;
  background: #101a2d; text-align: center;
}
.demo-out { white-space: pre-wrap; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: .86rem; background:#0a1020; border:1px solid var(--line); border-radius: 10px; padding: 1rem; }
.table { width:100%; border-collapse: collapse; font-size: .92rem; }
.table th, .table td { border:1px solid var(--line); padding: .55rem .65rem; text-align:left; vertical-align:top; }
.table th { background:#121c31; }
.filters { display:flex; gap:.6rem; flex-wrap:wrap; margin-bottom: 1rem; }
.filters select { width: auto; min-width: 140px; }
.breadcrumbs { color: var(--muted); font-size: .9rem; margin-bottom: 1rem; }
.sponsor-slot {
  min-height: 88px; border:1px dashed #3a5078; border-radius: 12px; display:grid; place-items:center;
  color: var(--muted); background: repeating-linear-gradient(-45deg, transparent, transparent 8px, rgba(255,255,255,.02) 8px, rgba(255,255,255,.02) 16px);
}
@media (max-width: 640px) {
  .kv { grid-template-columns: 1fr; }
}
"""

def nav(active=""):
    items = [
        ("首页", "index.html", "home"),
        ("用例目录", "cases/index.html", "cases"),
        ("废标速查", "demo/feibiao.html", "demo"),
        ("关于", "about.html", "about"),
    ]
    links = []
    for label, href, key in items:
        # Fix relative paths depending on depth - handled by callers via prefix
        cls = "active" if active == key else ""
        links.append(f'<a class="{cls}" href="__PREFIX__{href}">{label}</a>')
    return f"""
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="__PREFIX__index.html">
      <span class="brand-mark">智</span>
      <span>{SITE_NAME}</span>
    </a>
    <nav class="nav-links">
      {''.join(links)}
    </nav>
  </div>
</header>
""".replace("__PREFIX__", "{prefix}")

FOOTER = """
<footer class="footer">
  <div class="wrap row">
    <div>
      <strong style="color:var(--text)">{SITE_NAME}</strong> · {TAGLINE}<br>
      用例均标注公开来源；指标为原文披露，跨案例不可直接对比。<br>
      废标速查为示意 Demo，须人工复核，不保证防废标。
    </div>
    <div>
      <a href="{prefix}about.html">免责声明</a> ·
      <a href="{prefix}demo/feibiao.html">废标速查</a> ·
      MVP · 2026
    </div>
  </div>
</footer>
""".format(SITE_NAME=SITE_NAME, TAGLINE=TAGLINE, prefix="{prefix}")

def page(title, body, prefix="", active="", desc=None):
    n = nav(active).replace("{prefix}", prefix)
    f = FOOTER.replace("{prefix}", prefix)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title} · {SITE_NAME}</title>
<meta name="description" content="{html.escape((desc or TAGLINE)[:150], quote=True)}"/>
<link rel="stylesheet" href="{prefix}assets/style.css"/>
</head>
<body>
{n}
<main>
{body}
</main>
{f}
<script src="{prefix}assets/app.js"></script>
</body>
</html>
"""

def case_card(c, prefix=""):
    featured = '<span class="tag green">精选</span>' if c.get("featured") else ""
    return f"""
<article class="card case-card" data-industry="{c['industry']}" data-role="{c['role']}">
  <div class="meta">{featured}<span class="tag">{c['industry']}</span><span class="tag">{c['role'].split('、')[0]}</span></div>
  <h3><a href="{prefix}cases/{c['id']}.html">{c['title']}</a></h3>
  <p>{c['summary'][:120]}…</p>
  <p class="source">来源：<a href="{c['source_url']}" target="_blank" rel="noopener">{c['source_name']}</a></p>
</article>
"""

# --- write CSS ---
(ASSETS / "style.css").write_text(CSS, encoding="utf-8")

# --- app.js ---
APP_JS = r"""
(function(){
  // Newsletter / sponsor placeholders
  document.querySelectorAll('[data-newsletter]').forEach(function(form){
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var email = form.querySelector('input[type=email]');
      var msg = form.querySelector('[data-msg]');
      if(!email || !email.value){ return; }
      if(msg){
        msg.textContent = '已记录意向（本地示意，尚未接邮箱服务）：' + email.value;
        msg.hidden = false;
      }
      form.reset();
    });
  });

  // Case filters
  var list = document.querySelector('[data-case-list]');
  var ind = document.querySelector('#filter-industry');
  var q = document.querySelector('#filter-q');
  function applyFilter(){
    if(!list) return;
    var iv = ind ? ind.value : '';
    var qv = (q && q.value || '').trim().toLowerCase();
    list.querySelectorAll('.case-card').forEach(function(card){
      var ok = true;
      if(iv && card.getAttribute('data-industry') !== iv) ok = false;
      if(qv){
        var t = card.textContent.toLowerCase();
        if(t.indexOf(qv) === -1) ok = false;
      }
      card.style.display = ok ? '' : 'none';
    });
  }
  if(ind) ind.addEventListener('change', applyFilter);
  if(q) q.addEventListener('input', applyFilter);

  // Feibiao demo
  var runBtn = document.querySelector('#run-sample');
  var out = document.querySelector('#demo-result');
  var fileInput = document.querySelector('#tender-file');
  var uploadHint = document.querySelector('#upload-hint');
  if(fileInput && uploadHint){
    fileInput.addEventListener('change', function(){
      if(fileInput.files && fileInput.files[0]){
        uploadHint.textContent = '已选择：' + fileInput.files[0].name + '（MVP 仅前端示意，请点「运行内置样例」查看结构化输出）';
      }
    });
  }
  if(runBtn && out){
    runBtn.addEventListener('click', function(){
      fetch('sample-tender.json').then(function(r){ return r.json(); }).then(function(data){
        out.hidden = false;
        out.innerHTML = renderFeibiao(data);
      }).catch(function(err){
        out.hidden = false;
        out.textContent = '加载样例失败：' + err;
      });
    });
  }
  function renderFeibiao(data){
    function rows(items, cols){
      return '<table class="table"><thead><tr>' + cols.map(function(c){return '<th>'+c+'</th>';}).join('') +
        '</tr></thead><tbody>' + items.map(function(it){
          return '<tr>' + cols.map(function(c){
            var key = ({'类型':'type','条款':'text','引用':'cite','类别':'category','要求':'text','分值/权重':'weight','说明':'note'})[c] || c;
            return '<td>' + (it[key] || '') + '</td>';
          }).join('') + '</tr>';
        }).join('') + '</tbody></table>';
    }
    return '<div class="ok-note">以下为<strong>内置样例招标文本</strong>的结构化抽取示意，非真实投标建议。必须人工复核。</div>' +
      '<p><strong>项目</strong>：' + data.project + '<br><strong>截止时间</strong>：' + data.deadline +
      ' <span class="muted">（引自 ' + data.deadline_cite + '）</span></p>' +
      '<h3>废标 / 否决项</h3>' + rows(data.disqualify, ['类型','条款','引用']) +
      '<h3>资格门槛</h3>' + rows(data.qualification, ['类别','要求','引用']) +
      '<h3>评分点</h3>' + rows(data.scoring, ['类别','说明','分值/权重','引用']) +
      '<p class="muted" style="margin-top:1rem">样例来源文件：' + data.sample_file + ' · 生成方式：规则+人工标注示意</p>';
  }
})();
"""
(ASSETS / "app.js").write_text(APP_JS, encoding="utf-8")

# sample tender
SAMPLE = {
  "project": "某某市智慧客服与知识库建设项目（示意招标文件节选）",
  "deadline": "2026年11月20日 09:30（北京时间）",
  "deadline_cite": "§1.4 投标截止与开标时间",
  "sample_file": "demo/sample-tender.txt",
  "disqualify": [
    {"type": "否决投标", "text": "未按招标文件要求密封、签署或加盖公章的投标文件", "cite": "§3.2.1"},
    {"type": "否决投标", "text": "投标报价超过采购预算（人民币 280 万元）", "cite": "§3.2.3 / §1.3"},
    {"type": "否决投标", "text": "串联投标、弄虚作假或提供虚假材料", "cite": "§3.2.5"},
    {"type": "废标情形", "text": "符合专业条件的供应商或对招标文件实质性响应的供应商不足三家", "cite": "§3.3.1"},
    {"type": "实质性偏离", "text": "交付周期超过合同签订后 90 日历天视为实质性不响应", "cite": "§2.4.2"}
  ],
  "qualification": [
    {"category": "主体资格", "text": "在中华人民共和国境内注册的独立法人，提供营业执照复印件加盖公章", "cite": "§2.1.1"},
    {"category": "财务", "text": "提供近三年（2023–2025）经审计的财务报表或财务状况说明", "cite": "§2.1.2"},
    {"category": "业绩", "text": "2023年1月以来至少完成 2 个金额≥100 万元的企业智能客服或知识库相关项目，提供合同关键页与验收证明", "cite": "§2.1.3"},
    {"category": "人员", "text": "项目经理具备 PMP 或信息系统项目管理师证书，且提供在职证明", "cite": "§2.1.4"},
    {"category": "信誉", "text": "未被列入失信被执行人名单；近三年无重大违法记录声明", "cite": "§2.1.5"},
    {"category": "联合体", "text": "本项目不接受联合体投标", "cite": "§2.1.6"}
  ],
  "scoring": [
    {"category": "技术", "note": "方案完整性、架构与安全、知识库与 Agent 编排能力演示", "weight": "40 分", "cite": "§4.2"},
    {"category": "商务", "note": "报价得分（最低有效价法，公式见文件）", "weight": "30 分", "cite": "§4.3"},
    {"category": "业绩与团队", "note": "类似案例质量、团队配置与驻场响应", "weight": "20 分", "cite": "§4.4"},
    {"category": "服务与培训", "note": "质保期、培训计划、SLA", "weight": "10 分", "cite": "§4.5"}
  ]
}

(DEMO / "sample-tender.json").write_text(json.dumps(SAMPLE, ensure_ascii=False, indent=2), encoding="utf-8")
(DEMO / "sample-tender.txt").write_text("""【示意招标文件节选 · 非真实项目】
项目名称：某某市智慧客服与知识库建设项目
采购预算：人民币 280 万元

§1.3 采购预算
本项目采购预算为人民币 280 万元，投标报价超过预算的按否决投标处理。

§1.4 投标截止与开标时间
投标截止时间：2026年11月20日 09:30（北京时间）。逾期送达的投标文件概不接收。

§2.1 资格要求
§2.1.1 投标人须为在中华人民共和国境内注册的独立法人，投标文件中提供营业执照复印件并加盖公章。
§2.1.2 提供近三年（2023–2025）经审计的财务报表或财务状况说明。
§2.1.3 2023年1月以来至少完成 2 个金额不低于 100 万元的企业智能客服或知识库相关项目，提供合同关键页与验收证明。
§2.1.4 项目经理具备 PMP 或信息系统项目管理师证书，并提供在职证明。
§2.1.5 投标人未被列入失信被执行人名单；近三年无重大违法记录之声明。
§2.1.6 本项目不接受联合体投标。

§2.4.2 交付周期
合同签订后 90 日历天内完成上线交付；超过该周期视为对招标文件的实质性不响应。

§3.2 否决投标
§3.2.1 未按招标文件要求密封、签署或加盖公章的。
§3.2.3 投标报价超过采购预算的。
§3.2.5 串通投标、弄虚作假或提供虚假材料的。

§3.3 废标
§3.3.1 符合专业条件的供应商或者对招标文件作出实质性响应的供应商不足三家的，应予废标。

§4 评标方法（综合评分法）
§4.2 技术部分 40 分：方案完整性、架构与安全、知识库与 Agent 编排能力演示。
§4.3 商务部分 30 分：报价得分按最低有效价法计算。
§4.4 业绩与团队 20 分。
§4.5 服务与培训 10 分。
""", encoding="utf-8")

# data export
(ROOT / "data").mkdir(exist_ok=True)
(ROOT / "data" / "cases.json").write_text(json.dumps(CASES, ensure_ascii=False, indent=2), encoding="utf-8")

# HOME
featured = [c for c in CASES if c.get("featured")][:4]
home_body = f"""
<section class="wrap hero">
  <span class="badge">中文站 · MVP · 公开可溯源</span>
  <h1>{SITE_NAME}<br><span style="font-size:.55em;font-weight:600;color:var(--muted)">{TAGLINE}</span></h1>
  <p class="lead">{BRAND_SUB}。精选企业智能体（Agent）真实落地用例：行业、角色、工具栈、步骤、风险与来源链接一页看清。同仓附「招标 PDF → 废标项/资格/评分点」最小 Demo。</p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="cases/index.html">浏览用例目录</a>
    <a class="btn" href="demo/feibiao.html">试用废标速查 Demo</a>
    <a class="btn btn-ghost" href="#subscribe">周刊意向</a>
  </div>
</section>

<section class="wrap section">
  <h2>为什么做这个站</h2>
  <p class="desc">演示多、可验证少。我们只收录带来源链接的公开案例，方便中国企业决策者对照行业与岗位做落地选型。</p>
  <div class="grid grid-3">
    <div class="card"><h3>可溯源</h3><p class="muted">每条用例标注来源 URL；宁缺毋滥，不编造数据。</p></div>
    <div class="card"><h3>可对照</h3><p class="muted">统一字段：行业、角色、工具栈、步骤摘要、风险。</p></div>
    <div class="card"><h3>可行动</h3><p class="muted">附废标速查最小 Demo，服务招投标场景的「先看门槛」。</p></div>
  </div>
</section>

<section class="wrap section">
  <h2>精选用例</h2>
  <p class="desc">从零售、贸易、保险到客服——先看这几条完整公开材料较充分的案例。</p>
  <div class="grid grid-2">
    {''.join(case_card(c) for c in featured)}
  </div>
  <p style="margin-top:1rem"><a class="btn" href="cases/index.html">查看全部 {len(CASES)} 条 →</a></p>
</section>

<section class="wrap section" id="sponsor">
  <h2>赞助位（占位）</h2>
  <p class="desc">面向 Agent 平台、云厂商、实施商的目录赞助与周刊赞助。以下为版位示意。</p>
  <div class="grid grid-2">
    <div class="card"><div class="sponsor-slot">首页横幅赞助位 · 敬请联系</div></div>
    <div class="card"><div class="sponsor-slot">用例列表侧栏 / 周刊标头 · 敬请联系</div></div>
  </div>
</section>

<section class="wrap section" id="subscribe">
  <h2>周刊意向报名</h2>
  <p class="desc">「智体用例周刊」：每周精选可溯源落地案例与踩坑要点。当前为意向收集（未接发送服务）。</p>
  <div class="card" style="max-width:520px">
    <form class="form" data-newsletter>
      <label>工作邮箱</label>
      <input type="email" required placeholder="you@company.com"/>
      <label>关注方向（可选）</label>
      <input type="text" placeholder="如：客服 / 制造 / 招投标"/>
      <button class="btn btn-primary" type="submit">提交意向</button>
      <p class="ok-note" data-msg hidden></p>
    </form>
  </div>
</section>

<section class="wrap section">
  <h2>废标工具 · 按次定价文案占位</h2>
  <div class="card">
    <p class="muted">计划能力：上传招标文件 → 抽取废标项 / 资格门槛 / 评分点 / 截止日（带来源段落引用）。</p>
    <p><strong>定价占位</strong>：¥9.9 / 次试跑 · ¥99 / 包月 20 次 · 企业私有化另议。</p>
    <p class="danger-note">输出仅供辅助，须人工复核；不构成法律或投标意见；不保证防废标。</p>
    <a class="btn" href="demo/feibiao.html">打开 Demo</a>
  </div>
</section>
"""
(ROOT / "index.html").write_text(page(SITE_NAME, home_body, prefix="", active="home"), encoding="utf-8")

# CASES INDEX
industries = sorted(set(c["industry"] for c in CASES))
opts = ''.join(f'<option value="{i}">{i}</option>' for i in industries)
cases_body = f"""
<section class="wrap section" style="padding-top:2rem">
  <div class="breadcrumbs"><a href="../index.html">首页</a> / 用例目录</div>
  <h2>用例目录</h2>
  <p class="desc">共 <strong>{len(CASES)}</strong> 条公开可溯源用例。指标来自原文披露，跨案例勿直接对比。</p>
  <div class="filters">
    <select id="filter-industry"><option value="">全部行业</option>{opts}</select>
    <input id="filter-q" type="search" placeholder="搜索标题 / 角色 / 工具…"/>
  </div>
  <div class="grid grid-2" data-case-list>
    {''.join(case_card(c, prefix="../") for c in CASES)}
  </div>
</section>
"""
# fix case_card links when prefix is ../ — case_card uses prefix+cases/id — for list page we need prefix ../ and href cases/id -> wait
# On cases/index.html, link should be just {id}.html not ../cases/{id}.html
# Let me fix: for list page, pass a custom prefix for cards

def case_card_list(c):
    featured = '<span class="tag green">精选</span>' if c.get("featured") else ""
    return f"""
<article class="card case-card" data-industry="{c['industry']}" data-role="{c['role']}">
  <div class="meta">{featured}<span class="tag">{c['industry']}</span></div>
  <h3><a href="{c['id']}.html">{c['title']}</a></h3>
  <p>{c['summary'][:130]}…</p>
  <p class="source">来源：<a href="{c['source_url']}" target="_blank" rel="noopener">{c['source_name']}</a></p>
</article>
"""

cases_body = f"""
<section class="wrap section" style="padding-top:2rem">
  <div class="breadcrumbs"><a href="../index.html">首页</a> / 用例目录</div>
  <h2>用例目录</h2>
  <p class="desc">共 <strong>{len(CASES)}</strong> 条公开可溯源用例。指标来自原文披露，跨案例勿直接对比。</p>
  <div class="filters">
    <select id="filter-industry"><option value="">全部行业</option>{opts}</select>
    <input id="filter-q" type="search" placeholder="搜索标题 / 角色 / 工具…"/>
  </div>
  <div class="grid grid-2" data-case-list>
    {''.join(case_card_list(c) for c in CASES)}
  </div>
</section>
"""
(CASES_DIR / "index.html").write_text(page("用例目录", cases_body, prefix="../", active="cases"), encoding="utf-8")

# individual cases
for c in CASES:
    steps = ''.join(f"<li>{s}</li>" for s in c["steps"])
    extra = ""
    if len(c.get("source_urls", [])) > 1:
        extra = "<ul>" + ''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{u}</a></li>' for u in c["source_urls"]) + "</ul>"
    else:
        extra = f'<p><a href="{c["source_url"]}" target="_blank" rel="noopener">{c["source_url"]}</a></p>'
    body = f"""
<section class="wrap section" style="padding-top:2rem">
  <div class="breadcrumbs"><a href="../index.html">首页</a> / <a href="index.html">用例目录</a> / {c['title'][:20]}…</div>
  <h1 style="font-size:1.6rem;margin:0 0 .6rem">{c['title']}</h1>
  <div class="meta">
    <span class="tag">{c['industry']}</span>
    <span class="tag orange">{c['role']}</span>
    {"<span class='tag green'>精选</span>" if c.get("featured") else ""}
  </div>
  <div class="card" style="margin-top:1rem">
    <dl class="kv">
      <dt>行业</dt><dd>{c['industry']}</dd>
      <dt>角色</dt><dd>{c['role']}</dd>
      <dt>工具栈</dt><dd>{c['stack']}</dd>
    </dl>
    <h3>摘要</h3>
    <p>{c['summary']}</p>
    <h3>步骤摘要</h3>
    <ol class="steps">{steps}</ol>
    <h3>风险与注意</h3>
    <p class="note">{c['risks']}</p>
    <h3>来源</h3>
    <p>{c['source_name']}</p>
    {extra}
  </div>
  <p style="margin-top:1rem"><a class="btn" href="index.html">← 返回目录</a></p>
</section>
"""
    (CASES_DIR / f"{c['id']}.html").write_text(page(c["title"], body, prefix="../", active="cases", desc=c["summary"]), encoding="utf-8")

# DEMO page
demo_body = """
<section class="wrap section" style="padding-top:2rem">
  <div class="breadcrumbs"><a href="../index.html">首页</a> / 废标速查 Demo</div>
  <h2>废标速查 Demo</h2>
  <p class="desc">上传区为前端示意；请运行内置样例，查看「废标项 / 资格门槛 / 评分点 / 截止日」结构化输出（带来源章节引用）。</p>
  <div class="danger-note">人工复核必做。本工具不保证防废标，不构成法律或投标意见。</div>

  <div class="grid grid-2" style="margin-top:1.2rem">
    <div class="card">
      <h3>1. 上传招标文件（示意）</h3>
      <div class="upload-box">
        <p>拖拽 PDF / Word / 文本，或点击选择</p>
        <input id="tender-file" type="file" accept=".pdf,.doc,.docx,.txt"/>
        <p class="muted" id="upload-hint" style="margin-top:.6rem">MVP 不解析真实上传文件，仅示意交互。</p>
      </div>
      <p style="margin-top:1rem" class="muted">按次定价占位：¥9.9/次 · ¥99/月20次 · 企业版另议</p>
    </div>
    <div class="card">
      <h3>2. 运行内置样例</h3>
      <p class="muted">样例文本见 <code>demo/sample-tender.txt</code>，结构化结果见 JSON。</p>
      <button class="btn btn-primary" id="run-sample" type="button">运行内置样例</button>
      <p style="margin-top:.8rem"><a href="sample-tender.txt" target="_blank">查看样例原文</a></p>
    </div>
  </div>

  <div class="card" style="margin-top:1rem">
    <h3>结构化输出</h3>
    <div id="demo-result" hidden></div>
    <p class="muted" id="demo-placeholder">点击「运行内置样例」后在此展示。</p>
  </div>
</section>
<script>
document.getElementById('run-sample') && document.getElementById('run-sample').addEventListener('click', function(){
  var p = document.getElementById('demo-placeholder'); if(p) p.hidden = true;
});
</script>
"""
(DEMO / "feibiao.html").write_text(page("废标速查 Demo", demo_body, prefix="../", active="demo"), encoding="utf-8")

# ABOUT
about_body = f"""
<section class="wrap section" style="padding-top:2rem">
  <div class="breadcrumbs"><a href="index.html">首页</a> / 关于与免责声明</div>
  <h2>关于 {SITE_NAME}</h2>
  <p class="desc">{TAGLINE}。由 milo（agentic business）方向拍板的 1–2 周 MVP：先可展示、可分享。</p>
  <div class="card">
    <h3>我们收录什么</h3>
    <ul>
      <li>公开报道、厂商案例页、监管/研究机构摘要中可核对的企业 Agent 落地叙述</li>
      <li>统一字段：行业、角色、工具栈、步骤、风险、来源 URL</li>
    </ul>
    <h3>我们不做什么</h3>
    <ul>
      <li>不编造用例数据或虚构来源</li>
      <li>无真实素材时不撰写「内部知本策研案例」；若需展示结构会明确标「示例结构」</li>
      <li>不对跨案例指标做简单排名</li>
    </ul>
    <h3>免责声明</h3>
    <p class="note">本站信息来自公开网络，仅供学习与商业调研参考，不构成投资、采购、投标或法律建议。案例中的效果数据以原出处为准，可能随时间变化。废标速查 Demo 输出必须经专业人员人工复核，开发者与运营方不对据此产生的任何损失负责。</p>
    <h3>联系 / 赞助 / 投稿</h3>
    <p class="muted">赞助位与周刊意向见首页表单（当前本地示意）。用例投稿请附可公开 URL。</p>
  </div>
</section>
"""
(ROOT / "about.html").write_text(page("关于", about_body, prefix="", active="about"), encoding="utf-8")

# README
readme = f"""# {SITE_NAME}

{TAGLINE}

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

当前用例数：**{len(CASES)}**

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

正式采用：**{SITE_NAME}**（候选「Agent用例港」未采用，因中英混排较长）。

副标题：{TAGLINE}

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
"""
(ROOT / "README.md").write_text(readme, encoding="utf-8")

print(f"OK: {len(CASES)} cases → {ROOT}")
for c in CASES:
    print(" -", c["id"])
