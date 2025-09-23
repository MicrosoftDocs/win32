---
description: Links an IPsec rule to its auth and crypto sets.
ms.assetid: 10a0bd87-3762-4f43-b67d-22ac30db0eb1
title: MSFT\_NetSAActionInSARule class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetSAActionInSARule
- MSFT_NetSAActionInSARule.GroupComponent
- MSFT_NetSAActionInSARule.PartComponent
- MSFT_NetSAActionInSARule.ActionOrder
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetSAActionInSARule class

Links an IPsec rule to its auth and crypto sets.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetSAActionInSARule : CIM_PolicyActionInPolicyRule
{
  CIM_SARule   REF GroupComponent;
  CIM_SAAction REF PartComponent;
  uint16           ActionOrder;
};
```

## Members

The **MSFT\_NetSAActionInSARule** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetSAActionInSARule** class has these properties.

<dl> <dt>

**ActionOrder**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SARule**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The IPsec rule.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SAAction**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The auth/crypto sets.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




