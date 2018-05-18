---
title: Set method of the MSFT\_MpPreference class
description: TBD.
ms.assetid: 'efed53ac-40e0-45b4-bfc8-69b245eb8836'
keywords: ["Set method", "Set method, MSFT_MpPreference class", "MSFT_MpPreference class, Set method"]
topic_type:
- apiref
api_name:
- MSFT_MpPreference.Set
api_location:
- ProtectionManagement.dll
api_type:
- COM
---

# Set method of the MSFT\_MpPreference class

TBD

## Syntax


```mof
uint32 Set(
  [in] string   ExclusionPath[],
  [in] string   ExclusionExtension[],
  [in] string   ExclusionProcess[],
  [in] uint32   QuarantinePurgeItemsAfterDelay,
  [in] uint8    RealTimeScanDirection,
  [in] uint8    RemediationScheduleDay,
  [in] DateTime RemediationScheduleTime,
  [in] uint32   ReportingAdditionalActionTimeOut,
  [in] uint32   ReportingCriticalFailureTimeOut,
  [in] uint32   ReportingNonCriticalTimeOut,
  [in] uint8    ScanAvgCPULoadFactor,
  [in] boolean  CheckForSignaturesBeforeRunningScan,
  [in] uint32   ScanPurgeItemsAfterDelay,
  [in] boolean  ScanOnlyIfIdleEnabled,
  [in] uint8    ScanParameters,
  [in] uint8    ScanScheduleDay,
  [in] DateTime ScanScheduleQuickScanTime,
  [in] DateTime ScanScheduleTime,
  [in] uint32   SignatureFirstAuGracePeriod,
  [in] uint32   SignatureAuGracePeriod,
  [in] string   SignatureDefinitionUpdateFileSharesSources,
  [in] boolean  SignatureDisableUpdateOnStartupWithoutEngine,
  [in] string   SignatureFallbackOrder,
  [in] uint8    SignatureScheduleDay,
  [in] DateTime SignatureScheduleTime,
  [in] uint32   SignatureUpdateCatchupInterval,
  [in] uint32   SignatureUpdateInterval,
  [in] uint8    MAPSReporting,
       boolean  DisablePrivacyMode,
  [in] boolean  RandomizeScheduleTaskTimes,
  [in] boolean  DisableBehaviorMonitoring,
  [in] boolean  DisableIntrusionPreventionSystem,
  [in] boolean  DisableIOAVProtection,
  [in] boolean  DisableRealtimeMonitoring,
  [in] boolean  DisableScriptScanning,
  [in] boolean  DisableArchiveScanning,
  [in] boolean  DisableCatchupFullScan,
  [in] boolean  DisableCatchupQuickScan,
  [in] boolean  DisableEmailScanning,
  [in] boolean  DisableRemovableDriveScanning,
  [in] boolean  DisableRestorePoint,
  [in] boolean  DisableScanningMappedNetworkDrivesForFullScan,
  [in] boolean  DisableScanningNetworkFiles,
  [in] boolean  UILockdown,
  [in] sint64   ThreatIDDefaultAction_Ids[],
  [in] uint8    ThreatIDDefaultAction_Actions[],
  [in] uint8    UnknownThreatDefaultAction,
  [in] uint8    LowThreatDefaultAction,
  [in] uint8    ModerateThreatDefaultAction,
  [in] uint8    HighThreatDefaultAction,
  [in] uint8    SevereThreatDefaultAction,
  [in] boolean  Force
);
```



## Parameters

<dl> <dt>

*ExclusionPath* \[in\]
</dt> <dd>

Allows an administrator to explicitly disable a scan from checking any of the paths listed.

</dd> <dt>

*ExclusionExtension* \[in\]
</dt> <dd>

Allows an administrator to explicitly disable a scan from checking any of the extensions listed.

</dd> <dt>

*ExclusionProcess* \[in\]
</dt> <dd>

Allows an administrator to explicitly disable a scan from checking any of the processes listed.

</dd> <dt>

*QuarantinePurgeItemsAfterDelay* \[in\]
</dt> <dd>

Indicates how many days items should kept in Quarantine folder before being removed.

</dd> <dt>

*RealTimeScanDirection* \[in\]
</dt> <dd>

Real-time scan direction - Enumeration

<dl> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>**Both** (0)
</dt> <dt>

<span id="Incoming"></span><span id="incoming"></span><span id="INCOMING"></span>**Incoming** (1)
</dt> <dt>

<span id="Outcoming"></span><span id="outcoming"></span><span id="OUTCOMING"></span>**Outcoming** (2)
</dt> </dl> </dd> <dt>

*RemediationScheduleDay* \[in\]
</dt> <dd>

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
</dt> </dl> </dd> <dt>

