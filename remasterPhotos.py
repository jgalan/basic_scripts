#!/usr/bin/python

import os, time
from datetime import datetime
import exifread

test = False
overwrite = True

fproblem = open("/tmp/problemFiles2", "wt")

def get_image_info(path_to_file):

    info = []

    if not os.path.isfile( path_to_file ):
        return info
    else:

        f = open( path_to_file, 'rb')

        tags = None

        try:
            tags = exifread.process_file(f)
        except:
            print "PROBLEM in file : " + path_to_file
            fproblem.write( path_to_file + "\n" )
            return []

        if not tags:
            print "PROBLEM in file : " + path_to_file
            fproblem.write( path_to_file + "\n" )
            return []

#        print "\n TAGGGS : \n"
#        print tags
#        print "\n"

        try:
#            print tags["EXIF DateTimeOriginal"]
#            print "\n"

            dateTaken = str(tags["EXIF DateTimeOriginal"])
        except:
            return []

        if dateTaken[0:5] == "0000:":
            print "PROBLEM in file : " + path_to_file
            print "Model : " + str(tags['Image Make'])
            fproblem.write( path_to_file + "\n" )
            return []

        if dateTaken[0:5] == "   0:":
            print "PROBLEM in file : " + path_to_file
            print "Model : " + str(tags['Image Make'])
            fproblem.write( path_to_file + "\n" )
            return []

        if dateTaken[0:5] == "     ":
            print "PROBLEM in file : " + path_to_file
            print "Model : " + str(tags['Image Make'])
            fproblem.write( path_to_file + "\n" )
            return []


        date_time_obj = datetime.strptime(dateTaken, '%Y:%m:%d %H:%M:%S')

        timeStamp = time.mktime(date_time_obj.timetuple())

        return [ timeStamp, str(dateTaken), str(tags['Image Make']).split()[0] ]

######################################

sourcePath = '/Volumes/Untitled/'
destinationPath = '/Volumes/SOFT/finalFotos2/'

files = []
# r=root, d=directories, f=files
for r, d, f in os.walk(sourcePath):
    for file in f:
        if '.JPG' in file:
            files.append(os.path.join(r, file))
        if '.jpg' in file:
            files.append(os.path.join(r, file))

photoArray = []
for f in files:

    print f

    imageInfo = get_image_info( f )

    if not imageInfo:
        continue

    ts = imageInfo[0]

    newFilename = datetime.fromtimestamp( ts ).strftime('%Y%m%d_%H_%M_%S')

    year = datetime.fromtimestamp( ts ).strftime('%Y')
    monthNumber = datetime.fromtimestamp( ts ).strftime('%m')
    n = "%02d" % int(monthNumber)
    month = datetime.fromtimestamp( ts ).strftime('%b')

    try:
        os.stat(destinationPath + year)
    except:
        os.mkdir( destinationPath + year)

    try:
        os.stat(destinationPath + year + "/" + n + "." + month  )
    except:
        os.mkdir( destinationPath + year + "/" + n + "." + month)

    cont = 0
    for x in photoArray:
        if x[1][0:17] == newFilename:
#            print "Is same : " + x[1][0:17]
            cont = cont + 1

    x = "%03d" % cont
    newFilename = newFilename + "_" + str( x ) + "_" + imageInfo[2] + ".jpg"

    fileInfo = [f, newFilename, year, n, month ]
    
    print fileInfo
    photoArray.append( fileInfo )

#photoArray.sort()
#print photoArray

for x in photoArray:

    fname = destinationPath + x[2] + "/" + "/" + x[3] + "." + x[4] + "/" + x[1]

    if not overwrite and os.path.isfile( fname ):
            print "FILE already exists!"
            print x[1]
            print "EXITING"
            os.exit(1)

    fileOrigin = x[0].replace( " ", "\\ " )
    fileDestiny = fname.replace( " ", "\\ " )
    command = "cp " + fileOrigin + " " + fileDestiny
    print command

    if not test:
        os.system( command )

fproblem.close()
