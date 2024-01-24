---
description: The shutdown reason codes are used by the ExitWindowsEx and InitiateSystemShutdownEx functions in the dwReason parameter. A maximum of MAX\_NUM\_REASONS reason codes will be processed by the system. MAX\_NUM\_REASONS is defined in reason.h.
ms.assetid: db1ecee0-40eb-4761-b5d8-9cc3c1c98cdf
title: System Shutdown Reason Codes (Reason.h)
ms.topic: reference
ms.date: 05/31/2018
---

# System Shutdown Reason Codes

The shutdown reason codes are used by the [**ExitWindowsEx**](/windows/desktop/api/Winuser/nf-winuser-exitwindowsex) and [**InitiateSystemShutdownEx**](/windows/desktop/api/Winreg/nf-winreg-initiatesystemshutdownexa) functions in the *dwReason* parameter.

A maximum of MAX\_NUM\_REASONS reason codes will be processed by the system. MAX\_NUM\_REASONS is defined in reason.h.

The following are the major reason flags. They indicate the general issue type.



| Constant/value                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                        |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SHTDN_REASON_MAJOR_APPLICATION"></span><span id="shtdn_reason_major_application"></span><dl> <dt>**SHTDN\_REASON\_MAJOR\_APPLICATION**</dt> <dt>0x00040000</dt> </dl>             | Application issue.<br/>                                                                                                                                      |
| <span id="SHTDN_REASON_MAJOR_HARDWARE"></span><span id="shtdn_reason_major_hardware"></span><dl> <dt>**SHTDN\_REASON\_MAJOR\_HARDWARE**</dt> <dt>0x00010000</dt> </dl>                      | Hardware issue.<br/>                                                                                                                                         |
| <span id="SHTDN_REASON_MAJOR_LEGACY_API"></span><span id="shtdn_reason_major_legacy_api"></span><dl> <dt>**SHTDN\_REASON\_MAJOR\_LEGACY\_API**</dt> <dt>0x00070000</dt> </dl>               | The [**InitiateSystemShutdown**](/windows/desktop/api/Winreg/nf-winreg-initiatesystemshutdowna) function was used instead of [**InitiateSystemShutdownEx**](/windows/desktop/api/Winreg/nf-winreg-initiatesystemshutdownexa).<br/> |
| <span id="SHTDN_REASON_MAJOR_OPERATINGSYSTEM"></span><span id="shtdn_reason_major_operatingsystem"></span><dl> <dt>**SHTDN\_REASON\_MAJOR\_OPERATINGSYSTEM**</dt> <dt>0x00020000</dt> </dl> | Operating system issue.<br/>                                                                                                                                 |
| <span id="SHTDN_REASON_MAJOR_OTHER"></span><span id="shtdn_reason_major_other"></span><dl> <dt>**SHTDN\_REASON\_MAJOR\_OTHER**</dt> <dt>0x00000000</dt> </dl>                               | Other issue.<br/>                                                                                                                                            |
| <span id="SHTDN_REASON_MAJOR_POWER"></span><span id="shtdn_reason_major_power"></span><dl> <dt>**SHTDN\_REASON\_MAJOR\_POWER**</dt> <dt>0x00060000</dt> </dl>                               | Power failure.<br/>                                                                                                                                          |
| <span id="SHTDN_REASON_MAJOR_SOFTWARE"></span><span id="shtdn_reason_major_software"></span><dl> <dt>**SHTDN\_REASON\_MAJOR\_SOFTWARE**</dt> <dt>0x00030000</dt> </dl>                      | Software issue.<br/>                                                                                                                                         |
| <span id="SHTDN_REASON_MAJOR_SYSTEM"></span><span id="shtdn_reason_major_system"></span><dl> <dt>**SHTDN\_REASON\_MAJOR\_SYSTEM**</dt> <dt>0x00050000</dt> </dl>                            | System failure.<br/>                                                                                                                                         |



The following are the minor reason flags. They modify the specified major reason flag. You can use any minor reason in conjunction with any major reason, but some combinations do not make sense.



