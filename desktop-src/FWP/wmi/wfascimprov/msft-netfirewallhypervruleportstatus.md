---
title: MSFT_NetFirewallHyperVRulePortStatus class
description: Represents the status of a firewall rule on a particular port.
ms.topic: reference
ms.date: 05/16/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallHyperVRulePortStatus
api_type: 
- DllExport
api_location: 
- WFasCim.dll
---

# MSFT_NetFirewallHyperVRulePortStatus class

Represents the status of a firewall rule on a particular port.

The following syntax is simplified from Managed Object Format (MOF) code, and includes all of the inherited properties.

## Syntax

```syntax
class MSFT_NetFirewallHyperVRulePortStatus
{
  string Port;
  uint16 Status;
};
```

## Members

The **MSFT_NetFirewallHyperVRulePortStatus** class has these types of members:

- [Properties](#properties)

### Properties

The **MSFT_NetFirewallHyperVRulePortStatus** class has these properties.

`Port`

Data type: **string**

Access type: Read/write

Hyper-V Port object that this rule has been applied to.

`Status`

Data type: **uint16**

Access type: Read/write

The status gives an indicator of which level of enforcement this rule is applied to on this port. It will be either *Enforced* or *Error*.

**Unknown** (0)

**Enforced** (1)

**Error** (2)

**EmptyResolution** (3)

**PortNotFound** (4)

**RuleInactive** (5)

**VMCreatorNotApplicable** (6)

**ProfileNotApplicable** (7)

**ProfileDisabled** (8)

**LocalRulesDisallowed** (9)

**ConstrainedInterfaceNotApplicable** (10)

**InboundRuleOptimizedOut** (11)

**LocalAddressRuleNotApplicable** (12)

**HostFirewallDisabled** (13)

**HostFirewallSettingConflict** (14)

**HostFirewallLocalRulesDisallowed** (15)

**HostFirewallRuleCategoryDisabled** (16)

## Requirements

| | |
|-|-|
| Minimum supported client | Windows 8 |
| Minimum supported server | Windows Server 2012 |
| Namespace | Root\\StandardCimv2 |
| MOF | WFasCim.mof |
| DLL | WFasCim.dll |
