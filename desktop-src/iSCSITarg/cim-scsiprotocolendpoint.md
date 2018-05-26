---
title: CIM\_SCSIProtocolEndpoint class
description: A SCSIProtocolEndpoint represents the protocol (command) aspects of a logical SCSI port, independent of the connection/transport.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b96d8bce-cdd2-4ae0-a88b-163da469de5f
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_SCSIProtocolEndpoint class iSCSI Software Target API
- CIM_SCSIProtocolEndpoint class iSCSI Software Target API , described
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_SCSIProtocolEndpoint class

A SCSIProtocolEndpoint represents the protocol (command) aspects of a logical SCSI port, independent of the connection/transport. SCSIProtocolEndpoint is either directly or indirectly associated to one or more instances of LogicalPort (via PortImplementsEndpoint) depending on the underlying transport. Indirect associations aggregate one or more LogicalPorts using intermediate ProtocolEndpoints (iSCSI, etc). SCSIProtocolEndpoint is also associated to a SCSIProtocolController, representing the SCSI device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.11.0"), UMLPackagePath("CIM::Network::ProtocolEndpoints")]
class CIM_SCSIProtocolEndpoint : CIM_ProtocolEndpoint
{
  string   Caption;
  string   ElementName;
  datetime InstallDate;
  string   StatusDescriptions[];
  string   Status;
  uint16   HealthState;
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  uint16   EnabledDefault = 2;
  string   SystemCreationClassName;
  string   SystemName;
  string   CreationClassName;
  datetime TimeOfLastStateChange;
  uint16   EnabledState;
  uint16   OperationalStatus[];
  string   Description;
  string   NameFormat;
  uint16   ProtocolType;
  uint16   ProtocolIFType;
  string   OtherTypeDescription;
  string   Name;
  uint16   ConnectionType;
  uint16   Role;
  uint32   TargetRelativePortNumber;
  string   OtherConnectionType;
};
```

## Members

The **CIM\_SCSIProtocolEndpoint** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CIM\_SCSIProtocolEndpoint** class has these methods.



| Method                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:--------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RequestStateChange**](cim-scsiprotocolendpoint-requeststatechange.md) | Requests that the state of the element be changed to the value specified in the RequestedState parameter. When the requested state change takes place, the EnabledState and RequestedState of the element will be the same. Invoking the RequestStateChange method multiple times could result in earlier requests being overwritten or lost. If 0 is returned, then the task completed successfully and the use of ConcreteJob was not required. If 4096 (0x1000) is returned, then the task will take some time to complete, ConcreteJob will be created, and its reference returned in the output parameter Job. Any other return code indicates an error condition.<br/> This method is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).<br/> |



 

### Properties

The **CIM\_SCSIProtocolEndpoint** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ConnectionType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("SPC.INCITS-T10 \| Protocol Identifier \| Values"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SCSIProtocolEndpoint.Name", "CIM\_SCSIProtocolEndpoint.OtherConnectionType")
</dt> </dl>

The supported connection type for this endpoint. The connection type may be needed before the port(s) are associated and also is used in some SCSI commands.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Fibre_Channel"></span><span id="fibre_channel"></span><span id="FIBRE_CHANNEL"></span>

**Fibre Channel** (2)


</dt> <dd></dd> <dt>

<span id="Parallel_SCSI"></span><span id="parallel_scsi"></span><span id="PARALLEL_SCSI"></span>

**Parallel SCSI** (3)


</dt> <dd></dd> <dt>

<span id="SSA"></span><span id="ssa"></span>

**SSA** (4)


</dt> <dd></dd> <dt>

<span id="IEEE_1394"></span><span id="ieee_1394"></span>

**IEEE 1394** (5)


</dt> <dd></dd> <dt>

<span id="RDMA"></span><span id="rdma"></span>

**RDMA** (6)


</dt> <dd></dd> <dt>

<span id="iSCSI"></span><span id="iscsi"></span><span id="ISCSI"></span>

**iSCSI** (7)


</dt> <dd></dd> <dt>

<span id="SAS"></span><span id="sas"></span>

**SAS** (8)


</dt> <dd></dd> <dt>

<span id="ADT"></span><span id="adt"></span>

**ADT** (9)


</dt> <dd></dd> </dl>

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|IF-MIB.ifDescr")
</dt> </dl>

TBD

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains a user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An enumerated value indicating an administrator's default or startup configuration for the Enabled State of an element. By default, the element is "Enabled" (value=2).

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (5)


</dt> <dd></dd> <dt>

<span id="Enabled_but_Offline"></span><span id="enabled_but_offline"></span><span id="ENABLED_BUT_OFFLINE"></span>

**Enabled but Offline** (6)


</dt> <dd></dd> <dt>

<span id="No_Default"></span><span id="no_default"></span><span id="NO_DEFAULT"></span>

**No Default** (7)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (9)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>10 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|IF-MIB.ifAdminStatus")
</dt> </dl>

TBD

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current health of the element. This attribute expresses the health of this element but not necessarily that of its sub-components.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

The following values have been defined:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The implementation cannot report on **HealthState** at this time.

</dd> <dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (5)


</dt> <dd>

The element is fully functional and is operating within normal operational parameters and without error.

</dd> <dt>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>**Degraded/Warning** (10)


</dt> <dd>

The element is in working order and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element might not be operating at optimal performance or it might be reporting recoverable errors

</dd> <dt>

<span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span>

<span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span>**Minor failure** (15)


</dt> <dd>

All functionality is available but some might be degraded.

</dd> <dt>

<span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span>

<span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span>**Major failure** (20)


</dt> <dd>

The element is failing. It is possible that some or all of the functionality of this component is degraded or not working.

</dd> <dt>

<span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span>

<span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span>**Critical failure** (25)


</dt> <dd>

The element is non-functional and recovery might not be possible.

</dd> <dt>

<span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

<span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-recoverable error** (30)


</dt> <dd>

The element has completely failed, and recovery is not possible. All functionality provided by this element has been lost.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

DMTF has reserved the unused portion of the continuum for additional HealthStates in the future.

</dd> </dl>

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

Indicates when the object was installed. The lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Name"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("SPC.INCITS-T10 \|Protocol Specific Parameters \| Name"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SCSIProtocolEndpoint.ConnectionType", "CIM\_SCSIProtocolEndpoint.OtherConnectionType")
</dt> </dl>

The SCSI identifier for the target or initiator device, in the format appropriate for the ConnectionType. If a ConnectionType specific subclass is defined, the subclass may override Name to define the format. For other ConnectionTypes, the format (and content) should match that of PermamnentAddress of the corresponding LogicalPort.

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

NameFormat contains the naming heuristic that is selected to ensure that the value of the Name property is unique. For example, you might choose to prepend the name of the port or interface with the Type of ProtocolEndpoint (for example, IPv4) of this instance followed by an underscore.

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|IF-MIB.ifOperStatus")
</dt> </dl>

TBD

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).

</dd> <dt>

**OtherConnectionType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SCSIProtocolEndpoint.Name", "CIM\_SCSIProtocolEndpoint.ConnectionType")
</dt> </dl>

The connection type, if ConnectionType is "Other".

</dd> <dt>

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_EnabledLogicalElement.EnabledState")
</dt> </dl>

A string that describes the enabled or disabled state of the element when the EnabledState property is set to 1 ("Other"). This property must be set to null when EnabledState is any value other than 1.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

</dd> <dt>

**OtherTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ProtocolEndpoint.ProtocolType", "CIM\_ProtocolEndpoint.ProtocolIFType")
</dt> </dl>

A string that describes the type of ProtocolEndpoint when the Type property of this class (or any of its subclasses) is set to 1 (Other). This property should be set to null when the Type property is any value other than 1.

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).

</dd> <dt>

**ProtocolIFType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|IF-MIB.ifType"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ProtocolEndpoint.OtherTypeDescription")
</dt> </dl>

ProtocolIFType is an enumeration that is synchronized with the IANA ifType MIB. The ifType MIB is maintained at the URL, http://www.iana.org/assignments/ianaiftype-mib. Also, additional values defined by the DMTF are included. The property is used to categorize and classify instances of the ProtocolEndpoint class. Note that if the ProtocolIFType is set to 1 (Other), then the type information should be provided in the OtherTypeDescription string property.

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Regular_1822"></span><span id="regular_1822"></span><span id="REGULAR_1822"></span>

**Regular 1822** (2)


</dt> <dd></dd> <dt>

<span id="HDH_1822"></span><span id="hdh_1822"></span>

**HDH 1822** (3)


</dt> <dd></dd> <dt>

<span id="DDN_X.25"></span><span id="ddn_x.25"></span>

**DDN X.25** (4)


</dt> <dd></dd> <dt>

<span id="RFC877_X.25"></span><span id="rfc877_x.25"></span>

**RFC877 X.25** (5)


</dt> <dd></dd> <dt>

<span id="Ethernet_CSMA_CD"></span><span id="ethernet_csma_cd"></span><span id="ETHERNET_CSMA_CD"></span>

**Ethernet CSMA/CD** (6)


</dt> <dd></dd> <dt>

<span id="ISO_802.3_CSMA_CD"></span><span id="iso_802.3_csma_cd"></span>

**ISO 802.3 CSMA/CD** (7)


</dt> <dd></dd> <dt>

<span id="ISO_802.4_Token_Bus"></span><span id="iso_802.4_token_bus"></span><span id="ISO_802.4_TOKEN_BUS"></span>

**ISO 802.4 Token Bus** (8)


</dt> <dd></dd> <dt>

<span id="ISO_802.5_Token_Ring"></span><span id="iso_802.5_token_ring"></span><span id="ISO_802.5_TOKEN_RING"></span>

**ISO 802.5 Token Ring** (9)


</dt> <dd></dd> <dt>

<span id="ISO_802.6_MAN"></span><span id="iso_802.6_man"></span>

**ISO 802.6 MAN** (10)


</dt> <dd></dd> <dt>

<span id="StarLAN"></span><span id="starlan"></span><span id="STARLAN"></span>

**StarLAN** (11)


</dt> <dd></dd> <dt>

<span id="Proteon_10Mbit"></span><span id="proteon_10mbit"></span><span id="PROTEON_10MBIT"></span>

**Proteon 10Mbit** (12)


</dt> <dd></dd> <dt>

<span id="Proteon_80Mbit"></span><span id="proteon_80mbit"></span><span id="PROTEON_80MBIT"></span>

**Proteon 80Mbit** (13)


</dt> <dd></dd> <dt>

<span id="HyperChannel"></span><span id="hyperchannel"></span><span id="HYPERCHANNEL"></span>

**HyperChannel** (14)


</dt> <dd></dd> <dt>

<span id="FDDI"></span><span id="fddi"></span>

**FDDI** (15)


</dt> <dd></dd> <dt>

<span id="LAP-B"></span><span id="lap-b"></span>

**LAP-B** (16)


</dt> <dd></dd> <dt>

<span id="SDLC"></span><span id="sdlc"></span>

**SDLC** (17)


</dt> <dd></dd> <dt>

<span id="DS1"></span><span id="ds1"></span>

**DS1** (18)


</dt> <dd></dd> <dt>

<span id="E1"></span><span id="e1"></span>

**E1** (19)


</dt> <dd></dd> <dt>

<span id="Basic_ISDN"></span><span id="basic_isdn"></span><span id="BASIC_ISDN"></span>

**Basic ISDN** (20)


</dt> <dd></dd> <dt>

<span id="Primary_ISDN"></span><span id="primary_isdn"></span><span id="PRIMARY_ISDN"></span>

**Primary ISDN** (21)


</dt> <dd></dd> <dt>

<span id="Proprietary_Point-to-Point_Serial"></span><span id="proprietary_point-to-point_serial"></span><span id="PROPRIETARY_POINT-TO-POINT_SERIAL"></span>

**Proprietary Point-to-Point Serial** (22)


</dt> <dd></dd> <dt>

<span id="PPP"></span><span id="ppp"></span>

**PPP** (23)


</dt> <dd></dd> <dt>

<span id="Software_Loopback"></span><span id="software_loopback"></span><span id="SOFTWARE_LOOPBACK"></span>

**Software Loopback** (24)


</dt> <dd></dd> <dt>

<span id="EON"></span><span id="eon"></span>

**EON** (25)


</dt> <dd></dd> <dt>

<span id="Ethernet_3Mbit"></span><span id="ethernet_3mbit"></span><span id="ETHERNET_3MBIT"></span>

**Ethernet 3Mbit** (26)


</dt> <dd></dd> <dt>

<span id="NSIP"></span><span id="nsip"></span>

**NSIP** (27)


</dt> <dd></dd> <dt>

<span id="SLIP"></span><span id="slip"></span>

**SLIP** (28)


</dt> <dd></dd> <dt>

<span id="Ultra"></span><span id="ultra"></span><span id="ULTRA"></span>

**Ultra** (29)


</dt> <dd></dd> <dt>

<span id="DS3"></span><span id="ds3"></span>

**DS3** (30)


</dt> <dd></dd> <dt>

<span id="SIP"></span><span id="sip"></span>

**SIP** (31)


</dt> <dd></dd> <dt>

<span id="Frame_Relay"></span><span id="frame_relay"></span><span id="FRAME_RELAY"></span>

**Frame Relay** (32)


</dt> <dd></dd> <dt>

<span id="RS-232"></span><span id="rs-232"></span>

**RS-232** (33)


</dt> <dd></dd> <dt>

<span id="Parallel"></span><span id="parallel"></span><span id="PARALLEL"></span>

**Parallel** (34)


</dt> <dd></dd> <dt>

<span id="ARCNet"></span><span id="arcnet"></span><span id="ARCNET"></span>

**ARCNet** (35)


</dt> <dd></dd> <dt>

<span id="ARCNet_Plus"></span><span id="arcnet_plus"></span><span id="ARCNET_PLUS"></span>

**ARCNet Plus** (36)


</dt> <dd></dd> <dt>

<span id="ATM"></span><span id="atm"></span>

**ATM** (37)


</dt> <dd></dd> <dt>

<span id="MIO_X.25"></span><span id="mio_x.25"></span>

**MIO X.25** (38)


</dt> <dd></dd> <dt>

<span id="SONET"></span><span id="sonet"></span>

**SONET** (39)


</dt> <dd></dd> <dt>

<span id="X.25_PLE"></span><span id="x.25_ple"></span>

**X.25 PLE** (40)


</dt> <dd></dd> <dt>

<span id="ISO_802.211c"></span><span id="iso_802.211c"></span><span id="ISO_802.211C"></span>

**ISO 802.211c** (41)


</dt> <dd></dd> <dt>

<span id="LocalTalk"></span><span id="localtalk"></span><span id="LOCALTALK"></span>

**LocalTalk** (42)


</dt> <dd></dd> <dt>

<span id="SMDS_DXI"></span><span id="smds_dxi"></span>

**SMDS DXI** (43)


</dt> <dd></dd> <dt>

<span id="Frame_Relay_Service"></span><span id="frame_relay_service"></span><span id="FRAME_RELAY_SERVICE"></span>

**Frame Relay Service** (44)


</dt> <dd></dd> <dt>

<span id="V.35"></span><span id="v.35"></span>

**V.35** (45)


</dt> <dd></dd> <dt>

<span id="HSSI"></span><span id="hssi"></span>

**HSSI** (46)


</dt> <dd></dd> <dt>

<span id="HIPPI"></span><span id="hippi"></span>

**HIPPI** (47)


</dt> <dd></dd> <dt>

<span id="Modem"></span><span id="modem"></span><span id="MODEM"></span>

**Modem** (48)


</dt> <dd></dd> <dt>

<span id="AAL5"></span><span id="aal5"></span>

**AAL5** (49)


</dt> <dd></dd> <dt>

<span id="SONET_Path"></span><span id="sonet_path"></span><span id="SONET_PATH"></span>

**SONET Path** (50)


</dt> <dd></dd> <dt>

<span id="SONET_VT"></span><span id="sonet_vt"></span>

**SONET VT** (51)


</dt> <dd></dd> <dt>

<span id="SMDS_ICIP"></span><span id="smds_icip"></span>

**SMDS ICIP** (52)


</dt> <dd></dd> <dt>

<span id="Proprietary_Virtual_Internal"></span><span id="proprietary_virtual_internal"></span><span id="PROPRIETARY_VIRTUAL_INTERNAL"></span>

**Proprietary Virtual/Internal** (53)


</dt> <dd></dd> <dt>

<span id="Proprietary_Multiplexor"></span><span id="proprietary_multiplexor"></span><span id="PROPRIETARY_MULTIPLEXOR"></span>

**Proprietary Multiplexor** (54)


</dt> <dd></dd> <dt>

<span id="IEEE_802.12"></span><span id="ieee_802.12"></span>

**IEEE 802.12** (55)


</dt> <dd></dd> <dt>

<span id="Fibre_Channel"></span><span id="fibre_channel"></span><span id="FIBRE_CHANNEL"></span>

**Fibre Channel** (56)


</dt> <dd></dd> <dt>

<span id="HIPPI_Interface"></span><span id="hippi_interface"></span><span id="HIPPI_INTERFACE"></span>

**HIPPI Interface** (57)


</dt> <dd></dd> <dt>

<span id="Frame_Relay_Interconnect"></span><span id="frame_relay_interconnect"></span><span id="FRAME_RELAY_INTERCONNECT"></span>

**Frame Relay Interconnect** (58)


</dt> <dd></dd> <dt>

<span id="ATM_Emulated_LAN_for_802.3"></span><span id="atm_emulated_lan_for_802.3"></span><span id="ATM_EMULATED_LAN_FOR_802.3"></span>

**ATM Emulated LAN for 802.3** (59)


</dt> <dd></dd> <dt>

<span id="ATM_Emulated_LAN_for_802.5"></span><span id="atm_emulated_lan_for_802.5"></span><span id="ATM_EMULATED_LAN_FOR_802.5"></span>

**ATM Emulated LAN for 802.5** (60)


</dt> <dd></dd> <dt>

<span id="ATM_Emulated_Circuit"></span><span id="atm_emulated_circuit"></span><span id="ATM_EMULATED_CIRCUIT"></span>

**ATM Emulated Circuit** (61)


</dt> <dd></dd> <dt>

<span id="Fast_Ethernet__100BaseT_"></span><span id="fast_ethernet__100baset_"></span><span id="FAST_ETHERNET__100BASET_"></span>

**Fast Ethernet (100BaseT)** (62)


</dt> <dd></dd> <dt>

<span id="ISDN"></span><span id="isdn"></span>

**ISDN** (63)


</dt> <dd></dd> <dt>

<span id="V.11"></span><span id="v.11"></span>

**V.11** (64)


</dt> <dd></dd> <dt>

<span id="V.36"></span><span id="v.36"></span>

**V.36** (65)


</dt> <dd></dd> <dt>

<span id="G703_at_64K"></span><span id="g703_at_64k"></span><span id="G703_AT_64K"></span>

**G703 at 64K** (66)


</dt> <dd></dd> <dt>

<span id="G703_at_2Mb"></span><span id="g703_at_2mb"></span><span id="G703_AT_2MB"></span>

**G703 at 2Mb** (67)


</dt> <dd></dd> <dt>

<span id="QLLC"></span><span id="qllc"></span>

**QLLC** (68)


</dt> <dd></dd> <dt>

<span id="Fast_Ethernet_100BaseFX"></span><span id="fast_ethernet_100basefx"></span><span id="FAST_ETHERNET_100BASEFX"></span>

**Fast Ethernet 100BaseFX** (69)


</dt> <dd></dd> <dt>

<span id="Channel"></span><span id="channel"></span><span id="CHANNEL"></span>

**Channel** (70)


</dt> <dd></dd> <dt>

<span id="IEEE_802.11"></span><span id="ieee_802.11"></span>

**IEEE 802.11** (71)


</dt> <dd></dd> <dt>

<span id="IBM_260_370_OEMI_Channel"></span><span id="ibm_260_370_oemi_channel"></span><span id="IBM_260_370_OEMI_CHANNEL"></span>

**IBM 260/370 OEMI Channel** (72)


</dt> <dd></dd> <dt>

<span id="ESCON"></span><span id="escon"></span>

**ESCON** (73)


</dt> <dd></dd> <dt>

<span id="Data_Link_Switching"></span><span id="data_link_switching"></span><span id="DATA_LINK_SWITCHING"></span>

**Data Link Switching** (74)


</dt> <dd></dd> <dt>

<span id="ISDN_S_T_Interface"></span><span id="isdn_s_t_interface"></span><span id="ISDN_S_T_INTERFACE"></span>

**ISDN S/T Interface** (75)


</dt> <dd></dd> <dt>

<span id="ISDN_U_Interface"></span><span id="isdn_u_interface"></span><span id="ISDN_U_INTERFACE"></span>

**ISDN U Interface** (76)


</dt> <dd></dd> <dt>

<span id="LAP-D"></span><span id="lap-d"></span>

**LAP-D** (77)


</dt> <dd></dd> <dt>

<span id="IP_Switch"></span><span id="ip_switch"></span><span id="IP_SWITCH"></span>

**IP Switch** (78)


</dt> <dd></dd> <dt>

<span id="Remote_Source_Route_Bridging"></span><span id="remote_source_route_bridging"></span><span id="REMOTE_SOURCE_ROUTE_BRIDGING"></span>

**Remote Source Route Bridging** (79)


</dt> <dd></dd> <dt>

<span id="ATM_Logical"></span><span id="atm_logical"></span><span id="ATM_LOGICAL"></span>

**ATM Logical** (80)


</dt> <dd></dd> <dt>

<span id="DS0"></span><span id="ds0"></span>

**DS0** (81)


</dt> <dd></dd> <dt>

<span id="DS0_Bundle"></span><span id="ds0_bundle"></span><span id="DS0_BUNDLE"></span>

**DS0 Bundle** (82)


</dt> <dd></dd> <dt>

<span id="BSC"></span><span id="bsc"></span>

**BSC** (83)


</dt> <dd></dd> <dt>

<span id="Async"></span><span id="async"></span><span id="ASYNC"></span>

**Async** (84)


</dt> <dd></dd> <dt>

<span id="Combat_Net_Radio"></span><span id="combat_net_radio"></span><span id="COMBAT_NET_RADIO"></span>

**Combat Net Radio** (85)


</dt> <dd></dd> <dt>

<span id="ISO_802.5r_DTR"></span><span id="iso_802.5r_dtr"></span><span id="ISO_802.5R_DTR"></span>

**ISO 802.5r DTR** (86)


</dt> <dd></dd> <dt>

<span id="Ext_Pos_Loc_Report_System"></span><span id="ext_pos_loc_report_system"></span><span id="EXT_POS_LOC_REPORT_SYSTEM"></span>

**Ext Pos Loc Report System** (87)


</dt> <dd></dd> <dt>

<span id="AppleTalk_Remote_Access_Protocol"></span><span id="appletalk_remote_access_protocol"></span><span id="APPLETALK_REMOTE_ACCESS_PROTOCOL"></span>

**AppleTalk Remote Access Protocol** (88)


</dt> <dd></dd> <dt>

<span id="Proprietary_Connectionless"></span><span id="proprietary_connectionless"></span><span id="PROPRIETARY_CONNECTIONLESS"></span>

**Proprietary Connectionless** (89)


</dt> <dd></dd> <dt>

<span id="ITU_X.29_Host_PAD"></span><span id="itu_x.29_host_pad"></span><span id="ITU_X.29_HOST_PAD"></span>

**ITU X.29 Host PAD** (90)


</dt> <dd></dd> <dt>

<span id="ITU_X.3_Terminal_PAD"></span><span id="itu_x.3_terminal_pad"></span><span id="ITU_X.3_TERMINAL_PAD"></span>

**ITU X.3 Terminal PAD** (91)


</dt> <dd></dd> <dt>

<span id="Frame_Relay_MPI"></span><span id="frame_relay_mpi"></span><span id="FRAME_RELAY_MPI"></span>

**Frame Relay MPI** (92)


</dt> <dd></dd> <dt>

<span id="ITU_X.213"></span><span id="itu_x.213"></span>

**ITU X.213** (93)


</dt> <dd></dd> <dt>

<span id="ADSL"></span><span id="adsl"></span>

**ADSL** (94)


</dt> <dd></dd> <dt>

<span id="RADSL"></span><span id="radsl"></span>

**RADSL** (95)


</dt> <dd></dd> <dt>

<span id="SDSL"></span><span id="sdsl"></span>

**SDSL** (96)


</dt> <dd></dd> <dt>

<span id="VDSL"></span><span id="vdsl"></span>

**VDSL** (97)


</dt> <dd></dd> <dt>

<span id="ISO_802.5_CRFP"></span><span id="iso_802.5_crfp"></span>

**ISO 802.5 CRFP** (98)


</dt> <dd></dd> <dt>

<span id="Myrinet"></span><span id="myrinet"></span><span id="MYRINET"></span>

**Myrinet** (99)


</dt> <dd></dd> <dt>

<span id="Voice_Receive_and_Transmit"></span><span id="voice_receive_and_transmit"></span><span id="VOICE_RECEIVE_AND_TRANSMIT"></span>

**Voice Receive and Transmit** (100)


</dt> <dd></dd> <dt>

<span id="Voice_Foreign_Exchange_Office"></span><span id="voice_foreign_exchange_office"></span><span id="VOICE_FOREIGN_EXCHANGE_OFFICE"></span>

**Voice Foreign Exchange Office** (101)


</dt> <dd></dd> <dt>

<span id="Voice_Foreign_Exchange_Service"></span><span id="voice_foreign_exchange_service"></span><span id="VOICE_FOREIGN_EXCHANGE_SERVICE"></span>

**Voice Foreign Exchange Service** (102)


</dt> <dd></dd> <dt>

<span id="Voice_Encapsulation"></span><span id="voice_encapsulation"></span><span id="VOICE_ENCAPSULATION"></span>

**Voice Encapsulation** (103)


</dt> <dd></dd> <dt>

<span id="Voice_over_IP"></span><span id="voice_over_ip"></span><span id="VOICE_OVER_IP"></span>

**Voice over IP** (104)


</dt> <dd></dd> <dt>

<span id="ATM_DXI"></span><span id="atm_dxi"></span>

**ATM DXI** (105)


</dt> <dd></dd> <dt>

<span id="ATM_FUNI"></span><span id="atm_funi"></span>

**ATM FUNI** (106)


</dt> <dd></dd> <dt>

<span id="ATM_IMA"></span><span id="atm_ima"></span>

**ATM IMA** (107)


</dt> <dd></dd> <dt>

<span id="PPP_Multilink_Bundle"></span><span id="ppp_multilink_bundle"></span><span id="PPP_MULTILINK_BUNDLE"></span>

**PPP Multilink Bundle** (108)


</dt> <dd></dd> <dt>

<span id="IP_over_CDLC"></span><span id="ip_over_cdlc"></span><span id="IP_OVER_CDLC"></span>

**IP over CDLC** (109)


</dt> <dd></dd> <dt>

<span id="IP_over_CLAW"></span><span id="ip_over_claw"></span><span id="IP_OVER_CLAW"></span>

**IP over CLAW** (110)


</dt> <dd></dd> <dt>

<span id="Stack_to_Stack"></span><span id="stack_to_stack"></span><span id="STACK_TO_STACK"></span>

**Stack to Stack** (111)


</dt> <dd></dd> <dt>

<span id="Virtual_IP_Address"></span><span id="virtual_ip_address"></span><span id="VIRTUAL_IP_ADDRESS"></span>

**Virtual IP Address** (112)


</dt> <dd></dd> <dt>

<span id="MPC"></span><span id="mpc"></span>

**MPC** (113)


</dt> <dd></dd> <dt>

<span id="IP_over_ATM"></span><span id="ip_over_atm"></span><span id="IP_OVER_ATM"></span>

**IP over ATM** (114)


</dt> <dd></dd> <dt>

<span id="ISO_802.5j_Fibre_Token_Ring"></span><span id="iso_802.5j_fibre_token_ring"></span><span id="ISO_802.5J_FIBRE_TOKEN_RING"></span>

**ISO 802.5j Fibre Token Ring** (115)


</dt> <dd></dd> <dt>

<span id="TDLC"></span><span id="tdlc"></span>

**TDLC** (116)


</dt> <dd></dd> <dt>

<span id="Gigabit_Ethernet"></span><span id="gigabit_ethernet"></span><span id="GIGABIT_ETHERNET"></span>

**Gigabit Ethernet** (117)


</dt> <dd></dd> <dt>

<span id="HDLC"></span><span id="hdlc"></span>

**HDLC** (118)


</dt> <dd></dd> <dt>

<span id="LAP-F"></span><span id="lap-f"></span>

**LAP-F** (119)


</dt> <dd></dd> <dt>

<span id="V.37"></span><span id="v.37"></span>

**V.37** (120)


</dt> <dd></dd> <dt>

<span id="X.25_MLP"></span><span id="x.25_mlp"></span>

**X.25 MLP** (121)


</dt> <dd></dd> <dt>

<span id="X.25_Hunt_Group"></span><span id="x.25_hunt_group"></span><span id="X.25_HUNT_GROUP"></span>

**X.25 Hunt Group** (122)


</dt> <dd></dd> <dt>

<span id="Transp_HDLC"></span><span id="transp_hdlc"></span><span id="TRANSP_HDLC"></span>

**Transp HDLC** (123)


</dt> <dd></dd> <dt>

<span id="Interleave_Channel"></span><span id="interleave_channel"></span><span id="INTERLEAVE_CHANNEL"></span>

**Interleave Channel** (124)


</dt> <dd></dd> <dt>

<span id="FAST_Channel"></span><span id="fast_channel"></span><span id="FAST_CHANNEL"></span>

**FAST Channel** (125)


</dt> <dd></dd> <dt>

<span id="IP__for_APPN_HPR_in_IP_Networks_"></span><span id="ip__for_appn_hpr_in_ip_networks_"></span><span id="IP__FOR_APPN_HPR_IN_IP_NETWORKS_"></span>

**IP (for APPN HPR in IP Networks)** (126)


</dt> <dd></dd> <dt>

<span id="CATV_MAC_Layer"></span><span id="catv_mac_layer"></span><span id="CATV_MAC_LAYER"></span>

**CATV MAC Layer** (127)


</dt> <dd></dd> <dt>

<span id="CATV_Downstream"></span><span id="catv_downstream"></span><span id="CATV_DOWNSTREAM"></span>

**CATV Downstream** (128)


</dt> <dd></dd> <dt>

<span id="CATV_Upstream"></span><span id="catv_upstream"></span><span id="CATV_UPSTREAM"></span>

**CATV Upstream** (129)


</dt> <dd></dd> <dt>

<span id="Avalon_12MPP_Switch"></span><span id="avalon_12mpp_switch"></span><span id="AVALON_12MPP_SWITCH"></span>

**Avalon 12MPP Switch** (130)


</dt> <dd></dd> <dt>

<span id="Tunnel"></span><span id="tunnel"></span><span id="TUNNEL"></span>

**Tunnel** (131)


</dt> <dd></dd> <dt>

<span id="Coffee"></span><span id="coffee"></span><span id="COFFEE"></span>

**Coffee** (132)


</dt> <dd></dd> <dt>

<span id="Circuit_Emulation_Service"></span><span id="circuit_emulation_service"></span><span id="CIRCUIT_EMULATION_SERVICE"></span>

**Circuit Emulation Service** (133)


</dt> <dd></dd> <dt>

<span id="ATM_SubInterface"></span><span id="atm_subinterface"></span><span id="ATM_SUBINTERFACE"></span>

**ATM SubInterface** (134)


</dt> <dd></dd> <dt>

<span id="Layer_2_VLAN_using_802.1Q"></span><span id="layer_2_vlan_using_802.1q"></span><span id="LAYER_2_VLAN_USING_802.1Q"></span>

**Layer 2 VLAN using 802.1Q** (135)


</dt> <dd></dd> <dt>

<span id="Layer_3_VLAN_using_IP"></span><span id="layer_3_vlan_using_ip"></span><span id="LAYER_3_VLAN_USING_IP"></span>

**Layer 3 VLAN using IP** (136)


</dt> <dd></dd> <dt>

<span id="Layer_3_VLAN_using_IPX"></span><span id="layer_3_vlan_using_ipx"></span><span id="LAYER_3_VLAN_USING_IPX"></span>

**Layer 3 VLAN using IPX** (137)


</dt> <dd></dd> <dt>

<span id="Digital_Power_Line"></span><span id="digital_power_line"></span><span id="DIGITAL_POWER_LINE"></span>

**Digital Power Line** (138)


</dt> <dd></dd> <dt>

<span id="Multimedia_Mail_over_IP"></span><span id="multimedia_mail_over_ip"></span><span id="MULTIMEDIA_MAIL_OVER_IP"></span>

**Multimedia Mail over IP** (139)


</dt> <dd></dd> <dt>

<span id="DTM"></span><span id="dtm"></span>

**DTM** (140)


</dt> <dd></dd> <dt>

<span id="DCN"></span><span id="dcn"></span>

**DCN** (141)


</dt> <dd></dd> <dt>

<span id="IP_Forwarding"></span><span id="ip_forwarding"></span><span id="IP_FORWARDING"></span>

**IP Forwarding** (142)


</dt> <dd></dd> <dt>

<span id="MSDSL"></span><span id="msdsl"></span>

**MSDSL** (143)


</dt> <dd></dd> <dt>

<span id="IEEE_1394"></span><span id="ieee_1394"></span>

**IEEE 1394** (144)


</dt> <dd></dd> <dt>

<span id="IF-GSN_HIPPI-6400"></span><span id="if-gsn_hippi-6400"></span>

**IF-GSN/HIPPI-6400** (145)


</dt> <dd></dd> <dt>

<span id="DVB-RCC_MAC_Layer"></span><span id="dvb-rcc_mac_layer"></span><span id="DVB-RCC_MAC_LAYER"></span>

**DVB-RCC MAC Layer** (146)


</dt> <dd></dd> <dt>

<span id="DVB-RCC_Downstream"></span><span id="dvb-rcc_downstream"></span><span id="DVB-RCC_DOWNSTREAM"></span>

**DVB-RCC Downstream** (147)


</dt> <dd></dd> <dt>

<span id="DVB-RCC_Upstream"></span><span id="dvb-rcc_upstream"></span><span id="DVB-RCC_UPSTREAM"></span>

**DVB-RCC Upstream** (148)


</dt> <dd></dd> <dt>

<span id="ATM_Virtual"></span><span id="atm_virtual"></span><span id="ATM_VIRTUAL"></span>

**ATM Virtual** (149)


</dt> <dd></dd> <dt>

<span id="MPLS_Tunnel"></span><span id="mpls_tunnel"></span><span id="MPLS_TUNNEL"></span>

**MPLS Tunnel** (150)


</dt> <dd></dd> <dt>

<span id="SRP"></span><span id="srp"></span>

**SRP** (151)


</dt> <dd></dd> <dt>

<span id="Voice_over_ATM"></span><span id="voice_over_atm"></span><span id="VOICE_OVER_ATM"></span>

**Voice over ATM** (152)


</dt> <dd></dd> <dt>

<span id="Voice_over_Frame_Relay"></span><span id="voice_over_frame_relay"></span><span id="VOICE_OVER_FRAME_RELAY"></span>

**Voice over Frame Relay** (153)


</dt> <dd></dd> <dt>

<span id="ISDL"></span><span id="isdl"></span>

**ISDL** (154)


</dt> <dd></dd> <dt>

<span id="Composite_Link"></span><span id="composite_link"></span><span id="COMPOSITE_LINK"></span>

**Composite Link** (155)


</dt> <dd></dd> <dt>

<span id="SS7_Signaling_Link"></span><span id="ss7_signaling_link"></span><span id="SS7_SIGNALING_LINK"></span>

**SS7 Signaling Link** (156)


</dt> <dd></dd> <dt>

<span id="Proprietary_P2P_Wireless"></span><span id="proprietary_p2p_wireless"></span><span id="PROPRIETARY_P2P_WIRELESS"></span>

**Proprietary P2P Wireless** (157)


</dt> <dd></dd> <dt>

<span id="Frame_Forward"></span><span id="frame_forward"></span><span id="FRAME_FORWARD"></span>

**Frame Forward** (158)


</dt> <dd></dd> <dt>

<span id="RFC1483_Multiprotocol_over_ATM"></span><span id="rfc1483_multiprotocol_over_atm"></span><span id="RFC1483_MULTIPROTOCOL_OVER_ATM"></span>

**RFC1483 Multiprotocol over ATM** (159)


</dt> <dd></dd> <dt>

<span id="USB"></span><span id="usb"></span>

**USB** (160)


</dt> <dd></dd> <dt>

<span id="IEEE_802.3ad_Link_Aggregate"></span><span id="ieee_802.3ad_link_aggregate"></span><span id="IEEE_802.3AD_LINK_AGGREGATE"></span>

**IEEE 802.3ad Link Aggregate** (161)


</dt> <dd></dd> <dt>

<span id="BGP_Policy_Accounting"></span><span id="bgp_policy_accounting"></span><span id="BGP_POLICY_ACCOUNTING"></span>

**BGP Policy Accounting** (162)


</dt> <dd></dd> <dt>

<span id="FRF_.16_Multilink_FR"></span><span id="frf_.16_multilink_fr"></span><span id="FRF_.16_MULTILINK_FR"></span>

**FRF .16 Multilink FR** (163)


</dt> <dd></dd> <dt>

<span id="H.323_Gatekeeper"></span><span id="h.323_gatekeeper"></span><span id="H.323_GATEKEEPER"></span>

**H.323 Gatekeeper** (164)


</dt> <dd></dd> <dt>

<span id="H.323_Proxy"></span><span id="h.323_proxy"></span><span id="H.323_PROXY"></span>

**H.323 Proxy** (165)


</dt> <dd></dd> <dt>

<span id="MPLS"></span><span id="mpls"></span>

**MPLS** (166)


</dt> <dd></dd> <dt>

<span id="Multi-Frequency_Signaling_Link"></span><span id="multi-frequency_signaling_link"></span><span id="MULTI-FREQUENCY_SIGNALING_LINK"></span>

**Multi-Frequency Signaling Link** (167)


</dt> <dd></dd> <dt>

<span id="HDSL-2"></span><span id="hdsl-2"></span>

**HDSL-2** (168)


</dt> <dd></dd> <dt>

<span id="S-HDSL"></span><span id="s-hdsl"></span>

**S-HDSL** (169)


</dt> <dd></dd> <dt>

<span id="DS1_Facility_Data_Link"></span><span id="ds1_facility_data_link"></span><span id="DS1_FACILITY_DATA_LINK"></span>

**DS1 Facility Data Link** (170)


</dt> <dd></dd> <dt>

<span id="Packet_over_SONET_SDH"></span><span id="packet_over_sonet_sdh"></span><span id="PACKET_OVER_SONET_SDH"></span>

**Packet over SONET/SDH** (171)


</dt> <dd></dd> <dt>

<span id="DVB-ASI_Input"></span><span id="dvb-asi_input"></span><span id="DVB-ASI_INPUT"></span>

**DVB-ASI Input** (172)


</dt> <dd></dd> <dt>

<span id="DVB-ASI_Output"></span><span id="dvb-asi_output"></span><span id="DVB-ASI_OUTPUT"></span>

**DVB-ASI Output** (173)


</dt> <dd></dd> <dt>

<span id="Power_Line"></span><span id="power_line"></span><span id="POWER_LINE"></span>

**Power Line** (174)


</dt> <dd></dd> <dt>

<span id="Non_Facility_Associated_Signaling"></span><span id="non_facility_associated_signaling"></span><span id="NON_FACILITY_ASSOCIATED_SIGNALING"></span>

**Non Facility Associated Signaling** (175)


</dt> <dd></dd> <dt>

<span id="TR008"></span><span id="tr008"></span>

**TR008** (176)


</dt> <dd></dd> <dt>

<span id="GR303_RDT"></span><span id="gr303_rdt"></span>

**GR303 RDT** (177)


</dt> <dd></dd> <dt>

<span id="GR303_IDT"></span><span id="gr303_idt"></span>

**GR303 IDT** (178)


</dt> <dd></dd> <dt>

<span id="ISUP"></span><span id="isup"></span>

**ISUP** (179)


</dt> <dd></dd> <dt>

<span id="Proprietary_Wireless_MAC_Layer"></span><span id="proprietary_wireless_mac_layer"></span><span id="PROPRIETARY_WIRELESS_MAC_LAYER"></span>

**Proprietary Wireless MAC Layer** (180)


</dt> <dd></dd> <dt>

<span id="Proprietary_Wireless_Downstream"></span><span id="proprietary_wireless_downstream"></span><span id="PROPRIETARY_WIRELESS_DOWNSTREAM"></span>

**Proprietary Wireless Downstream** (181)


</dt> <dd></dd> <dt>

<span id="Proprietary_Wireless_Upstream"></span><span id="proprietary_wireless_upstream"></span><span id="PROPRIETARY_WIRELESS_UPSTREAM"></span>

**Proprietary Wireless Upstream** (182)


</dt> <dd></dd> <dt>

<span id="HIPERLAN_Type_2"></span><span id="hiperlan_type_2"></span><span id="HIPERLAN_TYPE_2"></span>

**HIPERLAN Type 2** (183)


</dt> <dd></dd> <dt>

<span id="Proprietary_Broadband_Wireless_Access_Point_to_Mulipoint"></span><span id="proprietary_broadband_wireless_access_point_to_mulipoint"></span><span id="PROPRIETARY_BROADBAND_WIRELESS_ACCESS_POINT_TO_MULIPOINT"></span>

**Proprietary Broadband Wireless Access Point to Mulipoint** (184)


</dt> <dd></dd> <dt>

<span id="SONET_Overhead_Channel"></span><span id="sonet_overhead_channel"></span><span id="SONET_OVERHEAD_CHANNEL"></span>

**SONET Overhead Channel** (185)


</dt> <dd></dd> <dt>

<span id="Digital_Wrapper_Overhead_Channel"></span><span id="digital_wrapper_overhead_channel"></span><span id="DIGITAL_WRAPPER_OVERHEAD_CHANNEL"></span>

**Digital Wrapper Overhead Channel** (186)


</dt> <dd></dd> <dt>

<span id="ATM_Adaptation_Layer_2"></span><span id="atm_adaptation_layer_2"></span><span id="ATM_ADAPTATION_LAYER_2"></span>

**ATM Adaptation Layer 2** (187)


</dt> <dd></dd> <dt>

<span id="Radio_MAC"></span><span id="radio_mac"></span><span id="RADIO_MAC"></span>

**Radio MAC** (188)


</dt> <dd></dd> <dt>

<span id="ATM_Radio"></span><span id="atm_radio"></span><span id="ATM_RADIO"></span>

**ATM Radio** (189)


</dt> <dd></dd> <dt>

<span id="Inter_Machine_Trunk"></span><span id="inter_machine_trunk"></span><span id="INTER_MACHINE_TRUNK"></span>

**Inter Machine Trunk** (190)


</dt> <dd></dd> <dt>

<span id="MVL_DSL"></span><span id="mvl_dsl"></span>

**MVL DSL** (191)


</dt> <dd></dd> <dt>

<span id="Long_Read_DSL"></span><span id="long_read_dsl"></span><span id="LONG_READ_DSL"></span>

**Long Read DSL** (192)


</dt> <dd></dd> <dt>

<span id="Frame_Relay_DLCI_Endpoint"></span><span id="frame_relay_dlci_endpoint"></span><span id="FRAME_RELAY_DLCI_ENDPOINT"></span>

**Frame Relay DLCI Endpoint** (193)


</dt> <dd></dd> <dt>

<span id="ATM_VCI_Endpoint"></span><span id="atm_vci_endpoint"></span><span id="ATM_VCI_ENDPOINT"></span>

**ATM VCI Endpoint** (194)


</dt> <dd></dd> <dt>

<span id="Optical_Channel"></span><span id="optical_channel"></span><span id="OPTICAL_CHANNEL"></span>

**Optical Channel** (195)


</dt> <dd></dd> <dt>

<span id="Optical_Transport"></span><span id="optical_transport"></span><span id="OPTICAL_TRANSPORT"></span>

**Optical Transport** (196)


</dt> <dd></dd> <dt>

<span id="Proprietary_ATM"></span><span id="proprietary_atm"></span><span id="PROPRIETARY_ATM"></span>

**Proprietary ATM** (197)


</dt> <dd></dd> <dt>

<span id="Voice_over_Cable"></span><span id="voice_over_cable"></span><span id="VOICE_OVER_CABLE"></span>

**Voice over Cable** (198)


</dt> <dd></dd> <dt>

<span id="Infiniband"></span><span id="infiniband"></span><span id="INFINIBAND"></span>

**Infiniband** (199)


</dt> <dd></dd> <dt>

<span id="TE_Link"></span><span id="te_link"></span><span id="TE_LINK"></span>

**TE Link** (200)


</dt> <dd></dd> <dt>

<span id="Q.2931"></span><span id="q.2931"></span>

**Q.2931** (201)


</dt> <dd></dd> <dt>

<span id="Virtual_Trunk_Group"></span><span id="virtual_trunk_group"></span><span id="VIRTUAL_TRUNK_GROUP"></span>

**Virtual Trunk Group** (202)


</dt> <dd></dd> <dt>

<span id="SIP_Trunk_Group"></span><span id="sip_trunk_group"></span><span id="SIP_TRUNK_GROUP"></span>

**SIP Trunk Group** (203)


</dt> <dd></dd> <dt>

<span id="SIP_Signaling"></span><span id="sip_signaling"></span><span id="SIP_SIGNALING"></span>

**SIP Signaling** (204)


</dt> <dd></dd> <dt>

<span id="CATV_Upstream_Channel"></span><span id="catv_upstream_channel"></span><span id="CATV_UPSTREAM_CHANNEL"></span>

**CATV Upstream Channel** (205)


</dt> <dd></dd> <dt>

<span id="Econet"></span><span id="econet"></span><span id="ECONET"></span>

**Econet** (206)


</dt> <dd></dd> <dt>

<span id="FSAN_155Mb_PON"></span><span id="fsan_155mb_pon"></span><span id="FSAN_155MB_PON"></span>

**FSAN 155Mb PON** (207)


</dt> <dd></dd> <dt>

<span id="FSAN_622Mb_PON"></span><span id="fsan_622mb_pon"></span><span id="FSAN_622MB_PON"></span>

**FSAN 622Mb PON** (208)


</dt> <dd></dd> <dt>

<span id="Transparent_Bridge"></span><span id="transparent_bridge"></span><span id="TRANSPARENT_BRIDGE"></span>

**Transparent Bridge** (209)


</dt> <dd></dd> <dt>

<span id="Line_Group"></span><span id="line_group"></span><span id="LINE_GROUP"></span>

**Line Group** (210)


</dt> <dd></dd> <dt>

<span id="Voice_E_M_Feature_Group"></span><span id="voice_e_m_feature_group"></span><span id="VOICE_E_M_FEATURE_GROUP"></span>

**Voice E&M Feature Group** (211)


</dt> <dd></dd> <dt>

<span id="Voice_FGD_EANA"></span><span id="voice_fgd_eana"></span><span id="VOICE_FGD_EANA"></span>

**Voice FGD EANA** (212)


</dt> <dd></dd> <dt>

<span id="Voice_DID"></span><span id="voice_did"></span><span id="VOICE_DID"></span>

**Voice DID** (213)


</dt> <dd></dd> <dt>

<span id="MPEG_Transport"></span><span id="mpeg_transport"></span><span id="MPEG_TRANSPORT"></span>

**MPEG Transport** (214)


</dt> <dd></dd> <dt>

<span id="6To4"></span><span id="6to4"></span><span id="6TO4"></span>

**6To4** (215)


</dt> <dd></dd> <dt>

<span id="GTP"></span><span id="gtp"></span>

**GTP** (216)


</dt> <dd></dd> <dt>

<span id="Paradyne_EtherLoop_1"></span><span id="paradyne_etherloop_1"></span><span id="PARADYNE_ETHERLOOP_1"></span>

**Paradyne EtherLoop 1** (217)


</dt> <dd></dd> <dt>

<span id="Paradyne_EtherLoop_2"></span><span id="paradyne_etherloop_2"></span><span id="PARADYNE_ETHERLOOP_2"></span>

**Paradyne EtherLoop 2** (218)


</dt> <dd></dd> <dt>

<span id="Optical_Channel_Group"></span><span id="optical_channel_group"></span><span id="OPTICAL_CHANNEL_GROUP"></span>

**Optical Channel Group** (219)


</dt> <dd></dd> <dt>

<span id="HomePNA"></span><span id="homepna"></span><span id="HOMEPNA"></span>

**HomePNA** (220)


</dt> <dd></dd> <dt>

<span id="GFP"></span><span id="gfp"></span>

**GFP** (221)


</dt> <dd></dd> <dt>

<span id="ciscoISLvlan"></span><span id="ciscoislvlan"></span><span id="CISCOISLVLAN"></span>

**ciscoISLvlan** (222)


</dt> <dd></dd> <dt>

<span id="actelisMetaLOOP"></span><span id="actelismetaloop"></span><span id="ACTELISMETALOOP"></span>

**actelisMetaLOOP** (223)


</dt> <dd></dd> <dt>

<span id="Fcip"></span><span id="fcip"></span><span id="FCIP"></span>

**Fcip** (224)


</dt> <dd></dd> <dt>

<span id="IANA_Reserved"></span><span id="iana_reserved"></span><span id="IANA_RESERVED"></span>

**IANA Reserved**


</dt> <dd>225 4095</dd> <dt>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>

**IPv4** (4096)


</dt> <dd></dd> <dt>

<span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span>

**IPv6** (4097)


</dt> <dd></dd> <dt>

<span id="IPv4_v6"></span><span id="ipv4_v6"></span><span id="IPV4_V6"></span>

**IPv4/v6** (4098)


</dt> <dd></dd> <dt>

<span id="IPX"></span><span id="ipx"></span>

**IPX** (4099)


</dt> <dd></dd> <dt>

<span id="DECnet"></span><span id="decnet"></span><span id="DECNET"></span>

**DECnet** (4100)


</dt> <dd></dd> <dt>

<span id="SNA"></span><span id="sna"></span>

**SNA** (4101)


</dt> <dd></dd> <dt>

<span id="CONP"></span><span id="conp"></span>

**CONP** (4102)


</dt> <dd></dd> <dt>

<span id="CLNP"></span><span id="clnp"></span>

**CLNP** (4103)


</dt> <dd></dd> <dt>

<span id="VINES"></span><span id="vines"></span>

**VINES** (4104)


</dt> <dd></dd> <dt>

<span id="XNS"></span><span id="xns"></span>

**XNS** (4105)


</dt> <dd></dd> <dt>

<span id="ISDN_B_Channel_Endpoint"></span><span id="isdn_b_channel_endpoint"></span><span id="ISDN_B_CHANNEL_ENDPOINT"></span>

**ISDN B Channel Endpoint** (4106)


</dt> <dd></dd> <dt>

<span id="ISDN_D_Channel_Endpoint"></span><span id="isdn_d_channel_endpoint"></span><span id="ISDN_D_CHANNEL_ENDPOINT"></span>

**ISDN D Channel Endpoint** (4107)


</dt> <dd></dd> <dt>

<span id="BGP"></span><span id="bgp"></span>

**BGP** (4108)


</dt> <dd></dd> <dt>

<span id="OSPF"></span><span id="ospf"></span>

**OSPF** (4109)


</dt> <dd></dd> <dt>

<span id="UDP"></span><span id="udp"></span>

**UDP** (4110)


</dt> <dd></dd> <dt>

<span id="TCP"></span><span id="tcp"></span>

**TCP** (4111)


</dt> <dd></dd> <dt>

<span id="802.11a"></span><span id="802.11A"></span>

**802.11a** (4112)


</dt> <dd></dd> <dt>

<span id="802.11b"></span><span id="802.11B"></span>

**802.11b** (4113)


</dt> <dd></dd> <dt>

<span id="802.11g"></span><span id="802.11G"></span>

**802.11g** (4114)


</dt> <dd></dd> <dt>

<span id="802.11h"></span><span id="802.11H"></span>

**802.11h** (4115)


</dt> <dd></dd> <dt>

<span id="NFS"></span><span id="nfs"></span>

**NFS** (4200)


</dt> <dd></dd> <dt>

<span id="CIFS"></span><span id="cifs"></span>

**CIFS** (4201)


</dt> <dd></dd> <dt>

<span id="DAFS"></span><span id="dafs"></span>

**DAFS** (4202)


</dt> <dd></dd> <dt>

<span id="WebDAV"></span><span id="webdav"></span><span id="WEBDAV"></span>

**WebDAV** (4203)


</dt> <dd></dd> <dt>

<span id="HTTP"></span><span id="http"></span>

**HTTP** (4204)


</dt> <dd></dd> <dt>

<span id="FTP"></span><span id="ftp"></span>

**FTP** (4205)


</dt> <dd></dd> <dt>

<span id="NDMP"></span><span id="ndmp"></span>

**NDMP** (4300)


</dt> <dd></dd> <dt>

<span id="Telnet"></span><span id="telnet"></span><span id="TELNET"></span>

**Telnet** (4400)


</dt> <dd></dd> <dt>

<span id="SSH"></span><span id="ssh"></span>

**SSH** (4401)


</dt> <dd></dd> <dt>

<span id="SM_CLP"></span><span id="sm_clp"></span>

**SM CLP** (4402)


</dt> <dd></dd> <dt>

<span id="SMTP"></span><span id="smtp"></span>

**SMTP** (4403)


</dt> <dd></dd> <dt>

<span id="LDAP"></span><span id="ldap"></span>

**LDAP** (4404)


</dt> <dd></dd> <dt>

<span id="RDP"></span><span id="rdp"></span>

**RDP** (4405)


</dt> <dd></dd> <dt>

<span id="HTTPS"></span><span id="https"></span>

**HTTPS** (4406)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4407 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**ProtocolType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_ProtocolEndpoint.ProtocolIFType"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ProtocolEndpoint.OtherTypeDescription")
</dt> </dl>

Note: This property is deprecated in lieu of the ProtocolIFType enumeration. This deprecation was done to have better alignment between the IF-MIB of the IETF and this CIM class. Deprecated description: ProtocolType is an enumeration that provides information to categorize and classify different instances of this class. For most instances, information in this enumeration and the definition of the subclass overlap. However, there are several cases where a specific subclass of ProtocolEndpoint is not required (for example, there is no Fibre Channel subclass of ProtocolEndpoint). Therefore, this property is needed to define the type of Endpoint.

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>

**IPv4** (2)


</dt> <dd></dd> <dt>

<span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span>

**IPv6** (3)


</dt> <dd></dd> <dt>

<span id="IPX"></span><span id="ipx"></span>

**IPX** (4)


</dt> <dd></dd> <dt>

<span id="AppleTalk"></span><span id="appletalk"></span><span id="APPLETALK"></span>

**AppleTalk** (5)


</dt> <dd></dd> <dt>

<span id="DECnet"></span><span id="decnet"></span><span id="DECNET"></span>

**DECnet** (6)


</dt> <dd></dd> <dt>

<span id="SNA"></span><span id="sna"></span>

**SNA** (7)


</dt> <dd></dd> <dt>

<span id="CONP"></span><span id="conp"></span>

**CONP** (8)


</dt> <dd></dd> <dt>

<span id="CLNP"></span><span id="clnp"></span>

**CLNP** (9)


</dt> <dd></dd> <dt>

<span id="VINES"></span><span id="vines"></span>

**VINES** (10)


</dt> <dd></dd> <dt>

<span id="XNS"></span><span id="xns"></span>

**XNS** (11)


</dt> <dd></dd> <dt>

<span id="ATM"></span><span id="atm"></span>

**ATM** (12)


</dt> <dd></dd> <dt>

<span id="Frame_Relay"></span><span id="frame_relay"></span><span id="FRAME_RELAY"></span>

**Frame Relay** (13)


</dt> <dd></dd> <dt>

<span id="Ethernet"></span><span id="ethernet"></span><span id="ETHERNET"></span>

**Ethernet** (14)


</dt> <dd></dd> <dt>

<span id="TokenRing"></span><span id="tokenring"></span><span id="TOKENRING"></span>

**TokenRing** (15)


</dt> <dd></dd> <dt>

<span id="FDDI"></span><span id="fddi"></span>

**FDDI** (16)


</dt> <dd></dd> <dt>

<span id="Infiniband"></span><span id="infiniband"></span><span id="INFINIBAND"></span>

**Infiniband** (17)


</dt> <dd></dd> <dt>

<span id="Fibre_Channel"></span><span id="fibre_channel"></span><span id="FIBRE_CHANNEL"></span>

**Fibre Channel** (18)


</dt> <dd></dd> <dt>

<span id="ISDN_BRI_Endpoint"></span><span id="isdn_bri_endpoint"></span><span id="ISDN_BRI_ENDPOINT"></span>

**ISDN BRI Endpoint** (19)


</dt> <dd></dd> <dt>

<span id="ISDN_B_Channel_Endpoint"></span><span id="isdn_b_channel_endpoint"></span><span id="ISDN_B_CHANNEL_ENDPOINT"></span>

**ISDN B Channel Endpoint** (20)


</dt> <dd></dd> <dt>

<span id="ISDN_D_Channel_Endpoint"></span><span id="isdn_d_channel_endpoint"></span><span id="ISDN_D_CHANNEL_ENDPOINT"></span>

**ISDN D Channel Endpoint** (21)


</dt> <dd></dd> <dt>

<span id="IPv4_v6"></span><span id="ipv4_v6"></span><span id="IPV4_V6"></span>

**IPv4/v6** (22)


</dt> <dd></dd> <dt>

<span id="BGP"></span><span id="bgp"></span>

**BGP** (23)


</dt> <dd></dd> <dt>

<span id="OSPF"></span><span id="ospf"></span>

**OSPF** (24)


</dt> <dd></dd> <dt>

<span id="MPLS"></span><span id="mpls"></span>

**MPLS** (25)


</dt> <dd></dd> <dt>

<span id="UDP"></span><span id="udp"></span>

**UDP** (26)


</dt> <dd></dd> <dt>

<span id="TCP"></span><span id="tcp"></span>

**TCP** (27)


</dt> <dd></dd> </dl>

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_EnabledLogicalElement.EnabledState")
</dt> </dl>

RequestedState is an integer enumeration that indicates the last requested or desired state for the element. The actual state of the element is represented by EnabledState. This property is provided to compare the last requested and current enabled or disabled states. Note that when EnabledState is set to 5 ("Not Applicable"), then this property has no meaning. By default, the RequestedState of the element is 5 ("No Change"). Refer to the EnabledState property description for explanations of the values in the RequestedState enumeration. Offline (6) indicates that the element has been requested to transition to the Enabled but Offline EnabledState. It should be noted that there are two new values in RequestedState that build on the statuses of EnabledState. These are "Reboot" (10) and "Reset" (11). Reboot refers to doing a "Shut Down" and then moving to an "Enabled" state. Reset indicates that the element is first "Disabled" and then "Enabled". The distinction between requesting "Shut Down" and "Disabled" should also be noted. Shut Down requests an orderly transition to the Disabled state, and might involve removing power, to completely erase any existing state. The Disabled state requests an immediate disabling of the element, such that it will not execute or accept any commands or processing requests. This property is set as the result of a method invocation (such as Start or StopService on CIM\_Service), or can be overridden and defined as WRITEable in a subclass. The method approach is considered superior to a WRITEable property, because it allows an explicit invocation of the operation and the return of a result code. A particular instance of EnabledLogicalElement might not support RequestedStateChange. If this occurs, the value 12 ("Not Applicable") is used.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Shut_Down"></span><span id="shut_down"></span><span id="SHUT_DOWN"></span>

**Shut Down** (4)


</dt> <dd></dd> <dt>

<span id="No_Change"></span><span id="no_change"></span><span id="NO_CHANGE"></span>

**No Change** (5)


</dt> <dd></dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

**Offline** (6)


</dt> <dd></dd> <dt>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>

**Test** (7)


</dt> <dd></dd> <dt>

<span id="Deferred"></span><span id="deferred"></span><span id="DEFERRED"></span>

**Deferred** (8)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (9)


</dt> <dd></dd> <dt>

<span id="Reboot"></span><span id="reboot"></span><span id="REBOOT"></span>

**Reboot** (10)


</dt> <dd></dd> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>

**Reset** (11)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (12)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>13 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**Role**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

For iSCSI, each SCSIProtocolEndpoint MUST act as either a target or an initiator endpoint. Other transports allow a SCSI PE to act as both an initiator and target endpoint. This property indicates which role this ProtocolEndpoint implements.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Initiator"></span><span id="initiator"></span><span id="INITIATOR"></span>

**Initiator** (2)


</dt> <dd></dd> <dt>

<span id="Target"></span><span id="target"></span><span id="TARGET"></span>

**Target** (3)


</dt> <dd></dd> <dt>

<span id="Both_Initiator_and_Target"></span><span id="both_initiator_and_target"></span><span id="BOTH_INITIATOR_AND_TARGET"></span>

**Both Initiator and Target** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_ManagedSystemElement.OperationalStatus"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

Contains a string indicating the primary status of the object.

> [!Note]  
> This property is deprecated and replaced by the **OperationalStatus** property. If you choose to use the **Status** property for backward compatibility it should be secondary to the **OperationalStatus** property.

 

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>



 ("OK")


</dt> <dd></dd> <dt>



 ("Error")


</dt> <dd></dd> <dt>



 ("Degraded")


</dt> <dd></dd> <dt>



 ("Unknown")


</dt> <dd></dd> <dt>



 ("Pred Fail")


</dt> <dd></dd> <dt>



 ("Starting")


</dt> <dd></dd> <dt>



 ("Stopping")


</dt> <dd></dd> <dt>



 ("Service")


</dt> <dd></dd> <dt>



 ("Stressed")


</dt> <dd></dd> <dt>



 ("NonRecover")


</dt> <dd></dd> <dt>



 ("No Contact")


</dt> <dd></dd> <dt>



 ("Lost Comm")


</dt> <dd></dd> <dt>



 ("Stopped")


</dt> <dd></dd> </dl>

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ManagedSystemElement.OperationalStatus")
</dt> </dl>

Contains strings describing the corresponding values in the **OperationalStatus** array. For example, if an element in **OperationalStatus** contains the value **Stopping**, then the element at the same array index in this property may contain an explanation as to why an object is being stopped.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_System.CreationClassName"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The CreationClassName of the scoping System.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_System.Name"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The Name of the scoping System.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

</dd> <dt>

**TargetRelativePortNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("SPC.INCITS-T10 \| RelativeTargetPort \| IdentifierFormat")
</dt> </dl>

For ports on a target device, the port number, relative to the storage system. 0 is reserved by T10, 1 is port A, 2 is port B, etc. These numbers are used in SCSI commands that operate on target port groups.

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|IF-MIB.ifLastChange")
</dt> </dl>

TBD

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md)
</dt> </dl>

 

 





