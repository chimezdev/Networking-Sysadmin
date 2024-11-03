#!/usr/bin/bash

# this is a comment
message="Hello World!"
echo $message

filename=$0
echo $filename

# how many arguments was the script called with
num_args=$#

# what wer the arguments

name=$1 
number=$2
echo "Your first two arguments were: $1 $2"
# # if statement
# if [[ "$NAME" == "Stone" ]]; then
#     echo "Hi Stone!"
# elif [[ "$NAME" == "Steve" ]]; then
#     echo $2
# else
#     echo $3
# fi 

NUM_REQUIRED_ARGS=2
if [[ $num_args -lt $NUM_REQUIRED_ARGS ]]; then
    echo "Not enough arguments. Call this script with {$0} <name> <number>"
    exit 1
fi

# for loops; iteration, string interpolation
echo "You ran this program with ${num_args} arguments. Here they are:"
for arg in "$@"; do
    echo "$arg"
done

# two ways of defining function
function_name() {
    echo
    echo "########"
    echo "$1"
    echo "########"
    echo 
}

function javatest() {
    # testing and conditionals
    if [[ $number -eq 99 ]]; then
        function_name "You win!"
    elif (( $number < 10 )); then
        function_name "You're a courageous one."

        # set a variable iteractively
        echo "Hi ${name}, to avert a horrible death, please enter the password:"
        read password

        if [[ "$password" != "Java" ]]; then
            spaced "Well, at least you're not a Java Programming sympathizer. You can go now."
        else
            function_name "DIEEEE! Actually, nevermind. Writing Java is enough \
            of a hellish punishment. You are free to leave."
        fi
    fi

}

javatest $number
exit 0
