# Hadoop_stream_jar_file_add="/opt/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar"
# input_file_add_local="/q1/input.txt"
# input_dir_add_hdfs="/bataoyrrpls/"
# output_dir_hdfs="/outputnew/"
# add_of_map_red_files="./q1/"
# newinput="output.txt"

Hadoop_stream_jar_file_add="$1"
input_file_add_local="$2"
input_dir_add_hdfs="$3"
output_dir_hdfs="$4"
add_of_map_red_files="$5"
newinput="output.txt"

input=$(cat $input_file_add_local)

# echo $input


read no_of_states value_of_p <<< $(echo $input | tr " " "\n" | head -n 2 | paste - - -d' ')
# tail -n +4 $input_file_add_local > $tempinput
temp="temp.txt"

cp $input_file_add_local $temp
sed -i '1,3d' $temp





sed -i -e "/./ s/^/$value_of_p /" "$temp" 

cp $temp $newinput



# input=$(cat $newinput)
# echo $input
hdfs dfs -mkdir -p $input_dir_add_hdfs/
hdfs dfs -copyFromLocal  $newinput $input_dir_add_hdfs/

hadoop jar  $Hadoop_stream_jar_file_add -input $input_dir_add_hdfs/$newinput -output $output_dir_hdfs/ -mapper "python3 mapper.py" -reducer "python3 reducer.py" -file $add_of_map_red_files/mapper.py -file $add_of_map_red_files/reducer.py
