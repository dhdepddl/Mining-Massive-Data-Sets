#Hadoop version
hadoop 2.8.0
Subversion https://git-wip-us.apache.org/repos/asf/hadoop.git -r 91f2b7a13d1e97be65db92ddabc627cc29ac0009
Compiled by jdu on 2017-03-17T04:12Z
Compiled with protoc 2.5.0
From source with checksum 60125541c2b3e266cbf3becc5bda666
This command was run using /usr/local/Cellar/hadoop/2.8.0/libexec/share/hadoop/common/hadoop-common-2.8.0.jar


#Running python mapreduce file
Running python mapreduce file uses hadoop streaming API - "hadoop-streaming\*.jar"

$bin/hadoop jar /usr/local/Cellar/hadoop/2.8.0/libexec/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar" \
    -mapper path/to/mapper.py -reducer path/to/reducer.py \
    -input path/to/input/file/in/hdfs -output path/to/output/in/hdfs