| Constant/value                                                                                                                                                                                                                                                                                                    | Description                               |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------|
| <span id="SHTDN_REASON_MINOR_BLUESCREEN"></span><span id="shtdn_reason_minor_bluescreen"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_BLUESCREEN**</dt> <dt>0x0000000F</dt> </dl>                                   | Blue screen crash event.<br/>       |
| <span id="SHTDN_REASON_MINOR_CORDUNPLUGGED"></span><span id="shtdn_reason_minor_cordunplugged"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_CORDUNPLUGGED**</dt> <dt>0x0000000b</dt> </dl>                          | Unplugged.<br/>                     |
| <span id="SHTDN_REASON_MINOR_DISK"></span><span id="shtdn_reason_minor_disk"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_DISK**</dt> <dt>0x00000007</dt> </dl>                                                     | Disk.<br/>                          |
| <span id="SHTDN_REASON_MINOR_ENVIRONMENT"></span><span id="shtdn_reason_minor_environment"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_ENVIRONMENT**</dt> <dt>0x0000000c</dt> </dl>                                | Environment.<br/>                   |
| <span id="SHTDN_REASON_MINOR_HARDWARE_DRIVER"></span><span id="shtdn_reason_minor_hardware_driver"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_HARDWARE\_DRIVER**</dt> <dt>0x0000000d</dt> </dl>                   | Driver.<br/>                        |
| <span id="SHTDN_REASON_MINOR_HOTFIX"></span><span id="shtdn_reason_minor_hotfix"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_HOTFIX**</dt> <dt>0x00000011</dt> </dl>                                               | Hot fix.<br/>                       |
| <span id="SHTDN_REASON_MINOR_HOTFIX_UNINSTALL"></span><span id="shtdn_reason_minor_hotfix_uninstall"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_HOTFIX\_UNINSTALL**</dt> <dt>0x00000017</dt> </dl>                | Hot fix uninstallation.<br/>        |
| <span id="SHTDN_REASON_MINOR_HUNG"></span><span id="shtdn_reason_minor_hung"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_HUNG**</dt> <dt>0x00000005</dt> </dl>                                                     | Unresponsive.<br/>                  |
| <span id="SHTDN_REASON_MINOR_INSTALLATION"></span><span id="shtdn_reason_minor_installation"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_INSTALLATION**</dt> <dt>0x00000002</dt> </dl>                             | Installation.<br/>                  |
| <span id="SHTDN_REASON_MINOR_MAINTENANCE"></span><span id="shtdn_reason_minor_maintenance"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_MAINTENANCE**</dt> <dt>0x00000001</dt> </dl>                                | Maintenance.<br/>                   |
| <span id="SHTDN_REASON_MINOR_MMC"></span><span id="shtdn_reason_minor_mmc"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_MMC**</dt> <dt>0x00000019</dt> </dl>                                                        | MMC issue.<br/>                     |
| <span id="SHTDN_REASON_MINOR_NETWORK_CONNECTIVITY"></span><span id="shtdn_reason_minor_network_connectivity"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_NETWORK\_CONNECTIVITY**</dt> <dt>0x00000014</dt> </dl>    | Network connectivity.<br/>          |
| <span id="SHTDN_REASON_MINOR_NETWORKCARD"></span><span id="shtdn_reason_minor_networkcard"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_NETWORKCARD**</dt> <dt>0x00000009</dt> </dl>                                | Network card.<br/>                  |
| <span id="SHTDN_REASON_MINOR_OTHER"></span><span id="shtdn_reason_minor_other"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_OTHER**</dt> <dt>0x00000000</dt> </dl>                                                  | Other issue.<br/>                   |
| <span id="SHTDN_REASON_MINOR_OTHERDRIVER"></span><span id="shtdn_reason_minor_otherdriver"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_OTHERDRIVER**</dt> <dt>0x0000000e</dt> </dl>                                | Other driver event.<br/>            |
| <span id="SHTDN_REASON_MINOR_POWER_SUPPLY"></span><span id="shtdn_reason_minor_power_supply"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_POWER\_SUPPLY**</dt> <dt>0x0000000a</dt> </dl>                            | Power supply.<br/>                  |
| <span id="SHTDN_REASON_MINOR_PROCESSOR"></span><span id="shtdn_reason_minor_processor"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_PROCESSOR**</dt> <dt>0x00000008</dt> </dl>                                      | Processor.<br/>                     |
| <span id="SHTDN_REASON_MINOR_RECONFIG"></span><span id="shtdn_reason_minor_reconfig"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_RECONFIG**</dt> <dt>0x00000004</dt> </dl>                                         | Reconfigure.<br/>                   |
| <span id="SHTDN_REASON_MINOR_SECURITY"></span><span id="shtdn_reason_minor_security"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_SECURITY**</dt> <dt>0x00000013</dt> </dl>                                         | Security issue.<br/>                |
| <span id="SHTDN_REASON_MINOR_SECURITYFIX"></span><span id="shtdn_reason_minor_securityfix"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_SECURITYFIX**</dt> <dt>0x00000012</dt> </dl>                                | Security patch.<br/>                |
| <span id="SHTDN_REASON_MINOR_SECURITYFIX_UNINSTALL"></span><span id="shtdn_reason_minor_securityfix_uninstall"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_SECURITYFIX\_UNINSTALL**</dt> <dt>0x00000018</dt> </dl> | Security patch uninstallation.<br/> |
| <span id="SHTDN_REASON_MINOR_SERVICEPACK"></span><span id="shtdn_reason_minor_servicepack"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_SERVICEPACK**</dt> <dt>0x00000010</dt> </dl>                                | Service pack.<br/>                  |
| <span id="SHTDN_REASON_MINOR_SERVICEPACK_UNINSTALL"></span><span id="shtdn_reason_minor_servicepack_uninstall"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_SERVICEPACK\_UNINSTALL**</dt> <dt>0x00000016</dt> </dl> | Service pack uninstallation.<br/>   |
| <span id="SHTDN_REASON_MINOR_TERMSRV"></span><span id="shtdn_reason_minor_termsrv"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_TERMSRV**</dt> <dt>0x00000020</dt> </dl>                                            | Terminal Services.<br/>             |
| <span id="SHTDN_REASON_MINOR_UNSTABLE"></span><span id="shtdn_reason_minor_unstable"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_UNSTABLE**</dt> <dt>0x00000006</dt> </dl>                                         | Unstable.<br/>                      |
| <span id="SHTDN_REASON_MINOR_UPGRADE"></span><span id="shtdn_reason_minor_upgrade"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_UPGRADE**</dt> <dt>0x00000003</dt> </dl>                                            | Upgrade.<br/>                       |
| <span id="SHTDN_REASON_MINOR_WMI"></span><span id="shtdn_reason_minor_wmi"></span><dl> <dt>**SHTDN\_REASON\_MINOR\_WMI**</dt> <dt>0x00000015</dt> </dl>                                                        | WMI issue.<br/>                     |



