---
title: BITS Provider
description: The Background Intelligent Transfer Service (BITS) Compact Server with BITS Remote Management allows authenticated administrators or controller applications to create, modify and manage BITS transfer jobs remotely without using the Internet Information Services (IIS) service.
ms.assetid: f9d5c956-826c-4f50-951f-37dbe1f81480
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BITS Provider

The Background Intelligent Transfer Service (BITS) Compact Server with BITS Remote Management allows authenticated administrators or controller applications to create, modify and manage BITS transfer jobs remotely without using the Internet Information Services (IIS) service. The BITS provider can also be used to enable an application to remotely use the BITS client in conjunction with the BITS Compact Server to transfer files from one remote computer to another remote computer.

> [!Note]  
> The BITS provider can create BITS transfer jobs only if the job owner is one of the service accounts: "LocalSystem", "LocalService" or "NetworkService".

 

The BITS provider is available after the BITS Compact Server is installed. For more information about installing the Compact Server, see the [BITS Compact Server](http://go.microsoft.com/fwlink/p/?linkid=154264) documentation.

The BITS provider is a standard Windows Management Instrumentation (WMI) provider that supplies classes, methods, and properties to remotely manage BITS transfer jobs and the Compact Server service. For more information about the role of WMI providers, see [WMI Architecture](https://msdn.microsoft.com/library/aa394553).



| Class                                                              | Description                                                                                                                   |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**BitsClientFile**](bitsclientfile.md)                           | Represents client file information, which is an embedded object property in the [**BitsClientJob**](bitsclientjob.md) class. |
| [**BitsClientJob**](bitsclientjob.md)                             | Provides methods to manage BITS transfer jobs.                                                                                |
| [**BitsCompactServerUrlGroup**](bitslightweightserverurlgroup.md) | Provides methods to manage URLs and URL groups for the BITS Compact Server.                                                   |



 

## Related topics

<dl> <dt>

[Background Intelligent Transfer Service (BITS)]( http://go.microsoft.com/fwlink/p/?linkid=155790)
</dt> <dt>

[BITS Compact Server](http://go.microsoft.com/fwlink/p/?linkid=154264)
</dt> </dl>

 

 




