---
title: DefaultAccessPermission
description: Sets the Access Control List (ACL) of the principals that can access classes for which there is no AccessPermission setting.
ms.assetid: 02675d0e-a96c-476e-820e-e6ff3c2d1be1
keywords:
- DefaultAccessPermission registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# DefaultAccessPermission

Sets the Access Control List (ACL) of the principals that can access classes for which there is no [**AccessPermission**](accesspermission.md) setting. This ACL is used only by applications that do not call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) and do not have an **AccessPermission** value under their [**AppID**](appid-key.md) key.

> [!Caution]  
> It is not recommended that you change this value, because this will affect all COM server applications that do not set their own process-wide security, and might prevent them from working properly. If you are changing this value to affect the security settings for a particular COM application, then you should instead change the process-wide security settings for that particular COM application. For more information on setting process-wide security, see [Setting Process-wide Security](setting-processwide-security.md).

 

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   DefaultAccessPermission = ACL
```

## Remarks

This is a **REG\_BINARY** value.

The COM runtime in the server checks the ACL described by this value while impersonating the caller that is attempting to connect to the object, and its success determines whether the access is allowed or disallowed. If the access-check fails, the connection to the object is disallowed. If this named value does not exist, only the server principal and local system are allowed to call the server.

By default, this value has no entries in it. Only the server principal and system are allowed to call the server.

This value provides a simple level of centralized administration of the default connection access to running objects on a computer.

## Related topics

<dl> <dt>

[**AccessPermission**](accesspermission.md)
</dt> <dt>

[Registering COM Servers](registering-com-servers.md)
</dt> <dt>

[Setting Process-wide Security](setting-processwide-security.md)
</dt> </dl>

 

 




