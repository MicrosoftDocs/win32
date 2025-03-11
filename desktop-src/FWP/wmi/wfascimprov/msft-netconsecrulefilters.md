---
description: Associates a connection security rule with its filters. Instances of this class can be traversed and the values in the associated filters can be modified, but instances of this class may not be created or deleted.
ms.assetid: 09b65154-8fae-4be3-91e2-a8c7ae223adb
title: MSFT\_NetConSecRuleFilters class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetConSecRuleFilters
- MSFT_NetConSecRuleFilters.GroupComponent
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetConSecRuleFilters class

Associates a connection security rule with its filters. Instances of this class can be traversed and the values in the associated filters can be modified, but instances of this class may not be created or deleted.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetConSecRuleFilters : MSFT_NetPolicyRuleFilters
{
  MSFT_NetConSecRule REF GroupComponent;
};
```

## Members

The **MSFT\_NetConSecRuleFilters** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetConSecRuleFilters** class has these properties.

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

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




