# HW1

## Task1
*Two pass MapReduce*
- First pass with recommend\_mapper.py, recommend\_reducer.py
- Second pass with recommend\_mapper2.py, recommend\_reducer2.py

*execute*
- First, copy soc-LiveJournal1Adj.txt to hadoop file system
  * $hdfs dfs -copyFromLocal path/to/soc-LiveJournal1Adj.txt /user/hduser/input/soc-Live
  * After this, you can check whether the input file is in hdfs or not by using
    1) in web browser, localhost:50070 'browsing file system' menu
    2) $hdfs dfs -ls /user/hduser/input/

- Run the first pass
  * {HADOOP\_HOME}/bin$hadoop jar {hadoop/lib/directory}/hadoop-streaming-\*.jar \
    -mapper path/to/recommend_mapper.py -reducer path/to/recommend_reducer.py \
    -input /user/hduser/input/soc-Live -output /user/hduser/output/soc-Live-1
  * After this, there is \_SUCCESS, part-00000 file in /user/hduser/output/soc-Live-1 directory

- Run the second pass
  * {HADOOP\_HOME}/bin$hadoop jar {hadoop/lib/directory}/hadoop-streaming-\*.jar \
    -mapper path/to/rocommend_mapper2.py -reducer path/to/recommend_reducer2.py \
    -input /user/hduser/output/soc-Live-1/part-00000 -output /user/hduser/output/soc-Live-2
  * /user/hduser/output/soc-Live-2/part-00000 file is the final result
