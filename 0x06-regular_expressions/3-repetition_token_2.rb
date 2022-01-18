#!/usr/bin/env ruby
# Find the regular expression that will match hbtn - hbttttn.

puts ARGV[0].scan(/hbt+n/).join
