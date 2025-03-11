---
description: Filters a Windows firewall rule by application.
ms.assetid: 42a0512b-2ba6-4557-b2e4-4a74c1049977
title: MSFT\_NetFirewallRuleFilterByApplication class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallRuleFilterByApplication
- MSFT_NetFirewallRuleFilterByApplication.GroupComponent
- MSFT_NetFirewallRuleFilterByApplication.PartComponent
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetFirewallRuleFilterByApplication class

Filters a Windows firewall rule by application.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetFirewallRuleFilterByApplication : MSFT_NetFirewallRuleFilters
{
  MSFT_NetFirewallRule      REF GroupComponent;
  MSFT_NetApplicationFilter REF PartComponent;
};
```

## Members

The **MSFT\_NetFirewallRuleFilterByApplication** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetFirewallRuleFilterByApplication** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetFirewallRule**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The firewall rule.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetApplicationFilter**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The application filter applied to the rule.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




