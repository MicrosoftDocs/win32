---
title: SRPActivateAsActivatorChecks
description: Determines whether software restriction policy (SRP) trust levels are used during ActivateAsActivator activations.
ms.assetid: b0d616c3-1cb0-4854-a4f9-6635d61b0698
keywords:
- SRPActivateAsActivatorChecks registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# SRPActivateAsActivatorChecks

Determines whether software restriction policy (SRP) trust levels are used during ActivateAsActivator activations.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   SRPActivateAsActivatorChecks = value
```

## Remarks

This is a **REG\_SZ** value.

String values of {N, n, NO, No, no} indicate that the server object runs with the SRP trust level of the client object, regardless of the SRP trust level with which it was configured. If this registry value is set to any other value or does not exist, the SRP trust level that is configured for the server object is compared with the SRP trust level of the client object and that the more stringent trust level is used to run the server object.

## Related topics

<dl> <dt>

[SRPTrustLevel](srptrustlevel.md)
</dt> </dl>

 

 




