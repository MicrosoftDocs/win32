---
description: Associates a policy rule to its filters.
ms.assetid: 368b7ec6-d310-4e11-8ccc-abb091705222
title: MSFT\_NetPolicyRuleFilters class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetPolicyRuleFilters
- MSFT_NetPolicyRuleFilters.GroupComponent
- MSFT_NetPolicyRuleFilters.PartComponent
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetPolicyRuleFilters class

Associates a policy rule to its filters.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetPolicyRuleFilters : CIM_Component
{
  CIM_PolicyRule      REF GroupComponent;
  CIM_FilterEntryBase REF PartComponent;
};
```

## Members

The **MSFT\_NetPolicyRuleFilters** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetPolicyRuleFilters** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PolicyRule**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The rule.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_FilterEntryBase**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The filters associated with the rule.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




