---
description: The Multiple Provider Router (MPR) calls NPGetCaps to find out when the network providers will start (nIndex is set to WNNC\_START).
ms.assetid: f57bd8ff-647d-42f8-abaf-7937b24416dd
title: Overriding the Default MPR Time-out Interval
ms.topic: article
ms.date: 05/31/2018
---

# Overriding the Default MPR Time-out Interval

The [*Multiple Provider Router*](../secgloss/m-gly.md) (MPR) calls [**NPGetCaps**](/windows/desktop/api/Npapi/nf-npapi-npgetcaps) to find out when the network providers will start (*nIndex* is set to WNNC\_START). The MPR then waits for the longest time-out period specified by all network providers before it presents the consolidated network to the user. If one of the network providers does not know when it will start, MPR uses a default time-out of 60 seconds for that provider.

If necessary, the administrator can override the default time-out by creating the following **REG\_DWORD** registry time-out, where *n* is the time-out interval in milliseconds:

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**NetworkProvider**\\**RestoreTimeout** = *n*

The following pseudocode shows the complete logic flow for time-out handling by the MPR.


```C++
If there is a RegistryTimeout,
Then MaxTimeout = RegistryTimeout.
Otherwise,
MaxTimeout = 0.
For each provider,
if the provider does not supply a time-out and
if there is a RegistryTimeout,
ProviderTimeout is set to RegistryTimeout.
Otherwise,
ProviderTimeout is set to DefaultTimeout.
Otherwise,
If the ProviderTimeout is longer than MaxTimeout,
MaxTimeout = ProviderTimeout.
```



 

 
