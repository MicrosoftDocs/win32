---
title: LegacyImpersonationLevel
description: Sets the default level of impersonation for applications that do not call CoInitializeSecurity.
ms.assetid: 3f42c6d7-729d-4406-9391-4bfe28f7a59d
keywords:
- LegacyImpersonationLevel registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# LegacyImpersonationLevel

Sets the default level of impersonation for applications that do not call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity).

> [!Caution]  
> It is not recommended that you change this value, because this will affect all COM server applications that do not set their own process-wide security, and might prevent them from working properly. If you are changing this value to affect the security settings for a particular COM application, then you should instead change the process-wide security settings for that particular COM application. For more information on setting process-wide security, see [Setting Process-wide Security](setting-processwide-security.md).

 

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   LegacyImpersonationLevel = value
```

## Remarks

This is a **REG\_WORD** value that is equivalent to the RPC\_C\_IMP\_LEVEL constants.



| Value | Constant                        |
|-------|---------------------------------|
| 1     | RPC\_C\_IMP\_LEVEL\_ANONYMOUS   |
| 2     | RPC\_C\_IMP\_LEVEL\_IDENTIFY    |
| 3     | RPC\_C\_IMP\_LEVEL\_IMPERSONATE |
| 4     | RPC\_C\_IMP\_LEVEL\_DELEGATE    |



 

If this registry value is not present, the default impersonation level established by the system is 2 (RPC\_C\_IMP\_LEVEL\_IDENTIFY).

## Related topics

<dl> <dt>

[Registering COM Servers](registering-com-servers.md)
</dt> <dt>

[Setting Process-wide Security](setting-processwide-security.md)
</dt> </dl>

 

 




