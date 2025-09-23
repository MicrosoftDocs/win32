---
title: MSFT_NetFirewallHyperVPort class
description: Represents a particular Windows Defender Firewall Hyper-V port.
ms.topic: reference
ms.date: 05/16/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallHyperVPort
api_type: 
- DllExport
api_location: 
- WFasCim.dll
---

# MSFT_NetFirewallHyperVPort class

Represents a particular Windows Defender Firewall Hyper-V port.

For more info, see the Powershell documentation [Get-NetFirewallHyperVPort](/powershell/module/netsecurity/get-netfirewallhypervport).

The following syntax is simplified from Managed Object Format (MOF) code, and includes all of the inherited properties.

## Syntax

```syntax
class MSFT_NetFirewallHyperVPort : CIM_ManagedElement
{
  string SwitchName;
  string PortName;
  string VMCreatorId;
  string InterfaceGuid;
  string PartitionGuid;
  uint16 Constrained;
  uint16 Profile;
  uint16 NetworkType;
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **MSFT_NetFirewallHyperVPort** class has these types of members:

- [Properties](#properties)

### Properties

The **MSFT_NetFirewallHyperVPort** class has these properties.

`SwitchName`

Data type: **string**

Access type: Read/write

The name of the vswitch that this object applies to.

`PortName`

Data type: **string**

Access type: Read/write

The name of the vswitch port that this object applies to.

`VMCreatorId`

Data type: **string**

Access type: Read/write

The unique identifier of the VM Creator of this object.

`InterfaceGuid`

Data type: **string**

Access type: Read/write

The interface Guid of this port.

`PartitionGuid`

Data type: **string**

Access type: Read/write

The partition Guid of this port.

`Constrained`

Data type: **uint16**

Access type: Read/write

Whether this object has its traffic constrained. A value of constrained means that only Local Subnet traffic is permitted on this interface.

**NotConstrained** (0)

**Constrained** (1)

`Profile`

Data type: **uint16**

Access type: Read/write

The network profile of this port.

**Public** (0x4)

**Private** (0x2)

**Domain** (0x1)

`NetworkType`

Data type: **uint16**

Access type: Read/write

The network type of this port.

**Unknown** (0x0)

**FSE** (0x1)

**NAT** (0x2)

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
