---
title: AccessPermission
description: Describes the Access Control List (ACL) of the principals that can access instances of this class. This ACL is used only by applications that do not call CoInitializeSecurity.
ms.assetid: 92518de0-66ca-4d7a-8d91-63b41e6d3c24
keywords:
- AccessPermission registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# AccessPermission

Describes the Access Control List (ACL) of the principals that can access instances of this class. This ACL is used only by applications that do not call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity).

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {AppID_GUID}
      AccessPermission = ACL
```

## Remarks

This is a **REG\_BINARY** value. It contains data describing the Access Control List (ACL) of the principals that can access instances of this class. Upon receiving a request to connect to an existing object of this class, the ACL is checked by the application being called while impersonating the caller. If the access-check fails, the connection is disallowed. If this named value does not exist, the [**DefaultAccessPermission**](defaultaccesspermission.md) ACL is tested to determine whether the connection is to be allowed.

For applications that do not call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) or do not use the [**IGlobalOptions**](/windows/win32/api/objidlbase/nn-objidlbase-iglobaloptions) interface to specify the AppID, the executable of the application's binary must be mapped to the AppID of the application as described in [**AppID**](appid.md). This is required so that COM can locate the AppID of the application.

## Related topics

<dl> <dt>

[**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity)
</dt> <dt>

[**DefaultAccessPermission**](defaultaccesspermission.md)
</dt> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 