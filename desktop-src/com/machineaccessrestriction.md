---
title: MachineAccessRestriction
description: Sets the computer-wide restriction policy for component access.
ms.assetid: aeb37e49-6425-4058-968e-f9d00acf4fc2
keywords:
- MachineAccessRestriction registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# MachineAccessRestriction

Sets the computer-wide restriction policy for component access.

> [!Caution]  
> Changing this value will affect all COM server applications, and might prevent them from working properly. If there are COM server applications that have restrictions that are less stringent than the computer-wide restrictions, reducing the computer-wide restrictions may expose these applications to unwanted access. Conversely, if you increase the computer-wide restrictions, some COM server applications might no longer be accessible by calling applications.

 

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   MachineAccessRestriction = SECURITY_DESCRIPTOR
```

## Remarks

This is a **REG\_BINARY** value.

Principals not given permissions here cannot obtain them even if the permissions are granted by the [DefaultAccessPermission](defaultaccesspermission.md) registry value or by the [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) function.

By default, members of the Everyone group can obtain local and remote access permissions, and anonymous users can obtain local access permissions.

## Related topics

<dl> <dt>

[Setting Security for COM Applications](setting-security-for-com-applications.md)
</dt> </dl>

 

 




