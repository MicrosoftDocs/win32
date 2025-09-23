---
description: Relates an IPsec rule to its Main Mode crypto set.
ms.assetid: 0d821c6f-ea2f-4063-9b3e-4d2461ac7884
title: MSFT\_NetSARuleMMCrypto class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetSARuleMMCrypto
- MSFT_NetSARuleMMCrypto.GroupComponent
- MSFT_NetSARuleMMCrypto.PartComponent
- MSFT_NetSARuleMMCrypto.ActionOrder
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetSARuleMMCrypto class

Relates an IPsec rule to its Main Mode crypto set.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetSARuleMMCrypto : MSFT_NetSAActionInSARule
{
  CIM_SARule             REF GroupComponent;
  MSFT_NetIKEMMCryptoSet REF PartComponent;
  uint16                     ActionOrder;
};
```

## Members

The **MSFT\_NetSARuleMMCrypto** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetSARuleMMCrypto** class has these properties.

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

Data type: **MSFT\_NetIKEMMCryptoSet**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The Main Mode crypto set used in this rule.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




