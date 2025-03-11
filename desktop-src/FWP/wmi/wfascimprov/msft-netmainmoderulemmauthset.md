---
description: Relates a main mode rule to its Phase 1 Authentication Set.
ms.assetid: 50f57e68-2a79-4a21-9465-cf70d236b9da
title: MSFT\_NetMainModeRuleMMAuthSet class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetMainModeRuleMMAuthSet
- MSFT_NetMainModeRuleMMAuthSet.GroupComponent
- MSFT_NetMainModeRuleMMAuthSet.PartComponent
- MSFT_NetMainModeRuleMMAuthSet.ActionOrder
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetMainModeRuleMMAuthSet class

Relates a main mode rule to its Phase 1 Authentication Set.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetMainModeRuleMMAuthSet : MSFT_NetSARuleMMAuth
{
  MSFT_NetMainModeRule REF GroupComponent;
  MSFT_NetIKEP1AuthSet REF PartComponent;
  uint16                   ActionOrder;
};
```

## Members

The **MSFT\_NetMainModeRuleMMAuthSet** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetMainModeRuleMMAuthSet** class has these properties.

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

Data type: **MSFT\_NetMainModeRule**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The main mode rule.

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



 

 




