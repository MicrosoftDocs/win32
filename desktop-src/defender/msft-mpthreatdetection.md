---
title: MSFT\_MpThreatDetection class
description: This is a class that represents the current detailed state of a threat.
ms.assetid: 'ebc0a7a8-723c-453e-a82b-4fdedb276d19'
keywords: ["MSFT_MpThreatDetection class", "MSFT_MpThreatDetection class, described"]
topic_type:
- apiref
api_name:
- MSFT_MpThreatDetection
- MSFT_MpThreatDetection.DetectionID
- MSFT_MpThreatDetection.ThreatID
- MSFT_MpThreatDetection.ProcessName
- MSFT_MpThreatDetection.DomainUser
- MSFT_MpThreatDetection.DetectionSourceTypeID
- MSFT_MpThreatDetection.Resources
- MSFT_MpThreatDetection.InitialDetectionTime
- MSFT_MpThreatDetection.LastThreatStatusChangeTime
- MSFT_MpThreatDetection.RemediationTime
- MSFT_MpThreatDetection.CurrentThreatExecutionStatusID
- MSFT_MpThreatDetection.ThreatStatusID
- MSFT_MpThreatDetection.ThreatStatusErrorCode
- MSFT_MpThreatDetection.CleaningActionID
- MSFT_MpThreatDetection.AMProductVersion
- MSFT_MpThreatDetection.ActionSuccess
- MSFT_MpThreatDetection.AdditionalActionsBitMask
api_location:
- ProtectionManagement.dll
api_type:
- DllExport
---

# MSFT\_MpThreatDetection class

