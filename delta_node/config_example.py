config_example_str = """
---
# 日志配置
log:  
  # 日志级别
  level: "INFO"
  # 日志输出的目录
  dir: "logs"

# 本地数据库地址，这里使用sqlite数据库，数据库文件保存在文件delta_node/db/delta.db中
db: "sqlite:///db/delta.db"

# 区块链节点连接配置
chain_connector:
  # 区块链节点地址，必填
  address: ""

# 本节点对外的公开地址，将会公开到区块链上，供其他Delta Node节点连接
node_address:
  # 节点的公网地址，必填
  host: ""
  # 节点公开地址的端口
  port: 6800

# 本节点的http服务监听地址，用于Deltaboard的连接以及Delta Task的注册等
api_port: 6700

# 本节点的储存地址，用于保存任务执行的中间结果，本例中存放在delta_node/task文件夹下
task_dir: "task"

# 本节点的数据地址，用于存放节点提供的数据，本例中存放在delta_node/data文件夹下
data_dir: "data"
"""