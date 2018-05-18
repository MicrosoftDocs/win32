---
Description: 'Represents a physical IP address of the network interface the WNV module is configured on.'
ms.assetid: '4a3f5aa2-446e-4b9d-8422-d4b01bfcdbb9'
title: 'MSFT\_NetVirtualizationProviderAddressSettingData class'
---

# MSFT\_NetVirtualizationProviderAddressSettingData class

Represents a physical IP address of the network interface the WNV module is configured on.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetVirtualizationProviderAddressSettingData : MSFT_NetSettingData
{
  string  ProviderAddress;
  uint32  InterfaceIndex;
  uint8   PrefixLength;
  uint16  VlanID;
  uint16  AddressState;
  string  MACAddress;
  boolean ManagedByCluster;
};
```

## Members

The **MSFT\_NetVirtualizationProviderAddressSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetVirtualizationProviderAddressSettingData** class has these properties.

<dl> <dt>

**AddressState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the state of the IP address.

<dl> <dt>

<span id="0"></span>**0** (16)
</dt> <dt>

<span id="1"></span>**1** (17)
</dt> <dt>

<span id="2"></span>**2** (18)
</dt> <dt>

<span id="3"></span>**3** (19)
</dt> <dt>

<span id="4"></span>**4** (20)
</dt> </dl>

</dd> <dt>

**InterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Index of the interface the WNV module is configured on.

</dd> <dt>

**MACAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the MAC address of the network interface.

</dd> <dt>

**ManagedByCluster**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the network is managed by a cluster. This property can be set to one of the following values.

<dl> <dt>

<span id="0"></span>**0** (23)
</dt> <dt>

<span id="1"></span>**1** (24)
</dt> </dl>

</dd> <dt>

**PrefixLength**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The prefix length for the Provider IP address.

</dd> <dt>

**ProviderAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address.

</dd> <dt>

**VlanID**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Optional VLAN Identifier corresponding to the Provider IP address.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                        |
| MOF<br/>                      | <dl> <dt>NetWNV.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetWNV.dll</dt> </dl> |



 

 




