---
description: Associates a firewall rule with a profile that it is in.
ms.assetid: c5dae148-e59e-4d76-9544-8d49ed234adc
title: MSFT\_NetFirewallRuleInProfile class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallRuleInProfile
- MSFT_NetFirewallRuleInProfile.PartComponent
- MSFT_NetFirewallRuleInProfile.GroupComponent
- MSFT_NetFirewallRuleInProfile.Priority
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetFirewallRuleInProfile class

Associates a firewall rule with a profile that it is in.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetFirewallRuleInProfile : MSFT_NetRuleInProfile
{
  MSFT_NetFirewallRule    REF PartComponent;
  MSFT_NetFirewallProfile REF GroupComponent;
  uint16                      Priority;
};
```

## Members

The **MSFT\_NetFirewallRuleInProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetFirewallRuleInProfile** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetFirewallProfile**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The firewall profile.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetFirewallRule**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The firewall profile.

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




