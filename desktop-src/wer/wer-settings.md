---
title: WER Settings
description: Settings to customize the problem reporting experience. All of these settings can be set using Group Policy. Some can also be changed in Action Center for Windows 7 and Windows 8. For Windows 10, use the search function in Settings to locate View advanced system settings.
ms.assetid: 031c5591-31b0-42f1-9a98-ecf10a5d5571
keywords:
- Windows error reporting Windows Error Reporting , settings
ms.topic: article
ms.date: 03/12/2021
---

# WER Settings

Windows Error Reporting (WER) provides many settings to customize the problem reporting experience. All of these settings can be set using Group Policy. Some can also be changed in **Action Center** for Windows 7 and Windows 8. For Windows 10, use the search function in Settings to locate **View advanced system settings**. WER settings are located in one of the following registry subkeys:

-   **HKEY\_CURRENT\_USER**\\**Software**\\**Microsoft**\\**Windows**\\**Windows Error Reporting**
-   **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Windows**\\**Windows Error Reporting**

## Windows Error Reporting subkey

<dl> <dt>

<span id="BypassDataThrottling"></span><span id="bypassdatathrottling"></span><span id="BYPASSDATATHROTTLING"></span>**BypassDataThrottling**
</dt> <dd>

**REG\_DWORD**

Possible values:<dl> <dd>

0 - Disable data bypass throttling. If the bypass is disabled or not configured as a policy setting, WER throttles data by default. WER does not upload more than one CAB file for a report that contains data about the same event types.

</dd> <dd>

1 - Enable data bypass throttling. WER does not throttle data. WER uploads additional CAB files that can contain data about the same event types as an earlier uploaded report.

</dd> </dl>

Whether to enable the bypass of WER client data throttling

</dd> <dt>

<span id="ConfigureArchive"></span><span id="configurearchive"></span><span id="CONFIGUREARCHIVE"></span>**ConfigureArchive**
</dt> <dd>

**REG\_DWORD**

Possible values:<dl> <dd>1 - Parameters only (default on Windows 7)</dd> <dd>2 - All data (default on Windows Vista)</dd> </dl>

Whether to archive parameters only or all data

</dd> <dt>

<span id="Consent_DefaultConsent"></span><span id="consent_defaultconsent"></span><span id="CONSENT_DEFAULTCONSENT"></span>**Consent\\DefaultConsent**
</dt> <dd>

**REG\_DWORD**

Possible values:<dl> <dd>1 - Always ask (default)</dd> <dd>2 - Parameters only</dd> <dd>3 - Parameters and safe data</dd> <dd>4 - All data</dd> </dl>

Default consent choice

</dd> <dt>

<span id="Consent_DefaultOverrideBehavior"></span><span id="consent_defaultoverridebehavior"></span><span id="CONSENT_DEFAULTOVERRIDEBEHAVIOR"></span>**Consent\\DefaultOverrideBehavior**
</dt> <dd>

**REG\_DWORD**

Possible values:<dl> <dd>0 - Vertical consent will override the default consent (default)</dd> <dd>1 - Default consent will override the application-specific consent</dd> </dl>

Whether default consent overrides vertical consent

</dd> <dt>

<span id="Consent__VerticalName_"></span><span id="consent__verticalname_"></span><span id="CONSENT__VERTICALNAME_"></span>**Consent\\\[VerticalName\]**
</dt> <dd>

**REG\_DWORD**

Possible values:<dl> <dd>1 - Always ask (default)</dd> <dd>2 - Parameters only</dd> <dd>3 - Parameters and safe data</dd> <dd>4 - All data</dd> </dl>

Consent choice for the WER plug-in

</dd> <dt>

<span id="CorporateWERDirectory"></span><span id="corporatewerdirectory"></span><span id="CORPORATEWERDIRECTORY"></span>**CorporateWERDirectory**
</dt> <dd>

**REG\_SZ**

The directory path

Target directory on the server

</dd> <dt>

<span id="CorporateWERPortNumber"></span><span id="corporatewerportnumber"></span><span id="CORPORATEWERPORTNUMBER"></span>**CorporateWERPortNumber**
</dt> <dd>

**REG\_DWORD**

The port number

Port number to be used with the corporate server

</dd> <dt>

<span id="CorporateWERServer"></span><span id="corporatewerserver"></span><span id="CORPORATEWERSERVER"></span>**CorporateWERServer**
</dt> <dd>

**REG\_SZ**

The name of the server

Corporate server name

</dd> <dt>

