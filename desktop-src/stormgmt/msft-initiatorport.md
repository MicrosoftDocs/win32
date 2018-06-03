---
title: MSFT\_InitiatorPort class
description: Represents a Host Bus Adapter (HBA) initiator port on the host computer.
ms.assetid: FFD445F4-3A34-4681-B38E-6E84C0E5DF06
keywords:
- MSFT_InitiatorPort class Windows Storage Management API
- MSFT_InitiatorPort class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_InitiatorPort
- MSFT_InitiatorPort.ObjectId
- MSFT_InitiatorPort.PortAddress
- MSFT_InitiatorPort.NodeAddress
- MSFT_InitiatorPort.InstanceName
- MSFT_InitiatorPort.AlternatePortAddress
- MSFT_InitiatorPort.AlternateNodeAddress
- MSFT_InitiatorPort.PortType
- MSFT_InitiatorPort.ConnectionType
- MSFT_InitiatorPort.OtherConnectionTypeDescription
- MSFT_InitiatorPort.OperationalStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_InitiatorPort class

Represents a Host Bus Adapter (HBA) initiator port on the host computer.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_InitiatorPort
{
  String ObjectId;
  String PortAddress;
  String NodeAddress;
  String InstanceName;
  String AlternatePortAddress[];
  String AlternateNodeAddress[];
  UInt16 PortType;
  UInt16 ConnectionType;
  String OtherConnectionTypeDescription;
  UInt16 OperationalStatus[];
};
```

## Members

The **MSFT\_InitiatorPort** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_InitiatorPort** class has these methods.



| Method                                                      | Description                                              |
|:------------------------------------------------------------|:---------------------------------------------------------|
| [**SetNodeAddress**](msft-initiatorport-setnodeaddress.md) | Sets the node address for the initiator port.<br/> |



 

### Properties

The **MSFT\_InitiatorPort** class has these properties.

<dl> <dt>

**AlternateNodeAddress**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

A list of alternate node addresses for the initiator.

</dd> <dt>

**AlternatePortAddress**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

A list of alternate port addresses for the initiator.

</dd> <dt>

**ConnectionType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The connection type.

You can specify a predefined connection type or a custom connection type. To specify a predefined connection type, use a value other than **Other**.

To specify a custom connection type, use **Other** and specify a non-NULL value for the **OtherConnectionTypeDescription** property.

<dl> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (0)
</dt> <dt>

<span id="Fibre_Channel"></span><span id="fibre_channel"></span><span id="FIBRE_CHANNEL"></span>**Fibre Channel** (1)
</dt> <dt>

<span id="iSCSI"></span><span id="iscsi"></span><span id="ISCSI"></span>**iSCSI** (2)
</dt> <dt>

<span id="SAS"></span><span id="sas"></span>**SAS** (3)
</dt> </dl>

</dd> <dt>

**InstanceName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The instance name for the initiator.

</dd> <dt>

**NodeAddress**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The node address for the initiator.

</dd> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The object identifier for the initiator.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of values that denote the current status of the initiator port.

You can specify a predefined status or a custom status. To specify a predefined status, use a value other than **Other**.

To specify a custom status, use **Other** and specify a non-NULL value for the **OtherOperationalStatusDescription** property.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (1)
</dt> <dt>

<span id="Operational"></span><span id="operational"></span><span id="OPERATIONAL"></span>**Operational** (2)
</dt> <dt>

<span id="User_Offline"></span><span id="user_offline"></span><span id="USER_OFFLINE"></span>**User Offline** (3)
</dt> <dt>

<span id="Bypassed"></span><span id="bypassed"></span><span id="BYPASSED"></span>**Bypassed** (4)
</dt> <dt>

<span id="In_diagnostics_mode"></span><span id="in_diagnostics_mode"></span><span id="IN_DIAGNOSTICS_MODE"></span>**In diagnostics mode** (5)
</dt> <dt>

<span id="Link_Down"></span><span id="link_down"></span><span id="LINK_DOWN"></span>**Link Down** (6)
</dt> <dt>

<span id="Port_Error"></span><span id="port_error"></span><span id="PORT_ERROR"></span>**Port Error** (7)
</dt> <dt>

<span id="Loopback"></span><span id="loopback"></span><span id="LOOPBACK"></span>**Loopback** (8)
</dt> </dl>

</dd> <dt>

**OtherConnectionTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representation of the vendor-defined connection type. This property should be set only if the value of the **ConnectionType** property is **Other**.

</dd> <dt>

**PortAddress**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port address for the initiator.

</dd> <dt>

**PortType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port type for the initiator.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (1)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (2)
</dt> <dt>

<span id="Not_present"></span><span id="not_present"></span><span id="NOT_PRESENT"></span>**Not present** (3)
</dt> <dt>

<span id="Fabric"></span><span id="fabric"></span><span id="FABRIC"></span>**Fabric** (5)
</dt> <dt>

<span id="Public_Loop"></span><span id="public_loop"></span><span id="PUBLIC_LOOP"></span>**Public Loop** (6)
</dt> <dt>

<span id="FL_Port"></span><span id="fl_port"></span><span id="FL_PORT"></span>**FL Port** (7)
</dt> <dt>

<span id="Fabric_Port"></span><span id="fabric_port"></span><span id="FABRIC_PORT"></span>**Fabric Port** (8)
</dt> <dt>

<span id="Fabric_expansion_port"></span><span id="fabric_expansion_port"></span><span id="FABRIC_EXPANSION_PORT"></span>**Fabric expansion port** (9)
</dt> <dt>

<span id="Generic_Fabric_Port"></span><span id="generic_fabric_port"></span><span id="GENERIC_FABRIC_PORT"></span>**Generic Fabric Port** (10)
</dt> <dt>

<span id="Private_Loop"></span><span id="private_loop"></span><span id="PRIVATE_LOOP"></span>**Private Loop** (20)
</dt> <dt>

<span id="Point_to_Point"></span><span id="point_to_point"></span><span id="POINT_TO_POINT"></span>**Point to Point** (21)
</dt> <dt>

<span id="SAS"></span><span id="sas"></span>**SAS** (30)
</dt> <dt>

<span id="SATA"></span><span id="sata"></span>**SATA** (31)
</dt> <dt>

<span id="SAS_Expander"></span><span id="sas_expander"></span><span id="SAS_EXPANDER"></span>**SAS Expander** (32)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





