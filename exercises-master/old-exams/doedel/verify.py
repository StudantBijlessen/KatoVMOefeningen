from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 25)
assert_file_contents_hash_to(output_file, '49f486550bd8f87d48303ea816f906b344f6d5dab7cd782a81a9151b6336b8ed409eb436e1d8068aebd407186dc5d8bbdfb706bcc1fcee128233fa3a5f1d5036')
compute_code_for_file(output_file)
