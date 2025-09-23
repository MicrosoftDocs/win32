---
title: UpdateDynamicKeywordAddress method of the MSFT_NetFirewallDynamicKeywordAddress class
description: Updates the dynamic keyword address.
ms.topic: reference
ms.date: 05/14/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallDynamicKeywordAddress.UpdateDynamicKeywordAddress
api_type: 
- COM
api_location: 
- WFasCim.dll
---

# UpdateDynamicKeywordAddress method of the MSFT_NetFirewallDynamicKeywordAddress class

Updates the dynamic keyword address.

## Syntax

```mof
uint32 UpdateDynamicKeywordAddress
(
  [in] string Id,
  [in] string Addresses,
  [in] boolean Append
);
```

## Parameters

`Id` \[in\]

GUID of the keyword to update.

`Addresses` \[in\]

Comma separated list of addresses, subnets, or ranges to update the keyword with. The string format for this field matches the 'Addresses' field.

`Append` \[in\]

TRUE if the addresses should be appended to keyword's existing addresses, FALSE if it should overwrite them.

## Requirements

| | |
|-|-|
| Minimum supported client | Windows 8 |
| Minimum supported server | Windows Server 2012 |
| Namespace | Root\\StandardCimv2 |
| MOF | WFasCim.mof |
| DLL | WFasCim.dll |

## See also

* [MSFT_NetFirewallDynamicKeywordAddress](./msft-netfirewalldynamickeywordaddress.md)
