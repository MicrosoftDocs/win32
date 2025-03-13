---
title: RegisterHyperVVMCreator method of the MSFT_NetFirewallHyperVVMCreator class
description: Registers a Hyper-V VM Creator with the firewall service.
ms.topic: reference
ms.date: 05/17/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallHyperVVMCreator.RegisterHyperVVMCreator
api_type: 
- COM
api_location: 
- WFasCim.dll
---

# RegisterHyperVVMCreator method of the MSFT_NetFirewallHyperVVMCreator class

Registers a Hyper-V VM Creator with the firewall service.

## Syntax

```mof
uint32 RegisterHyperVVMCreator(
  [in] string VMCreatorId, 
  [in] string FriendlyName
); 
```

## Parameters

`VMCreatorId` \[in\]

String representation of the unique GUID identifier of the Hyper-V VM Creator to register.

`FriendlyName` \[in\]

A friendly name of the Hyper-V VM Creator.

## Requirements

| | |
|-|-|
| Minimum supported client | Windows 8 |
| Minimum supported server | Windows Server 2012 |
| Namespace | Root\\StandardCimv2 |
| MOF | WFasCim.mof |
| DLL | WFasCim.dll |

## See also

* [MSFT_NetFirewallHyperVVMCreator](./msft-netfirewallhypervvmcreator.md)
