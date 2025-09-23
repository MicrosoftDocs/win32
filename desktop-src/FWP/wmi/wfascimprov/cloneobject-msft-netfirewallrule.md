---
description: Copy this rule.
ms.assetid: f16e26ee-3072-4254-b905-0c584b607297
title: CloneObject method of the MSFT\_NetFirewallRule class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallRule.CloneObject
api_type: 
- COM
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# CloneObject method of the MSFT\_NetFirewallRule class

Copy this rule.

## Syntax


```mof
uint32 CloneObject(
  [in] string NewName,
  [in] string NewPolicyStore,
  [in] string NewGPOSession
);
```



## Parameters

<dl> <dt>

*NewName* \[in\]
</dt> <dd>

The new name for the rule.

</dd> <dt>

*NewPolicyStore* \[in\]
</dt> <dd>

The new policy store for the rule.

</dd> <dt>

*NewGPOSession* \[in\]
</dt> <dd>

The new GPOSession for the rule.

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

 

 