The following optional flags provide additional information about the event.



| Constant/value                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SHTDN_REASON_FLAG_USER_DEFINED"></span><span id="shtdn_reason_flag_user_defined"></span><dl> <dt>**SHTDN\_REASON\_FLAG\_USER\_DEFINED**</dt> <dt>0x40000000</dt> </dl> | The reason code is defined by the user. For more information, see Defining a Custom Reason Code. <br/> If this flag is not present, the reason code is defined by the system.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="SHTDN_REASON_FLAG_PLANNED"></span><span id="shtdn_reason_flag_planned"></span><dl> <dt>**SHTDN\_REASON\_FLAG\_PLANNED**</dt> <dt>0x80000000</dt> </dl>                 | The shutdown was planned. The system generates a System State Data (SSD) file. This file contains system state information such as the processes, threads, memory usage, and configuration. <br/> If this flag is not present, the shutdown was unplanned. Notification and reporting options are controlled by a set of policies. For example, after logging in, the system displays a dialog box reporting the unplanned shutdown if the policy has been enabled. An SSD file is created only if the SSD policy is enabled on the system. The administrator can use [Windows Error Reporting](../wer/windows-error-reporting.md) to send the SSD data to a central location, or to Microsoft.<br/> |



## Remarks

The following combinations are recognized by the system. The table indicates the string that is displayed in the Shutdown Event Tracker, and provides a more detailed description. The default string is "No title for this reason could be found."



