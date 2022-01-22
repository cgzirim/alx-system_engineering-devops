#!/usr/bin/env ruby
# Find regular expression that match only capital letters.

puts ARGV[0].scan(/[A-Z]/).join
