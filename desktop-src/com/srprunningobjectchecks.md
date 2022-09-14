---
title: SRPRunningObjectChecks
description: Determines whether attempts to connect to running objects are screened for compatible software restriction policy (SRP) trust levels.
ms.assetid: ab5e74f0-d167-4fb2-af1b-03704039e87c
keywords:
- SRPRunningObjectChecks registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# SRPRunningObjectChecks

Determines whether attempts to connect to running objects are screened for compatible software restriction policy (SRP) trust levels.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   SRPRunningObjectChecks = value
```

## Remarks

This is a **REG\_SZ** value.

String values of {N, n, NO, No, no} indicate that attempts to connect to running objects are not screened for compatible SRP trust levels. If this registry value is set to any other value or does not exist, the running object cannot have a less stringent SRP trust level than the client object. For example, the running object cannot have a Disallowed trust level if the client object has an Unrestricted trust level.

## Related topics

<dl> <dt>

[SRPTrustLevel](srptrustlevel.md)
</dt> </dl>

 

 




