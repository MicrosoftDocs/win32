---
title: MSISCSITARGET\_iSCSISessionSettings class
description: Contains the default settings for an iSCSI Session. These properties are used as the starting position for login negotiations between initiator and target nodes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '60e787f5-e202-460e-ad5a-31cdf78ba6ea'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSISCSITARGET_iSCSISessionSettings class iSCSI Software Target API", "MSISCSITARGET_iSCSISessionSettings class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_iSCSISessionSettings
- MSISCSITARGET_iSCSISessionSettings.Caption
- MSISCSITARGET_iSCSISessionSettings.Description
- MSISCSITARGET_iSCSISessionSettings.InstanceID
- MSISCSITARGET_iSCSISessionSettings.ElementName
- MSISCSITARGET_iSCSISessionSettings.MaxConnectionsPerSession
- MSISCSITARGET_iSCSISessionSettings.InitialR2TPreference
- MSISCSITARGET_iSCSISessionSettings.ImmediateDataPreference
- MSISCSITARGET_iSCSISessionSettings.MaxOutstandingR2T
- MSISCSITARGET_iSCSISessionSettings.MaxUnsolicitedFirstDataBurstLength
- MSISCSITARGET_iSCSISessionSettings.MaxDataBurstLength
- MSISCSITARGET_iSCSISessionSettings.DataSequenceInOrderPreference
- MSISCSITARGET_iSCSISessionSettings.DataPDUInOrderPreference
- MSISCSITARGET_iSCSISessionSettings.DefaultTimeToWaitPreference
- MSISCSITARGET_iSCSISessionSettings.DefaultTimeToRetainPreference
- MSISCSITARGET_iSCSISessionSettings.ErrorRecoveryLevelPreference
- MSISCSITARGET_iSCSISessionSettings.SystemName
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSISCSITARGET\_iSCSISessionSettings class

Contains the default settings for an iSCSI Session. These properties are used as the starting position for login negotiations between initiator and target nodes.

