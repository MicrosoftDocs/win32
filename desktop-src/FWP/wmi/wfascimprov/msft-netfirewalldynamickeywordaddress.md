---
title: MSFT_NetFirewallDynamicKeywordAddress class
description: This class represents a Windows Defender Firewall dynamic keyword address.
ms.topic: reference
ms.date: 05/14/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallDynamicKeywordAddress
api_type: 
- DllExport
api_location: 
- WFasCim.dll
---

# MSFT_NetFirewallDynamicKeywordAddress class

This class represents a Windows Defender Firewall dynamic keyword address.

For more info, see the Powershell documentation [New-NetFirewallDynamicKeywordAddress](/powershell/module/netsecurity/new-netfirewalldynamickeywordaddress).

The following syntax is simplified from Managed Object Format (MOF) code, and includes all of the inherited properties.

## Syntax

```syntax
class MSFT_NetFirewallDynamicKeywordAddress : CIM_ManagedElement
{
  string Id;
  string Keyword;
  string Addresses;
  boolean AutoResolve;
  uint16 PolicyStoreSourceType;
  string PolicyStoreSource;
  uint32 UpdateDynamicKeywordAddress
  (
    string Id,
    string Addresses,
    boolean Append
  );
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
}
```

## Members

The **MSFT_NetFirewallDynamicKeywordAddress** class has these types of members:

- [Methods](#methods)
- [Properties](#properties)

### Methods

The **MSFT_NetFirewallDynamicKeywordAddress** class has these methods.

| Method | Description |
|:-|:-|
| [**UpdateDynamicKeywordAddress**](updatedynamickeywordaddress-msft-netfirewalldynamickeywordaddress.md) | Updates the dynamic keyword address. |

### Properties

The **MSFT_NetFirewallDynamicKeywordAddress** class has these properties.

`Id`

Data type: **string**

Access type: Read/write

Qualifiers: **Key**, **Override**

GUID that uniquely identifies this keyword.

`Keyword`

Data type: **string**

Access type: Read/write

Qualifiers: **Override**

Name for this keyword. If the 'AutoResolve' flag is 'TRUE', then this should be a resolvable name.

`Addresses`

Data type: **string**

Access type: Read/write

Qualifiers: **Override**

Name for this keyword. If the 'AutoResolve' flag is 'TRUE', then this should be a resolvable name.

A comma-separated list of addresses, subnets, or ranges that this keyword represents. This must not be set upon creation if the 'AutoResolve' flag is 'TRUE'. Valid formats include: a valid IPv4 address in strict four-part dotted decimal notation (for example, 10.0.0.10), a valid IPv6 address in Internet standard format as described in section 2.2 of RFC 4291 (for example, 2620:1ec:c11::200), an IPv4 address range in the format of 'start address - end address' with no spaces included (for example, 10.0.0.0-10.0.0.255), an IPv6 address range in the format of 'start address - end address' with no spaces included (for example, 2001:db8:abcd:12::-2001:db8:abcd:12:ffff:ffff:ffff:ffff), a valid IPv4 subnet specified using the network prefix notation (for example, 10.0.0.0/24), a valid IPv6 subnet specified using the prefix length notation (for example, 2001:db8:abcd:0012::/64)".

`AutoResolve`

Data type: **boolean**

Access type: Read/write

Qualifiers: **Override**

A 'TRUE' value indicates that a component outside the firewall service is responsible for resolving the 'Keyword' and updating the addresses in this object. If this value is 'TRUE' the 'Keyword' value should be a resolvable name".

`PolicyStoreSourceType`

Data type: **uint16**

Access type: Read/write

This value is set by the server which indicates the type of PolicyStore where this dynamic keyword address originally came from. This value is 1 when the 'PolicyStore' is 'Local' or 6 when the 'PolicyStore' is 'MDM'.

`PolicyStoreSource`

Data type: **string**

Access type: Read/write

This value is set by the server which indicates the PolicyStore where this dynamic keyword address originally came from. This value is either 'Local' if the object was created on the local machine or 'MDM' if the object was created via Mobile Device Management.

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
