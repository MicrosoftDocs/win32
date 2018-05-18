---
title: Msvm\_VLANEndpointSettingData class
description: Represents the settings for a VLAN endpoint of a switch port.
ms.assetid: '44e1d530-3b9c-4f99-8472-9532eb8a4b07'
keywords: ["Msvm_VLANEndpointSettingData class Hyper-V", "Msvm_VLANEndpointSettingData class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_VLANEndpointSettingData
- Msvm_VLANEndpointSettingData.Caption
- Msvm_VLANEndpointSettingData.Description
- Msvm_VLANEndpointSettingData.InstanceID
- Msvm_VLANEndpointSettingData.PruneEligibleVLANList
- Msvm_VLANEndpointSettingData.NativeVLAN
- Msvm_VLANEndpointSettingData.DefaultVLAN
- Msvm_VLANEndpointSettingData.TrunkedVLANList
- Msvm_VLANEndpointSettingData.AccessVLAN
- Msvm_VLANEndpointSettingData.SecondaryVlan
- Msvm_VLANEndpointSettingData.PrimaryVlan
- Msvm_VLANEndpointSettingData.PVlanMode
- Msvm_VLANEndpointSettingData.ElementName
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_VLANEndpointSettingData class

Represents the settings for a VLAN endpoint of a switch port. The configuration of this setting will change the way the switch port sends VLAN packets through the switch.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VLANEndpointSettingData : CIM_VLANEndpointSettingData
{
  string Caption;
  string Description;
  string InstanceID = "Microsoft:GUID\Root";
  uint16 PruneEligibleVLANList[];
  uint16 NativeVLAN;
  uint16 DefaultVLAN;
  uint16 TrunkedVLANList[];
  uint16 AccessVLAN;
  uint16 SecondaryVlan;
  uint16 PrimaryVlan;
  uint8  PVlanMode;
  string ElementName;
};
```

## Members

The **Msvm\_VLANEndpointSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VLANEndpointSettingData** class has these properties.

<dl> <dt>

**AccessVLAN**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**OperationalEndpointMode**")
</dt> </dl>

The access VLAN for the referenced VLANEndpoint. This property is inherited from [**CIM\_VLANEndpointSettingData**](https://msdn.microsoft.com/library/cc150676).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

</dd> <dt>

**DefaultVLAN**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**OperationalEndpointMode**")
</dt> </dl>

The default value for the native VLAN on this trunk endpoint/port. This property is applicable only when the endpoint is operating in trunking mode (determined by examining the **OperationalEndpointMode** property). This property is inherited from [**CIM\_VLANEndpointSettingData**](https://msdn.microsoft.com/library/cc150676).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. Note that the [**Name**](https://msdn.microsoft.com/library/aa387898) property of the **CIM\_ManagedSystemElement** class is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where [**Name**](msvm-keyboard.md) exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the **Name** and **ElementName** properties. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A unique identifier for this resource pool. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291) and it is always set to "Microsoft:*GUID*\\Root".

</dd> <dt>

**NativeVLAN**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**OperationalEndpointMode**")
</dt> </dl>

The VLAN Id that is used to tag untagged traffic received on this trunk endpoint/port. This property is applicable only when the endpoint is operating in trunking mode (determined by examining the **SwitchEndpointMode** property). This property is inherited from [**CIM\_VLANEndpointSettingData**](https://msdn.microsoft.com/library/cc150676).

</dd> <dt>

**PrimaryVlan**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The primary Vlan if the port is in Private Vlan mode.

</dd> <dt>

**PruneEligibleVLANList**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**OperationalEndpointMode**")
</dt> </dl>

If a VLAN ID is part of this array, then the system MAY prune that VLAN on the related trunk endpoint/port. This property is applicable only when the endpoint is operating in trunking mode (determined by examining the **OperationalEndpointMode** property). This property is inherited from [**CIM\_VLANEndpointSettingData**](https://msdn.microsoft.com/library/cc150676).

</dd> <dt>

**PVlanMode**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The private VLAN Mode mode supported by this port.

<dt>

<span id="unknown"></span><span id="UNKNOWN"></span>

**unknown** (0)


</dt> <dd></dd> <dt>

<span id="Incoming"></span><span id="incoming"></span><span id="INCOMING"></span>

**Incoming** (1)


</dt> <dd></dd> <dt>

<span id="Outgoing"></span><span id="outgoing"></span><span id="OUTGOING"></span>

**Outgoing** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**SecondaryVlan**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The secondary Vlan if the port is in Private Vlan mode.

</dd> <dt>

**TrunkedVLANList**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**OperationalEndpointMode**")
</dt> </dl>

If a VLAN Id is part of this array, then the system MAY trunk the traffic on the related endpoint/port. This property is applicable only when the endpoint is operating in trunking mode (determined by examining the **OperationalEndpointMode** property). This property is inherited from [**CIM\_VLANEndpointSettingData**](https://msdn.microsoft.com/library/cc150676).

</dd> </dl>

## Remarks

The [**Msvm\_NetworkElementSettingData**](msvm-networkelementsettingdata.md) class is used to hold the association between the [**Msvm\_VLANEndpoint**](msvm-vlanendpoint.md) and **Msvm\_VLANEndpointSettingData** classes.

Access to the **Msvm\_VLANEndpointSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

See [Querying Networking Objects](querying-networking-objects.md).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_VLANEndpointSettingData**](cim-vlanendpointsettingdata.md)
</dt> <dt>

[**CIM\_VLANEndpointSettingData**](https://msdn.microsoft.com/library/cc150676)
</dt> <dt>

[Networking Classes](networking-classes.md)
</dt> </dl>

 

 





