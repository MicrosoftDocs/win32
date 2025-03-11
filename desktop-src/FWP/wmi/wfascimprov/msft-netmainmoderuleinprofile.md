---
description: Indicates that a rule applies to a particular firewall profile.
ms.assetid: 26cec2e2-ef6f-441f-8426-d5fff69912af
title: MSFT\_NetMainModeRuleInProfile class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetMainModeRuleInProfile
- MSFT_NetMainModeRuleInProfile.PartComponent
- MSFT_NetMainModeRuleInProfile.GroupComponent
- MSFT_NetMainModeRuleInProfile.Priority
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetMainModeRuleInProfile class

Indicates that a rule applies to a particular firewall profile.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetMainModeRuleInProfile : MSFT_NetRuleInProfile
{
  MSFT_NetMainModeRule    REF PartComponent;
  MSFT_NetFirewallProfile REF GroupComponent;
  uint16                      Priority;
};
```

## Members

The **MSFT\_NetMainModeRuleInProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetMainModeRuleInProfile** class has these properties.

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

Data type: **MSFT\_NetMainModeRule**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The main mode rule.

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



 

 




