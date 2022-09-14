---
description: Winmgmt is the WMI service within the SVCHOST process running under the &\#0034;LocalSystem&\#0034; account.
ms.assetid: 3923322a-3acb-407e-8a07-09c59d252e8b
ms.tgt_platform: multiple
title: winmgmt
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- winmgmt
api_type: 
- NA
api_location: 
---

# winmgmt

Winmgmt is the WMI service within the SVCHOST process running under the "LocalSystem" account.

In all cases, the WMI service automatically starts when the first management application or script requests connection to a WMI namespace. For more information, see [Starting and Stopping the WMI Service](starting-and-stopping-the-wmi-service.md).

> [!Note]  
> WMI is a core component of the Windows operating system that allows developers and IT administrators to write scripts and applications to automate certain tasks. Winmgmt.exe is the service that allows WMI to run on your local computer. For more information on using WMI, see [Using WMI](using-wmi.md). If you have received an error message regarding winmgmt.exe, see [WMI Troubleshooting](wmi-troubleshooting.md). For more information on Winmgmt.exe, see [Using WMI Management Tools](/previous-versions/system-center/configuration-manager-2003/cc180468(v=technet.10)).

 

When run from the command prompt, the WMI service has the following switches.

``` syntax
winmgmt 
  [/backup <filename>] 
  [/restore <filename> <mode>] 
  [/resyncperf <winmgmt service process id>] 
  [/standalonehost <level>]
  [/sharedhost]
  [/verifyrepository <path>]
  [/salvagerepository] 
  [/resetrepository]
```

## Switches

<dl> <dt>

<span id="__________backup__filename_________"></span><span id="__________BACKUP__FILENAME_________"></span> **/backup** *&lt;filename&gt;* 
</dt> <dd>

Causes WMI to back up the repository to the specified file name. The *filename* argument should contain the full path to the file location. This process requires a write lock on the repository so that write operations to the repository are suspended until the backup process is completed.

If you do not specify a path for the file, it is put in the %Windir%\\System32 directory.

</dd> <dt>

<span id="__________restore__filename____flag_____"></span><span id="__________RESTORE__FILENAME____FLAG_____"></span> **/restore** *&lt;filename&gt;* *&lt;flag&gt;* 
</dt> <dd>

Manually restores the WMI repository from the specified backup file. The *filename* argument should contain the full path to the backup file location. To perform the restore operation, WMI saves the existing repository to write back if the operation fails. Then the repository is restored from the backup file that is specified in the *filename* argument. If exclusive access to the repository cannot be achieved, existing clients are disconnected from WMI.

The *flag* argument must be a 1 (force   disconnect users and restore) or 0 (default   restore if no users connected) and specifies the restore mode.

</dd> <dt>

<span id="__________resyncperf__winmgmt-service-process-id_____"></span><span id="__________RESYNCPERF__WINMGMT-SERVICE-PROCESS-ID_____"></span> **/resyncperf** *&lt;winmgmt-service-process-id&gt;* 
</dt> <dd>

Registers the computer's performance libraries with WMI. WMI PID is the process ID for the WMI service.

Only needed if the performance monitor classes are not returning reliable results.

</dd> <dt>

<span id="_standalonehost__level_"></span><span id="_STANDALONEHOST__LEVEL_"></span>**/standalonehost** \[*&lt;level&gt;*\]
</dt> <dd>

Moves the Winmgmt service to a standalone Svchost process that has a fixed DCOM endpoint. The default endpoint is "ncacn\_ip\_tcp.0.24158". However, the endpoint may be changed by running Dcomcnfg.exe. For more information about setting up a fixed port for WMI, see [Setting Up a Fixed Port for WMI](setting-up-a-fixed-port-for-wmi.md).

The *level* argument is the authentication level for the Svchost process. WMI normally runs as part of a shared service host and you cannot increase the authentication level for WMI alone. If *level* is not specified, the default is 4 (**RPC\_C\_AUTHN\_LEVEL\_PKT** or **WbemAuthenticationLevelPkt**).

