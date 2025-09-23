---
description: Filters a Windows firewall rule by network layer security.
ms.assetid: 8631503b-4180-4ca8-91ae-7eda95fd9c11
title: MSFT\_NetFirewallRuleFilterBySecurity class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallRuleFilterBySecurity
- MSFT_NetFirewallRuleFilterBySecurity.GroupComponent
- MSFT_NetFirewallRuleFilterBySecurity.PartComponent
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetFirewallRuleFilterBySecurity class

Filters a Windows firewall rule by network layer security.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetFirewallRuleFilterBySecurity : MSFT_NetFirewallRuleFilters
{
  MSFT_NetFirewallRule               REF GroupComponent;
  MSFT_NetNetworkLayerSecurityFilter REF PartComponent;
};
```

## Members

The **MSFT\_NetFirewallRuleFilterBySecurity** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetFirewallRuleFilterBySecurity** class has these properties.

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

Data type: **MSFT\_NetNetworkLayerSecurityFilter**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The security filter applied to the rule.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




