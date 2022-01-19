#!/usr/bin/env ruby
# Find  [SENDER],[RECEIVER],[FLAGS] in a message transaction log.

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
