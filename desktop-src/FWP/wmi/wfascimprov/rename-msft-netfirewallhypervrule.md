---
title: Rename method of the MSFT_NetFirewallHyperVRule class
description: Rename this rule.
ms.topic: reference
ms.date: 05/16/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallHyperVRule.Rename
api_type: 
- COM
api_location: 
- WFasCim.dll
---

# Rename method of the MSFT_NetFirewallHyperVRule class

Rename this rule.

## Syntax

```mof
uint32 Rename
(
  [in] string NewName
);
```

## Parameters

`NewName` \[in\]

The new name for the rule.

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
