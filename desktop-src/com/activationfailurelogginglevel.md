---
title: ActivationFailureLoggingLevel
description: Sets the verbosity of event log entries about failed requests for component launch and activation.
ms.assetid: c3981621-5826-405c-8962-edfa9c783c2d
keywords:
- ActivationFailureLoggingLevel registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# ActivationFailureLoggingLevel

Sets the verbosity of event log entries about failed requests for component launch and activation.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   ActivationFailureLoggingLevel = value
```

## Remarks

This is a **REG\_DWORD** value.



| Value | Description                                                                                                                                                                                                       |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | Use discretionary logging. Log failures by default, but clients can override this behavior by specifying CLSCTX\_NO\_FAILURE\_LOG in [**CoCreateInstanceEx**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstanceex). This is the default value. |
| 1     | Always log all failures no matter what the client specified.                                                                                                                                                      |
| 2     | Never log any failures no matter what the client specified.                                                                                                                                                       |



 

If you need an application to control event logging, it is recommended that you set this value to 0 and write the client code to override it when needed. It is strongly recommended that you do not set the value to 2. If event logging is disabled, it is more difficult to diagnose problems. For machine restrictions permission failures, where COM does not have the CLSCTX bits, COM will treat a value of 0 as 1.

## Related topics

<dl> <dt>

[Setting Security for COM Applications](setting-security-for-com-applications.md)
</dt> </dl>

 

 




