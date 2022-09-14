---
title: DoNotAddAllApplicationPackagesToRestrictions
description: Determines whether RPCSS automatically appends an ALL\_APPLICATION\_PACKAGES SID to COM restrictions by default.
ms.assetid: 4DC1237E-F3EF-40EA-8E64-57320F0C4CC5
ms.topic: article
ms.date: 05/31/2018
---

# DoNotAddAllApplicationPackagesToRestrictions

Determines whether RPCSS automatically appends an ALL\_APPLICATION\_PACKAGES SID to COM restrictions by default.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   DoNotAddAllApplicationPackagesToRestrictions = value
```

## Remarks

This is a **REG\_DWORD** value.



| Value | Description                                                                               |
|-------|-------------------------------------------------------------------------------------------|
| 0     | Disables Windows Store apps upon migration from Windows 7 to Windows 8.                   |
| 1     | Does not add the ALL\_APPLICATION\_PACKAGES SID to COM restrictions. This is the default. |



 

## Related topics

<dl> <dt>

[Setting Security for COM Applications](setting-security-for-com-applications.md)
</dt> </dl>

 

 




