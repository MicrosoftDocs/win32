---
title: LegacySecureReferences
description: Determines whether AddRef/Release invocations are secured for applications that do not call CoInitializeSecurity.
ms.assetid: 955b599b-1858-475a-95c4-a55038a28e69
keywords:
- LegacySecureReferences registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# LegacySecureReferences

Determines whether **AddRef**/**Release** invocations are secured for applications that do not call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity).

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   LegacySecureReferences = value
```

## Remarks

This is a **REG\_SZ** value. A value of 'Y' or 'y' indicate that **AddRef** and **Release** are secured. If this registry value is not present or is set to a value other than 'Y' or 'y', **AddRef** and **Release** are not secured. Enabling secure references slows remote calls.

## Related topics

<dl> <dt>

[Registering COM Servers](registering-com-servers.md)
</dt> <dt>

[Setting Process-wide Security](setting-processwide-security.md)
</dt> </dl>

 

 




