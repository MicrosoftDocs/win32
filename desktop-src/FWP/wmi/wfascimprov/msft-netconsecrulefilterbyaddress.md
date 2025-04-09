---
description: Filters a connection security rule by address.
ms.assetid: 4675c606-abed-4906-b5b9-932c990e413e
title: MSFT\_NetConSecRuleFilterByAddress class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetConSecRuleFilterByAddress
- MSFT_NetConSecRuleFilterByAddress.GroupComponent
- MSFT_NetConSecRuleFilterByAddress.PartComponent
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetConSecRuleFilterByAddress class

Filters a connection security rule by address.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetConSecRuleFilterByAddress : MSFT_NetConSecRuleFilters
{
  MSFT_NetConSecRule    REF GroupComponent;
  MSFT_NetAddressFilter REF PartComponent;
};
```

## Members

The **MSFT\_NetConSecRuleFilterByAddress** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetConSecRuleFilterByAddress** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetConSecRule**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The connection security rule being filtered.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetAddressFilter**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The address filter applied to the rule.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