This is a class that represents the current detailed state of a threat

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_MpThreatDetection : BaseStatus
{
  string   DetectionID;
  sint64   ThreatID;
  string   ProcessName;
  string   DomainUser;
  uint8    DetectionSourceTypeID;
  string   Resources[];
  DateTime InitialDetectionTime;
  DateTime LastThreatStatusChangeTime;
  DateTime RemediationTime;
  uint8    CurrentThreatExecutionStatusID;
  uint8    ThreatStatusID;
  sint32   ThreatStatusErrorCode;
  uint8    CleaningActionID;
  string   AMProductVersion = tatusID;
  boolean  ActionSuccess = false;
  Uint32   AdditionalActionsBitMask;
};
```

## Members

The **MSFT\_MpThreatDetection** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_MpThreatDetection** class has these properties.

<dl> <dt>

**ActionSuccess**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies if the cleaning action was successful

</dd> <dt>

**AdditionalActionsBitMask**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Additional actions required to complete remediation - Enumeration

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="FullScanRequired"></span><span id="fullscanrequired"></span><span id="FULLSCANREQUIRED"></span>**FullScanRequired** (4)
</dt> <dt>

<span id="RebootRequired"></span><span id="rebootrequired"></span><span id="REBOOTREQUIRED"></span>**RebootRequired** (8)
</dt> <dt>

<span id="FullScanAndRebootRequired"></span><span id="fullscanandrebootrequired"></span><span id="FULLSCANANDREBOOTREQUIRED"></span>**FullScanAndRebootRequired** (12)
</dt> <dt>

<span id="ManualStepsRequired"></span><span id="manualstepsrequired"></span><span id="MANUALSTEPSREQUIRED"></span>**ManualStepsRequired** (16)
</dt> <dt>

<span id="FullScanAndManualStepsRequired"></span><span id="fullscanandmanualstepsrequired"></span><span id="FULLSCANANDMANUALSTEPSREQUIRED"></span>**FullScanAndManualStepsRequired** (20)
</dt> <dt>

<span id="RebootAndManualStepsRequired"></span><span id="rebootandmanualstepsrequired"></span><span id="REBOOTANDMANUALSTEPSREQUIRED"></span>**RebootAndManualStepsRequired** (24)
</dt> <dt>

<span id="FullScanAndRebootAndManualStepsRequired"></span><span id="fullscanandrebootandmanualstepsrequired"></span><span id="FULLSCANANDREBOOTANDMANUALSTEPSREQUIRED"></span>**FullScanAndRebootAndManualStepsRequired** (28)
</dt> <dt>

<span id="OfflineScanRequired"></span><span id="offlinescanrequired"></span><span id="OFFLINESCANREQUIRED"></span>**OfflineScanRequired** (32768)
</dt> <dt>

<span id="FullScanAndOfflineScanRequired"></span><span id="fullscanandofflinescanrequired"></span><span id="FULLSCANANDOFFLINESCANREQUIRED"></span>**FullScanAndOfflineScanRequired** (32772)
</dt> <dt>

<span id="RebootAndOfflineScanRequired"></span><span id="rebootandofflinescanrequired"></span><span id="REBOOTANDOFFLINESCANREQUIRED"></span>**RebootAndOfflineScanRequired** (32776)
</dt> <dt>

<span id="FullScanAndRebootAndOfflineScanRequired"></span><span id="fullscanandrebootandofflinescanrequired"></span><span id="FULLSCANANDREBOOTANDOFFLINESCANREQUIRED"></span>**FullScanAndRebootAndOfflineScanRequired** (32780)
</dt> <dt>

<span id="ManualStepsAndOfflineScanRequired"></span><span id="manualstepsandofflinescanrequired"></span><span id="MANUALSTEPSANDOFFLINESCANREQUIRED"></span>**ManualStepsAndOfflineScanRequired** (32784)
</dt> <dt>

<span id="FullScanAndManualStepsAndOfflineScanRequired"></span><span id="fullscanandmanualstepsandofflinescanrequired"></span><span id="FULLSCANANDMANUALSTEPSANDOFFLINESCANREQUIRED"></span>**FullScanAndManualStepsAndOfflineScanRequired** (32788)
</dt> <dt>

<span id="RebootAndManualStepsAndOfflineScanRequired"></span><span id="rebootandmanualstepsandofflinescanrequired"></span><span id="REBOOTANDMANUALSTEPSANDOFFLINESCANREQUIRED"></span>**RebootAndManualStepsAndOfflineScanRequired** (32792)
</dt> <dt>

<span id="FullScanAndRebootAndManualStepsAndOfflineScanRequired_"></span><span id="fullscanandrebootandmanualstepsandofflinescanrequired_"></span><span id="FULLSCANANDREBOOTANDMANUALSTEPSANDOFFLINESCANREQUIRED_"></span>**FullScanAndRebootAndManualStepsAndOfflineScanRequired** (32796 )
</dt> </dl>

</dd> <dt>

**AMProductVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Product version (major, minor, build, revision)

</dd> <dt>

**CleaningActionID**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cleaning action - Enumeration

</dd> <dt>

**CurrentThreatExecutionStatusID**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Execution Status ID - Enumeration

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Blocked"></span><span id="blocked"></span><span id="BLOCKED"></span>**Blocked** (1)
</dt> <dt>

<span id="Allowed"></span><span id="allowed"></span><span id="ALLOWED"></span>**Allowed** (2)
</dt> <dt>

<span id="Executing"></span><span id="executing"></span><span id="EXECUTING"></span>**Executing** (3)
</dt> <dt>

<span id="NotExecuting"></span><span id="notexecuting"></span><span id="NOTEXECUTING"></span>**NotExecuting** (4)
</dt> </dl>

</dd> <dt>

**DetectionID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Unique Detection ID

</dd> <dt>

**DetectionSourceTypeID**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Detection Source Type ID - Enumeration

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="User"></span><span id="user"></span><span id="USER"></span>**User** (1)
</dt> <dt>

<span id="System"></span><span id="system"></span><span id="SYSTEM"></span>**System** (2)
</dt> <dt>

<span id="Real-time"></span><span id="real-time"></span><span id="REAL-TIME"></span>**Real-time** (3)
</dt> <dt>

<span id="IOAV"></span><span id="ioav"></span>**IOAV** (4)
</dt> <dt>

<span id="NRI"></span><span id="nri"></span>**NRI** (5)
</dt> <dt>

<span id="ELAM"></span><span id="elam"></span>**ELAM** (7)
</dt> <dt>

<span id="LocalAttestation"></span><span id="localattestation"></span><span id="LOCALATTESTATION"></span>**LocalAttestation** (8)
</dt> <dt>

<span id="RemoteAttestation"></span><span id="remoteattestation"></span><span id="REMOTEATTESTATION"></span>**RemoteAttestation** (9)
</dt> </dl>

</dd> <dt>

**DomainUser**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user who requested remediation

</dd> <dt>

**InitialDetectionTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The initial threat detection time

</dd> <dt>

**LastThreatStatusChangeTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The most recent time of the threat status change

</dd> <dt>

**ProcessName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the process involved

</dd> <dt>

**RemediationTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time of the remediation.

</dd> <dt>

**Resources**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

List of resources affected by the detection

</dd> <dt>

**ThreatID**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Unique Threat ID

</dd> <dt>

**ThreatStatusErrorCode**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The threat status error code

</dd> <dt>

**ThreatStatusID**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Threat Status ID - Enumeration

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Detected"></span><span id="detected"></span><span id="DETECTED"></span>**Detected** (1)
</dt> <dt>

<span id="Cleaned"></span><span id="cleaned"></span><span id="CLEANED"></span>**Cleaned** (2)
</dt> <dt>

<span id="Quarantined"></span><span id="quarantined"></span><span id="QUARANTINED"></span>**Quarantined** (3)
</dt> <dt>

<span id="Removed"></span><span id="removed"></span><span id="REMOVED"></span>**Removed** (4)
</dt> <dt>

<span id="Allowed"></span><span id="allowed"></span><span id="ALLOWED"></span>**Allowed** (5)
</dt> <dt>

<span id="Blocked"></span><span id="blocked"></span><span id="BLOCKED"></span>**Blocked** (6)
</dt> <dt>

<span id="CleanFailed"></span><span id="cleanfailed"></span><span id="CLEANFAILED"></span>**CleanFailed** (Blocked)
</dt> <dt>

<span id="QuarantineFailed"></span><span id="quarantinefailed"></span><span id="QUARANTINEFAILED"></span>**QuarantineFailed** (102)
</dt> <dt>

<span id="RemoveFailed"></span><span id="removefailed"></span><span id="REMOVEFAILED"></span>**RemoveFailed** (103)
</dt> <dt>

<span id="AllowFailed"></span><span id="allowfailed"></span><span id="ALLOWFAILED"></span>**AllowFailed** (104)
</dt> <dt>

<span id="Abondoned"></span><span id="abondoned"></span><span id="ABONDONED"></span>**Abondoned** (105)
</dt> <dt>

<span id="BlockedFailed"></span><span id="blockedfailed"></span><span id="BLOCKEDFAILED"></span>**BlockedFailed** (107)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Defender<br/>                                                       |
| MOF<br/>                      | <dl> <dt>ProtectionManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ProtectionManagement.dll</dt> </dl> |



 

 





