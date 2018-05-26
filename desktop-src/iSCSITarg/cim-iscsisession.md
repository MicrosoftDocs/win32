---
title: CIM\_iSCSISession class
description: ISCSISession is a network pipe between an initiator and target SCSIProtocolEndpoints.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 76a85e0d-932b-4a70-ab90-2d4e36035b1d
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_iSCSISession class iSCSI Software Target API
- CIM_iSCSISession class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_iSCSISession
- CIM_iSCSISession.Caption
- CIM_iSCSISession.Description
- CIM_iSCSISession.ElementName
- CIM_iSCSISession.InstallDate
- CIM_iSCSISession.Name
- CIM_iSCSISession.OperationalStatus
- CIM_iSCSISession.StatusDescriptions
- CIM_iSCSISession.Status
- CIM_iSCSISession.HealthState
- CIM_iSCSISession.OtherEnabledState
- CIM_iSCSISession.EnabledDefault
- CIM_iSCSISession.TimeOfLastStateChange
- CIM_iSCSISession.InstanceID
- CIM_iSCSISession.AggregationBehavior
- CIM_iSCSISession.EnabledState
- CIM_iSCSISession.RequestedState
- CIM_iSCSISession.Directionality
- CIM_iSCSISession.SessionType
- CIM_iSCSISession.TSIH
- CIM_iSCSISession.EndPointName
- CIM_iSCSISession.CurrentConnections
- CIM_iSCSISession.InitialR2T
- CIM_iSCSISession.ImmediateData
- CIM_iSCSISession.MaxOutstandingR2T
- CIM_iSCSISession.MaxUnsolicitedFirstDataBurstLength
- CIM_iSCSISession.MaxDataBurstLength
- CIM_iSCSISession.DataSequenceInOrder
- CIM_iSCSISession.DataPDUInOrder
- CIM_iSCSISession.ErrorRecoveryLevel
- CIM_iSCSISession.MaxConnectionsPerSession
- CIM_iSCSISession.DefaultTimeToWait
- CIM_iSCSISession.DefaultTimeToRetain
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_iSCSISession class

