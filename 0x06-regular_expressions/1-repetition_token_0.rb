#!/usr/bin/env ruby
# Find the regular expression that will match hbttn - hbtttttn.

puts ARGV[0].scan(/hbt{2,5}n/).join
