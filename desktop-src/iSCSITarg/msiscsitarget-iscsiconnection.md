---
title: MSISCSITARGET\_iSCSIConnection class
description: Describes the attributes and negotiated values for an iSCSI connection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fbc6f1c9-d195-4a05-bf3d-c2f306d5d060
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSISCSITARGET_iSCSIConnection class iSCSI Software Target API
- MSISCSITARGET_iSCSIConnection class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSISCSITARGET_iSCSIConnection
- MSISCSITARGET_iSCSIConnection.Caption
- MSISCSITARGET_iSCSIConnection.Description
- MSISCSITARGET_iSCSIConnection.ElementName
- MSISCSITARGET_iSCSIConnection.InstallDate
- MSISCSITARGET_iSCSIConnection.Name
- MSISCSITARGET_iSCSIConnection.OperationalStatus
- MSISCSITARGET_iSCSIConnection.StatusDescriptions
- MSISCSITARGET_iSCSIConnection.Status
- MSISCSITARGET_iSCSIConnection.HealthState
- MSISCSITARGET_iSCSIConnection.OtherEnabledState
- MSISCSITARGET_iSCSIConnection.EnabledDefault
- MSISCSITARGET_iSCSIConnection.TimeOfLastStateChange
- MSISCSITARGET_iSCSIConnection.InstanceID
- MSISCSITARGET_iSCSIConnection.Directionality
- MSISCSITARGET_iSCSIConnection.AggregationBehavior
- MSISCSITARGET_iSCSIConnection.EnabledState
- MSISCSITARGET_iSCSIConnection.RequestedState
- MSISCSITARGET_iSCSIConnection.ConnectionID
- MSISCSITARGET_iSCSIConnection.MaxReceiveDataSegmentLength
- MSISCSITARGET_iSCSIConnection.MaxTransmitDataSegmentLength
- MSISCSITARGET_iSCSIConnection.HeaderDigestMethod
- MSISCSITARGET_iSCSIConnection.OtherHeaderDigestMethod
- MSISCSITARGET_iSCSIConnection.DataDigestMethod
- MSISCSITARGET_iSCSIConnection.OtherDataDigestMethod
- MSISCSITARGET_iSCSIConnection.ReceivingMarkers
- MSISCSITARGET_iSCSIConnection.SendingMarkers
- MSISCSITARGET_iSCSIConnection.ActiveiSCSIVersion
- MSISCSITARGET_iSCSIConnection.AuthenticationMethodUsed
- MSISCSITARGET_iSCSIConnection.MutualAuthentication
- MSISCSITARGET_iSCSIConnection.SystemName
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSISCSITARGET\_iSCSIConnection class

