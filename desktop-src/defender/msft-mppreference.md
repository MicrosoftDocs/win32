---
title: MSFT\_MpPreference class
description: Windows Defender Preferences Class.
ms.assetid: '3b3b6dfa-2387-44eb-9241-fe6cd3bd3062'
keywords: ["MSFT_MpPreference class", "MSFT_MpPreference class, described"]
---

# MSFT\_MpPreference class

Windows Defender Preferences Class

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_MpPreference
{
  string   ComputerID = msft_mppreference.xml;
  boolean  DisableAutoExclusions = FALSE;
  string   ExclusionPath[];
  string   ExclusionExtension[];
  string   ExclusionProcess[];
  uint32   QuarantinePurgeItemsAfterDelay;
  uint8    RealTimeScanDirection = 0;
  uint8    RemediationScheduleDay;
  DateTime RemediationScheduleTime;
  uint32   ReportingAdditionalActionTimeOut;
  uint32   ReportingCriticalFailureTimeOut;
  uint32   ReportingNonCriticalTimeOut;
  uint8    ScanAvgCPULoadFactor;
  boolean  CheckForSignaturesBeforeRunningScan;
  uint32   ScanPurgeItemsAfterDelay;
  boolean  ScanOnlyIfIdleEnabled;
  uint8    ScanParameters;
  uint8    ScanScheduleDay;
  DateTime ScanScheduleQuickScanTime;
  DateTime ScanScheduleTime;
  uint32   SignatureFirstAuGracePeriod;
  uint32   SignatureAuGracePeriod;
  string   SignatureDefinitionUpdateFileSharesSources;
  boolean  SignatureDisableUpdateOnStartupWithoutEngine;
  string   SignatureFallbackOrder;
  uint8    SignatureScheduleDay;
  DateTime SignatureScheduleTime;
  uint32   SignatureUpdateCatchupInterval;
  uint32   SignatureUpdateInterval;
  uint8    MAPSReporting;
  uint8    SubmitSamplesConsent;
  boolean  DisablePrivacyMode;
  boolean  RandomizeScheduleTaskTimes;
  boolean  DisableBehaviorMonitoring;
  boolean  DisableIntrusionPreventionSystem;
  boolean  DisableIOAVProtection;
  boolean  DisableRealtimeMonitoring;
  boolean  DisableScriptScanning;
  boolean  DisableArchiveScanning;
  boolean  DisableCatchupFullScan;
  boolean  DisableCatchupQuickScan;
  boolean  DisableEmailScanning;
  boolean  DisableRemovableDriveScanning;
  boolean  DisableRestorePoint;
  boolean  DisableScanningMappedNetworkDrivesForFullScan;
  boolean  DisableScanningNetworkFiles;
  boolean  UILockdown;
  sint64   ThreatIDDefaultAction_Ids[];
  uint8    ThreatIDDefaultAction_Actions[];
  uint8    UnknownThreatDefaultAction;
  uint8    LowThreatDefaultAction;
  uint8    ModerateThreatDefaultAction;
  uint8    HighThreatDefaultAction;
  uint8    SevereThreatDefaultAction;
};
```

## Members

The **MSFT\_MpPreference** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_MpPreference** class has these methods.



| Method                                     | Description    |
|:-------------------------------------------|:---------------|
| [**Add**](add-msft-mppreference.md)       | TBD<br/> |
| [**Remove**](remove-msft-mppreference.md) | TBD<br/> |
| [**Set**](set-msft-mppreference.md)       | TBD<br/> |



 

### Properties

The **MSFT\_MpPreference** class has these properties.

<dl> <dt>

**CheckForSignaturesBeforeRunningScan**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When set, Windows Defender will check for new signatures before running a scan. If new signatures are found they will be downloaded and installed before the scan begins. If no new signatures are found, the scan will start based on the existing signatures.

</dd> <dt>

**ComputerID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Computer ID created by MAPS

</dd> <dt>

**DisableArchiveScanning**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Disable archive scanning.

</dd> <dt>

**DisableAutoExclusions**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Beginning in Windows 10:** Allows an administrator to specify if the Automatic Exclusions feature for Server SKUs should be turned off.

</dd> <dt>

**DisableBehaviorMonitoring**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Disable behavior monitoring.

</dd> <dt>

**DisableCatchupFullScan**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Disable catch-up full scan. A catch-up scan is a scan that is initiated because a regularly scheduled scan was missed. Usually these scheduled scans are missed because the computer was turned off at the scheduled time.

</dd> <dt>

**DisableCatchupQuickScan**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Disable catch-up quick scan. A catch-up scan is a scan that is initiated because a regularly scheduled scan was missed. Usually these scheduled scans are missed because the computer was turned off at the scheduled time.

</dd> <dt>

**DisableEmailScanning**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Disable email scanning.

</dd> <dt>

**DisableIntrusionPreventionSystem**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Disable intrusion prevention system.

</dd> <dt>

**DisableIOAVProtection**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Disable IOAV protection.

</dd> <dt>

**DisablePrivacyMode**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Disable the privacy mode.

</dd> <dt>

**DisableRealtimeMonitoring**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Disable real-time monitoring.

</dd> <dt>

**DisableRemovableDriveScanning**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Disable removable drive scanning.

</dd> <dt>

**DisableRestorePoint**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Disables restore point.

</dd> <dt>

**DisableScanningMappedNetworkDrivesForFullScan**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Disable running full scan on mapped network drives.

</dd> <dt>

**DisableScanningNetworkFiles**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Disables scanning network files.

</dd> <dt>

**DisableScriptScanning**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Disable script scanning.

</dd> <dt>

**ExclusionExtension**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Allows an administrator to explicitly disable a scan from checking any of the extensions listed.

</dd> <dt>

**ExclusionPath**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Allows an administrator to explicitly disable a scan from checking any of the paths listed.

</dd> <dt>

**ExclusionProcess**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Allows an administrator to explicitly disable a scan from checking any of the processes listed.

</dd> <dt>

**HighThreatDefaultAction**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Default action for high severity threats.

<dl> <dt>

<span id="Clean"></span><span id="clean"></span><span id="CLEAN"></span>**Clean** (1)
</dt> <dt>

<span id="Quarantine"></span><span id="quarantine"></span><span id="QUARANTINE"></span>**Quarantine** (2)
</dt> <dt>

<span id="Remove"></span><span id="remove"></span><span id="REMOVE"></span>**Remove** (3)
</dt> <dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>**Allow** (6)
</dt> <dt>

<span id="UserDefined"></span><span id="userdefined"></span><span id="USERDEFINED"></span>**UserDefined** (8)
</dt> <dt>

<span id="NoAction"></span><span id="noaction"></span><span id="NOACTION"></span>**NoAction** (9)
</dt> <dt>

<span id="Block_"></span><span id="block_"></span><span id="BLOCK_"></span>**Block** (10)
</dt> </dl>

</dd> <dt>

**LowThreatDefaultAction**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Default action for low severity threats.

<dl> <dt>

<span id="Clean"></span><span id="clean"></span><span id="CLEAN"></span>**Clean** (1)
</dt> <dt>

<span id="Quarantine"></span><span id="quarantine"></span><span id="QUARANTINE"></span>**Quarantine** (2)
</dt> <dt>

<span id="Remove"></span><span id="remove"></span><span id="REMOVE"></span>**Remove** (3)
</dt> <dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>**Allow** (6)
</dt> <dt>

<span id="UserDefined"></span><span id="userdefined"></span><span id="USERDEFINED"></span>**UserDefined** (8)
</dt> <dt>

<span id="NoAction"></span><span id="noaction"></span><span id="NOACTION"></span>**NoAction** (9)
</dt> <dt>

<span id="Block_"></span><span id="block_"></span><span id="BLOCK_"></span>**Block** (10)
</dt> </dl>

</dd> <dt>

**MAPSReporting**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Join Microsoft MAPS.

<dl> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (0)
</dt> <dt>

<span id="Basic"></span><span id="basic"></span><span id="BASIC"></span>**Basic** (1)
</dt> <dt>

<span id="Advanced"></span><span id="advanced"></span><span id="ADVANCED"></span>**Advanced** (2)
</dt> </dl>

</dd> <dt>

**ModerateThreatDefaultAction**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Default action for moderate severity threats.

<dl> <dt>

<span id="Clean"></span><span id="clean"></span><span id="CLEAN"></span>**Clean** (1)
</dt> <dt>

<span id="Quarantine"></span><span id="quarantine"></span><span id="QUARANTINE"></span>**Quarantine** (2)
</dt> <dt>

<span id="Remove"></span><span id="remove"></span><span id="REMOVE"></span>**Remove** (3)
</dt> <dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>**Allow** (6)
</dt> <dt>

<span id="UserDefined"></span><span id="userdefined"></span><span id="USERDEFINED"></span>**UserDefined** (8)
</dt> <dt>

<span id="NoAction"></span><span id="noaction"></span><span id="NOACTION"></span>**NoAction** (9)
</dt> <dt>

<span id="Block_"></span><span id="block_"></span><span id="BLOCK_"></span>**Block** (10)
</dt> </dl>

</dd> <dt>

**QuarantinePurgeItemsAfterDelay**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates how many days items should kept in Quarantine folder before being removed.

</dd> <dt>

**RandomizeScheduleTaskTimes**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This setting allows you to enable or disable randomization of the scheduled scan start time and the scheduled definition update start time. This setting is used to distribute the resource impact of scanning. For example, it could be used in guest virtual machines sharing a host, to prevent multiple guest virtual machines from undertaking a disk-intensive operation at the same time.

</dd> <dt>

**RealTimeScanDirection**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Real-time scan direction - Enumeration

<dl> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>**Both** (0)
</dt> <dt>

<span id="Incoming"></span><span id="incoming"></span><span id="INCOMING"></span>**Incoming** (1)
</dt> <dt>

<span id="Outcoming"></span><span id="outcoming"></span><span id="OUTCOMING"></span>**Outcoming** (2)
</dt> </dl>

</dd> <dt>

**RemediationScheduleDay**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates what day of the week to perform the scheduled full scan to complete remediation.

<dl> <dt>

<span id="Every_Day"></span><span id="every_day"></span><span id="EVERY_DAY"></span>**Every Day** (0)
</dt> <dt>

<span id="Sunday"></span><span id="sunday"></span><span id="SUNDAY"></span>**Sunday** (1)
</dt> <dt>

<span id="Monday"></span><span id="monday"></span><span id="MONDAY"></span>**Monday** (2)
</dt> <dt>

<span id="Tuesday"></span><span id="tuesday"></span><span id="TUESDAY"></span>**Tuesday** (3)
</dt> <dt>

<span id="Wednesday"></span><span id="wednesday"></span><span id="WEDNESDAY"></span>**Wednesday** (4)
</dt> <dt>

<span id="Thursday"></span><span id="thursday"></span><span id="THURSDAY"></span>**Thursday** (5)
</dt> <dt>

<span id="Friday"></span><span id="friday"></span><span id="FRIDAY"></span>**Friday** (6)
</dt> <dt>

<span id="Saturday"></span><span id="saturday"></span><span id="SATURDAY"></span>**Saturday** (7)
</dt> <dt>

<span id="Never_"></span><span id="never_"></span><span id="NEVER_"></span>**Never** (8)
</dt> </dl>

</dd> <dt>

**RemediationScheduleTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates what time to perform the scheduled full scan to complete remediation.

</dd> <dt>

**ReportingAdditionalActionTimeOut**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Configure timeout for detections requiring additional action.

</dd> <dt>

**ReportingCriticalFailureTimeOut**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time in minutes for a detection in the 'critically failed' state to move to either 'additional action' or 'cleared' state.

</dd> <dt>

**ReportingNonCriticalTimeOut**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time in minutes for a detection in the 'failed' state to move to the 'cleared' state.

</dd> <dt>

**ScanAvgCPULoadFactor**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specify the maximum percentage of CPU utilization during a scan. This policy setting allows you to configure the maximum percentage CPU utilization permitted during a scan. Valid values for this setting are a percentage represented by the integers 5 to 100. A value of 0 indicates that there should be no throttling of CPU utilization.

</dd> <dt>

**ScanOnlyIfIdleEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Run scheduled scans only if system is idle.

</dd> <dt>

**ScanParameters**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specify the scan type to use for a scheduled scan.

<dl> <dt>

<span id="Quick_Scan"></span><span id="quick_scan"></span><span id="QUICK_SCAN"></span>**Quick Scan** (1)
</dt> <dt>

<span id="Full_Scan"></span><span id="full_scan"></span><span id="FULL_SCAN"></span>**Full Scan** (2)
</dt> </dl>

</dd> <dt>

**ScanPurgeItemsAfterDelay**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Turn on removal of items from scan history folder. This setting defines the number of days items should be kept in the scan history folder before being permanently removed. The value represents the number of days to keep items in the folder. If set to zero, items will be kept forever and will not be automatically removed.

</dd> <dt>

**ScanScheduleDay**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specify the day of the week to run a scheduled scan.

<dl> <dt>

<span id="Every_Day"></span><span id="every_day"></span><span id="EVERY_DAY"></span>**Every Day** (0)
</dt> <dt>

<span id="Sunday"></span><span id="sunday"></span><span id="SUNDAY"></span>**Sunday** (1)
</dt> <dt>

<span id="Monday"></span><span id="monday"></span><span id="MONDAY"></span>**Monday** (2)
</dt> <dt>

<span id="Tuesday"></span><span id="tuesday"></span><span id="TUESDAY"></span>**Tuesday** (3)
</dt> <dt>

<span id="Wednesday"></span><span id="wednesday"></span><span id="WEDNESDAY"></span>**Wednesday** (4)
</dt> <dt>

<span id="Thursday"></span><span id="thursday"></span><span id="THURSDAY"></span>**Thursday** (5)
</dt> <dt>

<span id="Friday"></span><span id="friday"></span><span id="FRIDAY"></span>**Friday** (6)
</dt> <dt>

<span id="Saturday"></span><span id="saturday"></span><span id="SATURDAY"></span>**Saturday** (7)
</dt> <dt>

<span id="Never_"></span><span id="never_"></span><span id="NEVER_"></span>**Never** (8)
</dt> </dl>

</dd> <dt>

**ScanScheduleQuickScanTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specify the time of day to run a scheduled quick scan.

</dd> <dt>

**ScanScheduleTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specify the time of day to run a scheduled scan.

</dd> <dt>

**SevereThreatDefaultAction**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Default action for severe severity threats.

<dl> <dt>

<span id="Clean"></span><span id="clean"></span><span id="CLEAN"></span>**Clean** (1)
</dt> <dt>

<span id="Quarantine"></span><span id="quarantine"></span><span id="QUARANTINE"></span>**Quarantine** (2)
</dt> <dt>

<span id="Remove"></span><span id="remove"></span><span id="REMOVE"></span>**Remove** (3)
</dt> <dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>**Allow** (6)
</dt> <dt>

<span id="UserDefined"></span><span id="userdefined"></span><span id="USERDEFINED"></span>**UserDefined** (8)
</dt> <dt>

<span id="NoAction"></span><span id="noaction"></span><span id="NOACTION"></span>**NoAction** (9)
</dt> <dt>

<span id="Block_"></span><span id="block_"></span><span id="BLOCK_"></span>**Block** (10)
</dt> </dl>

</dd> <dt>

**SignatureAuGracePeriod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Overrides CheckForSignatureBeforeRunningScan. Aborts any service-initiated update if signature was updated successfully within this amount of time. Time in minutes.

</dd> <dt>

**SignatureDefinitionUpdateFileSharesSources**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Defines the file shares for downloading definition updates. setting allows you to configure UNC file share sources for downloading definition updates. Sources will be contacted in the order specified. The value of this setting should be entered as a pipe-separated string enumerating the definition update sources. For example: {\\\\unc1 \| \\\\unc2 }. The list is empty by default.

</dd> <dt>

**SignatureDisableUpdateOnStartupWithoutEngine**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When set to true, AM Service will not initiate definition update on start-up, regardless of whether an Engine is present or not.

</dd> <dt>

**SignatureFallbackOrder**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Define the order of sources for downloading definition updates. This setting allows you to define the order in which different definition update sources should be contacted. The value of this setting should be entered as a pipe-separated string enumerating the definition update sources in order. Possible values are: 'InternalDefinitionUpdateServer' 'MicrosoftUpdateServer' 'MMPC' 'FileShares'

</dd> <dt>

**SignatureFirstAuGracePeriod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Aborts any service-initiated update immediately after first install by the configured amount of time.

</dd> <dt>

**SignatureScheduleDay**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the day of the week in which signature updates occur. If set to zero (0x0) then signature update occurs daily.

<dl> <dt>

<span id="Every_Day"></span><span id="every_day"></span><span id="EVERY_DAY"></span>**Every Day** (0)
</dt> <dt>

<span id="Sunday"></span><span id="sunday"></span><span id="SUNDAY"></span>**Sunday** (1)
</dt> <dt>

<span id="Monday"></span><span id="monday"></span><span id="MONDAY"></span>**Monday** (2)
</dt> <dt>

<span id="Tuesday"></span><span id="tuesday"></span><span id="TUESDAY"></span>**Tuesday** (3)
</dt> <dt>

<span id="Wednesday"></span><span id="wednesday"></span><span id="WEDNESDAY"></span>**Wednesday** (4)
</dt> <dt>

<span id="Thursday"></span><span id="thursday"></span><span id="THURSDAY"></span>**Thursday** (5)
</dt> <dt>

<span id="Friday"></span><span id="friday"></span><span id="FRIDAY"></span>**Friday** (6)
</dt> <dt>

<span id="Saturday"></span><span id="saturday"></span><span id="SATURDAY"></span>**Saturday** (7)
</dt> <dt>

<span id="Never_"></span><span id="never_"></span><span id="NEVER_"></span>**Never** (8)
</dt> </dl>

</dd> <dt>

**SignatureScheduleTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the time at which signature update check happens. By default the signatures are checked before the scheduled scan.

</dd> <dt>

**SignatureUpdateCatchupInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Defines the number of days after which a catch-up signature is warranted. Works with SignatureUpdateLastChecked. 0 = no catch-up; 1 = 1 day; 2 = 2 days, etc.

</dd> <dt>

**SignatureUpdateInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time value is represented as the number of hours between update checks. Valid values range from 1 (every hour) to 24 (once per day).

</dd> <dt>

**SubmitSamplesConsent**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Beginning in Windows 10:** For certain samples the service checks for user consent. If the required consent has already been granted, the service submits them. If not, (and if the user has specified never to ask), the UI is launched to ask for user consent when opt-in for MAPS telemetry is set (*MAPSReporting* != 0).

<dl> <dt>

<span id="Always_Prompt"></span><span id="always_prompt"></span><span id="ALWAYS_PROMPT"></span>**Always Prompt** (0)
</dt> <dt>

<span id="Send_safe_samples_automatically"></span><span id="send_safe_samples_automatically"></span><span id="SEND_SAFE_SAMPLES_AUTOMATICALLY"></span>**Send safe samples automatically** (1)
</dt> <dt>

<span id="Never_send"></span><span id="never_send"></span><span id="NEVER_SEND"></span>**Never send** (2)
</dt> <dt>

<span id="Send_all_samples_automatically"></span><span id="send_all_samples_automatically"></span><span id="SEND_ALL_SAMPLES_AUTOMATICALLY"></span>**Send all samples automatically** (3)
</dt> </dl>

</dd> <dt>

**ThreatIDDefaultAction\_Actions**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Default actions for threats upon which default action should not be taken when detected. The actions need to be in the same order as their respective Ids specified in the ThreatIDDefaultAction\_Ids property.

<dl> <dt>

<span id="Clean"></span><span id="clean"></span><span id="CLEAN"></span>**Clean** (1)
</dt> <dt>

<span id="Quarantine"></span><span id="quarantine"></span><span id="QUARANTINE"></span>**Quarantine** (2)
</dt> <dt>

<span id="Remove"></span><span id="remove"></span><span id="REMOVE"></span>**Remove** (3)
</dt> <dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>**Allow** (6)
</dt> <dt>

<span id="UserDefined"></span><span id="userdefined"></span><span id="USERDEFINED"></span>**UserDefined** (8)
</dt> <dt>

<span id="NoAction"></span><span id="noaction"></span><span id="NOACTION"></span>**NoAction** (9)
</dt> <dt>

<span id="Block_"></span><span id="block_"></span><span id="BLOCK_"></span>**Block** (10)
</dt> </dl>

</dd> <dt>

**ThreatIDDefaultAction\_Ids**
</dt> <dd> <dl> <dt>

Data type: **sint64** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Ids of threats upon which default action should not be taken when detected. The actions in ThreatIDDefaultAction\_Actions need to be specified in the same order as the Ids in ThreatIDDefaultAction\_Ids

</dd> <dt>

**UILockdown**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Enable UI Lockdown mode.

</dd> <dt>

**UnknownThreatDefaultAction**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Default action for unknown threats.

<dl> <dt>

<span id="Clean"></span><span id="clean"></span><span id="CLEAN"></span>**Clean** (1)
</dt> <dt>

<span id="Quarantine"></span><span id="quarantine"></span><span id="QUARANTINE"></span>**Quarantine** (2)
</dt> <dt>

<span id="Remove"></span><span id="remove"></span><span id="REMOVE"></span>**Remove** (3)
</dt> <dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>**Allow** (6)
</dt> <dt>

<span id="UserDefined"></span><span id="userdefined"></span><span id="USERDEFINED"></span>**UserDefined** (8)
</dt> <dt>

<span id="NoAction"></span><span id="noaction"></span><span id="NOACTION"></span>**NoAction** (9)
</dt> <dt>

<span id="Block_"></span><span id="block_"></span><span id="BLOCK_"></span>**Block** (10)
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



 

 





