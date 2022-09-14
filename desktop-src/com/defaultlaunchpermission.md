---
title: DefaultLaunchPermission
description: Defines the Access Control List (ACL) of the principals that can launch classes that do not specify their own ACL through the LaunchPermission registry value.
ms.assetid: 23ca87fc-7829-46a9-9fc3-2cd7f677bbff
keywords:
- DefaultLaunchPermission registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# DefaultLaunchPermission

Defines the Access Control List (ACL) of the principals that can launch classes that do not specify their own ACL through the [**LaunchPermission**](launchpermission.md) registry value.

> [!Caution]  
> It is not recommended that you change this value, because this will affect all COM server applications that do not set their own process-wide security, and might prevent them from working properly. If you are changing this value to affect the security settings for a particular COM application, then you should instead change the process-wide security settings for that particular COM application. For more information on setting process-wide security, see [Setting Process-wide Security](setting-processwide-security.md).

 

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   DefaultLaunchPermission = ACL
```

## Remarks

This is a **REG\_BINARY** value.

The default access permissions are as follows:

-   Administrators: allow launch
-   SYSTEM: allow launch
-   INTERACTIVE: allow launch

If the [**LaunchPermission**](launchpermission.md) value is set for a server, it takes precedence over the **DefaultLaunchPermission** value. Upon receiving a local or remote request to launch a server whose [**AppID**](appid-key.md) key has no **LaunchPermission** value of its own, the ACL described by this value is checked while impersonating the client and its success either allows or disallows the launching of the class code.

This value provides a simple level of centralized administration of the default launching access to otherwise unadministered classes on a computer. For example, an administrator might use the DCOMCNFG tool to configure the system to allow read-only access for Power Users. OLE would therefore restrict requests to launch class code to members of the Power Users group. An administrator could subsequently configure launch permissions for individual classes to grant the ability to launch class code to other groups or individual users as needed.

## Related topics

<dl> <dt>

[**LaunchPermission**](launchpermission.md)
</dt> <dt>

[Registering COM Servers](registering-com-servers.md)
</dt> <dt>

[Setting Process-wide Security](setting-processwide-security.md)
</dt> </dl>

 

 




