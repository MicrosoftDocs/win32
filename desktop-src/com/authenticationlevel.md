---
title: AuthenticationLevel
description: Sets the authentication level for applications that do not call CoInitializeSecurity or for applications that call CoInitializeSecurity and specify an AppID.
ms.assetid: 137cbffe-6f45-43f4-bf35-b064b3607fcc
keywords:
- AuthenticationLevel registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# AuthenticationLevel

Sets the authentication level for applications that do not call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) or for applications that call **CoInitializeSecurity** and specify an AppID.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {AppID_GUID}
      AuthenticationLevel = value
```

## Remarks

This is a **REG\_DWORD** value that is equivalent to the RPC\_C\_AUTHN\_LEVEL constants.



| Value | Constant                             |
|-------|--------------------------------------|
| 1     | RPC\_C\_AUTHN\_LEVEL\_NONE           |
| 2     | RPC\_C\_AUTHN\_LEVEL\_CONNECT        |
| 3     | RPC\_C\_AUTHN\_LEVEL\_CALL           |
| 4     | RPC\_C\_AUTHN\_LEVEL\_PKT            |
| 5     | RPC\_C\_AUTHN\_LEVEL\_PKT\_INTEGRITY |
| 6     | RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY   |



 

The **AuthenticationLevel** value is similar to the [**LegacyAuthenticationLevel**](legacyauthenticationlevel.md) value. If the **AuthenticationLevel** value is present, it is used instead of the **LegacyAuthenticationLevel** value for that AppID.

If the **AuthenticationLevel** value is of the wrong type or out of range, [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) fails, causing interface marshaling to fail. This prevents the application from making any calls at all (cross-apartment, cross-thread, cross-process, or cross-computer).

The **AuthenticationLevel** and [**AccessPermission**](accesspermission.md) values are independent. If one is not present, the default is used. The following rules list the interaction between the **AuthenticationLevel** value and the **AccessPermission** value:

-   If the **AuthenticationLevel** is NONE, the [**AccessPermission**](accesspermission.md) and [**DefaultAccessPermission**](defaultaccesspermission.md) values are ignored (for that application).
-   If the **AuthenticationLevel** is not present and the [**LegacyAuthenticationLevel**](legacyauthenticationlevel.md) is NONE, the [**AccessPermission**](accesspermission.md) and [**DefaultAccessPermission**](defaultaccesspermission.md) values are ignored (for that application).

## Related topics

<dl> <dt>

[Authentication Level Constants](com-authentication-level-constants.md)
</dt> <dt>

[**LegacyAuthenticationLevel**](legacyauthenticationlevel.md)
</dt> <dt>

[Registering COM Servers](registering-com-servers.md)
</dt> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 




