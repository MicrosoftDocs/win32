---
description: Filters a connection security rule by protocol or port.
ms.assetid: 21e3c3ef-d543-4e76-9987-3fca2d2e8b85
title: MSFT\_NetConSecRuleFilterByProtocolPort class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetConSecRuleFilterByProtocolPort
- MSFT_NetConSecRuleFilterByProtocolPort.GroupComponent
- MSFT_NetConSecRuleFilterByProtocolPort.PartComponent
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetConSecRuleFilterByProtocolPort class

Filters a connection security rule by protocol or port.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetConSecRuleFilterByProtocolPort : MSFT_NetConSecRuleFilters
{
  MSFT_NetConSecRule         REF GroupComponent;
  MSFT_NetProtocolPortFilter REF PartComponent;
};
```

## Members

The **MSFT\_NetConSecRuleFilterByProtocolPort** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetConSecRuleFilterByProtocolPort** class has these properties.

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

Data type: **MSFT\_NetProtocolPortFilter**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The protocol/port filter applied to the rule.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