You can run WMI more securely by increasing the authentication level to Packet Privacy (**RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY** or **WbemAuthenticationLevelPktPrivacy**). The authentication levels for Visual Basic and scripting are described in [**WbemAuthenticationLevelEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemauthenticationlevelenum). For C++, see [Setting the Default Process Security Level Using C++](setting-the-default-process-security-level-using-c-.md). For more information, see [Maintaining WMI Security](maintaining-wmi-security.md).

</dd> <dt>

<span id="_sharedhost"></span><span id="_SHAREDHOST"></span>**/sharedhost**
</dt> <dd>

Moves the Winmgmt service into the shared Svchost process.

</dd> <dt>

<span id="__________verifyrepository__path_____"></span><span id="__________VERIFYREPOSITORY__PATH_____"></span> **/verifyrepository** *&lt;path&gt;* 
</dt> <dd>

Performs a consistency check on the WMI repository. When you add the **/verifyrepository** switch without the *&lt;path&gt;* argument, then the live repository currently used by WMI is verified. When you specify the *path* argument, you can verify any saved copy of the repository. In this case, the path argument should contain the full path to the saved repository copy. The saved repository should be a copy of the entire repository folder. For more information about errors returned by this command, see the Remarks section.

</dd> <dt>

<span id="_salvagerepository"></span><span id="_SALVAGEREPOSITORY"></span>**/salvagerepository**
</dt> <dd>

Performs a consistency check on the WMI repository, and if an inconsistency is detected, rebuilds the repository. The content of the inconsistent repository is merged into the rebuilt repository, if it can be read. The salvage operation always works with the repository that the WMI service is currently using. For more information about errors returned by this command, see the Remarks section.

% MOF files that contain the [**\#pragma autorecover**](pragma-autorecover.md) preprocessor statement are restored to the repository.

</dd> <dt>

<span id="_resetrepository"></span><span id="_RESETREPOSITORY"></span>**/resetrepository**
</dt> <dd>

The repository is reset to the initial state when the operating system is first installed. MOF files that contain the [**\#pragma autorecover**](pragma-autorecover.md) preprocessor statement are restored to the repository.

</dd> </dl>

## Remarks

This tool is located in the %Windir%\\System32\\wbem directory. For a list of the available switches, type `WinMgmt /?` at the command prompt.

The WMI repository, also known as the CIM repository, is not just a single file, but a collection of files within the Repository folder that work together as a database. When you use the **/backup** switch to backup the repository, the resulting backup is a single compressed file.

WMI returns the error **ERROR\_INTERNAL\_DB\_CORRUPTION** (net helpmsg 1358) if a verification operation indicates that the repository is not in a consistent state. This error can be returned from any command which performs repository verification, such as **/verifyrepository** or **/salvagerepository**.

> [!Note]
>
> If WMI returns error messages, be aware that they may not indicate problems in the WMI service or in WMI providers. Failures can originate in other parts of the operating system and emerge as errors through WMI. Under any circumstances, do not delete the WMI repository as a first action because deleting the repository can cause damage to the system or to installed applications.
>
> For more information about the source of the problem, download and run the [WMI Diagnosis Utility](https://www.microsoft.com/downloads/en/details.aspx?familyid=d7ba3cd6-18d1-4d05-b11e-4c64192ae97d&displaylang=en) diagnostic command line tool. This tool produces a report that can usually isolate the source of the problem and provide instructions on how to fix it. The report also aids Microsoft support services in assisting you. You can download the [WMI Diagnosis Utility](https://www.microsoft.com/downloads/details.aspx?FamilyID=d7ba3cd6-18d1-4d05-b11e-4c64192ae97d).

 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[WMI Troubleshooting](wmi-troubleshooting.md)
</dt> <dt>

[Connecting to WMI Remotely Starting with Vista](connecting-to-wmi-remotely-starting-with-vista.md)
</dt> </dl>

 

