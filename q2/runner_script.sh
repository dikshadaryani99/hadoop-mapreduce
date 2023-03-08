
# Hadoop-stream jar file address, input file
# address (local one), input directory address(where to copy local input files in HDFS), output directory
# address(where to store the output files in HDFS), 
# ddress of the directory where all mappers and reducers

Hadoop_stream_jar_file_add="$1"
input_file_add_local="$2"
input_dir_add_hdfs="$3"
output_dir_hdfs="$4"
add_of_map_red_files="$5"

# Hadoop_stream_jar_file_add="/opt/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar"
# input_file_add_local="/q2/input.txt"
# input_dir_add_hdfs="/ques2/"
# output_dir_hdfs="/outputques2/"
# add_of_map_red_files="./q2/"

# Hadoop_stream_jar_file_add="/opt/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar"
# input_file_add_local="./q2/input.txt"
# input_dir_add_hdfs="/ques2/"
# output_dir_hdfs="/outques2/"
# add_of_map_red_files="./q2/"



# Read input from file and store as an array
# input_file=$input_file_add_local
# echo $input_file
input=$(cat $input_file_add_local)
# # input=($(cat input.txt))
# echo $input
newinput="newinput.txt"
> $newinput
read rows_a cols_a <<< $(echo $input | tr " " "\n" | head -n 2 | paste - - -d' ')


# newinput=$(echo $input | cut -d " " -f 2-)
# echo $newinput
# # echo "a1=$var1, b1=$var2"

# no_of_ele_in_a=$(($rows_a * $cols_a))
no_of_ele_in_a=$(expr $rows_a \* $cols_a)

# echo $no_of_ele_in_a

input=$(echo $input | cut -d " " -f 3-)

# echo $input


elements_of_a_matrix=$(echo $input | cut -d " " -f 1-$no_of_ele_in_a)
# echo $elements_of_a_matrix
# echo $input
temp=$(($no_of_ele_in_a + 1)) 
input_for_matrix_b=$(echo $input | cut -d " " -f $temp-)

read rows_b cols_b <<< $(echo $input_for_matrix_b | tr " " "\n" | head -n 2 | paste - - -d' ')

no_of_ele_in_b=$(expr $rows_b \* $cols_b)

# echo $no_of_ele_in_a

input_for_matrix_b=$(echo $input_for_matrix_b | cut -d " " -f 3-)



elements_of_b_matrix=$(echo $input_for_matrix_b | cut -d " " -f 1-$no_of_ele_in_b)


# echo $rows_a
# echo $cols_a
# echo $elements_of_a_matrix
# echo $rows_b
# echo $cols_b
# echo $elements_of_b_matrix

# read rows_b cols_b <<< $(echo $ | tr " " "\n" | head -n 2 | paste - - -d' ')


# # Loop over each row and column of the matrix A
for i in $(seq 1 $rows_a); do
  for j in $(seq 1 $cols_a); do
    # Calculate the index of the current element in the input string
    index=$((($i - 1) * $cols_a + $j))

    # Extract the value of the current element from the input string
    value=$(echo $elements_of_a_matrix | cut -d ' ' -f $index)

    # Print the row index, column index, and value of the current element
    echo "A $cols_b $i $j $value $rows_a $cols_b" >>  $newinput
  done
done



for i in $(seq 1 $rows_b); do
  for j in $(seq 1 $cols_b); do
    # Calculate the index of the current element in the input string
    index=$((($i - 1) * $cols_b + $j))

    # Extract the value of the current element from the input string
    value=$(echo $elements_of_b_matrix | cut -d ' ' -f $index)

    # Print the row index, column index, and value of the current element
    echo "B $rows_a $i $j $value $rows_a $cols_b" >>  $newinput
  done
done

# cat $newinput



#############################33      DOCKER COMMANDS     ############################################33

# cd ~/docker-hadoop-python


# echo "Current directory is: $(pwd)"
# sudo docker-compose up -d


# # cd ~/$add_of_map_red_files

# # echo "Current directory is: $(pwd)"

# sudo docker cp ~/$add_of_map_red_files/mapper.py namenode:mapper.py
# sudo docker cp ~/$add_of_map_red_files/reducer.py namenode:reducer.py
# echo "Current directory is: $(pwd)"
# sudo docker cp ./newinput.txt namenode:input.txt



# sudo docker exec  namenode hdfs dfs -mkdir -p $input_dir_add_hdfs
# sudo docker exec  namenode hdfs dfs -copyFromLocal ./newinput.txt $input_dir_add_hdfs

# hdfs dfs -mkdir -p $input_dir_add_hdfs
# hdfs dfs -copyFromLocal ./newinput.txt $input_dir_add_hdfs

# hadoop jar $Hadoop_stream_jar_file_add -input input.txt -output $output_dir_hdfs -mapper "python3 mapper.py" -reducer "python3 reducer.py" -file mapper.py -file reducer.py
# sudo docker-compose down

hdfs dfs -mkdir -p $input_dir_add_hdfs/
hdfs dfs -copyFromLocal  $newinput $input_dir_add_hdfs/

hadoop jar  $Hadoop_stream_jar_file_add -input $input_dir_add_hdfs/$newinput -output $output_dir_hdfs/ -mapper "python3 mapper.py" -reducer "python3 reducer.py" -file $add_of_map_red_files/mapper.py -file $add_of_map_red_files/reducer.py
