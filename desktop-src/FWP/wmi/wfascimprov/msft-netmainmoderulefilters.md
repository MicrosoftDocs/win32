---
description: Associates a main mode rule with its filters. Instances of this class can be traversed and the values in the associated filters can be modified, but instances of this class may not be created or deleted.
ms.assetid: 1bfef69c-2a5c-46f0-955a-8243fd61bbe4
title: MSFT\_NetMainModeRuleFilters class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetMainModeRuleFilters
- MSFT_NetMainModeRuleFilters.GroupComponent
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetMainModeRuleFilters class

Associates a main mode rule with its filters. Instances of this class can be traversed and the values in the associated filters can be modified, but instances of this class may not be created or deleted.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetMainModeRuleFilters : MSFT_NetPolicyRuleFilters
{
  MSFT_NetMainModeRule REF GroupComponent;
};
```

## Members

The **MSFT\_NetMainModeRuleFilters** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetMainModeRuleFilters** class has these properties.

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

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




