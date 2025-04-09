---
title: MSFT_NetFirewallHyperVVMSetting class
description: Represents Windows Defender Firewall Hyper-V settings for a VM type.
ms.topic: reference
ms.date: 05/17/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallHyperVVMSetting
api_type: 
- DllExport
api_location: 
- WFasCim.dll
---

# MSFT_NetFirewallHyperVVMSetting class

Represents Windows Defender Firewall Hyper-V settings for a VM type.

For more info, see the Powershell documentation [Set-NetFirewallHyperVVMSetting](/powershell/module/netsecurity/set-netfirewallhypervvmsetting).

The following syntax is simplified from Managed Object Format (MOF) code, and includes all of the inherited properties.

## Syntax

```syntax
class MSFT_NetFirewallHyperVVMSetting : CIM_ManagedElement
{
  string Name;
  uint16 Enabled;
  uint16 DefaultInboundAction;
  uint16 DefaultOutboundAction;
  uint16 LoopbackEnabled;
  uint16 AllowHostPolicyMerge;
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **MSFT_NetFirewallHyperVVMSetting** class has these types of members:

- [Properties](#properties)

### Properties

The **MSFT_NetFirewallHyperVVMSetting** class has these properties.

`Name`

Data type: **string**

Access type: Read/write

The unique identifier of the VM creator ID for which these settings apply.

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

`LoopbackEnabled`

Data type: **uint16**

Access type: Read/write

Whether loopback is enabled for this VM type.

**Disabled** (0)

**Enabled** (1)

**NotConfigured** (2)

`AllowHostPolicyMerge`

Data type: **uint16**

Access type: Read/write

Determines whether host firewall rules and settings should be merged into the effective policy.

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
