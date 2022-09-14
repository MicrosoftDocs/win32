---
title: InvalidSecurityDescriptorLoggingLevel
description: Sets the verbosity of event log entries about invalid security descriptors for component launch and access permissions.
ms.assetid: 44f680b8-083d-44f0-a353-e66b87787ab7
keywords:
- InvalidSecurityDescriptorLoggingLevel registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# InvalidSecurityDescriptorLoggingLevel

Sets the verbosity of event log entries about invalid security descriptors for component launch and access permissions.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   InvalidSecurityDescriptorLoggingLevel = value
```

## Remarks

This is a **REG\_DWORD** value.



| Value | Description                                                                                                                                                                    |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Always log failures when COM finds an invalid security descriptor. This is the default value.                                                                                  |
| 2     | Never log failures when COM finds an invalid security descriptor. It is not recommended that you disable event logging, as it can make it more difficult to diagnose problems. |



 

If you set launch and access permission security descriptors (commonly called ACLs) directly, it is possible to construct a security descriptor whose meaning cannot be interpreted unambiguously. COM makes an event log entry when it encounters such an invalid security descriptor.

Note that [**ActivationFailureLoggingLevel**](activationfailurelogginglevel.md) and [**CallFailureLoggingLevel**](callfailurelogginglevel.md) have no control over logging invalid security descriptor errors. Use **InvalidSecurityDescriptorLoggingLevel** for full control over this functionality.

## Related topics

<dl> <dt>

[Setting Security for COM Applications](setting-security-for-com-applications.md)
</dt> </dl>

 

 




