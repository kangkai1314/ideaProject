#--*-- coding:utf-8 --*--
import sys,os
import time


def main():
    if len(sys.argv)<0 or len(sys.argv)>4:
        print 'Usage:python project_name'
        sys.exit()
    else:
        project_name=sys.argv[1]
        spidername=sys.argv[2]
        domain_name=sys.argv[3]

        cmd='scrapy startproject %s'%(project_name)
        ret=os.system(cmd)
        time.sleep(5)
        cmd='scrapy genspider %s %s'%(spidername,domain_name)
        print cmd
        ret=os.system(cmd)

if __name__ == '__main__':
    main()