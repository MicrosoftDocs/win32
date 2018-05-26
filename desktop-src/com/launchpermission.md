---
title: LaunchPermission
description: Describes the Access Control List (ACL) of the principals that can start new servers for this class. This value may be added under any AppID key to limit activation by remote clients of specific classes.
ms.assetid: 23ca87fc-7829-46a9-9fc3-2cd7f677bbff
keywords:
- LaunchPermission registry value COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LaunchPermission

Describes the Access Control List (ACL) of the principals that can start new servers for this class. This value may be added under any [**AppID**](appid-key.md) key to limit activation by remote clients of specific classes.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {AppID_GUID}
      LaunchPermission = ACL
```

## Remarks

This is a **REG\_BINARY** value. Upon receiving a local or remote request to launch the server of this class, the ACL described by this value is checked while impersonating the client, and its success either allows or disallows the launching of the server. If this value does not exist, the [**DefaultLaunchPermission**](defaultlaunchpermission.md) value is checked in the same way to determine whether the class code can be launched.

## Related topics

<dl> <dt>

[**CoInitializeSecurity**](/windows/win32/combaseapi/nf-combaseapi-coinitializesecurity?branch=master)
</dt> <dt>

[**DefaultLaunchPermission**](defaultlaunchpermission.md)
</dt> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 




