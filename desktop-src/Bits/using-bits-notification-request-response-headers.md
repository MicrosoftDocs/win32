---
title: Using BITS Notification Request/Response Headers
description: BITS can send the location of the upload file (by reference) to your server application or it can send the upload file in the body of the request (by value).
ms.assetid: b80f9077-54e7-4d10-909a-dee7d8822627
ms.topic: article
ms.date: 11/29/2018
---

# Using BITS Notification Request/Response Headers

BITS can send the location of the upload file (by reference) to your server application or it can send the upload file in the body of the request (by value). To specify how BITS sends the upload file to your server application, set the IIS metabase property, [**BITSServerNotificationType**](bits-iis-extension-properties.md). If you specify by reference, BITS passes the location of the file in the BITS-Request-DataFile-Name header. To send a reply, create and write your response to the file specified in the BITS-Response-DataFile-Name header.

Server applications that send the same reply to many clients should use by reference, so there is only one copy of the reply on the server. For example, in a software update application, the client would upload its software configuration to the server application. The server application determines which package the client needs and sends the URL of the package to BITS. Then, BITS downloads the package as the reply.

Server applications that generate unique replies for each client should use by value. For example, a server application that supports the purchase of music files would need to send a signed music file to the client. Because the signed music file is unique to the client, the server application would not store it on the server. By value is also useful for an application that is already written to accept web client data directly.

For details on the request and response headers used between BITS and your server application, see [Notification Protocol for Server Applications](notification-protocol-for-server-applications.md).

The following JavaScript example shows how to access the request and response files in a server application that uses by reference notification (BITS passes the location of the files in the headers).


```JavaScript
  var fso = new ActiveXObject ("Scripting.FileSystemObject")
  var requestFileName = Request.ServerVariables ("HTTP_BITS-Request-DataFile-Name")
  var responseFileName = Request.ServerVariables ("HTTP_BITS-Response-DataFile-Name")
  var requestStream
  var responseStream
  var ForReading = 1
  var ForWriting = 2
  var TristateUseDefault = -2

  //Open the upload data file as text stream for reading.
  requestStream = fso.OpenTextFile(requestFileName, ForReading, false, TristateUseDefault);

  //Do something with the uploaded data.

  //Close the upload stream.
  requestStream.Close()

  //Open response data file as text stream for writing.
  responseStream = fso.OpenTextFile(responseFileName, ForWriting, true, TristateUseDefault);

  //Write a response to the response file.

  //Close the response text stream
  responseStream.Close()
```



If you want to use a different response file than the one specified in BITS-Response-DataFile-Name, call the **Response.AddHeader** method to add the BITS-Static-Response-URL as shown in the following example. If you specify a different response file, do not create the response file specified in BITS-Response-DataFile-Name.


```JavaScript
  Response.AddHeader "BITS-Static-Response-URL" "https://myserver/mypath/myfile"
```
 

 