Describes the attributes and negotiated values for an iSCSI connection. The original settings that are a starting point for negotiation are found in the class **CIM\_iSCSIConnectionSettings**.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Version("1.0.0")]
class MSISCSITARGET_iSCSIConnection : CIM_iSCSIConnection
{
  string   Caption;
  string   Description;
  string   ElementName;
  datetime InstallDate;
  string   Name;
  uint16   OperationalStatus[];
  string   StatusDescriptions[];
  string   Status;
  uint16   HealthState;
  string   OtherEnabledState;
  uint16   EnabledDefault = 2;
  datetime TimeOfLastStateChange;
  string   InstanceID;
  uint16   Directionality;
  uint16   AggregationBehavior;
  uint16   EnabledState = 5;
  uint16   RequestedState = 512;
  uint32   ConnectionID;
  uint32   MaxReceiveDataSegmentLength;
  uint32   MaxTransmitDataSegmentLength;
  uint16   HeaderDigestMethod;
  string   OtherHeaderDigestMethod;
  uint16   DataDigestMethod;
  string   OtherDataDigestMethod;
  boolean  ReceivingMarkers;
  boolean  SendingMarkers;
  boolean  ActiveiSCSIVersion;
  uint16   AuthenticationMethodUsed;
  boolean  MutualAuthentication;
  string   SystemName;
};
```

## Members

The **MSISCSITARGET\_iSCSIConnection** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSISCSITARGET\_iSCSIConnection** class has these methods.



| Method                                                                         | Description                                                                                                                                                                                    |
|:-------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RequestStateChange**](requeststatechange-msiscsitarget-iscsiconnection.md) | Requests that the state of the element be changed to the specified value.<br/> This method is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).<br/> |



 

### Properties

The **MSISCSITARGET\_iSCSIConnection** class has these properties.

<dl> <dt>

**ActiveiSCSIVersion**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (255), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiCxnVersionActive"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSICapabilities.MinimumSpecificationVersionSupported", "CIM\_iSCSICapabilities.MaximumSpecificationVersionSupported")
</dt> </dl>

Active version number of the iSCSI specification negotiated on this connection.

This property is inherited from [**CIM\_iSCSIConnection**](cim-iscsiconnection.md).

</dd> <dt>

**AggregationBehavior**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the pipe is composed of lower-level pipes, and if so, how these lower-level pipes are aggregated (in parallel or in sequence). The specific instances of NetworkPipe that are combined are described using the NetworkPipeComposition association.

In the context of M.3100, the ability to be composed of lower-level pipes is modeled as a Trail. A Trail is made up of one or more Connections. (Note that both Trails and Connections are subclasses of Pipe). Because of the flexibility of the NetworkPipeComposition association, there is no need to subclass NetworkPipe, as was done in M.3100, but merely to instantiate the NetworkPipeComposition association to describe the bundling of the lower-level pipes (i.e., the connections), or the sequencing of them.

This property is inherited from [**CIM\_NetworkPipe**](cim-networkpipe.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="No_Lower-Level_Composition"></span><span id="no_lower-level_composition"></span><span id="NO_LOWER-LEVEL_COMPOSITION"></span>

**No Lower-Level Composition** (2)


</dt> <dd></dd> <dt>

<span id="Combined_In_Parallel"></span><span id="combined_in_parallel"></span><span id="COMBINED_IN_PARALLEL"></span>

**Combined In Parallel** (3)


</dt> <dd></dd> <dt>

<span id="Combined_In_Sequence"></span><span id="combined_in_sequence"></span><span id="COMBINED_IN_SEQUENCE"></span>

**Combined In Sequence** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**AuthenticationMethodUsed**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|IPS-AUTH-MIB.ipsAuthCredAuthMethod"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSIConnectionSettings.PrimaryAuthenticationMethod", "CIM\_iSCSIConnectionSettings.SecondaryAuthenticationMethod", "CIM\_iSCSICapabilities.AuthenticationMethodsSupported")
</dt> </dl>

The authentication method being used on this connection, as communicated during the login phase.

This property is inherited from [**CIM\_iSCSIConnection**](cim-iscsiconnection.md).

<dt>

<span id="No_Authentication"></span><span id="no_authentication"></span><span id="NO_AUTHENTICATION"></span>

**No Authentication** (2)


</dt> <dd></dd> <dt>

<span id="SRP"></span><span id="srp"></span>

**SRP** (3)


</dt> <dd></dd> <dt>

<span id="CHAP"></span><span id="chap"></span>

**CHAP** (4)


</dt> <dd></dd> <dt>

<span id="Kerberos"></span><span id="kerberos"></span><span id="KERBEROS"></span>

**Kerberos** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

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

**ConnectionID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (65535), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiCxnCid")
</dt> </dl>

The iSCSI Connection ID for this connection.

This property is inherited from [**CIM\_iSCSIConnection**](cim-iscsiconnection.md).

</dd> <dt>

**DataDigestMethod**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiCxnDataIntegrity"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSIConnectionSettings.PrimaryHeaderDigestMethod", "CIM\_iSCSIConnectionSettings.SecondaryHeaderDigestMethod", "CIM\_iSCSIConnection.OtherDataDigestMethod")
</dt> </dl>

This property identifies the iSCSI data digest scheme in use within this connection.

This property is inherited from [**CIM\_iSCSIConnection**](cim-iscsiconnection.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="No_Digest"></span><span id="no_digest"></span><span id="NO_DIGEST"></span>

**No Digest** (2)


</dt> <dd></dd> <dt>

<span id="CRC32C"></span><span id="crc32c"></span>

**CRC32C** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Directionality**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Recommendation.ITU\|M3100.Pipe.directionality")
</dt> </dl>

Indicates whether the pipe is bi-directional (value = 2), unidirectional (value = 3), or this information is not known (value = 0). For unidirectional pipes, the source and sink are indicated by a property (SourceOrSink) of the association, EndpointOfNetworkPipe.

This property is inherited from [**CIM\_NetworkPipe**](cim-networkpipe.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Bi-Directional"></span><span id="bi-directional"></span><span id="BI-DIRECTIONAL"></span>

**Bi-Directional** (2)


</dt> <dd></dd> <dt>

<span id="Unidirectional"></span><span id="unidirectional"></span><span id="UNIDIRECTIONAL"></span>

**Unidirectional** (3)


</dt> <dd></dd> </dl>

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

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Recommendation.ITU\|M3100.Pipe.operationalState")
</dt> </dl>

An integer enumeration that indicates the enabled and disabled states of an element. It can also indicate the transitions between these requested states.

This property is inherited from [**CIM\_NetworkPipe**](cim-networkpipe.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>

**Shutting Down** (4)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (5)


</dt> <dd></dd> <dt>

<span id="Enabled_but_Offline"></span><span id="enabled_but_offline"></span><span id="ENABLED_BUT_OFFLINE"></span>

**Enabled but Offline** (6)


</dt> <dd></dd> <dt>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>

**In Test** (7)


</dt> <dd></dd> <dt>

<span id="Deferred"></span><span id="deferred"></span><span id="DEFERRED"></span>

**Deferred** (8)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (9)


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** (10)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>11 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**HeaderDigestMethod**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiCxnHeaderIntegrity"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSIConnectionSettings.PrimaryHeaderDigestMethod", "CIM\_iSCSIConnectionSettings.SecondaryHeaderDigestMethod", "CIM\_iSCSIConnection.OtherHeaderDigestMethod")
</dt> </dl>

This property identifies the iSCSI header digest scheme in use within this connection.

This property is inherited from [**CIM\_iSCSIConnection**](cim-iscsiconnection.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="No_Digest"></span><span id="no_digest"></span><span id="NO_DIGEST"></span>

**No Digest** (2)


</dt> <dd></dd> <dt>

<span id="CRC32C"></span><span id="crc32c"></span>

**CRC32C** (3)


</dt> <dd></dd> </dl>

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

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Recommendation.ITU\|M3100.TrailR1.trailId", "Recommendation.ITU\|M3100.ConnectionR1.connectionID", "Recommendation.ITU\|M3100.SubNetworkConnection.subNetworkConnectionID")
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon ':', and where &lt;OrgID&gt; MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority. (This is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness &lt;OrgID&gt; MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between &lt;OrgID&gt; and &lt;LocalID&gt;. (For DMTF defined instances, the 'preferred' algorithm MUST be used with the &lt;OrgID&gt; set to 'CIM'.)

&lt;LocalID&gt; MUST include either a vendor specified unique identifier, or if mapping from an ITU M.3100 environment, the trailID, connectionID or subNetworkConnectionID of the instances of PipeR2.

This property is inherited from [**CIM\_NetworkPipe**](cim-networkpipe.md).

</dd> <dt>

**MaxReceiveDataSegmentLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (512), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (16777215), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiCxnMaxRecvDataSegLength"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSIConnectionSettings.MaxReceiveDataSegmentLength")
</dt> </dl>

The maximum data payload size supported for command or data PDUs able to be received on this connection.

This property is inherited from [**CIM\_iSCSIConnection**](cim-iscsiconnection.md).

</dd> <dt>

**MaxTransmitDataSegmentLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (512), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (16777215), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiCxnMaxXmitDataSegLength")
</dt> </dl>

The maximum data payload size supported for command or data PDUs to be sent on this connection.

This property is inherited from [**CIM\_iSCSIConnection**](cim-iscsiconnection.md).

</dd> <dt>

**MutualAuthentication**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

This property when true, indicates that the Target was required to authenticate itself to the Initiator, in addition to the Initiator authenticating itself to the Target. When false, and AuthenticationMethod is other than 'No Authentication', only the Initatior authenticated itself to the Target.

When AuthenticationMethodUsed is 'No Authentication', this property must be false.

This property is inherited from [**CIM\_iSCSIConnection**](cim-iscsiconnection.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (1024)
</dt> </dl>

The Name property defines the label by which the object is known. When subclassed, the Name property can be overridden to be a Key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ManagedSystemElement.StatusDescriptions")
</dt> </dl>

Contains indicators of the current status of the element. The first value of **OperationalStatus** should contain the primary status for the element.

> [!Note]  
> **OperationalStatus** replaces the deprecated **Status** property. Due to the widespread use of the existing **Status** property in management applications, Microsoft strongly recommends that providers or instrumentation provide both the **Status** and **OperationalStatus** properties. When instrumented, **Status** (because it is single-valued) should also provide the primary status of the element.

 

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

The following values have been defined:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

Indicates the implementation cannot report on **OperationalStatus** at this time.

</dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

Indicates an undefined state.

</dd> <dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (2)


</dt> <dd>

Indicates full functionality without errors.

</dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (3)


</dt> <dd>

Indicates the element is working and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element might not be operating at optimal performance or it might be reporting recoverable errors

</dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>**Stressed** (4)


</dt> <dd>

Indicates that the element is functioning, but needs attention. Overload and overheated are examples of **Stressed** states.

</dd> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>**Predictive Failure** (5)


</dt> <dd>

Indicates that an element is functioning nominally but predicting a failure in the near future.

</dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (6)


</dt> <dd>

Indicates that an error has occurred.

</dd> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (7)


</dt> <dd>

A non-recoverable error has occurred.

</dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (8)


</dt> <dd>

The job is starting.

</dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>**Stopping** (9)


</dt> <dd>

The job is stopping.

</dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (10)


</dt> <dd>

The element has been intentionally stopped.

</dd> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (11)


</dt> <dd>

Indicates the element is being configured, maintained, cleaned, or otherwise administered.

</dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (12)


</dt> <dd>

Indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it.

</dd> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (13)


</dt> <dd>

Indicates that the job is known to exist and has been contacted successfully in the past, but is currently unreachable.

</dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted** (14)


</dt> <dd>

Indicates the job stopped in an unexpected way. The state and configuration of the job might need to be updated.

</dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (15)


</dt> <dd>

Indicates that the job is inactive.

</dd> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (16)


</dt> <dd>

Indicates that an element on which this job depends is in error. This element may be **OK** but is unable to function because of the state of a dependent element. An example is a network service or endpoint that cannot function due to lower-layer networking problems.

</dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (17)


</dt> <dd>

Indicates that the job has completed its operation. This value should be combined with either **OK**, **Error**Error, or **Degraded** so that a client can tell if the complete operation **Completed** with **OK** (passed), Completed with **Error** (failed), or Completed with **Degraded** (the operation finished, but it did not complete OK or did not report an error).

</dd> <dt>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>**Power Mode** (18)


</dt> <dd>

"Power Mode" indicates that the element has additional power model information contained in the associated PowerManagementService association.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

DMTF has reserved this portion of the range for additional *OperationalStatus* values in the future.

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

Microsoft has reserved the unused portion of the range for additional *OperationalStatus* values in the future.

</dd> </dl>

</dd> <dt>

**OtherDataDigestMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSIConnectionSettings.OtherPrimaryDataDigestMethod", "CIM\_iSCSIConnectionSettings.OtherSecondaryDataDigestMethod", "CIM\_iSCSIConnection.DataDigestMethod")
</dt> </dl>

A string describing the Data Digest scheme in use when DataDigestMethod is equal to the value 1, "Other".

This property is inherited from [**CIM\_iSCSIConnection**](cim-iscsiconnection.md).

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

**OtherHeaderDigestMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSIConnectionSettings.OtherPrimaryHeaderDigestMethod", "CIM\_iSCSIConnectionSettings.OtherSecondaryHeaderDigestMethod", "CIM\_iSCSIConnection.HeaderDigestMethod")
</dt> </dl>

A string describing the Header Digest scheme in use when HeaderDigestMethod is equal to the value 1, "Other".

This property is inherited from [**CIM\_iSCSIConnection**](cim-iscsiconnection.md).

</dd> <dt>

**ReceivingMarkers**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiCxnRecvMarker"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSIConnectionSettings.RequestingMarkersOnReceive")
</dt> </dl>

This property indicates whether or not this connection is receiving markers in in its incoming data stream.

This property is inherited from [**CIM\_iSCSIConnection**](cim-iscsiconnection.md).

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Recommendation.ITU\|M3100.Pipe.administrativeState")
</dt> </dl>

Indicates the last requested or desired state for the element. The actual state of the element is represented by **EnabledState**.

This property is inherited from [**CIM\_NetworkPipe**](cim-networkpipe.md).

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

**SendingMarkers**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiCxnSendMarker")
</dt> </dl>

This property indicates whether or not this connection is inserting markers in in its outgoing data stream.

This property is inherited from [**CIM\_iSCSIConnection**](cim-iscsiconnection.md).

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

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the computer system name.

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date or time when the EnabledState of the element last changed. If the state of the element has not changed and this property is populated, then it must be set to a 0 interval value. If a state change was requested, but rejected or not yet processed, the property must not be updated.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

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

[**CIM\_iSCSIConnection**](cim-iscsiconnection.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





