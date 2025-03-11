---
description: Relates a connection security rule to its Quick Mode Crypto Set.
ms.assetid: d6e6f654-09ac-4666-a8f5-f364a5045514
title: MSFT\_NetConSecRuleQMCryptoSet class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetConSecRuleQMCryptoSet
- MSFT_NetConSecRuleQMCryptoSet.GroupComponent
- MSFT_NetConSecRuleQMCryptoSet.PartComponent
- MSFT_NetConSecRuleQMCryptoSet.ActionOrder
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetConSecRuleQMCryptoSet class

Relates a connection security rule to its Quick Mode Crypto Set.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetConSecRuleQMCryptoSet : MSFT_NetSARuleQMCrypto
{
  MSFT_NetConSecRule     REF GroupComponent;
  MSFT_NetIKEQMCryptoSet REF PartComponent;
  uint16                     ActionOrder;
};
```

## Members

The **MSFT\_NetConSecRuleQMCryptoSet** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetConSecRuleQMCryptoSet** class has these properties.

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

Data type: **MSFT\_NetIKEQMCryptoSet**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The Quick Mode crypto set used by this rule.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




