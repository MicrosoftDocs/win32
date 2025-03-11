---
description: Filters a Windows firewall rule by interface type.
ms.assetid: 0adf2432-0fa1-449c-adaf-22943e3d650c
title: MSFT\_NetFirewallRuleFilterByInterfaceType class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallRuleFilterByInterfaceType
- MSFT_NetFirewallRuleFilterByInterfaceType.GroupComponent
- MSFT_NetFirewallRuleFilterByInterfaceType.PartComponent
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetFirewallRuleFilterByInterfaceType class

Filters a Windows firewall rule by interface type.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetFirewallRuleFilterByInterfaceType : MSFT_NetFirewallRuleFilters
{
  MSFT_NetFirewallRule        REF GroupComponent;
  MSFT_NetInterfaceTypeFilter REF PartComponent;
};
```

## Members

The **MSFT\_NetFirewallRuleFilterByInterfaceType** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetFirewallRuleFilterByInterfaceType** class has these properties.

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

Data type: **MSFT\_NetInterfaceTypeFilter**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The interface type filter applied to the rule.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




