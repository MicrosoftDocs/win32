---
title: Using the Cell Directory Service (CDS)
description: If you have CDS, you can use it instead of Microsoft Locator.
ms.assetid: df4b8db1-08f1-4ed8-895d-236199289e87
keywords:
- Remote Procedure Call RPC , tasks, using cell directory service
ms.topic: article
ms.date: 05/31/2018
---

# Using the Cell Directory Service (CDS)

If you have CDS, you can use it instead of Microsoft Locator. Change the registry entries as shown:

``` syntax
HKEY_LOCAL_MACHINE
    Software
        Microsoft
            Rpc
                Name Service
                    NetworkAddress
 
HKEY_LOCAL_MACHINE
    Software
        Microsoft
            Rpc
                Name Service
                    Endpoint
```

Changing these entries will point to a gateway computer that is running the NSID. This will be used as the master locator. In the event of a crash, there will be no search for a replacement.

 

 




