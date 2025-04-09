---
description: Enumerates the dependent parts of every Windows firewall rule.
ms.assetid: ccd1ae3e-6ad9-4287-983d-673f8ea58e57
title: EnumerateFull method of the MSFT\_NetFirewallRule class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallRule.EnumerateFull
api_type: 
- COM
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# EnumerateFull method of the MSFT\_NetFirewallRule class

Enumerates the dependent parts of every Windows firewall rule.

## Syntax


```mof
uint32 EnumerateFull(
  [out] string Dependents[]
);
```



## Parameters

<dl> <dt>

*Dependents* \[out\]
</dt> <dd>

When this method returns, contains an array of dependent parts.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetFirewallRule**](msft-netfirewallrule.md)
</dt> </dl>

 

 




