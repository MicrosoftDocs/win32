---
description: Associates a firewall rule with its filters. Instances of this class can be traversed and the values in the associated filters can be modified, but instances of this class may not be created or deleted.
ms.assetid: 99f07c0b-e30d-4cbf-8f78-b52c9832b0a8
title: MSFT\_NetFirewallRuleFilters class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallRuleFilters
- MSFT_NetFirewallRuleFilters.GroupComponent
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetFirewallRuleFilters class

Associates a firewall rule with its filters. Instances of this class can be traversed and the values in the associated filters can be modified, but instances of this class may not be created or deleted.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetFirewallRuleFilters : MSFT_NetPolicyRuleFilters
{
  MSFT_NetFirewallRule REF GroupComponent;
};
```

## Members

The **MSFT\_NetFirewallRuleFilters** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetFirewallRuleFilters** class has these properties.

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

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




