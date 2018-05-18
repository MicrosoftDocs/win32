---
title: MSFT\_MpComputerStatus class
description: This is the base status class for the user's PC.
ms.assetid: '13999054-6b88-4b26-bad0-5a40e30d7c0a'
keywords: ["MSFT_MpComputerStatus class", "MSFT_MpComputerStatus class, described"]
topic_type:
- apiref
api_name:
- MSFT_MpComputerStatus
- MSFT_MpComputerStatus.ComputerID
- MSFT_MpComputerStatus.ComputerState
- MSFT_MpComputerStatus.AMProductVersion
- MSFT_MpComputerStatus.AMServiceVersion
- MSFT_MpComputerStatus.AntispywareSignatureVersion
- MSFT_MpComputerStatus.AntispywareSignatureAge
- MSFT_MpComputerStatus.AntispywareSignatureLastUpdated
- MSFT_MpComputerStatus.AntivirusSignatureVersion
- MSFT_MpComputerStatus.AntivirusSignatureAge
- MSFT_MpComputerStatus.AntivirusSignatureLastUpdated
- MSFT_MpComputerStatus.NISSignatureVersion
- MSFT_MpComputerStatus.NISSignatureAge
- MSFT_MpComputerStatus.NISSignatureLastUpdated
- MSFT_MpComputerStatus.FullScanStartTime
- MSFT_MpComputerStatus.FullScanEndTime
- MSFT_MpComputerStatus.FullScanAge
- MSFT_MpComputerStatus.LastFullScanSource
- MSFT_MpComputerStatus.RealTimeScanDirection
- MSFT_MpComputerStatus.QuickScanStartTime
- MSFT_MpComputerStatus.QuickScanEndTime
- MSFT_MpComputerStatus.QuickScanAge
- MSFT_MpComputerStatus.LastQuickScanSource
- MSFT_MpComputerStatus.AMEngineVersion
- MSFT_MpComputerStatus.AMServiceEnabled
- MSFT_MpComputerStatus.OnAccessProtectionEnabled
- MSFT_MpComputerStatus.IoavProtectionEnabled
- MSFT_MpComputerStatus.BehaviorMonitorEnabled
- MSFT_MpComputerStatus.AntivirusEnabled
- MSFT_MpComputerStatus.AntispywareEnabled
- MSFT_MpComputerStatus.RealTimeProtectionEnabled
- MSFT_MpComputerStatus.NISEngineVersion
- MSFT_MpComputerStatus.NISEnabled
api_location:
- ProtectionManagement.dll
api_type:
- DllExport
---

# MSFT\_MpComputerStatus class