| Combination                                                                                                | Description                                                                                                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SHTDN\_REASON\_MAJOR\_APPLICATION \| SHTDN\_REASON\_MINOR\_HUNG                                            | "Application: Unresponsive" An unplanned restart or shutdown to troubleshoot an unresponsive application.<br/>                                                                                                                             |
| SHTDN\_REASON\_MAJOR\_APPLICATION \| SHTDN\_REASON\_MINOR\_INSTALLATION \| SHTDN\_REASON\_FLAG\_PLANNED    | "Application: Installation (Planned)" A planned restart or shutdown to perform application installation.<br/>                                                                                                                              |
| SHTDN\_REASON\_MAJOR\_APPLICATION \| SHTDN\_REASON\_MINOR\_MAINTENANCE                                     | "Application: Maintenance (Unplanned)" An unplanned restart or shutdown to service an application.<br/>                                                                                                                                    |
| SHTDN\_REASON\_MAJOR\_APPLICATION \| SHTDN\_REASON\_MINOR\_MAINTENANCE \| SHTDN\_REASON\_FLAG\_PLANNED     | "Application: Maintenance (Planned)" A planned restart or shutdown to perform planned maintenance on an application.<br/>                                                                                                                  |
| SHTDN\_REASON\_MAJOR\_APPLICATION \| SHTDN\_REASON\_MINOR\_UNSTABLE                                        | "Application: Unstable" An unplanned restart or shutdown to troubleshoot an unstable application.<br/>                                                                                                                                     |
| SHTDN\_REASON\_MAJOR\_HARDWARE \| SHTDN\_REASON\_MINOR\_INSTALLATION                                       | "Hardware: Installation (Unplanned)" An unplanned restart or shutdown to begin or complete hardware installation.<br/>                                                                                                                     |
| SHTDN\_REASON\_MAJOR\_HARDWARE \| SHTDN\_REASON\_MINOR\_INSTALLATION \| SHTDN\_REASON\_FLAG\_PLANNED       | "Hardware: Installation (Planned)" A planned restart or shutdown to begin or complete hardware installation.<br/>                                                                                                                          |
| SHTDN\_REASON\_MAJOR\_HARDWARE \| SHTDN\_REASON\_MINOR\_MAINTENANCE                                        | "Hardware: Maintenance (Unplanned)" An unplanned restart or shutdown to service hardware on the system.<br/>                                                                                                                               |
| SHTDN\_REASON\_MAJOR\_HARDWARE \| SHTDN\_REASON\_MINOR\_MAINTENANCE \| SHTDN\_REASON\_FLAG\_PLANNED        | "Hardware: Maintenance (Planned)" A planned restart or shutdown to service hardware on the system.<br/>                                                                                                                                    |
| SHTDN\_REASON\_MAJOR\_LEGACY\_API                                                                          | "Legacy API shutdown" This shutdown was initiated by the legacy [**InitiateSystemShutdown**](/windows/desktop/api/Winreg/nf-winreg-initiatesystemshutdowna) function. Applications should use the [**InitiateSystemShutdownEx**](/windows/desktop/api/Winreg/nf-winreg-initiatesystemshutdownexa) function.<br/> |
| SHTDN\_REASON\_MAJOR\_OPERATINGSYSTEM \| SHTDN\_REASON\_MINOR\_HOTFIX                                      | "Operating System: Hot fix (Unplanned)" An unplanned restart or shutdown to install a hot fix.<br/>                                                                                                                                        |
| SHTDN\_REASON\_MAJOR\_OPERATINGSYSTEM \| SHTDN\_REASON\_MINOR\_HOTFIX \| SHTDN\_REASON\_FLAG\_PLANNED      | "Operating System: Hot fix (Planned)" A planned restart or shutdown to install a hot fix.<br/>                                                                                                                                             |
| SHTDN\_REASON\_MAJOR\_OPERATINGSYSTEM \| SHTDN\_REASON\_MINOR\_RECONFIG                                    | "Operating System: Reconfiguration (Unplanned)" An unplanned restart or shutdown to change the operating system configuration.<br/>                                                                                                        |
| SHTDN\_REASON\_MAJOR\_OPERATINGSYSTEM \| SHTDN\_REASON\_MINOR\_RECONFIG \| SHTDN\_REASON\_FLAG\_PLANNED    | "Operating System: Reconfiguration (Planned)" A planned restart or shutdown to change the operating system configuration.<br/>                                                                                                             |
| SHTDN\_REASON\_MAJOR\_OPERATINGSYSTEM \| SHTDN\_REASON\_MINOR\_SECURITYFIX                                 | "Operating System: Security fix (Unplanned)" An unplanned restart or shutdown to install a security patch.<br/>                                                                                                                            |
| SHTDN\_REASON\_MAJOR\_OPERATINGSYSTEM \| SHTDN\_REASON\_MINOR\_SECURITYFIX \| SHTDN\_REASON\_FLAG\_PLANNED | "Operating System: Security fix (Planned)" A planned restart or shutdown to install a security patch.<br/>                                                                                                                                 |
| SHTDN\_REASON\_MAJOR\_OPERATINGSYSTEM \| SHTDN\_REASON\_MINOR\_SERVICEPACK \| SHTDN\_REASON\_FLAG\_PLANNED | "Operating System: Service pack (Planned)" A planned restart or shutdown to install a service pack.<br/>                                                                                                                                   |
| SHTDN\_REASON\_MAJOR\_OPERATINGSYSTEM \| SHTDN\_REASON\_MINOR\_UPGRADE \| SHTDN\_REASON\_FLAG\_PLANNED     | "Operating System: Upgrade (Planned)" A planned restart or shutdown to upgrade the operating system configuration.<br/>                                                                                                                    |
| SHTDN\_REASON\_MAJOR\_OTHER \| SHTDN\_REASON\_MINOR\_OTHER                                                 | "Other (Unplanned)" An unplanned shutdown or restart.<br/>                                                                                                                                                                                 |
| SHTDN\_REASON\_MAJOR\_OTHER \| SHTDN\_REASON\_MINOR\_OTHER \| SHTDN\_REASON\_FLAG\_PLANNED                 | "Other (Planned)" A planned shutdown or restart.<br/>                                                                                                                                                                                      |
| SHTDN\_REASON\_MAJOR\_OTHER \| SHTDN\_REASON\_MINOR\_HUNG                                                  | "Other Failure: System Unresponsive" The system became unresponsive.<br/>                                                                                                                                                                  |
| SHTDN\_REASON\_MAJOR\_POWER \| SHTDN\_REASON\_MINOR\_CORDUNPLUGGED                                         | "Power Failure: Cord Unplugged" The computer was unplugged.<br/>                                                                                                                                                                           |
| SHTDN\_REASON\_MAJOR\_POWER \| SHTDN\_REASON\_MINOR\_ENVIRONMENT                                           | "Power Failure: Environment" There was a power outage.<br/>                                                                                                                                                                                |
| SHTDN\_REASON\_MAJOR\_SYSTEM \| SHTDN\_REASON\_MINOR\_BLUESCREEN                                           | "System Failure: Stop error" The computer displayed a blue screen crash event.<br/>                                                                                                                                                        |
| SHTDN\_REASON\_MAJOR\_SYSTEM \| SHTDN\_REASON\_MINOR\_NETWORK\_CONNECTIVITY                                | "Loss of network connectivity (Unplanned)" The computer needs to be shut down due to a network connectivity issue.<br/>                                                                                                                    |
| SHTDN\_REASON\_MAJOR\_SYSTEM \| SHTDN\_REASON\_MINOR\_SECURITY                                             | "Security issue" The computer needs to be shut down due to a security issue.<br/>                                                                                                                                                          |



 

