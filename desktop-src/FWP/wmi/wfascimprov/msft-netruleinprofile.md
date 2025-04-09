---
description: Indicates that a rule applies to a particular firewall profile.
ms.assetid: 7ce34abf-8f1d-46f3-aca0-15185fcce16a
title: MSFT\_NetRuleInProfile class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetRuleInProfile
- MSFT_NetRuleInProfile.GroupComponent
- MSFT_NetRuleInProfile.PartComponent
- MSFT_NetRuleInProfile.Priority
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetRuleInProfile class

Indicates that a rule applies to a particular firewall profile.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetRuleInProfile : CIM_PolicySetComponent
{
  MSFT_NetFirewallProfile REF GroupComponent;
  CIM_PolicyRule          REF PartComponent;
  uint16                      Priority;
};
```

## Members

The **MSFT\_NetRuleInProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetRuleInProfile** class has these properties.

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

Data type: **CIM\_PolicyRule**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The policy rule within the profile.

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



 

 




