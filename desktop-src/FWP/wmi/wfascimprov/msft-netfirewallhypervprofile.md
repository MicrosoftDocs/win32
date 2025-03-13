---
title: MSFT_NetFirewallHyperVProfile class
description: Represents Windows Defender Firewall Hyper-V settings that are applicable to a VM Creator and profile type.
ms.topic: reference
ms.date: 05/16/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallHyperVProfile
api_type: 
- DllExport
api_location: 
- WFasCim.dll
---

# MSFT_NetFirewallHyperVProfile class

Represents Windows Defender Firewall Hyper-V settings that are applicable to a VM Creator and profile type.

For more info, see the Powershell documentation [Set-NetFirewallHyperVProfile](/powershell/module/netsecurity/set-netfirewallhypervprofile).

The following syntax is simplified from Managed Object Format (MOF) code, and includes all of the inherited properties.

## Syntax

```syntax
class MSFT_NetFirewallHyperVProfile : CIM_ManagedElement
{
  string Name;
  uint16 Profile;
  uint16 Enabled;
  uint16 DefaultInboundAction;
  uint16 DefaultOutboundAction;
  uint16 AllowLocalFirewallRules;
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **MSFT_NetFirewallHyperVProfile** class has these types of members:

- [Properties](#properties)

### Properties

The **MSFT_NetFirewallHyperVProfile** class has these properties.

`Name`

Data type: **string**

Access type: Read/write

The unique identifier of the VM creator ID for which these settings apply.

`Profile`

Data type: **uint16**

Access type: Read/write

The network profile that these settings apply on.

**Public** (0x4)

**Private** (0x2)

**Domain** (0x1)

`Enabled`

Data type: **uint16**

Access type: Read/write

Whether the firewall is enabled for this VM type.

**Disabled** (0)

**Enabled** (1)

**NotConfigured** (2)

`DefaultInboundAction`

Data type: **uint16**

Access type: Read/write

The default action for inbound traffic.

**NotConfigured** (0)

**Allow** (2)

**Block** (4)

`DefaultOutboundAction`

Data type: **uint16**

Access type: Read/write

The default action for outbound traffic.

**NotConfigured** (0)

**Allow** (2)

**Block** (4)

`AllowLocalFirewallRules`

Data type: **uint16**

Access type: Read/write

Determines whether local firewall rules should be merged into the effective policy along with Enterprise settings.

**Disabled** (0)

**Enabled** (1)

**NotConfigured** (2)

`InstanceID`

Data type: **string**

Access type: Read-only

Qualifiers: **Key**, **Override**

Reserved for internal use by the WMI provider only.

`Caption`

Data type: **string**

Access type: Read-only

Qualifiers: **Override**

Used in `CimInstance.ToString()`. A short string for describing this instance when debugging.

`Description`

Data type: **string**

Access type: Read-only

Qualifiers: **Override**

This field is ignored.

`ElementName`

Data type: **string**

Access type: Read-only

Qualifiers: **Override**

This field is ignored.

## Requirements

| | |
|-|-|
| Minimum supported client | Windows 8 |
| Minimum supported server | Windows Server 2012 |
| Namespace | Root\\StandardCimv2 |
| MOF | WFasCim.mof |
| DLL | WFasCim.dll |
