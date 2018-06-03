---
title: Properties element
description: This element describes assessment properties.
ms.assetid: B9648DC5-D829-47D4-93B6-2EBC9DB31CEE
keywords:
- Properties element Access Execution Engine
topic_type:
- apiref
api_name:
- Properties
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Properties element

This element describes assessment properties.

## Usage

``` syntax
<Properties>
  child elements
</Properties>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                                           | Description                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Author**](author.md)<br/>                                               | The author of the assessment.<br/> <br/>                                                                                                                                            |
| [**AuthorUrl**](authorurl.md)<br/>                                         | This URL refers to the main web site or page for the Assessment s author.<br/> <br/>                                                                                                |
| [**AVOffWarn**](avoffwarn.md)<br/>                                         | If present then this assessment prefers to have anti-virus software installed and enabled.<br/> <br/>                                                                               |
| [**BasicDisplayBlock**](basicdisplayblock.md)<br/>                         | If present then the operating system must not be using the basic display device driver.<br/> <br/>                                                                                  |
| [**BasicDisplayWarn**](basicdisplaywarn.md)<br/>                           | If present then this assessment performs better with a display device driver that is specific to the installed graphics hardware.<br/> <br/>                                        |
| [**BestPractices**](https://msdn.microsoft.com/library/windows/desktop/hh449345)<br/>                                 | The best ways to use a particular assessment. <br/> <br/>                                                                                                                           |
| [**CheckForProcess**](checkforprocess.md)<br/>                             | Identifies a process that should not or cannot be running when an assessment begins.<br/> <br/>                                                                                     |
| [**ConnectedStandbyDisabledBlock**](connectedstandbydisabledblock.md)<br/> | Connected standby idle periods cannot be disabled.<br/> <br/>                                                                                                                       |
| [**Copyright**](copyright.md)<br/>                                         | This is the copyright string.<br/> <br/>                                                                                                                                            |
| [**Details**](details.md)<br/>                                             | This node describes the Author of an assessment. This could be a person or a company.<br/> <br/>                                                                                    |
| [**DriverVerifierWarn**](driververifierwarn.md)<br/>                       | If present then this assessment prefers that Driver Verifier is not enabled on the system.<br/> <br/>                                                                               |
| [**EstimatedRunTime**](estimatedruntime.md)<br/>                           | Describes the estimated run time of the assessment. <br/> <br/>                                                                                                                     |
| [**EventTracing**](eventtracing.md)<br/>                                   | Specifies a configuration for the use of Event Tracing for Windows (ETW) by AXE.<br/> <br/>                                                                                         |
| [**ExitValueMeaning**](exitvaluemeaning.md)<br/>                           | Indicates whether the exit value means success or is a **HRESULT**.<br/> <br/>                                                                                                      |
| [**HibernateDisabledBlock**](hibernatedisabledblock.md)<br/>               | If present then the operating system must be configured to allow the system to go into hibernation.<br/> <br/>                                                                      |
| [**IconResource**](iconresource.md)<br/>                                   | Name of the icon that represents the assessment.<br/> <br/>                                                                                                                         |
| [**JobKind**](jobkind.md)<br/>                                             | This node contains the job kind enumeration.<br/> <br/>                                                                                                                             |
| [**KernelDebuggerWarn**](kerneldebuggerwarn.md)<br/>                       | If present then the results or behavior of this assessment may be adversely affected if the operating system is configured to support a kernel debugger.<br/> <br/>                 |
| [**LastSavedId**](lastsavedid.md)<br/>                                     | When AXE saves a job (at the behest of a solution) it will give the job a new &lt;LastSaved&gt; ID. <br/> <br/>                                                                     |
| [**LastSavedTimeAndDate**](lastsavedtimeanddate.md)<br/>                   | Last date and time a solution saved the manifest to a file. <br/> <br/>                                                                                                             |
| [**License**](https://msdn.microsoft.com/library/windows/desktop/hh449386)<br/>                                             | This is text that describes license associated with the assessment.<br/> <br/>                                                                                                      |
| [**LockOnWakeBlock**](lockonwakeblock.md)<br/>                             | If present then the operating system must not be configured to prompt for a password when the system wakes from sleep or hibernation when on DC power.<br/> <br/>                   |
| [**MayEmptyRecycleBin**](mayemptyrecyclebininfo.md)<br/>                   | If present then the user is notified that the assessment may empty the contents of the Recycle Bin.<br/> <br/>                                                                      |
| [**MayRebootSystem**](mayrebootsystem.md)<br/>                             | If present then this assessment may reboot the system.<br/> <br/>                                                                                                                   |
| [**NoInteractionInfo**](nointeractioninfo.md)<br/>                         | If present then the user is instructed not to interact with the system while the assessment is running.<br/> <br/>                                                                  |
| [**OnlyForProcessor**](onlyforprocessor.md)<br/>                           | Indicates the platforms on which the assessment should run.<br/> <br/>                                                                                                              |
| [**PowerProfileNotBalancedWarn**](powerprofilenotbalancedwarn.md)<br/>     | If present then this assessment prefers to have the power profile set to one that is classified as "Balanced".<br/> <br/>                                                           |
| [**ProblemDevicesWarn**](problemdeviceswarn.md)<br/>                       | If present then if any devices in the system have an issue, a warning will be generated.<br/> <br/>                                                                                 |
| [**ProcessIdleTasks**](processidletasks.md)<br/>                           | Requests the system run the maintenance tasks scheduled to run when the system is idle. This prevents the maintenance tasks from running during the assessment.<br/> <br/>          |
| [**RequiresACPower**](requiresacpower.md)<br/>                             | If present then this assessment requires AC power.<br/> <br/>                                                                                                                       |
| [**RequiresACPowerWarn**](requiresacpowerwarn.md)<br/>                     | If present then this assessment prefers AC power, but it can run on DC power.<br/> <br/>                                                                                            |
| [**RequiresAppVersions**](requiresappversions.md)<br/>                     | The minimum version of an application required to be installed on the system.<br/> <br/>                                                                                            |
| [**RequiresAudioRenderDeviceWarn**](requiresaudiorenderdevicewarn.md)<br/> | If present then this assessment prefers that the system contains a hardware device for playing audio.<br/> <br/>                                                                    |
| [**RequiresAutoLogOnBlock**](requiresautologonblock.md)<br/>               | f present then the operating system must be configured to log on automatically.<br/> <br/>                                                                                          |
| [**RequiresAutoLogOnWarn**](requiresautologonwarn.md)<br/>                 | If present then this assessment prefers that the operating system is configured to automatically log on. The assessment may reboot the system.<br/> <br/>                           |
| [**RequiresBattery**](requiresbattery.md)<br/>                             | If present then this assessment should only run on a system that has a battery.<br/> <br/>                                                                                          |
| [**RequiresDisplay**](requiresdisplay.md)<br/>                             | The assessment must be displayed.<br/> <br/>                                                                                                                                        |
| [**RequiresElevation**](requireselevation.md)<br/>                         | If this node is present, it means that the assessment requires administrator privileges.<br/> <br/>                                                                                 |
| [**RequiresExecution**](requiresexecution.md)<br/>                         | The assessment must be executed.<br/> <br/>                                                                                                                                         |
| [**RequiresInternet**](requiresinternet.md)<br/>                           | If present this assessment requires an working internet connection.<br/> <br/>                                                                                                      |
| [**RequiresNoExecution**](requiresnoexecution.md)<br/>                     | The assessment need not be executed.<br/> <br/>                                                                                                                                     |
| [**RequiresTracing**](requirestracing.md)<br/>                             | f present then no system tracing can be running prior to the assessment running.<br/> <br/>                                                                                         |
| [**RequiresTracingWarn**](requirestracingwarn.md)<br/>                     | If present then the results of this assessment may be adversely affected if tracing session exists prior to this assessment running.<br/> <br/>                                     |
| [**RequiresWindowsGenuineWarn**](requireswindowsgenuinewarn.md)<br/>       | The assessment may be adversely affected if the warning message about Windows being genuine is displayed.<br/> <br/>                                                                |
| [**ScreensaverPasswordWarn**](screensaverpasswordwarn.md)<br/>             | If present then this assessment prefers that the screen saver is not configured to display the log on screen when the screen resumes.<br/> <br/>                                    |
| [**ShouldRunSilent**](shouldrunsilent.md)<br/>                             | If this node is present, then the assessment should run without any progress UX or other visible harness level UX.<br/> <br/>                                                       |
| [**SupportsRunningRemote**](supportsrunningremote.md)<br/>                 | The assessment can be run remotely.<br/> <br/>                                                                                                                                      |
| [**SupportsWindowsPE**](supportswindowspe.md)<br/>                         | If present this assessment can run in Windows PE. <br/> <br/>                                                                                                                       |
| [**SystemDiskLegacyModeWarn**](systemdisklegacymodewarn.md)<br/>           | If present then the results of this assessment may be adversely affected if the hard drive that the operating system uses as the system drive is configured in PIO mode.<br/> <br/> |
| [**UpdateUrl**](updateurl.md)<br/>                                         | This is URL that refers to a location that solution can use to check for an update to the assessment. <br/> <br/>                                                                   |
| [**Url**](url.md)<br/>                                                     | This is URL that refers to a web page about the assessment.<br/> <br/>                                                                                                              |
| [**VerifyOSVersion**](verifyosversion.md)<br/>                             | Describes the minimum Windows version required for this assessment.<br/> <br/>                                                                                                      |
| [**VersionNote**](versionnote.md)<br/>                                     | This element contains a note that is associated with the version of this assessment. <br/> <br/>                                                                                    |
| [**WatchDogTimeOut**](watchdogtimeout.md)<br/>                             | Describes when a solution should cancel or terminate an assessment.<br/> <br/>                                                                                                      |
| [**WirelessDisconnectedWarn**](wirelessdisconnectedwarn.md)<br/>           | If present then this assessment prefers to have the wireless networking hardware enabled and connected to a wireless network.<br/> <br/>                                            |



### Child element sequence

``` syntax
(
  LastSavedTimeAndDate, 
  LastSavedId, 
  VersionNote, 
  Details, 
  Url, 
  Author, 
  AuthorUrl, 
  UpdateUrl, 
  Copyright, 
  SupportsWindowsPE, 
  RequiresInternet, 
  ExitValueMeaning, 
  EstimatedRunTime, 
  WatchDogTimeOut, 
  JobKind, 
  VerifyOSVersion, 
  OnlyForProcessor, 
  RequiresACPower, 
  RequiresBattery, 
  RequiresElevation, 
  BasicDisplayBlock, 
  LockOnWakeBlock, 
  HibernateDisabledBlock, 
  RequiresAutoLogOnBlock, 
  RequiresTracing, 
  RequiresACPowerWarn, 
  BasicDisplayWarn, 
  WirelessDisconnectedWarn, 
  AVOffWarn, 
  PowerProfileNotBalancedWarn, 
  RequiresAutoLogOnWarn, 
  KernelDebuggerWarn, 
  DriverVerifierWarn, 
  SystemDiskLegacyModeWarn, 
  ProblemDevicesWarn, 
  ScreensaverPasswordWarn, 
  RequiresTracingWarn, 
  RequiresAudioRenderDeviceWarn, 
  MayRebootSystem, 
  ShouldRunSilent, 
  NoInteractionInfo, 
  MayEmptyRecycleBin, 
  RequiresAppVersions, 
  CheckForProcess, 
  IconResource, 
  EventTracing, 
  License, 
  BestPractices, 
  ConnectedStandbyDisabledBlock, 
  ProcessIdleTasks
, 
  RequiresDisplay
, 
  RequiresExecution
, 
  RequiresNoExecution
, 
  RequiresWindowsGenuineWarn
, 
  SupportsRunningRemote
)
```

## Parent elements



| Element                                                           | Description                                                             |
|-------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**AssessmentManifest**](https://msdn.microsoft.com/library/windows/desktop/hh449288)<br/>       | The root node of the assessment.<br/> <br/>                 |
| [**AxeAssessmentManifest**](axeassessmentmanifest.md)<br/> | This is the root node of an assessment manifest.<br/> <br/> |
| [**AxeJobManifest**](axejobmanifest.md)<br/>               | Name of the root node of the assessment.<br/> <br/>         |



## Remarks

As a solution assembles a job, the assessment management API s will check some of properties for consistency   returning warnings to the solution as appropriate.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> </dl>

 

 





