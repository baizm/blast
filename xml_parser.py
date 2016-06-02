import sys
import re

#usage: python xml_parser.py in_file out_file

in_file = sys.argv[1]
out_file = sys.argv[2]

output = open(out_file,'w')
print >> output, 'read'+'\t'+'hit_def'+'\t'+'hit_acc'+'\t'+'e'

with open(in_file,'r') as xml:
        for i in xml:
            if re.search('<Iteration_query-def>', i) != None:
                i = i.split('>',1)[-1]
                i = i.split('<', 1)[-2]
                query_def = i
            if re.search('No hits found', i) != None:
                i = i.split('>',1)[-1]
                i = i.split('<', 1)[-2]
                print >> output, query_def+'\t'+i
            if re.search('<Hit_def>', i) != None:
                i = i.split('>',1)[-1]
                i = i.split('<', 1)[-2]
                hit_def = i
            if re.search('<Hit_accession>', i) != None:
                i = i.split('>',1)[-1]
                i = i.split('<', 1)[-2]
                hit_acc = i       
            if re.search('<Hsp_evalue>', i) != None:
                i = i.split('>',1)[-1]
                i = i.split('<', 1)[-2]
                e_val = i
                print >> output, query_def+'\t'+hit_def+'\t'+hit_acc+'\t'+e_val 

output.close()

#modified from http://www.polarmicrobes.org/?p=753
