---
description: Associates a FirewallRule to its AddressFilter.
ms.assetid: 3dcc0d87-da52-43f9-8323-21a795676051
title: MSFT\_NetFirewallRuleFilterByAddress class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallRuleFilterByAddress
- MSFT_NetFirewallRuleFilterByAddress.GroupComponent
- MSFT_NetFirewallRuleFilterByAddress.PartComponent
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetFirewallRuleFilterByAddress class

Associates a FirewallRule to its AddressFilter.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetFirewallRuleFilterByAddress : MSFT_NetFirewallRuleFilters
{
  MSFT_NetFirewallRule  REF GroupComponent;
  MSFT_NetAddressFilter REF PartComponent;
};
```

## Members

The **MSFT\_NetFirewallRuleFilterByAddress** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetFirewallRuleFilterByAddress** class has these properties.

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

Data type: **MSFT\_NetAddressFilter**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The address filter applied to the rule.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




