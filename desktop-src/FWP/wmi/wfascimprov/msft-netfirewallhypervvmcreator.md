---
title: MSFT_NetFirewallHyperVVMCreator class
description: Represents a particular Windows Defender Firewall Hyper-V VM Creator.
ms.topic: reference
ms.date: 05/17/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallHyperVVMCreator
api_type: 
- DllExport
api_location: 
- WFasCim.dll
---

# MSFT_NetFirewallHyperVVMCreator class

Represents a particular Windows Defender Firewall Hyper-V VM Creator.

For more info, see the Powershell documentation [Get-NetFirewallHyperVVMCreator](/powershell/module/netsecurity/get-netfirewallhypervvmcreator).

The following syntax is simplified from Managed Object Format (MOF) code, and includes all of the inherited properties.

## Syntax

```syntax
class MSFT_NetFirewallHyperVVMCreator : CIM_ManagedElement
{
  string VMCreatorId;
  string FriendlyName;
  uint32 RegisterHyperVVMCreator
  (
    string VMCreatorId, 
    string FriendlyName
  ); 
  uint32 UnregisterHyperVVMCreator
  (
    string VMCreatorId
  );
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **MSFT_NetFirewallHyperVVMCreator** class has these types of members:

- [Methods](#methods)
- [Properties](#properties)

### Methods

The **MSFT_NetFirewallHyperVVMCreator** class has these methods.

| Method | Description |
|:-|:-|
| [**RegisterHyperVVMCreator**](./registerhypervvmcreator-msft-netfirewallhypervvmcreator.md) | Registers a Hyper-V VM Creator with the firewall service. |
| [**UnregisterHyperVVMCreator**](./unregisterhypervvmcreator-msft-netfirewallhypervvmcreator.md) | Unregisters a Hyper-V VM Creator with the firewall service. |

### Properties

The **MSFT_NetFirewallHyperVVMCreator** class has these properties.

`VMCreatorId`

Data type: **string**

Access type: Read/write

A GUID in string format that serves as the unique identifier for this VM Creator. This value will be used across Hyper-V firewall policy objects to scope their enforcement to Hyper-V ports created by this VM Creator.

`FriendlyName`

Data type: **string**

Access type: Read/write

The friendly name of this VM Creator.

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
