---
title: MSFT_NetFirewallHyperVRule class
description: Represents a Windows Defender firewall Hyper-V rule.
ms.topic: reference
ms.date: 05/17/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallHyperVRule
api_type: 
- DllExport
api_location: 
- WFasCim.dll
---

# MSFT_NetFirewallHyperVRule class

Represents a Windows Defender firewall Hyper-V rule.

For more info, see the Powershell documentation [New-NetFirewallHyperVRule](/powershell/module/netsecurity/new-netfirewallhypervrule).

The following syntax is simplified from Managed Object Format (MOF) code, and includes all of the inherited properties.

## Syntax

```syntax
class MSFT_NetFirewallHyperVRule : CIM_PolicyRule
{
  string DisplayName;
  uint16 RulePriority;
  uint16 Direction;
  string VMCreatorId;
  string Protocol;
  string LocalAddresses[];
  string LocalPorts[];
  string RemoteAddresses[];
  string RemotePorts[];
  uint16 Action;
  uint16 EnforcementStatus;
  uint16 PolicyStoreSourceType;
  string PortStatuses[];
  uint16 Profiles;
  uint32 Enable();
  uint32 Disable();
  uint32 Rename
  (
    string NewName
  );
  uint32 EnumerateFull
  (
    string Dependents[]
  );
  string SystemCreationClassName;
  string SystemName;
  string CreationClassName;
  string PolicyRuleName;
  uint16 ConditionListType;
  string RuleUsage;
  uint16 Priority;
  boolean Mandatory;
  uint16 SequencedActions;
  uint16 ExecutionStrategy;
  uint16 PolicyDecisionStrategy;
  string PolicyRoles[];
  uint16 Enabled = 1;
  string CommonName;
  string PolicyKeywords[];
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **MSFT_NetFirewallHyperVRule** class has these types of members:

- [Methods](#methods)
- [Properties](#properties)

### Methods

The **MSFT_NetFirewallHyperVRule** class has these methods.

| Method | Description |
|:-|:-|
| [**Disable**](./disable-msft-netfirewallhypervrule.md) | Disable this rule. |
| [**Enable**](./enable-msft-netfirewallhypervrule.md) | Enable this rule. |
| [**EnumerateFull**](./enumeratefull-msft-netfirewallhypervrule.md) | Enumerates all fields of all rules. |
| [**Rename**](./rename-msft-netfirewallhypervrule.md) | Rename this rule. |

### Properties

The **MSFT_NetFirewallHyperVRule** class has these properties.

`DisplayName`

Data type: **string**

Access type: Read-only

The localized name of this rule. This field's value is based on the value of *ElementName*. Changes to this field are ignored.

`RulePriority`

Data type: **uint16**

Access type: Read/write

Determines the order in which rules are evaluated. Lower priority rules are evaluated first. If this value is 0 (unset), then the system will assign a value of 1 to rules with action Block, and 2 to rules with action Allow.

`Direction`

Data type: **uint16**

Access type: Read/write

Specifies which direction of traffic to match with this rule.

**Inbound** (1)

**Outbound** (2)

`VMCreatorId`

Data type: **string**

Access type: Read/write

Specifies the unique identifier of the VM creator to which this rule is applicable. A NULL GUID value means that this rule is applicable to all Hyper-V ports on the system.

`Protocol`

Data type: **string**

Access type: Read/write

IANA Internet Protocol Number that this filter applies to. May be 0-255 or one of the following: TCP, UDP.

`LocalAddresses`

Data type: **string**\[\]

Access type: Read/write

An array of IP addresses, subnets, or ranges. Valid formats include: a valid IPv4 address in strict four-part dotted decimal notation (for example, 10.0.0.10), a valid IPv6 address in Internet standard format as described in section 2.2 of RFC 4291 (for example, 2620:1ec:c11::200), an IPv4 address range in the format of 'start address - end address' with no spaces included (for example, 10.0.0.0-10.0.0.255), an IPv6 address range in the format of 'start address - end address' with no spaces included (for example, 2001:db8:abcd:12::-2001:db8:abcd:12:ffff:ffff:ffff:ffff), a valid IPv4 subnet specified using the network prefix notation (for example, 10.0.0.0/24), a valid IPv6 subnet specified using the prefix length notation (for example, 2001:db8:abcd:0012::/64)".

`LocalPorts`

Data type: **string**\[\]

Access type: Read/write

Local ports that this filter applies to (applies only when Protocol is TCP or UDP). May be a number or range 0-65535, or one of the following: Any, RPC, RPC-EPMap, IPHTTPSIn, PlayToDiscovery.

`RemoteAddresses`

Data type: **string**\[\]

Access type: Read/write

An array of IP addresses, subnets, or ranges. Valid formats include: a valid IPv4 address in strict four-part dotted decimal notation (for example, 10.0.0.10), a valid IPv6 address in Internet standard format as described in section 2.2 of RFC 4291 (for example, 2620:1ec:c11::200), an IPv4 address range in the format of 'start address - end address' with no spaces included (for example, 10.0.0.0-10.0.0.255), an IPv6 address range in the format of 'start address - end address' with no spaces included (for example, 2001:db8:abcd:12::-2001:db8:abcd:12:ffff:ffff:ffff:ffff), a valid IPv4 subnet specified using the network prefix notation (for example, 10.0.0.0/24), a valid IPv6 subnet specified using the prefix length notation (for example, 2001:db8:abcd:0012::/64)".

`RemotePorts`

Data type: **string**\[\]

Access type: Read/write

Remote ports that this filter applies to (applies only when Protocol is TCP or UDP). May be a number or range 0-65535, or one of the following: Any, IPHTTPSOut.

`Action`

Data type: **uint16**

Access type: Read/write

Specifies the action to take on traffic that matches this rule.

**Allow** (2)

**Block** (4)

`EnforcementStatus`

Data type: **uint16**

Access type: Read/write

Describes the current enforcement status of this rule.

**Invalid** (0)

**FullyEnforced** (1)

**PartiallyEnforced** (2)

**NoApplicablePorts** (3)

**ParsingError** (4)

**Error** (5)

`PolicyStoreSourceType`

Data type: **uint16**

Access type: Read/write

Describes the type of PolicyStore where this rule originally came from.

**Unknown** (0)

**Local** (1)

**Dynamic** (3)

**Generated** (5)

**MDM** (6)

**HostFirewallLocal** (8)

**HostFirewallGroupPolicy** (9)

**HostFirewallDynamic** (10)

**HostFirewallMDM** (11)

`PortStatuses`

Data type: **string**\[\]

Access type: Read/write

List of statuses for each port that this rule has been applied to.

`Profiles`

Data type: **uint16**

Access type: Read/write

Bitmask of profiles that this rule is active on.

**Any** (0)

**Public** (0x4)

**Private** (0x2)

**Domain** (0x1)

`SystemCreationClassName`

Data type: **string**

Access type: Read-only

Qualifiers: **Override**

Reserved for internal use by the WMI provider only.

`SystemName`

Data type: **string**

Access type: Read-only

Qualifiers: **Override**

Reserved for internal use by the WMI provider only.

`CreationClassName`

Data type: **string**

Access type: Read-only

Qualifiers: **Override**

Reserved for internal use by the WMI provider only.

`PolicyRuleName`

Data type: **string**

Access type: Read-only

Qualifiers: **Override**

Reserved for internal use by the WMI provider only.

`ConditionListType`

Data type: **uint16**

Access type: Read-only

Qualifiers: **Override**

This field is ignored.

`RuleUsage`

Data type: **string**

Access type: Read-only

Qualifiers: **Override**

This field is ignored.

`Priority`

Data type: **uint16**

Access type: Read-only

Qualifiers: **Override**

This field is ignored.

`Mandatory`

Data type: **boolean**

Access type: Read-only

Qualifiers: **Override**

This field is ignored.

`SequencedActions`

Data type: **uint16**

Access type: Read-only

Qualifiers: **Override**

This field is ignored.

`ExecutionStrategy`

Data type: **uint16**

Access type: Read-only

Qualifiers: **Override**

This field is ignored.

`PolicyDecisionStrategy`

Data type: **uint16**

Access type: Read-only

Qualifiers: **Override**

This field is ignored.

`PolicyRoles`

Data type: **string**\[\]

Access type: Read-only

Qualifiers: **Override**

This field is ignored.

`Profiles`

Data type: **uint16**

Access type: Read-only

Qualifiers: **Override**

Indicates whether this rule is administratively enabled or disabled. The default value is "1" (Enabled).

**Enabled** (1)

**Disabled** (2)

`CommonName`

Data type: **string**

Access type: Read-only

Qualifiers: **Override**

This field is ignored.

`PolicyKeywords`

Data type: **string**\[\]

Access type: Read-only

Qualifiers: **Override**

This field is ignored.

`InstanceID`

Data type: **string**

Access type: Read-only

Qualifiers: **Override**

A string that uniquely identifies this instance within the PolicyStore.

`Caption`

Data type: **string**

Access type: Read-only

Qualifiers: **Override**, **MaxLen** (64)

The Caption property is a short textual description (a one-line string) of the object.

`Description`

Data type: **string**

Access type: Read/write

Qualifiers: **Override**

A brief description of the rule. Might be an indirect string. If it is an indirect string, then it might not be overwritten.

`ElementName`

Data type: **string**

Access type: Read/write

Qualifiers: **Override**

The locale-independent name of the rule. Might be an indirect string.

## Requirements

| | |
|-|-|
| Minimum supported client | Windows 8 |
| Minimum supported server | Windows Server 2012 |
| Namespace | Root\\StandardCimv2 |
| MOF | WFasCim.mof |
| DLL | WFasCim.dll |
