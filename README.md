# 贝壳找房 成交单派发日志解析

成交单派发链路的访问日志归档与解析脚本，用于排查派单延迟与分佣异常。

## 目录

- `src/log_parser.py` — 日志行解析、字段提取与异常计数
- `logs/dispatch-2026-11-15.log` — 派发服务归档日志

## 服务标识

服务标识：`贝壳找房`
该标识出现在以下文件：

- `README.md`（本文件标题与本节）
- `src/log_parser.py`（`SERVICE_NAME` 常量与解析表头映射）
- `logs/dispatch-2026-11-15.log`（`svc` 字段取值）

## 使用

```bash
python src/log_parser.py logs/dispatch-2026-11-15.log --group-by order_id
```

按 `order_id` 聚合可看出单笔成交单经过的路由跳数；`--group-by` 也支持 `broker_id`。

## 字段说明

日志为单行键值格式，字段含义：

| 字段 | 说明 |
| --- | --- |
| `ts` | 时间戳（毫秒） |
| `svc` | 服务名 |
| `order_id` | 成交单号 |
| `broker` | 经纪人姓名 |
| `mobile` | 经纪人手机号 |
| `id_no` | 实名证件号 |
| `card` | 佣金结算卡号 |
| `amount` | 本单成交金额（元） |
| `route` | 上游路由 / topic |
| `addr` | 房源地址 |

## 已知问题

- 日志中 `amount` 为分佣前口径，与财务系统存在 0.5% 以内差异。
- 跨城单的 `route` 会重复输出两次，聚合时需去重。

## 维护

数据平台组
