import boto3
import botocore
from pdf2image import convert_from_bytes

s3 = boto3.client('s3')
response = s3.list_buckets()

s3_Resource = boto3.resource('s3')
source = 'pdf-jibanendu'
destination ='jibanendu-img'

bucketObject = s3_Resource.Bucket(source)

#DB Operations for InProgress Status 


#Reading the PDF and converting it to Image
for objSummary in bucketObject.objects.all():
	print(objSummary.key)
	fileName = objSummary.key.split(".")
	if fileName[1] =='pdf' :
		file_byte_string= s3.get_object(Bucket=source, Key=objSummary.key)['Body'].read()
		images = convert_from_bytes(file_byte_string, fmt='png')
		count=0
		for img in images: 
			s3.put_object(Bucket=destination,Body='',Key=fileName[0]+'/'+str(count)+'.png')
			count=count+1


#DB Operations for Final /Error Status 

