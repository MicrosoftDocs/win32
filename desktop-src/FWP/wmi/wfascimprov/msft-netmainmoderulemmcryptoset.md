---
description: Relates a main mode rule to its Main Mode Crypto Set.
ms.assetid: 8aef3a12-721e-4167-8a2b-c31fb68d1818
title: MSFT\_NetMainModeRuleMMCryptoSet class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetMainModeRuleMMCryptoSet
- MSFT_NetMainModeRuleMMCryptoSet.GroupComponent
- MSFT_NetMainModeRuleMMCryptoSet.PartComponent
- MSFT_NetMainModeRuleMMCryptoSet.ActionOrder
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetMainModeRuleMMCryptoSet class

Relates a main mode rule to its Main Mode Crypto Set.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetMainModeRuleMMCryptoSet : MSFT_NetSARuleMMCrypto
{
  MSFT_NetMainModeRule   REF GroupComponent;
  MSFT_NetIKEMMCryptoSet REF PartComponent;
  uint16                     ActionOrder;
};
```

## Members

The **MSFT\_NetMainModeRuleMMCryptoSet** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetMainModeRuleMMCryptoSet** class has these properties.

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

Data type: **MSFT\_NetIKEMMCryptoSet**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The main mode crypto set used in this rule.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




