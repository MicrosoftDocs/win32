---
description: Filters a main mode rule by address.
ms.assetid: fd4e2bfd-8fd3-4744-8f4c-1e6c40ee0637
title: MSFT\_NetMainModeRuleFilterByAddress class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetMainModeRuleFilterByAddress
- MSFT_NetMainModeRuleFilterByAddress.GroupComponent
- MSFT_NetMainModeRuleFilterByAddress.PartComponent
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetMainModeRuleFilterByAddress class

Filters a main mode rule by address.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetMainModeRuleFilterByAddress : MSFT_NetMainModeRuleFilters
{
  MSFT_NetMainModeRule  REF GroupComponent;
  MSFT_NetAddressFilter REF PartComponent;
};
```

## Members

The **MSFT\_NetMainModeRuleFilterByAddress** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetMainModeRuleFilterByAddress** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetMainModeRule**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The main mode rule being filtered.

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



 

 