iSCSISession is a network pipe between an initiator and target SCSIProtocolEndpoints. An iSCSISession is composed of one or more TCP connections which MUST be selected from a SystemSpecificCollection representing an iSCSI Portal Group. NetworkPipeComposition aggregates NetworkPipe instances representing iSCSI connections, which are associated to TCPProtocolEndpoints. Only an iSCSI initiator can create an iSCSI Session, an iSCSI Target MUST accept (or reject) a session request. EndOfNetworkPipe associates iSCSISession with SCSIProtocolEndpoint.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.11.0"), UMLPackagePath("CIM::Network::Pipes")]
class CIM_iSCSISession : CIM_NetworkPipe
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
  uint16   AggregationBehavior;
  uint16   EnabledState = 5;
  uint16   RequestedState = 512;
  uint16   Directionality = 2;
  uint16   SessionType;
  uint32   TSIH;
  string   EndPointName;
  uint32   CurrentConnections;
  boolean  InitialR2T;
  boolean  ImmediateData;
  uint32   MaxOutstandingR2T;
  uint32   MaxUnsolicitedFirstDataBurstLength;
  uint32   MaxDataBurstLength;
  boolean  DataSequenceInOrder;
  boolean  DataPDUInOrder;
  uint32   ErrorRecoveryLevel;
  uint32   MaxConnectionsPerSession;
  uint32   DefaultTimeToWait;
  uint32   DefaultTimeToRetain;
};
```

## Members

The **CIM\_iSCSISession** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CIM\_iSCSISession** class has these methods.



| Method                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RequestStateChange**](cim-iscsisession-requeststatechange.md) | Requests that the state of the element be changed to the value specified in the RequestedState parameter. When the requested state change takes place, the EnabledState and RequestedState of the element will be the same. Invoking the RequestStateChange method multiple times could result in earlier requests being overwritten or lost. If 0 is returned, then the task completed successfully and the use of ConcreteJob was not required. If 4096 (0x1000) is returned, then the task will take some time to complete, ConcreteJob will be created, and its reference returned in the output parameter Job. Any other return code indicates an error condition.<br/> This method is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).<br/> |



 

### Properties

The **CIM\_iSCSISession** class has these properties.

<dl> <dt>

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

**CurrentConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (65535), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiSsnConnectionNumber"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISessionSettings.MaxConnectionsPerSession")
</dt> </dl>

The number of transport protocol connections that currently belong to this session.

</dd> <dt>

**DataPDUInOrder**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiSsnDataPDUInOrder"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISessionSettings.DataPDUInOrderPreference")
</dt> </dl>

False indicates that iSCSI data PDUs within sequences MAY be in any order. True indicates that data PDUs within sequences MUST be at continuously increasing addresses, with no gaps or overlay between PDUs. Default is true.

</dd> <dt>

**DataSequenceInOrder**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiSsnDataSequenceInOrder"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISessionSettings.DataSequenceInOrderPreference")
</dt> </dl>

False indicates that iSCSI data PDU sequences MAY be transferred in any order. True indicates that data PDU sequences MUST be transferred using continuously increasing offsets, except during error recovery.

</dd> <dt>

**DefaultTimeToRetain**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Seconds"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (3600), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiNodeDefaultTime2Retain"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISessionSettings.DefaultTimeToRetainPreference")
</dt> </dl>

The DefaultTime2Retain negotiated for this Session. This is the maximum time, in seconds after an initial wait (Time2Wait), before which an active iSCSI task reassignment is still possible after an unexpected connection termination or a connection reset.

</dd> <dt>

**DefaultTimeToWait**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Seconds"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (3600), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiNodeDefaultTime2Wait"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISessionSettings.DefaultTimeToWaitPreference")
</dt> </dl>

The DefaultTime2Wait negotiated for this Session. This is the minimum time, in seconds, to wait before attempting an explicit/implicit logout or active iSCSI task reassignment after an unexpected connection termination or a connection reset.

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

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Directionality")
</dt> </dl>

iSCSI sessions MUST be bidirectional.

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

**EndPointName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiSsnInitiatorName", "MIB.IETF\|iSCSI-MIB.iscsiSsnTargetName")
</dt> </dl>

The iSCSI Port Name (iSCSIProtocolEndPoint.Name), of the device at the other end of this iSCSISession.

</dd> <dt>

**ErrorRecoveryLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (255), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiSsnErrorRecoveryLevel"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISessionSettings.ErrorRecoveryLevelPreference")
</dt> </dl>

The level of error recovery negotiated between the initiator and the target. Higher numbers represent more detailed recovery schemes.

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

**ImmediateData**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiSsnImmediateData"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISessionSettings.ImmediateDataPreference")
</dt> </dl>

Indicates whether the initiator and target have agreed to support immediate data on this session.

</dd> <dt>

**InitialR2T**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiSsnInitialR2T"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISessionSettings.InitialR2TPreference")
</dt> </dl>

If set to true, indicates that the initiator MUST wait for an R2T before sending to the target. If set to false, the initiator MAY send data immediately, within limits set by iscsiSsnFirstBurstLength and the expected data transfer length of the request.

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

**MaxConnectionsPerSession**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (65535), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiNodeMaxConnections"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISessionSettings.MaxConnectionsPerSession")
</dt> </dl>

The maximum number of connections allowed in this session.

</dd> <dt>

**MaxDataBurstLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (512), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (16777215), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiSsnMaxBurstLength"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISessionSettings.MaxDataBurstLength")
</dt> </dl>

The maximum number of bytes which can be sent within a single sequence of Data-In or Data-Out PDUs.

</dd> <dt>

**MaxOutstandingR2T**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (65535), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiSsnMaxOutstandingR2T"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISessionSettings.MaxOutstandingR2T")
</dt> </dl>

The maximum number of outstanding request-to-transmit (R2T)s per iSCSI task within this session.

</dd> <dt>

**MaxUnsolicitedFirstDataBurstLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (512), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (16777215), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiSsnFirstBurstLength"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISessionSettings.MaxUnsolicitedFirstDataBurstLength")
</dt> </dl>

The maximum length supported for unsolicited data sent within this session.

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

**SessionType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiSsnType")
</dt> </dl>

iSCSI Session type.

<dt>

<span id="Discovery"></span><span id="discovery"></span><span id="DISCOVERY"></span>

**Discovery** (2)


</dt> <dd></dd> <dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

**Normal** (3)


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

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date or time when the EnabledState of the element last changed. If the state of the element has not changed and this property is populated, then it must be set to a 0 interval value. If a state change was requested, but rejected or not yet processed, the property must not be updated.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

</dd> <dt>

**TSIH**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiSsnTSIH")
</dt> </dl>

The Target Session Identifying Handle (TSIH) for this session.

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

[**CIM\_NetworkPipe**](cim-networkpipe.md)
</dt> </dl>

 

 





