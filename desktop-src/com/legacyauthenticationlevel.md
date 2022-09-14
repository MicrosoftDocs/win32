---
title: LegacyAuthenticationLevel
description: Sets the default authentication level for applications that do not call CoInitializeSecurity.
ms.assetid: e14d2203-c84e-46af-befd-d82ef1936c9d
keywords:
- LegacyAuthenticationLevel registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# LegacyAuthenticationLevel

Sets the default authentication level for applications that do not call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity).

> [!Caution]  
> It is not recommended that you change this value, because this will affect all COM server applications that do not set their own process-wide security, and might prevent them from working properly. If you are changing this value to affect the security settings for a particular COM application, then you should instead change the process-wide security settings for that particular COM application. For more information on setting process-wide security, see [Setting Process-wide Security](setting-processwide-security.md).

 

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   LegacyAuthenticationLevel = value
```

## Remarks

This is a **REG\_WORD** value that is equivalent to the RPC\_C\_AUTHN\_LEVEL constants.



| Value | Constant                             |
|-------|--------------------------------------|
| 1     | RPC\_C\_AUTHN\_LEVEL\_NONE           |
| 2     | RPC\_C\_AUTHN\_LEVEL\_CONNECT        |
| 3     | RPC\_C\_AUTHN\_LEVEL\_CALL           |
| 4     | RPC\_C\_AUTHN\_LEVEL\_PKT            |
| 5     | RPC\_C\_AUTHN\_LEVEL\_PKT\_INTEGRITY |
| 6     | RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY   |



 

If this registry value is not present, the default authentication level established by the system is 2 (RPC\_C\_AUTHN\_CONNECT).

## Related topics

<dl> <dt>

[**AuthenticationLevel**](authenticationlevel.md)
</dt> <dt>

[Registering COM Servers](registering-com-servers.md)
</dt> <dt>

[Setting Process-wide Security](setting-processwide-security.md)
</dt> </dl>

 

 




