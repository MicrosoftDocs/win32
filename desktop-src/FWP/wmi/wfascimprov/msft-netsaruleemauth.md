---
description: Relates an IPsec rule to its Phase 2 Authentication Set.
ms.assetid: 3f75cdcb-5387-4187-889e-5f46a4657d66
title: MSFT\_NetSARuleEMAuth class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetSARuleEMAuth
- MSFT_NetSARuleEMAuth.GroupComponent
- MSFT_NetSARuleEMAuth.PartComponent
- MSFT_NetSARuleEMAuth.ActionOrder
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetSARuleEMAuth class

Relates an IPsec rule to its Phase 2 Authentication Set.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetSARuleEMAuth : MSFT_NetSAActionInSARule
{
  CIM_SARule           REF GroupComponent;
  MSFT_NetIKEP2AuthSet REF PartComponent;
  uint16                   ActionOrder;
};
```

## Members

The **MSFT\_NetSARuleEMAuth** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetSARuleEMAuth** class has these properties.

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

Data type: **MSFT\_NetIKEP2AuthSet**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The Phase 2 Authentication Set used by the rule.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




