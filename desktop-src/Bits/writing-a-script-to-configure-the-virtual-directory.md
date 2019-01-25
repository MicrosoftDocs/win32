---
title: Writing a Script to Configure the Virtual Directory
description: Writing a Script to Configure the Virtual Directory
ms.assetid: 0324fbc8-1d64-454c-b021-4e010edcac8d
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Writing a Script to Configure the Virtual Directory

You can use the default BITS IIS property values to upload a file to the server. The upload file is written to the URL as specified in the remote file name of the job. To upload the file to a server application and receive a reply, change the [BITSServerNotificationType](bits-iis-extension-properties.md) property to send the data by reference (sends the name of the file that contains the data) or by value (sends the data in the body of the request).

For a list and description of the properties that you can modify, see [BITS IIS Extension Properties](bits-iis-extension-properties.md). Use the methods of the [**IBITSExtensionSetup**](/windows/desktop/api/Bitscfg/nn-bitscfg-ibitsextensionsetup) interface to enable and disable the virtual directory for uploads.

The following example shows how to use Windows Script Host to create, configure, and enable an IIS virtual directory for BITS uploads.


```JScript
if (WScript.Arguments.length < 2)
{
    WScript.Echo("Usage: bitsvdir virtual_directory local_directory");
    WScript.Quit(1);
}

VirtualDirectoryName = WScript.Arguments(0);
LocalDirectoryName = WScript.Arguments(1);

ServerObj = GetObject("IIS://LocalHost/W3SVC/1/ROOT");
VirtualDir = ServerObj.Create("IIsWebVirtualDir", VirtualDirectoryName );

VirtualDir.Path = LocalDirectoryName;
VirtualDir.AppIsolated = 0;
VirtualDir.AccessScript = true;
VirtualDir.AccessRead = false;
VirtualDir.AccessWrite = false;
VirtualDir.SetInfo();

//Set BITS specific IIS configuration settings
VirtualDir.EnableBITSUploads();
VirtualDir.BITSMaximumUploadSize = "4294967296";
VirtualDir.SetInfo();

WScript.Echo( "Created virtual directory " + VirtualDirectoryName + 
              " with a local directory of " + LocalDirectoryName );
WScript.Quit( 0 );
```



To change the previous example to upload the data to a server application, add the following code before **SetInfo**.


```JScript
VirtualDir.BITSServerNotificationType = 1;
VirtualDir.BITSServerNotificationURL = "https://myserver/mypath/myasp.asp";
```



The location of the upload file is passed to the server application, myasp.asp, in the BITS-Request-DataFile-Name header. To receive the upload file in the body of the request, set the [BITSServerNotificationType](bits-iis-extension-properties.md) property to 2.

For information on receiving the upload data in your server application, see [Using BITS Notification Request/Response Headers](using-bits-notification-request-response-headers.md).

 

 