This is the base status class for the user's PC.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_MpComputerStatus : BaseStatus
{
  string   ComputerID = msft_mpcomputerstatus.xml;
  uint32   ComputerState = 0;
  string   AMProductVersion = msft_mpcomputerstatus.xml;
  string   AMServiceVersion = msft_mpcomputerstatus.xml;
  string   AntispywareSignatureVersion = msft_mpcomputerstatus.xml;
  uint32   AntispywareSignatureAge = 0;
  DateTime AntispywareSignatureLastUpdated;
  string   AntivirusSignatureVersion = ed;
  uint32   AntivirusSignatureAge = 0;
  DateTime AntivirusSignatureLastUpdated;
  string   NISSignatureVersion = pdated;
  uint32   NISSignatureAge = 0;
  DateTime NISSignatureLastUpdated;
  DateTime FullScanStartTime;
  DateTime FullScanEndTime;
  uint32   FullScanAge = 0;
  uint8    LastFullScanSource = 0;
  uint8    RealTimeScanDirection = 0;
  DateTime QuickScanStartTime;
  DateTime QuickScanEndTime;
  uint32   QuickScanAge = 0;
  uint8    LastQuickScanSource = 0;
  string   AMEngineVersion = 0;
  boolean  AMServiceEnabled = false;
  boolean  OnAccessProtectionEnabled = false;
  boolean  IoavProtectionEnabled = false;
  boolean  BehaviorMonitorEnabled = false;
  boolean  AntivirusEnabled = false;
  boolean  AntispywareEnabled = false;
  boolean  RealTimeProtectionEnabled = false;
  string   NISEngineVersion = bled = false;
  boolean  NISEnabled = false;
};
```

## Members

The **MSFT\_MpComputerStatus** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_MpComputerStatus** class has these properties.

<dl> <dt>

**AMEngineVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The AM Engine version (major, minor, build, revision)

</dd> <dt>

**AMProductVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Product version (major, minor, build, revision)

</dd> <dt>

**AMServiceEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the AM Engine is enabled

</dd> <dt>

**AMServiceVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Service version (major, minor, build, revision)

</dd> <dt>

**AntispywareEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether Antispyware protection is enabled

</dd> <dt>

**AntispywareSignatureAge**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Antispyware Signature age in days - if signatures have never been updated you will see an age of 65535 days

</dd> <dt>

**AntispywareSignatureLastUpdated**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Antispyware Last updated local time. If this has never updated you will see a null value in this property

</dd> <dt>

**AntispywareSignatureVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Antispyware Signature version (major, minor, build, revision)

</dd> <dt>

**AntivirusEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether Antivirus protection is enabled

</dd> <dt>

**AntivirusSignatureAge**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Antivirus Signature age in days- if signatures have never been updated you will see an age of 65535 days

</dd> <dt>

**AntivirusSignatureLastUpdated**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Antivirus Last updated local time - If this has never updated you will see a null value in this property

</dd> <dt>

**AntivirusSignatureVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Antivirus Signature version (major, minor, build, revision)

</dd> <dt>

**BehaviorMonitorEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether behavior monitoring is enabled

</dd> <dt>

**ComputerID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Computer ID created by MAPS

</dd> <dt>

**ComputerState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current computer state

</dd> <dt>

**FullScanAge**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Last full scan age in days- if signatures have never been updated you will see an age of 65535 days

</dd> <dt>

**FullScanEndTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time of last Full Scan end - If this has never updated you will see a null value in this property

</dd> <dt>

**FullScanStartTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time of last Full Scan start - If this has never updated you will see a null value in this property

</dd> <dt>

**IoavProtectionEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scan all downloaded files and attachments

</dd> <dt>

**LastFullScanSource**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Last scan source

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
</dt> </dl>

</dd> <dt>

**LastQuickScanSource**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Last scan source

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
</dt> </dl>

</dd> <dt>

**NISEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the NRI Engine is enabled

</dd> <dt>

**NISEngineVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

NRI Engine version (major, minor, build, revision)

</dd> <dt>

**NISSignatureAge**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

NRI Signature age in days- if signatures have never been updated you will see an age of 65535 days

</dd> <dt>

**NISSignatureLastUpdated**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

NRI Last updated local time - If this has never updated you will see a null value in this property

</dd> <dt>

**NISSignatureVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The NRI Signature version (major, minor, build, revision)

</dd> <dt>

**OnAccessProtectionEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether the computer is monitoring file and program activity on your computer

</dd> <dt>

**QuickScanAge**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Last quick scan age in days- if signatures have never been updated you will see an age of 65535 days.

</dd> <dt>

**QuickScanEndTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time of last Quick Scan end - If this has never updated you will see a null value in this property

</dd> <dt>

**QuickScanStartTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time of last Quick Scan start - If this has never updated you will see a null value in this property

</dd> <dt>

**RealTimeProtectionEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether real-time protection is enabled

</dd> <dt>

**RealTimeScanDirection**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Real-time scan direction enumeration

<dl> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>**Both** (0)
</dt> <dt>

<span id="Incoming"></span><span id="incoming"></span><span id="INCOMING"></span>**Incoming** (1)
</dt> <dt>

<span id="Outcoming"></span><span id="outcoming"></span><span id="OUTCOMING"></span>**Outcoming** (2)
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



 

 





