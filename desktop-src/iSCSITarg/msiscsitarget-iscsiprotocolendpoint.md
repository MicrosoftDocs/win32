---
title: MSISCSITARGET\_iSCSIProtocolEndpoint class
description: Represents an iSCSI port.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 898b706b-d4e0-4fd1-aeb9-1356c26ffa98
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSISCSITARGET_iSCSIProtocolEndpoint class iSCSI Software Target API
- MSISCSITARGET_iSCSIProtocolEndpoint class iSCSI Software Target API , described
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSISCSITARGET\_iSCSIProtocolEndpoint class

Represents an iSCSI port.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Version("1.0.0")]
class MSISCSITARGET_iSCSIProtocolEndpoint : CIM_iSCSIProtocolEndpoint
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
  string   OtherTypeDescription;
  uint32   TargetRelativePortNumber;
  string   OtherConnectionType;
  string   Name;
  uint16   ProtocolIFType = 1;
  uint16   ConnectionType = 7;
  string   Identifier = 000000000001";
  uint16   Role = 3;
};
```

## Members

The **MSISCSITARGET\_iSCSIProtocolEndpoint** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSISCSITARGET\_iSCSIProtocolEndpoint** class has these methods.



| Method                                                                               | Description                                                                                                                                                                                              |
|:-------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RequestStateChange**](requeststatechange-msiscsitarget-iscsiprotocolendpoint.md) | Requests that the state of the element be changed to the specified value.<br/> This method is inherited from the [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) class.<br/> |



 

### Properties

The **MSISCSITARGET\_iSCSIProtocolEndpoint** class has these properties.

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

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("ConnectionType"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("SPC.INCITS-T10 \| Protocol Identifier \| Values"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SCSIProtocolEndpoint.Name", "CIM\_SCSIProtocolEndpoint.OtherConnectionType")
</dt> </dl>

Indicates the supported connection type for this endpoint. The connection type is used in some SCSI commands and might be required before the ports are associated.

> \[!Important\]  
> For **MSISCSITARGET\_iSCSIProtocolEndpoint** and all classes that are derived from it, the **ConnectionType** property must be **iSCSI** (7).

 

The possible values are.

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

**Identifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Identifier"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (13)
</dt> </dl>

Uniquely identifies the endpoint. The **Identifier** property must contain the Initiator Session ID (ISID) if it is an initiator, or the Target Portal Group Tag (TGPT) if it is a target. This property must be unique across all **CIM\_iSCSIProtocolEndpoint** instances that are associated with a common [**CIM\_SCSIProtocolController**](https://msdn.microsoft.com/library/cc136905) instance. This field is formatted as 12 hexadecimal digits.

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

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_SCSIProtocolEndpoint**](cim-scsiprotocolendpoint.md).**ConnectionType**", "**CIM\_SCSIProtocolEndpoint**.**OtherConnectionType**")
</dt> </dl>

The format of Name is based on the **ConnectionType** property. For iSCSI, the Name property of a [**CIM\_SCSIProtocolEndpoint**](cim-scsiprotocolendpoint.md) MUST contain the iSCSI port name as described in the iSCSI RFC (currently http://www.ietf.org/internet-drafts/draft-ietf- ips-iscsi-20.txt) -

&lt;iSCSI node name&gt; + 'i,' + ISID for initiators,

&lt;iSCSI node name&gt; + 't,' + TPGT for targets,

where &lt;iSCSI node name&gt; can be any of the standard iSCSI name namespaces (eg. iqn, eui); and includes the namespace prefix.

This property is inherited from [**CIM\_iSCSIProtocolEndpoint**](cim-iscsiprotocolendpoint.md).

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

The connection type, if **ConnectionType** is "Other".

This property is inherited from [**CIM\_SCSIProtocolEndpoint**](cim-scsiprotocolendpoint.md).

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

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("ProtocolIFType"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|IF-MIB.ifType"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ProtocolEndpoint.OtherTypeDescription")
</dt> </dl>

Indicates the Protocol Interface Type, which is used to categorize and to classify [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/cc136899) instances.

> [!Note]  
> Values are mapped to the Internet Assigned Numbers Authority (IANA) ifType Management Information Base (MIB). For more information, see the [IANA](http://www.iana.org/assignments/ianaiftype-mib) website at http://www.iana.org/assignments/ianaiftype-mib.

 

Additional values that are defined by the Distributed Management Task Force (DMTF) have been added.

If the **ProtocolIFType** property is set to 1 (**Other**), then the type information must be provided in the **OtherTypeDescription** property.

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
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Role")
</dt> </dl>

Indicates whether the **CIM\_SCSIProtocolEndpoint** is acting as a target or initiator endpoint.

The possible values are.

<dt>

<span id="Initiator"></span><span id="initiator"></span><span id="INITIATOR"></span>

**Initiator** (2)


</dt> <dd></dd> <dt>

<span id="Target"></span><span id="target"></span><span id="TARGET"></span>

**Target** (3)


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

This property is inherited from [**CIM\_SCSIProtocolEndpoint**](cim-scsiprotocolendpoint.md).

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

[**CIM\_iSCSIProtocolEndpoint**](cim-iscsiprotocolendpoint.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**CIM\_SCSIProtocolController**](https://msdn.microsoft.com/library/cc136905)
</dt> <dt>

[**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/cc136899)
</dt> <dt>

[**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447)
</dt> <dt>

[**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063)
</dt> <dt>

[**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898)
</dt> <dt>

[**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871)
</dt> </dl>

 

 