*RemediationScheduleTime* \[in\]
</dt> <dd>

Indicates what time to perform the scheduled full scan to complete remediation.

</dd> <dt>

*ReportingAdditionalActionTimeOut* \[in\]
</dt> <dd>

Configure timeout for detections requiring additional action.

</dd> <dt>

*ReportingCriticalFailureTimeOut* \[in\]
</dt> <dd>

Time in minutes for a detection in the 'critically failed' state to move to either 'additional action' or 'cleared' state.

</dd> <dt>

*ReportingNonCriticalTimeOut* \[in\]
</dt> <dd>

Time in minutes for a detection in the 'failed' state to move to the 'cleared' state.

</dd> <dt>

*ScanAvgCPULoadFactor* \[in\]
</dt> <dd>

Specify the maximum percentage of CPU utilization during a scan. This policy setting allows you to configure the maximum percentage CPU utilization permitted during a scan. Valid values for this setting are a percentage represented by the integers 5 to 100. A value of 0 indicates that there should be no throttling of CPU utilization.

</dd> <dt>

*CheckForSignaturesBeforeRunningScan* \[in\]
</dt> <dd>

When set, Windows Defender will check for new signatures before running a scan. If new signatures are found they will be downloaded and installed before the scan begins. If no new signatures are found, the scan will start based on the existing signatures.

</dd> <dt>

*ScanPurgeItemsAfterDelay* \[in\]
</dt> <dd>

Turn on removal of items from scan history folder. This setting defines the number of days items should be kept in the scan history folder before being permanently removed. The value represents the number of days to keep items in the folder. If set to zero, items will be kept forever and will not be automatically removed.

</dd> <dt>

*ScanOnlyIfIdleEnabled* \[in\]
</dt> <dd>

Run scheduled scans only if system is idle.

</dd> <dt>

*ScanParameters* \[in\]
</dt> <dd>

Specify the scan type to use for a scheduled scan.

<dl> <dt>

<span id="Quick_Scan"></span><span id="quick_scan"></span><span id="QUICK_SCAN"></span>**Quick Scan** (1)
</dt> <dt>

<span id="Full_Scan"></span><span id="full_scan"></span><span id="FULL_SCAN"></span>**Full Scan** (2)
</dt> </dl> </dd> <dt>

*ScanScheduleDay* \[in\]
</dt> <dd>

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
</dt> </dl> </dd> <dt>

*ScanScheduleQuickScanTime* \[in\]
</dt> <dd>

Specify the time of day to run a scheduled quick scan.

</dd> <dt>

*ScanScheduleTime* \[in\]
</dt> <dd>

Specify the time of day to run a scheduled scan.

</dd> <dt>

*SignatureFirstAuGracePeriod* \[in\]
</dt> <dd>

Aborts any service-initiated update immediately after first install by the configured amount of time.

</dd> <dt>

*SignatureAuGracePeriod* \[in\]
</dt> <dd>

Overrides CheckForSignatureBeforeRunningScan. Aborts any service-initiated update if signature was updated successfully within this amount of time. Time in minutes.

</dd> <dt>

*SignatureDefinitionUpdateFileSharesSources* \[in\]
</dt> <dd>

Defines the file shares for downloading definition updates. setting allows you to configure UNC file share sources for downloading definition updates. Sources will be contacted in the order specified. The value of this setting should be entered as a pipe-separated string enumerating the definition update sources. For example: {\\\\unc1 \| \\\\unc2 }. The list is empty by default.

</dd> <dt>

*SignatureDisableUpdateOnStartupWithoutEngine* \[in\]
</dt> <dd>

When set to true, AM Service will not initiate definition update on start-up, regardless of whether an Engine is present or not.

</dd> <dt>

*SignatureFallbackOrder* \[in\]
</dt> <dd>

Define the order of sources for downloading definition updates This setting allows you to define the order in which different definition update sources should be contacted. The value of this setting should be entered as a pipe-separated string enumerating the definition update sources in order. Possible values are: 'InternalDefinitionUpdateServer' 'MicrosoftUpdateServer' 'MMPC' 'FileShares'

</dd> <dt>

*SignatureScheduleDay* \[in\]
</dt> <dd>

Indicates the day of the week in which signature updates occur. If set to zero then signature update occurs daily.

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
</dt> </dl> </dd> <dt>

*SignatureScheduleTime* \[in\]
</dt> <dd>

Specifies the time at which signature update check happens. By default the signatures are checked before the scheduled scan.

</dd> <dt>

*SignatureUpdateCatchupInterval* \[in\]
</dt> <dd>

