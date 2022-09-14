---
title: Notification Protocol for Server Applications
description: BITS uses the BITSServerNotificationType property to determine how BITS sends the contents of the upload file to the server application.
ms.assetid: d5193d0c-3ab4-47ab-a570-fea2904a4371
ms.topic: article
ms.date: 05/31/2018
---

# Notification Protocol for Server Applications

BITS uses the [BITSServerNotificationType](bits-iis-extension-properties.md) property to determine how BITS sends the contents of the upload file to the server application. If the BITSServerNotificationType property is set to 1, [BITS passes the location of the upload file in a header](#sending-the-location-of-the-upload-file-in-a-header). If the BITSServerNotificationType property is set to 2, [BITS passes the contents of the upload file in the body of the request](#sending-the-upload-file-in-the-body-of-the-request).

For details on how BITS handles errors from the server application, see [Handling server application errors](#handling-server-application-errors).

## Sending the location of the upload file in a header

BITS passes the location of the upload and reply files to the server application in the headers if the [BITSServerNotificationType](bits-iis-extension-properties.md) property is set to 1. The server application opens the upload file, processes the data, and then generates the reply file. By default, BITS removes the upload and reply files from the server after it receives the response from the server application. To have BITS copy the upload file to the location specified by the remote file name in the job, include the BITS-Copy-File-To-Destination header in your response. If you do not include the header and you want to save the upload and reply files, you must copy the upload and reply files to a new location before responding. The following table shows the request headers.



| Request header              | Description                                                                                |
|-----------------------------|--------------------------------------------------------------------------------------------|
| BITS-Original-Request-URL   | Contains the remote name specified in the job.                                             |
| BITS-Request-DataFile-Name  | Contains the full path to the uploaded data.                                               |
| BITS-Response-DataFile-Name | Contains the full path to where BITS expects the server application to write the response. |



 

The following table shows the response headers.



| Response header               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BITS-Static-Response-URL      | Optional. Contains the absolute URL (do not specify a relative URL) to a static data file to use as the response. The static data file must be accessible by the BITS client. If you use this header, do not create the response file specified in the BITS-Response-DataFile-Name request header. Note that BITS does not delete this file for you.<br/>                                                                                                           |
| BITS-Copy-File-To-Destination | Optional. By default, if the [BITSServerNotificationType](bits-iis-extension-properties.md) property is set to 1 or 2, the BITS server does not copy the upload file to the location specified by the remote file name in the job. To have BITS copy the file to the location specified by the remote file name in the job, send this response header. You can specify any value; BITS does not use the value. Note that the folders in the remote file path must exist. |



 

The following request shows BITS sending the location of the upload file to the server application.

``` syntax
POST https://myserver/myvdir/handle_upload.asp?ACCOUNT=873112 HTTP/1.1
Host: myserver
BITS-Original-Request-URL: https://front-end-server/vdir
BITS-Request-DataFile-Name: c:\physical-path\BITS-Sessions\{5e53c221-f2d6-4bf2-
b994-1dc43ceaca8d}\request
BITS-Response-DataFile-Name: c:\physical-path\BITS-Sessions\{5e53c221-f2d6-4bf2-
b994-1dc43ceaca8d}\response
Content-Length: 0
```

The following shows the server application's reply to BITS; the reply is placed in the file specified by the BITS-Response-DataFile-Name request header.

``` syntax
HTTP/1.1 200 - OK
Content-Length: 0
```

## Sending the upload file in the body of the request

BITS sends the upload file in the body of the request if the [BITSServerNotificationType](bits-iis-extension-properties.md) property is set to 2. Sending the upload file in the body of the request lets existing scripts and applications work with minimal modifications. The upload file and reply file are passed in the request and response, respectively. The following table shows the request header.



| Request header            | Description                                    |
|---------------------------|------------------------------------------------|
| BITS-Original-Request-URL | Contains the remote name specified in the job. |



 

The following table shows the response headers.



| Response header               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BITS-Static-Response-URL      | Optional. Contains the absolute URL (do not specify a relative URL) to a static data file to use as the response. The static data file must be accessible by the BITS client. If you use this header, do not include the response in the stream. Note that BITS does not delete this file for you.<br/>                                                                                                                                      |
| BITS-Copy-File-To-Destination | Optional. If the [BITSServerNotificationType](bits-iis-extension-properties.md) property is set to 1 or 2, the BITS server does not copy the upload file to the location specified by the remote file name in the job. To have BITS copy the file to the location specified by the remote file name, send this response header. You can specify any value; BITS does not use the value. Note that the folders in the remote file path must exist. |



 

The following request shows BITS passing the uploaded file to the server application in the body of the request.

``` syntax
POST https://myserver/myvdir/handle_upload.asp?ACCOUNT=873112 HTTP/1.1
Host: myserver
BITS-Original-Request-URL: https://front-end-server/vdir
Content-Length: 80000

80000 bytes of upload data goes here
```

The following reply shows the server application passing the reply data to BITS in the body of the response.

``` syntax
HTTP/1.1 200 - OK
Content-Length: 100

100 bytes of reply data goes here
```

## Handling server application errors

See [Handling Server Application Errors](handling-server-application-errors.md).

 

 





