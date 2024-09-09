---
title: DoNotAddAllApplicationPackagesToRestrictions
description: Determines whether RPCSS automatically appends an **ALL_APPLICATION_PACKAGES** SID to COM restrictions by default.
ms.assetid: 4DC1237E-F3EF-40EA-8E64-57320F0C4CC5
ms.topic: article
ms.date: 07/24/2023
---

# DoNotAddAllApplicationPackagesToRestrictions

Determines whether RPCSS automatically appends an **ALL_APPLICATION_PACKAGES** SID to COM restrictions by default.

## Registry entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   DoNotAddAllApplicationPackagesToRestrictions = value
```

## Remarks

This is a **REG_DWORD** value.

| Value | Description |
|-|-|
| 0 | Disables Windows Store apps upon migration from Windows 7 to Windows 8. |
| 1 | Does not add the **ALL_APPLICATION_PACKAGES** SID to COM restrictions. This is the default. |

Many Windows APIs need access to resources (in some cases, system resources) that would normally be inaccessible to an app running inside an AppContainer (unless you changed the resources' ACLs). To solve that, many resources across Windows (various files, registry keys, and so on) are ACL'd with **ALL_APPLICATION_PACKAGES**, in order to grant access to *any* processes that's running in an AppContainer. When you hear **ALL_APPLICATION_PACKAGES**, it's best to interpret that as if it were named **ALL_APPCONTAINERS**, since that would be a more accurate name.

## Related topics

* [Setting security for COM applications](setting-security-for-com-applications.md)
