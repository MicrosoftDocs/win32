---
description: MSFT\_NetAdapterPowerManagementSettingData represents the Power Management settings and features of a network adapter.
ms.assetid: 525c5657-ebf4-4807-bd55-9fbf3f82458a
title: MSFT\_NetAdapterPowerManagementSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterPowerManagementSettingData
- MSFT_NetAdapterPowerManagementSettingData.Caption
- MSFT_NetAdapterPowerManagementSettingData.Description
- MSFT_NetAdapterPowerManagementSettingData.ElementName
- MSFT_NetAdapterPowerManagementSettingData.InstanceID
- MSFT_NetAdapterPowerManagementSettingData.SystemName
- MSFT_NetAdapterPowerManagementSettingData.Name
- MSFT_NetAdapterPowerManagementSettingData.InterfaceDescription
- MSFT_NetAdapterPowerManagementSettingData.Source
- MSFT_NetAdapterPowerManagementSettingData.AllowComputerToTurnOffDevice
- MSFT_NetAdapterPowerManagementSettingData.D0PacketCoalescing
- MSFT_NetAdapterPowerManagementSettingData.DeviceSleepOnDisconnect
- MSFT_NetAdapterPowerManagementSettingData.ArpOffload
- MSFT_NetAdapterPowerManagementSettingData.NSOffload
- MSFT_NetAdapterPowerManagementSettingData.RsnRekeyOffload
- MSFT_NetAdapterPowerManagementSettingData.OffloadParameters
- MSFT_NetAdapterPowerManagementSettingData.SelectiveSuspend
- MSFT_NetAdapterPowerManagementSettingData.WakeOnMagicPacket
- MSFT_NetAdapterPowerManagementSettingData.WakeOnPattern
- MSFT_NetAdapterPowerManagementSettingData.WakePatterns
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterPowerManagementSettingData class

