---
title: Persistent Handlers Registered for a Class
description: Persistent Handlers Registered for a Class
ms.assetid: c74988c7-a6ae-46ad-97e8-f15d1d9036bd
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Persistent Handlers Registered for a Class

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following is an example of the registry entry for a persistent handler registered for a class.

``` syntax
\HKEY_LOCAL_MACHINE\SOFTWARE\Classes
 
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
 
        {A6317C60-0386-11D0-AE19-00AA004B9986}
           = REG_SZ Sample file persistent handler
           PersistentAddinsRegistered
              {89BCB740-6119-101A-BCB7-00DD010655AF}
                 = REG_SZ {D7455400-0386-11D0-AE19-00AA004B9986}
 
        {D7455400-0386-11D0-AE19-00AA004B9986}
           = REG_SZ Sample files
           InprocServer32
              = REG_SZ sampfilt.dll
              ThreadingModel = Apartment
```

Up through the entry for the class (CLSID\\{40A45370-0386-11D0-AE19-00AA004B9986}), these entries are standard OLE registry entries. The DLL sample.dll implements running object behavior for the .sam class. But note the extra entry, **PersistentHandler**. This entry specifies the class responsible for brokering requests to the persistent objects of the sample class. The entry under **PersistentAddinsRegistered** identifies the implementation responsible for the interface named 89BCB740-6119-101A-BCB7-00DD010655AF (**IID\_IFilter**). Finally, we come to the class implementing **IID\_IFilter** and again, the entries are standard OLE registry entries. The InprocServer32 DLL is loaded through the standard OLE mechanism. Indexing Service observes the threading model specified for the filter. When the threading model is set to "Both," the filter must be thread safe. If the filter is not thread safe, specify "Apartment."

 

 




