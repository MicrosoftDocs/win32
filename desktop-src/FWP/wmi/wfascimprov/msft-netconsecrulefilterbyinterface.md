---
description: Filters a connection security rule by interface.
ms.assetid: 3598e9f1-c670-4d47-8bf0-a8ad8c59a780
title: MSFT\_NetConSecRuleFilterByInterface class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetConSecRuleFilterByInterface
- MSFT_NetConSecRuleFilterByInterface.GroupComponent
- MSFT_NetConSecRuleFilterByInterface.PartComponent
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetConSecRuleFilterByInterface class

Filters a connection security rule by interface.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetConSecRuleFilterByInterface : MSFT_NetConSecRuleFilters
{
  MSFT_NetConSecRule      REF GroupComponent;
  MSFT_NetInterfaceFilter REF PartComponent;
};
```

## Members

The **MSFT\_NetConSecRuleFilterByInterface** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetConSecRuleFilterByInterface** class has these properties.

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

Data type: **MSFT\_NetInterfaceFilter**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The interface filter applied to the rule.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




