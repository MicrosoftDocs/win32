---
title: Working with computers that are not running on Windows Server
description: This topic covers some of the design considerations regarding working with computers that are not running Windows Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 90296AAE-E454-4DE4-B59D-51CB79257A45
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Working with computers that are not running on Windows Server

This topic covers some of the design considerations regarding working with computers that are not running Windows Server.

There are some subtle differences between CIM Object Manager (CIMOM) servers that impact the user experience. A developer who is using CDXML to create cmdlets that manage a server running on server software other than Windows Server should be aware of the server configuration and capabilities.

-   Query capability - If the server does not support server filtering using WQL, then EnumerateInstance operations can be used instead of QueryInstances. In this case, the filtering happens on the client.
-   SchemaRetrievalSupport - Windows implements class schema retrieval (EnumerateClasses and GetClass) operations that provide a rich client experience. Not all end-points support this functionality.
-   Handling ShouldProcess (WhatIf or Confirm) - This should be implemented on the client instead of relying on a provider to do it. This is also applicable to WMI providers that have not implemented MI\_ShouldProcess (such as all legacy WMI providers in the root/cimv2 namespace).
-   Changing the namespace at runtime.

The following CDXML elements are used to describe the information outlined above.

``` syntax
<CmdletAdapterPrivateData>
```

 

 




