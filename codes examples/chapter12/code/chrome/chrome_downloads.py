#!usr/bin/env python3

import sqlite3
import datetime
import optparse

def fixDate(timestamp):
    epoch_start = datetime.datetime(1601,1,1)
    delta = datetime.timedelta(microseconds=int(timestamp))
    return epoch_start + delta

def getMetadataHistoryFile(locationHistoryFile):
	sql_connect = sqlite3.connect(locationHistoryFile)
	for row in sql_connect.execute('SELECT target_path, referrer, start_time, end_time, received_bytes FROM downloads;'):
		print ("Download:",str(row[0]))
		print ("\tFrom:",str(row[1]))
		print ("\tStarted:",str(fixDate(row[2])))
		print ("\tFinished:",str(fixDate(row[3])))
		print ("\tSize:",str(row[4]))
	
def main():
    parser = optparse.OptionParser('--location <target location>')
    parser.add_option('--location', dest='location', type='string', help='specify target location')
    (options, args) = parser.parse_args()
    location = options.location
    getMetadataHistoryFile(location)

if __name__ == '__main__':
    main()
