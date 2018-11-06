---
title: CallFailureLoggingLevel
description: Sets the verbosity of event log entries about failed calls to components.
ms.assetid: 68a7210c-f2a0-4db6-9759-08ff9132a563
keywords:
- CallFailureLoggingLevel registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# CallFailureLoggingLevel

Sets the verbosity of event log entries about failed calls to components.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   CallFailureLoggingLevel = value
```

## Remarks

This is a **REG\_DWORD** value.



| Value | Description                                                                            |
|-------|----------------------------------------------------------------------------------------|
| 1     | Always log failures during a call in the COM Server process.                           |
| 2     | Never log failures during a call in the COM Server process. This is the default value. |



 

## Related topics

<dl> <dt>

[Setting Security for COM Applications](setting-security-for-com-applications.md)
</dt> </dl>

 

 




