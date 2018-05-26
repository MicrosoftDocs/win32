---
Description: Windows loads and executes the standard Microsoft GINA DLL (MSGina.dll). To load a different GINA, you must alter a registry key value.
ms.assetid: 408511af-4430-4dd7-a2a1-c32b375821c4
title: Loading and Running a GINA DLL
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Loading and Running a GINA DLL

Windows loads and executes the standard Microsoft GINA DLL (MSGina.dll). To load a different [*GINA*](security.g_gly#-security-gina-gly), you must alter the following registry key value:

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows NT
            CurrentVersion
               Winlogon
                  GinaDLL<dl>
<dt>

                  Data type
</dt>
<dd>                  REG_SZ</dd>
</dl>
```

If the GinaDLL key value is present, it must contain the name of a GINA DLL, which [*Winlogon*](security.w_gly#-security-winlogon-gly) will load and use.

## Related topics

<dl> <dt>

[Building and Testing a GINA DLL](building-and-testing-a-gina-dll.md)
</dt> <dt>

[GINA Export Functions](authentication-functions.md#gina-export-functions)
</dt> <dt>

[GINA Structures](authentication-structures.md#gina-structures)
</dt> <dt>

[Terminal Services GINA Functions](terminal-services-gina-functions.md)
</dt> </dl>

 

 



