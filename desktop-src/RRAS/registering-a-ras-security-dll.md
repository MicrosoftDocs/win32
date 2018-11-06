---
title: Registering a RAS Security DLL
description: The setup program for a RAS security DLL must register the DLL with the Windows NT/Windows 2000 RAS server.
ms.assetid: 90a1f30e-ea68-4859-b436-219c25016677
ms.topic: article
ms.date: 05/31/2018
---

# Registering a RAS Security DLL

The setup program for a RAS security DLL must register the DLL with the Windows NT/Windows 2000 RAS server. Only one RAS security DLL can be registered as support for multiple security DLLs is not provided. To register a RAS security DLL, set the *DLLPath* value under the following key in the registry:

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         RAS
            SecurityHost
```



| Value name | Value data                                                                                                                                                   |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *DLLPath*  | A **REG\_SZ** string that contains the path of the DLL. This string should specify the full path unless the DLL is in a directory listed in the system path. |



 

The setup program for a RAS security DLL must also provide remove/uninstall functionality. If a user removes the DLL, the setup program must delete the *DLLPath* value from the registry. The RAS service does not start if the *DLLPath* value specifies a DLL that cannot be found.

A RAS security DLL must export the [**RasSecurityDialogBegin**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialogbegin) and [**RasSecurityDialogEnd**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialogend) functions.

 

 