<span id="CorporateWERUseAuthentication"></span><span id="corporateweruseauthentication"></span><span id="CORPORATEWERUSEAUTHENTICATION"></span>**CorporateWERUseAuthentication**
</dt> <dd>

**REG\_DWORD**

Possible values:<dl> <dd>0 - No (default)</dd> <dd>1 - Yes</dd> </dl>

Whether to use Windows Integrated Authentication

</dd> <dt>

<span id="CorporateWERUseSSL"></span><span id="corporatewerusessl"></span><span id="CORPORATEWERUSESSL"></span>**CorporateWERUseSSL**
</dt> <dd>

**REG\_DWORD**

Possible values:<dl> <dd>0 - No (default)</dd> <dd>1 - Yes</dd> </dl>

Whether to use SSL

</dd> <dt>

<span id="DebugApplications__ExeName___replace___ExeName___with_an_actual_name_of_an_.exe_file__for_example___notepad.exe__"></span><span id="debugapplications__exename___replace___exename___with_an_actual_name_of_an_.exe_file__for_example___notepad.exe__"></span><span id="DEBUGAPPLICATIONS__EXENAME___REPLACE___EXENAME___WITH_AN_ACTUAL_NAME_OF_AN_.EXE_FILE__FOR_EXAMPLE___NOTEPAD.EXE__"></span>**DebugApplications\\\[ExeName\] (replace "\[ExeName\]" with an actual name of an .exe file, for example, "notepad.exe")**
</dt> <dd>

**REG\_DWORD**

Possible values:

<dl> <dd>0 - Processes with an executable image name of **\[ExeName\]** do not require the user to choose **Debug** or **Continue** (default)</dd> <dd>1 - Processes with an executable image name of **\[ExeName\]** require the user to choose **Debug** or **Continue**</dd> </dl> </dd> <dt>

<span id="DebugApplications________is_the_literal_value_name_"></span><span id="debugapplications________is_the_literal_value_name_"></span><span id="DEBUGAPPLICATIONS________IS_THE_LITERAL_VALUE_NAME_"></span>**DebugApplications\\\* ("\*" is the literal value name)**
</dt> <dd>

**REG\_DWORD**

Possible values:

<dl> <dd>0 - All processes except ones specified explicitly in the setting **DebugApplications\\\[ExeName\]** do not require the user to choose **Debug** or **Continue** (default)</dd> <dd>1 - All processes except ones specified explicitly in the setting **DebugApplications\\\[ExeName\]** require the user to choose **Debug** or **Continue**</dd> </dl> </dd> <dt>

<span id="DisableArchive"></span><span id="disablearchive"></span><span id="DISABLEARCHIVE"></span>**DisableArchive**
</dt> <dd>

**REG\_DWORD**

Possible values:<dl> <dd>0 - Enabled</dd> <dd>1 - Disabled</dd> </dl>

Enable or disable the archive

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled**
</dt> <dd>

**REG\_DWORD**

Possible values:<dl> <dd>0 - Enabled (default)</dd> <dd>1 - Disabled</dd> </dl>

Enable or disable WER

</dd> <dt>

<span id="DisableQueue"></span><span id="disablequeue"></span><span id="DISABLEQUEUE"></span>**DisableQueue**
</dt> <dd>

**REG\_DWORD**

Possible values:<dl> <dd>0 - Enabled</dd> <dd>1 - Disabled</dd> </dl>

Enable or disable report queuing

</dd> <dt>

<span id="DontShowUI"></span><span id="dontshowui"></span><span id="DONTSHOWUI"></span>**DontShowUI**
</dt> <dd>

**REG\_DWORD**

Possible values:<dl> <dd>0 - UI (default)</dd> <dd>1 - No UI</dd> </dl>

Enable or disable the WER UI

</dd> <dt>

<span id="DontSendAdditionalData"></span><span id="dontsendadditionaldata"></span><span id="DONTSENDADDITIONALDATA"></span>**DontSendAdditionalData**
</dt> <dd>

**REG\_DWORD**

Possible values:<dl> <dd>0 - Send (default)</dd> <dd>1 - Do not send</dd> </dl>

Whether to prevent sending second-level data

</dd> <dt>

<span id="ExcludedApplications__Application_Name_"></span><span id="excludedapplications__application_name_"></span><span id="EXCLUDEDAPPLICATIONS__APPLICATION_NAME_"></span>**ExcludedApplications\\\[Application Name\]**
</dt> <dd>

**REG\_SZ**

Use [**WerAddExcludedApplication**](/windows/desktop/api/Werapi/nf-werapi-weraddexcludedapplication)

