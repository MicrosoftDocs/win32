---
Description: Privileges determine the type of system operations that a user account can perform. An administrator assigns privileges to user and group accounts. Each users privileges include those granted to the user and to the groups to which the user belongs.
ms.assetid: 973796a6-bc2e-4e64-92db-5e17b9c25460
title: Privilege Constants (Winnt.h)
ms.topic: reference
ms.custom: snippet-project
ms.date: 07/27/2020
---

# Privilege Constants (Authorization)

Privileges determine the type of system operations that a user account can perform. An administrator assigns privileges to user and group accounts. Each user's privileges include those granted to the user and to the groups to which the user belongs.

The functions that get and adjust the privileges in an [*access token*](/windows/desktop/SecGloss/a-gly) use the [*locally unique identifier*](/windows/desktop/SecGloss/l-gly) (LUID) type to identify privileges. Use the [**LookupPrivilegeValue**](/windows/desktop/api/Winbase/nf-winbase-lookupprivilegevaluea) function to determine the [**LUID**](/windows/desktop/api/Winnt/ns-winnt-luid) on the local system that corresponds to a privilege constant. Use the [**LookupPrivilegeName**](/windows/desktop/api/Winbase/nf-winbase-lookupprivilegenamea) function to convert a **LUID** to its corresponding string constant.

The operating system represents a privilege by using the string that follows "User Right" in the Description column of the following table. The operating system displays the user right strings in the **Policy** column of the **User Rights Assignment** node of the Local Security Settings Microsoft Management Console (MMC) snap-in.

## Example

