#!/usr/bin/env ruby
# Find the regular expression that starts with h ends
#+ with n and can have any single character in between.

puts ARGV[0].scan(/h[a-zA-Z0-9]n/).join