List of excluded applications

</dd> <dt>

<span id="ForceQueue"></span><span id="forcequeue"></span><span id="FORCEQUEUE"></span>**ForceQueue**
</dt> <dd>

**REG\_DWORD**

Possible values:<dl> <dd>0 - No (default)</dd> <dd>1 - Yes</dd> </dl>

Whether to send all reports to the user's queue

</dd> <dt>

<span id="LocalDumps_DumpFolder_or_LocalDumps__Application_Name__DumpFolder"></span><span id="localdumps_dumpfolder_or_localdumps__application_name__dumpfolder"></span><span id="LOCALDUMPS_DUMPFOLDER_OR_LOCALDUMPS__APPLICATION_NAME__DUMPFOLDER"></span>**LocalDumps\\DumpFolder** or **LocalDumps\\\[Application Name\]\\DumpFolder**
</dt> <dd>

**REG\_EXPAND\_SZ**

The directory path. The default value is %LOCALAPPDATA%\\CrashDumps. If the default is not used, the application must ensure that the folder has a sufficient ACL.

**Windows Vista:** The registry values under the **LocalDumps** key are not supported. Note that this behavior changed with Windows Server 2008 and Windows Vista with Service Pack 1 (SP1).

The path where the dump files are to be stored.

Note that per-process settings will override any global settings that exist For more information, see [Collecting User-Mode Dumps](collecting-user-mode-dumps.md).

This setting is not supported in the **HKEY\_CURRENT\_USER** registry hive.

</dd> <dt>

<span id="LocalDumps_DumpCount_or_LocalDumps__Application_Name__DumpCount"></span><span id="localdumps_dumpcount_or_localdumps__application_name__dumpcount"></span><span id="LOCALDUMPS_DUMPCOUNT_OR_LOCALDUMPS__APPLICATION_NAME__DUMPCOUNT"></span>**LocalDumps\\DumpCount** or **LocalDumps\\\[Application Name\]\\DumpCount**
</dt> <dd>

**REG\_DWORD**

The maximum number. The default is 10. When the maximum value is exceeded, the oldest dump file in the folder will be replaced with the new dump file.

**Windows Vista:** The registry values under the **LocalDumps** key are not supported. Note that this behavior changed with Windows Server 2008 and Windows Vista with SP1.

The maximum number of dump files in the folder.

This setting is not supported in the **HKEY\_CURRENT\_USER** registry hive.

</dd> <dt>

<span id="LocalDumps_DumpType_or_LocalDumps__Application_Name__DumpType"></span><span id="localdumps_dumptype_or_localdumps__application_name__dumptype"></span><span id="LOCALDUMPS_DUMPTYPE_OR_LOCALDUMPS__APPLICATION_NAME__DUMPTYPE"></span>**LocalDumps\\DumpType** or **LocalDumps\\\[Application Name\]\\DumpType**
</dt> <dd>

**REG\_DWORD**

Possible values:<dl> <dd>0 - Custom dump</dd> <dd>1 - Minidump (default)</dd> <dd>2 - Full dump</dd> </dl>

**Windows Vista:** The registry values under the **LocalDumps** key are not supported. Note that this behavior changed with Windows Server 2008 and Windows Vista with SP1.

The dump type.

This setting is not supported in the **HKEY\_CURRENT\_USER** registry hive.

</dd> <dt>

<span id="LocalDumps_CustomDumpFlags_or_LocalDumps__Application_Name__CustomDumpFlags"></span><span id="localdumps_customdumpflags_or_localdumps__application_name__customdumpflags"></span><span id="LOCALDUMPS_CUSTOMDUMPFLAGS_OR_LOCALDUMPS__APPLICATION_NAME__CUSTOMDUMPFLAGS"></span>**LocalDumps\\CustomDumpFlags** or **LocalDumps\\\[Application Name\]\\CustomDumpFlags**
</dt> <dd>

**REG\_DWORD**

One or more values from the [**MINIDUMP\_TYPE**](/windows/desktop/api/minidumpapiset/ne-minidumpapiset-minidump_type) enumeration. The default is {**MiniDumpWithDataSegs**\|**MiniDumpWithUnloadedModules**\|**MiniDumpWithProcessThreadData**}.

**Windows Vista:** The registry values under the **LocalDumps** key are not supported. Note that this behavior changed with Windows Server 2008 and Windows Vista with SP1.

The custom dump options to be used. This value is used only when **DumpType** is set to 0.

This setting is not supported in the **HKEY\_CURRENT\_USER** registry hive.

