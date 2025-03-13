---
title: EnumerateFull method of the MSFT_NetFirewallHyperVRule class
description: Enumerates all fields of all rules.
ms.topic: reference
ms.date: 05/16/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallHyperVRule.EnumerateFull
api_type: 
- COM
api_location: 
- WFasCim.dll
---

# EnumerateFull method of the MSFT_NetFirewallHyperVRule class

Enumerates all fields of all rules.

## Syntax

```mof
uint32 EnumerateFull
(
  [stream, out, EmbeddedInstance("CIM_ManagedSystemElement")] string Dependents[]
);
```

## Parameters

`EnumerateFull` \[stream, out, EmbeddedInstance("CIM_ManagedSystemElement")\]

TBD

## Requirements

| | |
|-|-|
| Minimum supported client | Windows 8 |
| Minimum supported server | Windows Server 2012 |
| Namespace | Root\\StandardCimv2 |
| MOF | WFasCim.mof |
| DLL | WFasCim.dll |

## See also

* [MSFT_NetFirewallHyperVRule](./msft-netfirewallhypervrule.md)