```cpp
BOOL EnablePrivilege()
{
    LUID PrivilegeRequired ;
    BOOL bRes = FALSE;
  
    bRes = LookupPrivilegeValue(NULL, SE_DEBUG_NAME, &PrivilegeRequired);

    // ...

    return bRes;
}
```
Example from [Windows Classic Samples](https://github.com/microsoft/Windows-classic-samples/blob/1d363ff4bd17d8e20415b92e2ee989d615cc0d91/Samples/ManagementInfrastructure/cpp/Process/Provider/WindowsProcess.c) on GitHub.

## Constants



| Constant/value | Description | 
|----------------|-------------|
| <span id="SE_ASSIGNPRIMARYTOKEN_NAME"></span><span id="se_assignprimarytoken_name"></span><dl><dt><strong>SE_ASSIGNPRIMARYTOKEN_NAME</strong></dt><dt>TEXT("SeAssignPrimaryTokenPrivilege")</dt></dl> | Required to assign the <a href="/windows/desktop/SecGloss/p-gly"><em>primary token</em></a> of a process. <br /> User Right: Replace a process-level token.<br /> | 
| <span id="SE_AUDIT_NAME"></span><span id="se_audit_name"></span><dl><dt><strong>SE_AUDIT_NAME</strong></dt><dt>TEXT("SeAuditPrivilege")</dt></dl> | Required to generate audit-log entries. Give this privilege to secure servers. <br /> User Right: Generate security audits.<br /> | 
| <span id="SE_BACKUP_NAME"></span><span id="se_backup_name"></span><dl><dt><strong>SE_BACKUP_NAME</strong></dt><dt>TEXT("SeBackupPrivilege")</dt></dl> | Required to perform backup operations. This privilege causes the system to grant all read access control to any file, regardless of the <a href="/windows/desktop/SecGloss/a-gly"><em>access control list</em></a> (ACL) specified for the file. Any access request other than read is still evaluated with the ACL. This privilege is required by the <a href="/windows/desktop/api/winreg/nf-winreg-regsavekeya"><strong>RegSaveKey</strong></a> and <a href="/windows/desktop/api/winreg/nf-winreg-regsavekeyexa"><strong>RegSaveKeyEx</strong></a>functions. The following access rights are granted if this privilege is held:<br /><ul><li>READ_CONTROL</li><li>ACCESS_SYSTEM_SECURITY</li><li>FILE_GENERIC_READ</li><li>FILE_TRAVERSE</li></ul>User Right: Back up files and directories.<br />If the file is located on a removable drive and the "Audit Removable Storage" is enabled, the SE_SECURITY_NAME is required to have ACCESS_SYSTEM_SECURITY. | 
| <span id="SE_CHANGE_NOTIFY_NAME"></span><span id="se_change_notify_name"></span><dl><dt><strong>SE_CHANGE_NOTIFY_NAME</strong></dt><dt>TEXT("SeChangeNotifyPrivilege")</dt></dl> | Required to receive notifications of changes to files or directories. This privilege also causes the system to skip all traversal access checks. It is enabled by default for all users. <br /> User Right: Bypass traverse checking.<br /> | 
| <span id="SE_CREATE_GLOBAL_NAME"></span><span id="se_create_global_name"></span><dl><dt><strong>SE_CREATE_GLOBAL_NAME</strong></dt><dt>TEXT("SeCreateGlobalPrivilege")</dt></dl> | Required to create named file mapping objects in the global namespace during Terminal Services sessions. This privilege is enabled by default for administrators, services, and the local system account.<br /> User Right: Create global objects.<br /> | 
| <span id="SE_CREATE_PAGEFILE_NAME"></span><span id="se_create_pagefile_name"></span><dl><dt><strong>SE_CREATE_PAGEFILE_NAME</strong></dt><dt>TEXT("SeCreatePagefilePrivilege")</dt></dl> | Required to create a paging file. <br /> User Right: Create a pagefile.<br /> | 
| <span id="SE_CREATE_PERMANENT_NAME"></span><span id="se_create_permanent_name"></span><dl><dt><strong>SE_CREATE_PERMANENT_NAME</strong></dt><dt>TEXT("SeCreatePermanentPrivilege")</dt></dl> | Required to create a permanent object. <br /> User Right: Create permanent shared objects.<br /> | 
| <span id="SE_CREATE_SYMBOLIC_LINK_NAME"></span><span id="se_create_symbolic_link_name"></span><dl><dt><strong>SE_CREATE_SYMBOLIC_LINK_NAME</strong></dt><dt>TEXT("SeCreateSymbolicLinkPrivilege")</dt></dl> | Required to create a symbolic link.<br /> User Right: Create symbolic links.<br /> | 
| <span id="SE_CREATE_TOKEN_NAME"></span><span id="se_create_token_name"></span><dl><dt><strong>SE_CREATE_TOKEN_NAME</strong></dt><dt>TEXT("SeCreateTokenPrivilege")</dt></dl> | Required to create a primary token. <br /> User Right: Create a token object.<br /> You cannot add this privilege to a user account with the "Create a token object" policy. Additionally, you cannot add this privilege to an owned process using Windows APIs.<strong>Windows Server 2003 and Windows XP with SP1 and earlier:</strong> Windows APIs can add this privilege to an owned process.<br /><br /> | 
| <span id="SE_DEBUG_NAME"></span><span id="se_debug_name"></span><dl><dt><strong>SE_DEBUG_NAME</strong></dt><dt>TEXT("SeDebugPrivilege")</dt></dl> | Required to debug and adjust the memory of a process owned by another account. <br /> User Right: Debug programs.<br /> | 
| <span id="SE_DELEGATE_SESSION_USER_IMPERSONATE_NAME"></span><span id="se_delegate_session_user_impersonate_name"></span><dl><dt><strong>SE_DELEGATE_SESSION_USER_IMPERSONATE_NAME</strong></dt><dt>TEXT("SeDelegateSessionUserImpersonatePrivilege")</dt></dl> | Required to obtain an impersonation token for another user in the same session. <br /> User Right: Impersonate other users.<br /> | 
| <span id="SE_ENABLE_DELEGATION_NAME"></span><span id="se_enable_delegation_name"></span><dl><dt><strong>SE_ENABLE_DELEGATION_NAME</strong></dt><dt>TEXT("SeEnableDelegationPrivilege")</dt></dl> | Required to mark user and computer accounts as trusted for delegation.<br /> User Right: Enable computer and user accounts to be trusted for delegation.<br /> | 
| <span id="SE_IMPERSONATE_NAME"></span><span id="se_impersonate_name"></span><dl><dt><strong>SE_IMPERSONATE_NAME</strong></dt><dt>TEXT("SeImpersonatePrivilege")</dt></dl> | Required to impersonate.<br /> User Right: Impersonate a client after authentication.<br /> | 
| <span id="SE_INC_BASE_PRIORITY_NAME"></span><span id="se_inc_base_priority_name"></span><dl><dt><strong>SE_INC_BASE_PRIORITY_NAME</strong></dt><dt>TEXT("SeIncreaseBasePriorityPrivilege")</dt></dl> | Required to increase the base priority of a process. <br /> User Right: Increase scheduling priority.<br /> | 
| <span id="SE_INCREASE_QUOTA_NAME"></span><span id="se_increase_quota_name"></span><dl><dt><strong>SE_INCREASE_QUOTA_NAME</strong></dt><dt>TEXT("SeIncreaseQuotaPrivilege")</dt></dl> | Required to increase the quota assigned to a process. <br /> User Right: Adjust memory quotas for a process.<br /> | 
| <span id="SE_INC_WORKING_SET_NAME"></span><span id="se_inc_working_set_name"></span><dl><dt><strong>SE_INC_WORKING_SET_NAME</strong></dt><dt>TEXT("SeIncreaseWorkingSetPrivilege")</dt></dl> | Required to allocate more memory for applications that run in the context of users.<br /> User Right: Increase a process working set.<br /> | 
| <span id="SE_LOAD_DRIVER_NAME"></span><span id="se_load_driver_name"></span><dl><dt><strong>SE_LOAD_DRIVER_NAME</strong></dt><dt>TEXT("SeLoadDriverPrivilege")</dt></dl> | Required to load or unload a device driver. <br /> User Right: Load and unload device drivers.<br /> | 
| <span id="SE_LOCK_MEMORY_NAME"></span><span id="se_lock_memory_name"></span><dl><dt><strong>SE_LOCK_MEMORY_NAME</strong></dt><dt>TEXT("SeLockMemoryPrivilege")</dt></dl> | Required to lock physical pages in memory. <br /> User Right: Lock pages in memory.<br /> | 
| <span id="SE_MACHINE_ACCOUNT_NAME"></span><span id="se_machine_account_name"></span><dl><dt><strong>SE_MACHINE_ACCOUNT_NAME</strong></dt><dt>TEXT("SeMachineAccountPrivilege")</dt></dl> | Required to create a computer account. <br /> User Right: Add workstations to domain.<br /> | 
| <span id="SE_MANAGE_VOLUME_NAME"></span><span id="se_manage_volume_name"></span><dl><dt><strong>SE_MANAGE_VOLUME_NAME</strong></dt><dt>TEXT("SeManageVolumePrivilege")</dt></dl> | Required to enable volume management privileges. <br /> User Right: Manage the files on a volume.<br /> | 
| <span id="SE_PROF_SINGLE_PROCESS_NAME"></span><span id="se_prof_single_process_name"></span><dl><dt><strong>SE_PROF_SINGLE_PROCESS_NAME</strong></dt><dt>TEXT("SeProfileSingleProcessPrivilege")</dt></dl> | Required to gather profiling information for a single process. <br /> User Right: Profile single process.<br /> | 
| <span id="SE_RELABEL_NAME"></span><span id="se_relabel_name"></span><dl><dt><strong>SE_RELABEL_NAME</strong></dt><dt>TEXT("SeRelabelPrivilege")</dt></dl> | Required to modify the mandatory integrity level of an object.<br /> User Right: Modify an object label.<br /> | 
| <span id="SE_REMOTE_SHUTDOWN_NAME"></span><span id="se_remote_shutdown_name"></span><dl><dt><strong>SE_REMOTE_SHUTDOWN_NAME</strong></dt><dt>TEXT("SeRemoteShutdownPrivilege")</dt></dl> | Required to shut down a system using a network request. <br /> User Right: Force shutdown from a remote system.<br /> | 
| <span id="SE_RESTORE_NAME"></span><span id="se_restore_name"></span><dl><dt><strong>SE_RESTORE_NAME</strong></dt><dt>TEXT("SeRestorePrivilege")</dt></dl> | Required to perform restore operations. This privilege causes the system to grant all write access control to any file, regardless of the ACL specified for the file. Any access request other than write is still evaluated with the ACL. Additionally, this privilege enables you to set any valid user or group SID as the owner of a file. This privilege is required by the <a href="/windows/desktop/api/winreg/nf-winreg-regloadkeya"><strong>RegLoadKey</strong></a> function. The following access rights are granted if this privilege is held:<br /><ul><li>WRITE_DAC</li><li>WRITE_OWNER</li><li>ACCESS_SYSTEM_SECURITY</li><li>FILE_GENERIC_WRITE</li><li>FILE_ADD_FILE</li><li>FILE_ADD_SUBDIRECTORY</li><li>DELETE</li></ul>User Right: Restore files and directories.<br />If the file is located on a removable drive and the "Audit Removable Storage" is enabled, the SE_SECURITY_NAME is required to have ACCESS_SYSTEM_SECURITY.<br /> | 
| <span id="SE_SECURITY_NAME"></span><span id="se_security_name"></span><dl><dt><strong>SE_SECURITY_NAME</strong></dt><dt>TEXT("SeSecurityPrivilege")</dt></dl> | Required to perform a number of security-related functions, such as controlling and viewing audit messages. This privilege identifies its holder as a security operator. <br /> User Right: Manage auditing and security log.<br /> | 
| <span id="SE_SHUTDOWN_NAME"></span><span id="se_shutdown_name"></span><dl><dt><strong>SE_SHUTDOWN_NAME</strong></dt><dt>TEXT("SeShutdownPrivilege")</dt></dl> | Required to shut down a local system. <br /> User Right: Shut down the system.<br /> | 
| <span id="SE_SYNC_AGENT_NAME"></span><span id="se_sync_agent_name"></span><dl><dt><strong>SE_SYNC_AGENT_NAME</strong></dt><dt>TEXT("SeSyncAgentPrivilege")</dt></dl> | Required for a domain controller to use the <a href="/windows/desktop/SecGloss/l-gly"><em>Lightweight Directory Access Protocol</em></a> directory synchronization services. This privilege enables the holder to read all objects and properties in the directory, regardless of the protection on the objects and properties. By default, it is assigned to the Administrator and LocalSystem accounts on domain controllers. <br /> User Right: Synchronize directory service data.<br /> | 
| <span id="SE_SYSTEM_ENVIRONMENT_NAME"></span><span id="se_system_environment_name"></span><dl><dt><strong>SE_SYSTEM_ENVIRONMENT_NAME</strong></dt><dt>TEXT("SeSystemEnvironmentPrivilege")</dt></dl> | Required to modify the nonvolatile RAM of systems that use this type of memory to store configuration information. <br /> User Right: Modify firmware environment values.<br /> | 
| <span id="SE_SYSTEM_PROFILE_NAME"></span><span id="se_system_profile_name"></span><dl><dt><strong>SE_SYSTEM_PROFILE_NAME</strong></dt><dt>TEXT("SeSystemProfilePrivilege")</dt></dl> | Required to gather profiling information for the entire system. <br /> User Right: Profile system performance.<br /> | 
| <span id="SE_SYSTEMTIME_NAME"></span><span id="se_systemtime_name"></span><dl><dt><strong>SE_SYSTEMTIME_NAME</strong></dt><dt>TEXT("SeSystemtimePrivilege")</dt></dl> | Required to modify the system time. <br /> User Right: Change the system time.<br /> | 
| <span id="SE_TAKE_OWNERSHIP_NAME"></span><span id="se_take_ownership_name"></span><dl><dt><strong>SE_TAKE_OWNERSHIP_NAME</strong></dt><dt>TEXT("SeTakeOwnershipPrivilege")</dt></dl> | Required to take ownership of an object without being granted discretionary access. This privilege allows the owner value to be set only to those values that the holder may legitimately assign as the owner of an object. <br /> User Right: Take ownership of files or other objects.<br /> | 
| <span id="SE_TCB_NAME"></span><span id="se_tcb_name"></span><dl><dt><strong>SE_TCB_NAME</strong></dt><dt>TEXT("SeTcbPrivilege")</dt></dl> | This privilege identifies its holder as part of the trusted computer base. Some trusted protected subsystems are granted this privilege. <br /> User Right: Act as part of the operating system.<br /> | 
| <span id="SE_TIME_ZONE_NAME"></span><span id="se_time_zone_name"></span><dl><dt><strong>SE_TIME_ZONE_NAME</strong></dt><dt>TEXT("SeTimeZonePrivilege")</dt></dl> | Required to adjust the time zone associated with the computer's internal clock.<br /> User Right: Change the time zone.<br /> | 
| <span id="SE_TRUSTED_CREDMAN_ACCESS_NAME"></span><span id="se_trusted_credman_access_name"></span><dl><dt><strong>SE_TRUSTED_CREDMAN_ACCESS_NAME</strong></dt><dt>TEXT("SeTrustedCredManAccessPrivilege")</dt></dl> | Required to access Credential Manager as a trusted caller.<br /> User Right: Access Credential Manager as a trusted caller.<br /> | 
| <span id="SE_UNDOCK_NAME"></span><span id="se_undock_name"></span><dl><dt><strong>SE_UNDOCK_NAME</strong></dt><dt>TEXT("SeUndockPrivilege")</dt></dl> | Required to undock a laptop.<br /> User Right: Remove computer from docking station.<br /> | 
| <span id="SE_UNSOLICITED_INPUT_NAME"></span><span id="se_unsolicited_input_name"></span><dl><dt><strong>SE_UNSOLICITED_INPUT_NAME</strong></dt><dt>TEXT("SeUnsolicitedInputPrivilege")</dt></dl> | Required to read unsolicited input from a <a href="/windows/desktop/SecGloss/t-gly"><em>terminal</em></a> device.<br /> User Right: Not applicable.<br /> | 




## Remarks

Privilege constants are defined as strings in Winnt.h. For example, the SE\_AUDIT\_NAME constant is defined as "SeAuditPrivilege".

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Winnt.h</dt> </dl> |



## See also

<dl> <dt>

[Privileges](privileges.md)
</dt> </dl>

