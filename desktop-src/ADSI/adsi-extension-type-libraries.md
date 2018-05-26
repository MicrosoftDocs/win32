---
title: ADSI Extension Type Libraries
description: The type libraries for extensions are not merged.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 33cde2fe-9b90-4f63-a215-cf0c8f8defb1
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- ADSI Extension Type Libraries ADSI
- extensions ADSI , extension type libraries
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ADSI Extension Type Libraries

The type libraries for extensions are not merged. ADSI clients must specifically include the type library for each extension. The type library is required for Visual Basic to enable early bindings. Client applications written in C/C++ can call the **QueryInterface** method on the extension interfaces defined in the extension header files.

 

 




