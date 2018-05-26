---
title: MSFT\_TargetPort class
description: Represents a target port.
ms.assetid: 00D10838-331D-4145-9040-2F96A85324EB
keywords:
- MSFT_TargetPort class Windows Storage Management API
- MSFT_TargetPort class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_TargetPort
- MSFT_TargetPort.FriendlyName
- MSFT_TargetPort.PortAddress
- MSFT_TargetPort.NodeAddress
- MSFT_TargetPort.StorageControllerId
- MSFT_TargetPort.Role
- MSFT_TargetPort.UsageRestriction
- MSFT_TargetPort.HealthStatus
- MSFT_TargetPort.OperationalStatus
- MSFT_TargetPort.OtherOperationalStatusDescription
- MSFT_TargetPort.ConnectionType
- MSFT_TargetPort.OtherConnectionTypeDescription
- MSFT_TargetPort.LinkTechnology
- MSFT_TargetPort.OtherLinkTechnology
- MSFT_TargetPort.Speed
- MSFT_TargetPort.MaxSpeed
- MSFT_TargetPort.NetworkAddresses
- MSFT_TargetPort.PortNumbers
- MSFT_TargetPort.PortType
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_TargetPort class

Represents a target port.

A target port is an endpoint in a storage subsystem with associated properties for showing and hiding virtual disks. Fibre Channel, Serial Attached SCSI, and iSCSI ports within a storage subsystem controller are all examples of target ports.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_TargetPort : MSFT_StorageObject
{
  String FriendlyName;
  String PortAddress;
  String NodeAddress;
  String StorageControllerId;
  UInt16 Role;
  UInt16 UsageRestriction;
  UInt16 HealthStatus;
  UInt16 OperationalStatus[];
  String OtherOperationalStatusDescription;
  UInt16 ConnectionType;
  String OtherConnectionTypeDescription;
  UInt16 LinkTechnology;
  String OtherLinkTechnology;
  UInt64 Speed;
  UInt64 MaxSpeed;
  String NetworkAddresses[];
  UInt16 PortNumbers[];
  UInt16 PortType;
};
```

## Members

The **MSFT\_TargetPort** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_TargetPort** class has these properties.

<dl> <dt>

**ConnectionType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>



| Value                                                                        | Meaning                  |
|------------------------------------------------------------------------------|--------------------------|
| <dl> <dt>1</dt> </dl> | Other<br/>         |
| <dl> <dt>2</dt> </dl> | Fibre Channel<br/> |
| <dl> <dt>3</dt> </dl> | Parallel SCSI<br/> |
| <dl> <dt>4</dt> </dl> | SSA<br/>           |
| <dl> <dt>5</dt> </dl> | IEEE 1394<br/>     |
| <dl> <dt>6</dt> </dl> | RDMA<br/>          |
| <dl> <dt>7</dt> </dl> | iSCSI<br/>         |
| <dl> <dt>8</dt> </dl> | SAS<br/>           |
| <dl> <dt>9</dt> </dl> | ADT<br/>           |



 

</dd> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly name for the target port.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The health status of the target port.

<dl> <dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>**Healthy** (0)
</dt> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>**Warning** (1)
</dt> <dt>

<span id="Unhealthy_"></span><span id="unhealthy_"></span><span id="UNHEALTHY_"></span>**Unhealthy** (2 )
</dt> </dl>

</dd> <dt>

**LinkTechnology**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The link technology of the target port.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Ethernet"></span><span id="ethernet"></span><span id="ETHERNET"></span>**Ethernet** (2)
</dt> <dt>

<span id="IB"></span><span id="ib"></span>**IB** (3)
</dt> <dt>

<span id="FC"></span><span id="fc"></span>**FC** (4)
</dt> <dt>

<span id="FDDI"></span><span id="fddi"></span>**FDDI** (5)
</dt> <dt>

<span id="ATM"></span><span id="atm"></span>**ATM** (6)
</dt> <dt>

<span id="Token_Ring"></span><span id="token_ring"></span><span id="TOKEN_RING"></span>**Token Ring** (7)
</dt> <dt>

<span id="Frame_Relay"></span><span id="frame_relay"></span><span id="FRAME_RELAY"></span>**Frame Relay** (8)
</dt> <dt>

<span id="Infrared"></span><span id="infrared"></span><span id="INFRARED"></span>**Infrared** (9)
</dt> <dt>

<span id="BlueTooth"></span><span id="bluetooth"></span><span id="BLUETOOTH"></span>**BlueTooth** (10)
</dt> <dt>

<span id="Wireless_LAN"></span><span id="wireless_lan"></span><span id="WIRELESS_LAN"></span>**Wireless LAN** (11)
</dt> <dt>

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (..)
</dt> </dl>

</dd> <dt>

**MaxSpeed**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("bits/sec")
</dt> </dl>

The maximum speed of the target port, in bits per second.

</dd> <dt>

**NetworkAddresses**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of strings that represent the various network addresses for the target port.

The type and format of these addresses are specified in the PortType property.

</dd> <dt>

**NodeAddress**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The node address.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

An array of values that denote the operational status of the target port.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="OK"></span><span id="ok"></span>**OK** (2)
</dt> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (3)
</dt> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>**Stressed** (4)
</dt> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>**Predictive Failure** (5)
</dt> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (6)
</dt> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (7)
</dt> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (8)
</dt> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>**Stopping** (9)
</dt> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (10)
</dt> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (11)
</dt> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (12)
</dt> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (13)
</dt> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted** (14)
</dt> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (15)
</dt> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (16)
</dt> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (17)
</dt> <dt>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>**Power Mode** (18)
</dt> <dt>

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (..)
</dt> </dl>

</dd> <dt>

**OtherConnectionTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representation of the vendor-defined connection type. Relevant only if the **ConnectionType** property is **Other.**

</dd> <dt>

**OtherLinkTechnology**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representation of the vendor-defined link technology. Relevant only if the **LinkTechnology** property is **Other**.

</dd> <dt>

**OtherOperationalStatusDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representation of the vendor-defined status. Relevant only if the **OperationalStatus** array contains **Other.**

</dd> <dt>

**PortAddress**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The port identifier or address.

For Fibre Channel networks, this property should be the World-Wide Name (WWN) for the port, formatted as a hexadecimal string (16 characters long), with the most significant byte first. For example, a WWN address of 01:23:45:67:89:AB:CD:EF should be represented as 0123456789ABCDEF.

For iSCSI networks, this field should be the IQN.

</dd> <dt>

**PortNumbers**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

A list of port numbers for the target port.

</dd> <dt>

**PortType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The specific mode that is currently enabled for the port. If the port is logged in, this will be the negotiated port type. Otherwise, the configured port type will be reported.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="N"></span><span id="n"></span>**N** (10)
</dt> <dt>

<span id="NL"></span><span id="nl"></span>**NL** (11)
</dt> <dt>

<span id="F_NL"></span><span id="f_nl"></span>**F/NL** (12)
</dt> <dt>

<span id="NX"></span><span id="nx"></span>**NX** (13)
</dt> <dt>

<span id="E"></span><span id="e"></span>**E** (14)
</dt> <dt>

<span id="F"></span><span id="f"></span>**F** (15)
</dt> <dt>

<span id="FL"></span><span id="fl"></span>**FL** (16)
</dt> <dt>

<span id="B"></span><span id="b"></span>**B** (17)
</dt> <dt>

<span id="G"></span><span id="g"></span>**G** (18)
</dt> <dt>

<span id="10BaseT"></span><span id="10baset"></span><span id="10BASET"></span>**10BaseT** (50)
</dt> <dt>

<span id="10-100BaseT"></span><span id="10-100baset"></span><span id="10-100BASET"></span>**10-100BaseT** (51)
</dt> <dt>

<span id="100BaseT"></span><span id="100baset"></span><span id="100BASET"></span>**100BaseT** (52)
</dt> <dt>

<span id="1000BaseT"></span><span id="1000baset"></span><span id="1000BASET"></span>**1000BaseT** (53)
</dt> <dt>

<span id="2500BaseT"></span><span id="2500baset"></span><span id="2500BASET"></span>**2500BaseT** (54)
</dt> <dt>

<span id="10GBaseT"></span><span id="10gbaset"></span><span id="10GBASET"></span>**10GBaseT** (55)
</dt> <dt>

<span id="10GBase-CX4"></span><span id="10gbase-cx4"></span><span id="10GBASE-CX4"></span>**10GBase-CX4** (56)
</dt> <dt>

<span id="SAS"></span><span id="sas"></span>**SAS** (94)
</dt> <dt>

<span id="100Base-FX"></span><span id="100base-fx"></span><span id="100BASE-FX"></span>**100Base-FX** (100)
</dt> <dt>

<span id="100Base-SX"></span><span id="100base-sx"></span><span id="100BASE-SX"></span>**100Base-SX** (101)
</dt> <dt>

<span id="1000Base-SX"></span><span id="1000base-sx"></span><span id="1000BASE-SX"></span>**1000Base-SX** (102)
</dt> <dt>

<span id="1000Base-LX"></span><span id="1000base-lx"></span><span id="1000BASE-LX"></span>**1000Base-LX** (103)
</dt> <dt>

<span id="1000Base-CX"></span><span id="1000base-cx"></span><span id="1000BASE-CX"></span>**1000Base-CX** (104)
</dt> <dt>

<span id="10GBase-SR"></span><span id="10gbase-sr"></span><span id="10GBASE-SR"></span>**10GBase-SR** (105)
</dt> <dt>

<span id="10GBase-SW"></span><span id="10gbase-sw"></span><span id="10GBASE-SW"></span>**10GBase-SW** (106)
</dt> <dt>

<span id="10GBase-LX4"></span><span id="10gbase-lx4"></span><span id="10GBASE-LX4"></span>**10GBase-LX4** (107)
</dt> <dt>

<span id="10GBase-LR"></span><span id="10gbase-lr"></span><span id="10GBASE-LR"></span>**10GBase-LR** (108)
</dt> <dt>

<span id="10GBase-LW"></span><span id="10gbase-lw"></span><span id="10GBASE-LW"></span>**10GBase-LW** (109)
</dt> <dt>

<span id="10GBase-ER"></span><span id="10gbase-er"></span><span id="10GBASE-ER"></span>**10GBase-ER** (110)
</dt> <dt>

<span id="10GBase-EW"></span><span id="10gbase-ew"></span><span id="10GBASE-EW"></span>**10GBase-EW** (111)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (112..15999)
</dt> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (16000..65535)
</dt> </dl>

</dd> <dt>

**Role**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The role of this controller port. For iSCSI, this port must act as either a target or an initiator endpoint. Other transports allow a port to act as both an initiator and a target.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Initiator"></span><span id="initiator"></span><span id="INITIATOR"></span>**Initiator** (1)
</dt> <dt>

<span id="Target"></span><span id="target"></span><span id="TARGET"></span>**Target** (2)
</dt> <dt>

<span id="Both_Initiator_and_Target"></span><span id="both_initiator_and_target"></span><span id="BOTH_INITIATOR_AND_TARGET"></span>**Both Initiator and Target** (3)
</dt> </dl>

</dd> <dt>

**Speed**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("bits/sec")
</dt> </dl>

The current speed (bandwidth) of the port, in bits per second. For ports that vary in bandwidth, or for those where no accurate estimation can be made, this property should contain the nominal bandwidth for the port.

</dd> <dt>

**StorageControllerId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The identifier of the controller to which this port belongs.

</dd> <dt>

**UsageRestriction**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The usage restriction of the target port.

In some circumstances, a target port may be identifiable as a front-end or back-end port. For example, a storage array might have back-end ports to communicate with physical disks, and front-end ports to communicate with hosts. If there is no restriction on the use of the port, then the value should be set to **Not restricted**.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Front-end_only"></span><span id="front-end_only"></span><span id="FRONT-END_ONLY"></span>**Front-end only** (2)
</dt> <dt>

<span id="Back-end_only"></span><span id="back-end_only"></span><span id="BACK-END_ONLY"></span>**Back-end only** (3)
</dt> <dt>

<span id="Not_restricted"></span><span id="not_restricted"></span><span id="NOT_RESTRICTED"></span>**Not restricted** (4)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 





