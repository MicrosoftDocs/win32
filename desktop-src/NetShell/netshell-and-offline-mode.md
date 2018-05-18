---
title: NetShell and Offline Mode
description: NetShell provides the ability to cache commands in offline mode, enabling blocks of changes to be configured, then applied once NetShell is taken out of offline mode.
ms.assetid: '4cbf0aee-2eee-4cc5-8155-14659e68e2a6'
keywords: ["offline mode NetSh", "components NetSh , offline mode"]
---

# NetShell and Offline Mode

NetShell provides the ability to cache commands in offline mode, enabling blocks of changes to be configured, then applied once NetShell is taken out of offline mode.

Top-level helpers provide contexts directly below the root context. For example, **ras** and **dhcp** are top-level contexts, so their helpers are considered top-level helpers. The following shows this from the command prompt:

``` syntax
netsh>
netsh ras>
netsh dhcp>
```

Top-level helpers are required to provide support for offline caching for their context, and for any subcontexts. For example, the helper that implements the **ras** context must provide offline caching support for its subcontexts.

> [!Note]  
> Offline mode is not implemented for the **ras** and **routing** contexts. Changes to the **ras** and **routing** contexts and their subcontexts made in offline mode do not require a **commit** command for the changes to be saved.

 

 

 




