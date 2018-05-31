---
Description: This topic describes how to disconnect from the fax server.
ms.assetid: 02d276b7-bcbc-4bbe-8051-d9b35f12dc93
title: Disconnecting from a Fax Server
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Disconnecting from a Fax Server

It is the responsibility of the calling fax client application to disconnect from the fax server.

## In the Win32 Environment

A fax client application must call the [**FaxClose**](-mfax-faxclose.md) function as the last function before it terminates. The function disconnects the calling application from the fax server by deallocating the following handles.

-   Fax server handles returned by calls to the [**FaxConnectFaxServer**](-mfax-faxconnectfaxserver.md) function
-   Fax port handles returned by calls to the [**FaxOpenPort**](-mfax-faxopenport.md) function

## In the COM Implementation Environment

If you are writing a C/C++ application, call the [**IFaxServer::Disconnect**](-mfax-ifaxserver-client-mfax-ifaxserver-disconnect-client-cpp.md) method to terminate the connection to a fax server. Then call the [IUnknown::Release](http://msdn.microsoft.com/en-us/library/ms682317.aspx) method to allow the [**FaxServer**](-mfax-faxserver.md) object to deallocate itself. You may also need to call IUnknown::Release again to destroy additional interface pointers.

If you are writing a Microsoft Visual Basic application, you must call the [**Disconnect**](-mfax-faxserver-cpp-mfax-faxserver-disconnect-cpp.md) method of the [**FaxServer**](-mfax-faxserver.md) object to disconnect from the fax server before your application terminates.

## Related topics

<dl> <dt>

[Connecting to a Fax Server](-mfax-connecting-to-a-fax-server.md)
</dt> </dl>

 

 



