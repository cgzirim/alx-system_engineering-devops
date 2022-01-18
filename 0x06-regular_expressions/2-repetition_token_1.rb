#!/usr/bin/env ruby
# Find the regular expression that match the case htn or hbtn.

puts ARGV[0].scan(/hb?tn/).join
