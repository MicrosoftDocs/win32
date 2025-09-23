---
description: Relates an IPsec rule to its Phase 1 Authentication Set.
ms.assetid: 0c3a5844-7d3d-483a-9ae4-0541cc521b0a
title: MSFT\_NetConSecRuleMMAuthSet class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetConSecRuleMMAuthSet
- MSFT_NetConSecRuleMMAuthSet.GroupComponent
- MSFT_NetConSecRuleMMAuthSet.PartComponent
- MSFT_NetConSecRuleMMAuthSet.ActionOrder
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetConSecRuleMMAuthSet class

Relates an IPsec rule to its Phase 1 Authentication Set.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetConSecRuleMMAuthSet : MSFT_NetSARuleMMAuth
{
  MSFT_NetConSecRule   REF GroupComponent;
  MSFT_NetIKEP1AuthSet REF PartComponent;
  uint16                   ActionOrder;
};
```

## Members

The **MSFT\_NetConSecRuleMMAuthSet** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetConSecRuleMMAuthSet** class has these properties.

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

Data type: **MSFT\_NetConSecRule**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The connection security rule.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetIKEP1AuthSet**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The Phase 1 Authentication Set used by the rule.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




