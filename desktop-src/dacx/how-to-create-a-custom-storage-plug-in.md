---
title: How to create a custom storage plug-in
description: File Classification Infrastructure (FCI) uses storage plug-ins or modules to store classification properties files.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 50DCE296-619C-46F5-8E85-1CB10C176D6B
ms.prod: windows-server-dev
ms.technology: dynamic-access-control
ms.tgt_platform: multiple
keywords:
- Dynamic Access Control developer extensibility DACx , create a custom storage plug-in
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# How to create a custom storage plug-in

File Classification Infrastructure (FCI) uses storage plug-ins or modules to store classification properties files. A few modules are provided by the system, including a plug-in to store properties in Office files. If properties need to be stored within other file types, a custom storage plug-in can be created.

Storage modules are queried when FCI reads properties for a file as well as when it writes properties for a file. Each plug-in can indicate which file extensions it can support.

### 

For more developer information, see [Developing FCI Pipeline Modules](https://msdn.microsoft.com/library/ee126210).

For more configuration information about properties, rules, and scheduling, see the TechNet article, [Working with File Classification](https://TechNet.Microsoft.Com/library/dd758765.aspx).

> [!Note]  
> A storage module code sample is not included in the Windows Server 2012 SDK.

 

## Related topics

<dl> <dt>

[Developing FCI Pipeline Modules](https://msdn.microsoft.com/library/ee126210)
</dt> <dt>

[Working with File Classification](https://TechNet.Microsoft.Com/library/dd758765.aspx)
</dt> </dl>

 

 




