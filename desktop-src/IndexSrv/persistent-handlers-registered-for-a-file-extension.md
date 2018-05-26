---
title: Persistent Handlers Registered for a File Extension
description: Persistent Handlers Registered for a File Extension
ms.assetid: 5caba9a1-b8ff-4200-97cf-802556c9403a
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Persistent Handlers Registered for a File Extension

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following is an example of the registry entry for a persistent handler registered for a file name extension.

``` syntax
\HKEY_CLASSES_ROOT\
 
    .sam
        = REG_SZ SampleFile
 
    SampleFile
        = REG_SZ Class for Sample Files
        CLSID
           = REG_SZ {40A45370-0386-11D0-AE19-00AA004B9986}
    CLSID
        {40A45370-0386-11D0-AE19-00AA004B9986}
           = REG_SZ Sample Files
           InprocServer32
              = REG_SZ sample.dll
           PersistentHandler
               = REG_SZ {A6317C60-0386-11D0-AE19-00AA004B9986}
...
```

The remaining content is as in the [Persistent Handlers Registered for a Class](persistent-handlers-registered-for-a-class.md) example.

 

 




