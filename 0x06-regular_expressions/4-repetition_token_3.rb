#!/usr/bin/env ruby
# Find the regular expression that will match hbn, hbt...tn.

puts ARGV[0].scan(/hbt*n/).join