Depending on a given implementation, an instance of **MSISCSITARGET\_iSCSISessionSettings** is associated by [**MSISCSITARGET\_ElementSettingData**](msiscsitarget-elementsettingdata.md) to one or more instances of [**MSISCSITARGET\_iSCSIProtocolEndpoint**](msiscsitarget-iscsiprotocolendpoint.md), [**MSISCSITARGET\_SCSIProtocolController**](msiscsitarget-scsiprotocolcontroller.md), or [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Version("1.0.0")]
class MSISCSITARGET_iSCSISessionSettings : CIM_iSCSISessionSettings
{
  string  Caption;
  string  Description;
  string  InstanceID;
  string  ElementName;
  uint32  MaxConnectionsPerSession = 1;
  boolean InitialR2TPreference = TRUE;
  boolean ImmediateDataPreference = TRUE;
  uint32  MaxOutstandingR2T = 1;
  uint32  MaxUnsolicitedFirstDataBurstLength = 65536;
  uint32  MaxDataBurstLength = 262144;
  boolean DataSequenceInOrderPreference = TRUE;
  boolean DataPDUInOrderPreference = TRUE;
  uint32  DefaultTimeToWaitPreference = 2;
  uint32  DefaultTimeToRetainPreference = 20;
  uint32  ErrorRecoveryLevelPreference = 0;
  string  SystemName;
};
```

## Members

The **MSISCSITARGET\_iSCSISessionSettings** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_iSCSISessionSettings** class has these properties.

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

**DataPDUInOrderPreference**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiNodeDataPDUInOrder"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISession.DataPDUInOrder")
</dt> </dl>

The DataPDUInOrder preference of this node. False (=No) indicates that iSCSI data PDUs within sequences MAY be in any order. True (=Yes) indicates that data PDUs within sequences MUST be at continuously increasing addresses, with no gaps or overlay between PDUs.

This property is inherited from [**CIM\_iSCSISessionSettings**](cim-iscsisessionsettings.md).

</dd> <dt>

**DataSequenceInOrderPreference**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiNodeDataSequenceInOrder"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISession.DataSequenceInOrder")
</dt> </dl>

The DataSequenceInOrder preference of this node. False (=No) indicates that iSCSI data PDU sequences MAY be transferred in any order. True (=Yes) indicates that data PDU sequences MUST be transferred using continuously increasing offsets, except during error recovery.

This property is inherited from [**CIM\_iSCSISessionSettings**](cim-iscsisessionsettings.md).

</dd> <dt>

**DefaultTimeToRetainPreference**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Seconds"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (3600), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiNodeDefaultTime2Retain"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISession.DefaultTimeToRetain")
</dt> </dl>

The DefaultTime2Retain preference of this node. This is the maximum time, in seconds after an initial wait (Time2Wait), before which an active iSCSI task reassignment is still possible after an unexpected connection termination or a connection reset.

This property is inherited from [**CIM\_iSCSISessionSettings**](cim-iscsisessionsettings.md).

</dd> <dt>

**DefaultTimeToWaitPreference**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Seconds"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (3600), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiNodeDefaultTime2Wait"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISession.DefaultTimeToWait")
</dt> </dl>

The DefaultTime2Wait preference of this node. This is the minimum time, in seconds, to wait before attempting an explicit/implicit logout or active iSCSI task reassignment after an unexpected connection termination or a connection reset.

This property is inherited from [**CIM\_iSCSISessionSettings**](cim-iscsisessionsettings.md).

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

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The user-friendly name for this instance of SettingData. In addition, the user-friendly name can be used as an index property for a search or query. (Note: The name does not have to be unique within a namespace.)

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**ErrorRecoveryLevelPreference**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (255), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiNodeErrorRecoveryLevel"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISession.ErrorRecoveryLevel")
</dt> </dl>

The ErrorRecoveryLevel preference of this node. Currently, only 0-2 are valid. This is designed to accommodate future error recover levels.

Higher error recovery levels imply support in addition to support for the lower error level functions. In other words, error level 2 implies support for levels 0-1, since those functions are subsets of error level 2.

This property is inherited from [**CIM\_iSCSISessionSettings**](cim-iscsisessionsettings.md).

</dd> <dt>

**ImmediateDataPreference**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiNodeImmediateData"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISession.ImmediateData")
</dt> </dl>

This property indicates ImmediateData preference for this node True = YES (but will accept NO), False = NO.

This property is inherited from [**CIM\_iSCSISessionSettings**](cim-iscsisessionsettings.md).

</dd> <dt>

**InitialR2TPreference**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiNodeInitialR2T"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISession.InitialR2T")
</dt> </dl>

This property indicates the InitialR2T preference for this node: true = YES, false = will try to negotiate NO, will accept YES.

This property is inherited from [**CIM\_iSCSISessionSettings**](cim-iscsisessionsettings.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon (:), and where &lt;OrgID&gt; must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness, &lt;OrgID&gt; must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between &lt;OrgID&gt; and &lt;LocalID&gt;.

&lt;LocalID&gt; is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance.

For DMTF-defined instances, the "preferred" algorithm must be used with the &lt;OrgID&gt; set to CIM.

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**MaxConnectionsPerSession**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (65535), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiNodeMaxConnections"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISession.MaxConnectionsPerSession")
</dt> </dl>

The maximum number of connections allowed in each session to and/or from this node.

This property is inherited from [**CIM\_iSCSISessionSettings**](cim-iscsisessionsettings.md).

</dd> <dt>

**MaxDataBurstLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (512), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (16777215), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiNodeMaxBurstLength"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISession.MaxDataBurstLength")
</dt> </dl>

The maximum number of bytes which can be sent within a single sequence of Data-In or Data-Out PDUs.

This property is inherited from [**CIM\_iSCSISessionSettings**](cim-iscsisessionsettings.md).

</dd> <dt>

**MaxOutstandingR2T**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (65535), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiNodeMaxOutstandingR2T"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISession.MaxOutstandingR2T")
</dt> </dl>

Maximum number of outstanding R2Ts allowed per ISCSI task.

This property is inherited from [**CIM\_iSCSISessionSettings**](cim-iscsisessionsettings.md).

</dd> <dt>

**MaxUnsolicitedFirstDataBurstLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (512), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (16777215), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiNodeFirstBurstLength"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSISession.MaxUnsolicitedFirstDataBurstLength")
</dt> </dl>

The maximum length (bytes) supported for unsolicited data to/from this node.

This property is inherited from [**CIM\_iSCSISessionSettings**](cim-iscsisessionsettings.md).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the computer system name.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_iSCSISessionSettings**](cim-iscsisessionsettings.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871)
</dt> <dt>

[**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911)
</dt> </dl>

 

 