Defines the number of days after which a catch-up signature is warranted. Works with SignatureUpdateLastChecked. 0 = no catch-up, 1 = 1 day, 2 = 2 days, etc.

</dd> <dt>

*SignatureUpdateInterval* \[in\]
</dt> <dd>

The time value is represented as the number of hours between update checks. Valid values range from 1 (every hour) to 24 (once per day).

</dd> <dt>

*MAPSReporting* \[in\]
</dt> <dd>

Join Microsoft MAPS.

<dl> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (0)
</dt> <dt>

<span id="Basic"></span><span id="basic"></span><span id="BASIC"></span>**Basic** (1)
</dt> <dt>

<span id="Advanced"></span><span id="advanced"></span><span id="ADVANCED"></span>**Advanced** (2)
</dt> </dl> </dd> <dt>

*DisablePrivacyMode* 
</dt> <dd>

Disable privacy mode.

</dd> <dt>

*RandomizeScheduleTaskTimes* \[in\]
</dt> <dd>

This setting allows you to enable or disable randomization of the scheduled scan start time and the scheduled definition update start time. This setting is used to distribute the resource impact of scanning. For example, it could be used in guest virtual machines sharing a host, to prevent multiple guest virtual machines from undertaking a disk-intensive operation at the same time.

</dd> <dt>

*DisableBehaviorMonitoring* \[in\]
</dt> <dd>

Disable behavior monitoring.

</dd> <dt>

*DisableIntrusionPreventionSystem* \[in\]
</dt> <dd>

Disable intrusion prevention system.

</dd> <dt>

*DisableIOAVProtection* \[in\]
</dt> <dd>

Disable IOAV protection.

</dd> <dt>

*DisableRealtimeMonitoring* \[in\]
</dt> <dd>

Disable real-time monitoring.

</dd> <dt>

*DisableScriptScanning* \[in\]
</dt> <dd>

Disable script scanning.

</dd> <dt>

*DisableArchiveScanning* \[in\]
</dt> <dd>

Disable archive scanning.

</dd> <dt>

*DisableCatchupFullScan* \[in\]
</dt> <dd>

Disable catch-up full scan. A catch-up scan is a scan that is initiated because a regularly scheduled scan was missed. Usually these scheduled scans are missed because the computer was turned off at the scheduled time.

</dd> <dt>

*DisableCatchupQuickScan* \[in\]
</dt> <dd>

Disable catch-up quick scan. A catch-up scan is a scan that is initiated because a regularly scheduled scan was missed. Usually these scheduled scans are missed because the computer was turned off at the scheduled time.

</dd> <dt>

*DisableEmailScanning* \[in\]
</dt> <dd>

Disable email scanning.

</dd> <dt>

*DisableRemovableDriveScanning* \[in\]
</dt> <dd>

Disable removable drive scanning.

</dd> <dt>

*DisableRestorePoint* \[in\]
</dt> <dd>

Disables restore point.

</dd> <dt>

*DisableScanningMappedNetworkDrivesForFullScan* \[in\]
</dt> <dd>

Disable running full scan on mapped network drives.

</dd> <dt>

*DisableScanningNetworkFiles* \[in\]
</dt> <dd>

Disables scanning network files.

</dd> <dt>

*UILockdown* \[in\]
</dt> <dd>

Enable UI Lockdown mode.

</dd> <dt>

*ThreatIDDefaultAction\_Ids* \[in\]
</dt> <dd>

The Ids of threats upon which default action should not be taken when detected. The actions in ThreatIDDefaultAction\_Actions need to be specified in the same order as the Ids in ThreatIDDefaultAction\_Ids

</dd> <dt>

*ThreatIDDefaultAction\_Actions* \[in\]
</dt> <dd>

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
</dt> </dl> </dd> <dt>

*UnknownThreatDefaultAction* \[in\]
</dt> <dd>

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
</dt> </dl> </dd> <dt>

*LowThreatDefaultAction* \[in\]
</dt> <dd>

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
</dt> </dl> </dd> <dt>

*ModerateThreatDefaultAction* \[in\]
</dt> <dd>

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
</dt> </dl> </dd> <dt>

*HighThreatDefaultAction* \[in\]
</dt> <dd>

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
</dt> </dl> </dd> <dt>

*SevereThreatDefaultAction* \[in\]
</dt> <dd>

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
</dt> </dl> </dd> <dt>

*Force* \[in\]
</dt> <dd>

A user confirmation is sought by default by this cmdlet. If -Force is specified, the default confirmation is not sought from the user.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Defender<br/>                                                       |
| MOF<br/>                      | <dl> <dt>ProtectionManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ProtectionManagement.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_MpPreference**](msft-mppreference.md)
</dt> </dl>

 

 