You can also define your own shutdown reasons and add them to the registry. Each reason code should be stored as a registry value in the following key:**HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Reliability\\UserDefined\\<default\_system\_language\_ID>**

This key contains value names of the following form: *xxxxx*;*nnn*;*nnnnn*. The semicolons delimit the components of a value name.

<dl> <dt>

<span id="xxxxx"></span><span id="XXXXX"></span>*xxxxx*
</dt> <dd>

One to five of the following control flags (no other characters can be used).



| Flag | Description                                                                                       |
|------|---------------------------------------------------------------------------------------------------|
| P    | Planned shutdown; otherwise, an unplanned shutdown.                                               |
| C    | A comment is required. This flag must be used with S.<br/>                                  |
| B    | An ID is required. This flag must be used with D.<br/>                                      |
| S    | Display the expected shutdown dialog box. Either S, D, or both S and D must be used.<br/>   |
| D    | Display the unexpected shutdown dialog box. Either S, D, or both S and D must be used.<br/> |



 

The order in which the flags are used is not important. For example, CSP indicates a planned shutdown where the expected shutdown dialog box is displayed, and a comment is required.

</dd> <dt>

<span id="nnn"></span><span id="NNN"></span>*nnn*
</dt> <dd>

Major reason. This component must be a number in the range 64-255. The range 0-63 is reserved for use by the system.

</dd> <dt>

<span id="nnnnn"></span><span id="NNNNN"></span>*nnnnn*
</dt> <dd>

Minor reason. This component must be in the range 0-65535.

</dd> </dl>

Custom reasons are sorted in the user interface by major reason number, then by minor reason number. No two custom reasons can use the same major and minor reasons, unless one is planned and the other is unplanned. Otherwise, the system will use the first instance and ignore the others.

The data for each registry value is two strings, separated by \\n\\r. The first string is a title string to be displayed in the shutdown dialog box, and written to the event log. The maximum size is 64 characters. Title strings must be unique. Custom titles cannot match the standard titles defined by the system, or another custom title. The second string is a description string to be displayed in the shutdown dialog box; it is optional. The maximum size is 256 characters.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps \| UWP apps\]<br/>                         |
| Header<br/>                   | <dl> <dt>Reason.h</dt> </dl> |



 

 
