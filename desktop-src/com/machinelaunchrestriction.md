---
title: MachineLaunchRestriction
description: Sets the computer-wide restriction policy for component launch and activation.
ms.assetid: 274e3d08-1f38-4179-b7e7-b218d6e184ee
keywords:
- MachineLaunchRestriction registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# MachineLaunchRestriction

Sets the computer-wide restriction policy for component launch and activation.

> [!Caution]  
> Changing this value will affect all COM server applications, and might prevent them from working properly. If there are COM server applications that have restrictions that are less stringent than the computer-wide restrictions, reducing the computer-wide restrictions may expose these applications to unwanted access. Conversely, if you increase the computer-wide restrictions, some COM server applications might no longer be accessible by calling applications.

 

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   MachineLaunchRestriction = SECURITY_DESCRIPTOR
```

## Remarks

This is a **REG\_BINARY** value.

Principals not given permissions here cannot obtain them even if the permissions are granted by the [DefaultAccessPermission](defaultaccesspermission.md) registry value or by the [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) function.

By default, administrators may obtain local and remote launch and activation permissions, and members of the Everyone group may obtain local activation and launch permissions.

## Related topics

<dl> <dt>

[Setting Security for COM Applications](setting-security-for-com-applications.md)
</dt> </dl>

 

 




