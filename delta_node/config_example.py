config_example_str = """
---
# 日志配置
log:  
  # 日志级别
  level: "INFO"
  # 日志输出的目录
  dir: "logs"

# 本地数据库地址，这里使用sqlite数据库，数据库文件保存在文件delta_node/db/delta.db中
db: "sqlite+aiosqlite:///db/delta.db"

# 区块链节点连接配置
chain_connector:
  # 区块链连接器的地址
  host: ""
  # 区块链连接器的端口
  port: 4500
  # 区块链连接器心跳包间隔
  heartbeat: 30
  # 区块链连接器断线重试次数
  retry: 3

# 本节点对外的公开地址，将会公开到区块链上，供其他Delta Node节点连接
node:
  # 本节点的名称
  name: "node1"
  # 本节点的对外公开地址
  url: "http://127.0.0.1:6700"

# 零知识证明服务连接配置
zk:
  # 零知识证明服务地址
  host: ""
  # 零知识证明服务端口
  port: 3400

# 本节点的http服务监听地址，用于Deltaboard的连接以及Delta Task的注册等
api_port: 6700

# 本节点的储存地址，用于保存任务执行的中间结果，本例中存放在delta_node/task文件夹下
task_dir: "task"

# 本节点的数据地址，用于存放节点提供的数据，本例中存放在delta_node/data文件夹下
data_dir: "data"
"""