MSFT\_NetAdapterPowerManagementSettingData represents the Power Management settings and features of a network adapter.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterPowerManagementSettingData : MSFT_NetAdapterSettingData
{
  string Caption;
  string Description;
  string ElementName;
  string InstanceID;
  string SystemName;
  string Name;
  string InterfaceDescription;
  uint32 Source;
  uint32 AllowComputerToTurnOffDevice;
  uint32 D0PacketCoalescing;
  uint32 DeviceSleepOnDisconnect;
  uint32 ArpOffload;
  uint32 NSOffload;
  uint32 RsnRekeyOffload;
  string OffloadParameters[];
  uint32 SelectiveSuspend;
  uint32 WakeOnMagicPacket;
  uint32 WakeOnPattern;
  string WakePatterns[];
};
```

## Members

The **MSFT\_NetAdapterPowerManagementSettingData** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetAdapterPowerManagementSettingData** class has these methods.



| Method                                                               | Description                                                                                    |
|:---------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**Disable**](disable-msft-netadapterpowermanagementsettingdata.md) | Provides a method to disable specific power management capabilities on the adapter.<br/> |
| [**Enable**](enable-msft-netadapterpowermanagementsettingdata.md)   | Provides a method to enable specific power management capabilities on the adapter.<br/>  |



 

### Properties

The **MSFT\_NetAdapterPowerManagementSettingData** class has these properties.

<dl> <dt>

**AllowComputerToTurnOffDevice**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the setting for power management of the adapter. If the property is anything other than Enabled, the remaining property values are undefined.

<dl> <dt>

<span id="Unsupported"></span><span id="unsupported"></span><span id="UNSUPPORTED"></span>**Unsupported** (0)
</dt> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (1)
</dt> <dt>

<span id="Enabled_"></span><span id="enabled_"></span><span id="ENABLED_"></span>**Enabled** (2 )
</dt> </dl>

</dd> <dt>

**ArpOffload**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the setting for ARP offloads on the adapter.

<dl> <dt>

<span id="Unsupported"></span><span id="unsupported"></span><span id="UNSUPPORTED"></span>**Unsupported** (0)
</dt> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (1)
</dt> <dt>

<span id="Enabled_"></span><span id="enabled_"></span><span id="ENABLED_"></span>**Enabled** (2 )
</dt> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** ( 64 )
</dt> </dl>

A short textual description of the object. This property inherits from [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)).

</dd> <dt>

**D0PacketCoalescing**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the setting for D0 Packet Coalescing on the adapter.

<dl> <dt>

<span id="Unsupported"></span><span id="unsupported"></span><span id="UNSUPPORTED"></span>**Unsupported** (0)
</dt> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (1)
</dt> <dt>

<span id="Enabled_"></span><span id="enabled_"></span><span id="ENABLED_"></span>**Enabled** (2 )
</dt> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property inherits from [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)).

</dd> <dt>

**DeviceSleepOnDisconnect**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the setting for sleeping on media disconnect. If this property is Enabled, then the adapter may enter a low power state on a media disconnect event.

<dl> <dt>

<span id="Unsupported"></span><span id="unsupported"></span><span id="UNSUPPORTED"></span>**Unsupported** (0)
</dt> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (1)
</dt> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (2)
</dt> <dt>

<span id="Inactive_"></span><span id="inactive_"></span><span id="INACTIVE_"></span>**Inactive** (3 )
</dt> </dl>

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property enables each instance to define a display name in addition to its key properties, identity data, and description information. Be aware that the Name property of ManagedSystemElement is also defined as a display name. However, it is often subclassed to be a Key. The same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. This property inherits from [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: *OrgID*:*LocalID* Where *OrgID* and *LocalID* are separated by a colon (:), and where *OrgID* must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the *SchemaName*\_*ClassName* structure of Schema class names.) In addition, to ensure uniqueness, *OrgID* must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between *OrgID* and *LocalID*. *LocalID* is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If the above preferred algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. For DMTF-defined instances, the "preferred" algorithm must be used with the *OrgID* set to CIM.

This property inherits from [**CIM\_SettingData**](/previous-versions/windows/desktop/ipamserverpsprov/cim-settingdata).

</dd> <dt>

**InterfaceDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A unique name assigned to the network adapter during installation. This name cannot be changed and is persisted as long as the network adapter is not uninstalled. Also known as the *ifDescr* or *friendly name*.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A unique name assigned to the adapter during installation. The Name of the adapter can be changed by the administrator and is persisted across the boot or network adapter restart. Also known as the *connection name*, *ifAlias*, or *InterfaceAlias.*

</dd> <dt>

**NSOffload**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the setting for NS offloads on the adapter.

<dl> <dt>

<span id="Unsupported"></span><span id="unsupported"></span><span id="UNSUPPORTED"></span>**Unsupported** (0)
</dt> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (1)
</dt> <dt>

<span id="Enabled_"></span><span id="enabled_"></span><span id="ENABLED_"></span>**Enabled** (2 )
</dt> </dl>

</dd> <dt>

**OffloadParameters**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the parameters for protocol offloads on the adapter.

</dd> <dt>

**RsnRekeyOffload**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the setting for 802.11i RSN offloading.

<dl> <dt>

<span id="Unsupported"></span><span id="unsupported"></span><span id="UNSUPPORTED"></span>**Unsupported** (0)
</dt> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (1)
</dt> <dt>

<span id="Enabled_"></span><span id="enabled_"></span><span id="ENABLED_"></span>**Enabled** (2 )
</dt> </dl>

</dd> <dt>

**SelectiveSuspend**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the setting for selective suspend on the adapter.

<dl> <dt>

<span id="Unsupported"></span><span id="unsupported"></span><span id="UNSUPPORTED"></span>**Unsupported** (0)
</dt> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (1)
</dt> <dt>

<span id="Enabled_"></span><span id="enabled_"></span><span id="ENABLED_"></span>**Enabled** (2 )
</dt> </dl>

</dd> <dt>

**Source**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The source of the setting data.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Device"></span><span id="device"></span><span id="DEVICE"></span>**Device** (2)
</dt> <dt>

<span id="Persistent_storage"></span><span id="persistent_storage"></span><span id="PERSISTENT_STORAGE"></span>**Persistent storage** (3)
</dt> </dl>

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The scoping System\\'s Name. This property inherits from [**MSFT\_NetAdapterSettingData**](msft-netadaptersettingdata.md).

</dd> <dt>

**WakeOnMagicPacket**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the setting for waking on Magic Packets. If this property is Enabled, then the adapter wakes the system on receipt of a Magic Packet.

<dl> <dt>

<span id="Unsupported"></span><span id="unsupported"></span><span id="UNSUPPORTED"></span>**Unsupported** (0)
</dt> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (1)
</dt> <dt>

<span id="Enabled_"></span><span id="enabled_"></span><span id="ENABLED_"></span>**Enabled** (2 )
</dt> </dl>

</dd> <dt>

**WakeOnPattern**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the setting for waking on a packet pattern. If this property is Enabled, then the adapter wakes the system on receipt of a specified pattern.

<dl> <dt>

<span id="Unsupported"></span><span id="unsupported"></span><span id="UNSUPPORTED"></span>**Unsupported** (0)
</dt> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (1)
</dt> <dt>

<span id="Enabled_"></span><span id="enabled_"></span><span id="ENABLED_"></span>**Enabled** (2 )
</dt> </dl>

</dd> <dt>

**WakePatterns**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the list of packet patterns programmed to wake the system.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