</dd> <dt>

<span id="LoggingDisabled"></span><span id="loggingdisabled"></span><span id="LOGGINGDISABLED"></span>**LoggingDisabled**
</dt> <dd>

**REG\_DWORD**

Possible values:<dl> <dd>0–Enabled (default)</dd> <dd>1–Disabled</dd> </dl>

Enable or disable logging

</dd> <dt>

<span id="MaxArchiveCount"></span><span id="maxarchivecount"></span><span id="MAXARCHIVECOUNT"></span>**MaxArchiveCount**
</dt> <dd>

**REG\_DWORD**

Range of possible values: 1–5000. The default is 1000.

Maximum size of the archive, in files

</dd> <dt>

<span id="MaxQueueCount"></span><span id="maxqueuecount"></span><span id="MAXQUEUECOUNT"></span>**MaxQueueCount**
</dt> <dd>

**REG\_DWORD**

Range of possible values: 1–500. The default is 50.

Maximum size of the queue

</dd> <dt>

<span id="QueuePesterInterval"></span><span id="queuepesterinterval"></span><span id="QUEUEPESTERINTERVAL"></span>**QueuePesterInterval**
</dt> <dd>

**REG\_DWORD**

Number of days

Interval between reminders to the user to check for solutions, in days

</dd> <dt>

<span id="RuntimeExceptionHelperModules___pwszOutOfProcessCallbackDll_name_including_path_"></span><span id="runtimeexceptionhelpermodules___pwszoutofprocesscallbackdll_name_including_path_"></span><span id="RUNTIMEEXCEPTIONHELPERMODULES___PWSZOUTOFPROCESSCALLBACKDLL_NAME_INCLUDING_PATH_"></span>**RuntimeExceptionHelperModules!\[ pwszOutOfProcessCallbackDll name including path\]**
</dt> <dd>

**REG\_DWORD**

The contents of the value are ignored.

The name of the value is used to fetch the pwszOutOfProcessCallbackDll value.

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This registry value is not supported.

</dd> </dl>

## WER Live Kernel Reports Settings

WER's Live Kernel Reports settings, which are described next, are both located under the following registry subkey:

-   **HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**CrashControl**

## FullLiveKernelReports subkey

<dl> <dt>

<span id="ComponentThrottleThreshold"></span><span id="componentthrottlethreshold"></span><span id="COMPONENTTHROTTLETHRESHOLD"></span>**ComponentThrottleThreshold**
</dt> <dd>

**REG\_DWORD**

The threshold (in hours) of how often any single component can create a full live dump. This value must be greater than or equal to **SystemThrottleThreshold**. Setting both to zero (0) will disable all time-based throttling. The default is 168 (7 days).

</dd> <dt>

<span id="FullLiveReportsMax"></span><span id="fulllivereportsmax"></span><span id="FULLLIVEREPORTSMAX"></span>**FullLiveReportsMax**
</dt> <dd>

**REG\_DWORD**

The maximum number of full live dumps that may be on disk at any given time. The default is 1. Setting this value to zero (0) will disable the live dump feature.

</dd> <dt>

<span id="LastFullLiveReport"></span><span id="lastfulllivereport"></span><span id="LASTFULLLIVEREPORT"></span>**LastFullLiveReport**
</dt> <dd>

**REG\_QWORD**

A [SystemTime](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) indicating the last full live report time, for the system or a specific ReportType. This is used to calculate whether a policy threshold has been satisfied.

</dd> <dt>

<span id="SystemThrottleThreshold"></span><span id="systemthrottlethreshold"></span><span id="SYSTEMTHROTTLETHRESHOLD"></span>**SystemThrottleThreshold**
</dt> <dd>

**REG\_DWORD**

The threshold (in hours) of how often any component on the system can create a full live dump. The default is 120 (5 days).

</dd> </dl>

## LiveKernelReports subkey

<dl> <dt>

<span id="LiveKernelReportsPath"></span><span id="livekernelreportspath"></span><span id="LIVEKERNELREPORTSPATH"></span>**LiveKernelReportsPath**
</dt> <dd>

**REG\_SZ**


The redirected storage location of live kernel reports. The default location is %systemroot%\LiveKernelReports. This value must be a valid path. The path must be in NT path format. For example, \??\C:\LiveDumpsFolder.  For more information on path formats, see  [File path formats on Windows systems](/dotnet/standard/io/file-path-formats).

</dd> </dl>

## Related topics

<dl> <dt>

[WER Reference](wer-reference.md)
</dt> </dl>

 

 
