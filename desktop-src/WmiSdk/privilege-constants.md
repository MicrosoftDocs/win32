---
description: The strPrivilege parameter of the SWbemPrivilegeSet.AddAsString method and the iPrivilege parameter for SWbemPrivilegeSet.Add require privilege strings from WbemPrivilegeEnum.
ms.assetid: f9400597-81bb-44a8-80dc-aba0160aea26
ms.tgt_platform: multiple
title: Privilege Constants (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- wbemPrivilegeCreateToken
- wbemPrivilegePrimaryToken
- wbemPrivilegeLockMemory
- wbemPrivilegeIncreaseQuota
- wbemPrivilegeMachineAccount
- wbemPrivilegeTcb
- wbemPrivilegeSecurity
- wbemPrivilegeTakeOwnership
- wbemPrivilegeLoadDriver
- wbemPrivilegeSystemProfile
- wbemPrivilegeSystemtime
- wbemPrivilegeProfileSingleProcess
- wbemPrivilegeIncreaseBasePriority
- wbemPrivilegeCreatePagefile
- wbemPrivilegeCreatePermanent
- wbemPrivilegeBackup
- wbemPrivilegeRestore
- wbemPrivilegeShutdown
- wbemPrivilegeDebug
- wbemPrivilegeAudit
- wbemPrivilegeSystemEnvironment
- wbemPrivilegeChangeNotify
- wbemPrivilegeRemoteShutdown
- wbemPrivilegeUndock
- wbemPrivilegeSyncAgent
- wbemPrivilegeEnableDelegation
- wbemPrivilegeManageVolume
api_type: 
- HeaderDef
api_location: 
- Wbemdisp.h
---

# Privilege Constants

The *strPrivilege* parameter of the [**SWbemPrivilegeSet.AddAsString**](swbemprivilegeset-addasstring.md) method and the *iPrivilege* parameter for [**SWbemPrivilegeSet.Add**](swbemprivilegeset-add.md) require privilege strings from [WbemPrivilegeEnum](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemprivilegeenum). For more information about how to use privilege constants, see [Executing Privileged Operations](executing-privileged-operations.md).

The following constants are defined in [**WbemPrivilegeEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemprivilegeenum). The following list includes the equivalent constants for C++ and strings for scripting. To form the scripting short name, remove the "Se" and "Privilege" from the C++ constant name.

The following VBScript code example shows how to enable the RemoteShutdown privilege in a script.


```VB
Set Service = GetObject("winmgmts:{impersonationLevel=impersonate, (RemoteShutdown)}")
```



Many WMI methods require that one or more permission be enabled. If an account has not been granted a privilege, it cannot be enabled for the method call.

<dl> <dt>

<span id="wbemPrivilegeCreateToken"></span><span id="wbemprivilegecreatetoken"></span><span id="WBEMPRIVILEGECREATETOKEN"></span>**wbemPrivilegeCreateToken**
</dt> <dd> <dl> <dt>

1 (0x1)
</dt> <dt>



C++ constant: **SE\_CREATE\_TOKEN\_NAME** string: **SeCreateTokenPrivilege**

Scripting short name: **CreateToken**

Required to create a primary token object.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegePrimaryToken"></span><span id="wbemprivilegeprimarytoken"></span><span id="WBEMPRIVILEGEPRIMARYTOKEN"></span>**wbemPrivilegePrimaryToken**
</dt> <dd> <dl> <dt>

2 (0x2)
</dt> <dt>



C++ constant: **SeAssignPrimaryTokenPrivilege** string: **SeAssignPrimaryTokenPrivilege**

Scripting short name: **AssignPrimaryToken**

Required to replace a process-level token.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeLockMemory"></span><span id="wbemprivilegelockmemory"></span><span id="WBEMPRIVILEGELOCKMEMORY"></span>**wbemPrivilegeLockMemory**
</dt> <dd> <dl> <dt>

3 (0x3)
</dt> <dt>



C++ constant: **SE\_LOCK\_MEMORY\_NAME** string: **SeLockMemoryPrivilege**

Scripting short name: **LockMemory**

Required to lock pages in memory.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeIncreaseQuota"></span><span id="wbemprivilegeincreasequota"></span><span id="WBEMPRIVILEGEINCREASEQUOTA"></span>**wbemPrivilegeIncreaseQuota**
</dt> <dd> <dl> <dt>

4 (0x4)
</dt> <dt>



C++ constant: **SE\_INCREASE\_QUOTA\_NAME** string: **SeIncreaseQuotaPrivilege**

Scripting short name: **IncreaseQuotaPrivilege**

Required to adjust memory quotas for a process.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeMachineAccount"></span><span id="wbemprivilegemachineaccount"></span><span id="WBEMPRIVILEGEMACHINEACCOUNT"></span>**wbemPrivilegeMachineAccount**
</dt> <dd> <dl> <dt>

5 (0x5)
</dt> <dt>



C++ constant: **SE\_MACINE\_ACCOUNT\_NAME** string: **SeMachineAccountPrivilege**

Scripting short name: **MachineAccount**

Required to add workstations to a domain.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeTcb"></span><span id="wbemprivilegetcb"></span><span id="WBEMPRIVILEGETCB"></span>**wbemPrivilegeTcb**
</dt> <dd> <dl> <dt>

6 (0x6)
</dt> <dt>



C++ constant: **SE\_TCB\_NAME** string: **SeTcbPrivilege**

Scripting short name: **Tcb**

Required to act as part of the operating system. The holder is part of the trusted computer base.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeSecurity"></span><span id="wbemprivilegesecurity"></span><span id="WBEMPRIVILEGESECURITY"></span>**wbemPrivilegeSecurity**
</dt> <dd> <dl> <dt>

7 (0x7)
</dt> <dt>



C++ constant: **SE\_SECURITY\_NAME** string: **SeSecurityPrivilege**

Scripting short name: **Security**

Required to manage auditing and the NT security log.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeTakeOwnership"></span><span id="wbemprivilegetakeownership"></span><span id="WBEMPRIVILEGETAKEOWNERSHIP"></span>**wbemPrivilegeTakeOwnership**
</dt> <dd> <dl> <dt>

8 (0x8)
</dt> <dt>



C++ constant: **SE\_TAKE\_OWNERSHIP\_NAME** string: **SeTakeOwnershipPrivilege**

Scripting short name: **TakeOwnership**

Required to assume ownership of files or other objects without having an [*Access Control Entry*](/windows/desktop/SecGloss/a-gly) (ACE) in the *discretionary access control list* (DACL).


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeLoadDriver"></span><span id="wbemprivilegeloaddriver"></span><span id="WBEMPRIVILEGELOADDRIVER"></span>**wbemPrivilegeLoadDriver**
</dt> <dd> <dl> <dt>

9 (0x9)
</dt> <dt>



C++ constant: **SE\_LOAD\_DRIVER** string: **SeLoadDriverPrivilege**

Scripting short name: **LoadDriver**

Required to load or unload a device driver.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeSystemProfile"></span><span id="wbemprivilegesystemprofile"></span><span id="WBEMPRIVILEGESYSTEMPROFILE"></span>**wbemPrivilegeSystemProfile**
</dt> <dd> <dl> <dt>

10 (0xA)
</dt> <dt>



C++ constant: **SE\_SYSTEM\_PROFILE\_NAME** string: **SeSystemProfilePrivilege**

Scripting short name: **SystemProfile**

Required to gather profile information about system performance.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeSystemtime"></span><span id="wbemprivilegesystemtime"></span><span id="WBEMPRIVILEGESYSTEMTIME"></span>**wbemPrivilegeSystemtime**
</dt> <dd> <dl> <dt>

11 (0xB)
</dt> <dt>



C++ constant: **SE\_SYSTEMTIME**\_NAME string: **SeSystemtimePrivilege**

Scripting short name: **Systemtime**

Required to change the system time.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeProfileSingleProcess"></span><span id="wbemprivilegeprofilesingleprocess"></span><span id="WBEMPRIVILEGEPROFILESINGLEPROCESS"></span>**wbemPrivilegeProfileSingleProcess**
</dt> <dd> <dl> <dt>

12 (0xC)
</dt> <dt>



C++ constant: **SE\_PROF\_SINGLE\_PROCESS\_NAME** string: **SeProfileSingleProcessPrivilege**

Scripting short name: **ProfileSingleProcess**

Required to gather profile information for a single process.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeIncreaseBasePriority"></span><span id="wbemprivilegeincreasebasepriority"></span><span id="WBEMPRIVILEGEINCREASEBASEPRIORITY"></span>**wbemPrivilegeIncreaseBasePriority**
</dt> <dd> <dl> <dt>

13 (0xD)
</dt> <dt>



C++ constant: **SE\_INC\_BASE\_PRIORITY\_NAME** string: **SeIncreaseBasePriorityPrivilege**

Scripting short name: **IncreaseBasePriority**

Required to increase scheduling priority.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeCreatePagefile"></span><span id="wbemprivilegecreatepagefile"></span><span id="WBEMPRIVILEGECREATEPAGEFILE"></span>**wbemPrivilegeCreatePagefile**
</dt> <dd> <dl> <dt>

14 (0xE)
</dt> <dt>



C++ constant: **SE\_CREATE\_PAGEFILE\_NAME** string: **SeCreatePagefilePrivilege**

Scripting short name: **CreatePagefile**

Required to create a pagefile.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeCreatePermanent"></span><span id="wbemprivilegecreatepermanent"></span><span id="WBEMPRIVILEGECREATEPERMANENT"></span>**wbemPrivilegeCreatePermanent**
</dt> <dd> <dl> <dt>

15 (0xF)
</dt> <dt>



C++ constant: **SE\_CREATE\_PERMANENT\_NAME** string: **SeCreatePermanentPrivilege**

Scripting short name: **CreatePermanent**

Required to create permanent shared objects.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeBackup"></span><span id="wbemprivilegebackup"></span><span id="WBEMPRIVILEGEBACKUP"></span>**wbemPrivilegeBackup**
</dt> <dd> <dl> <dt>

16 (0x10)
</dt> <dt>



C++ constant: **SE\_BACKUP\_NAME** string: **SeBackupPrivilege**

Scripting short name: **Backup**

Required to backup files and directories, regardless of the ACL specified for the file.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeRestore"></span><span id="wbemprivilegerestore"></span><span id="WBEMPRIVILEGERESTORE"></span>**wbemPrivilegeRestore**
</dt> <dd> <dl> <dt>

17 (0x11)
</dt> <dt>



C++ constant: **SE\_RESTORE\_NAME** string: **SeRestorePrivilege**

Scripting short name: **Restore**

Required to restore files and directories, regardless of the ACL specified for the file.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeShutdown"></span><span id="wbemprivilegeshutdown"></span><span id="WBEMPRIVILEGESHUTDOWN"></span>**wbemPrivilegeShutdown**
</dt> <dd> <dl> <dt>

18 (0x12)
</dt> <dt>



C++ constant: **SE\_SHUTDOWN\_NAME** string: **SeShutdownPrivilege**

Scripting short name: **Shutdown**

Required to shut down the local system.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeDebug"></span><span id="wbemprivilegedebug"></span><span id="WBEMPRIVILEGEDEBUG"></span>**wbemPrivilegeDebug**
</dt> <dd> <dl> <dt>

19 (0x13)
</dt> <dt>



C++ constant: **SE\_DEBUG\_NAME** string: **SeDebugPrivilege**

Scripting short name: **Debug**

Required to debug and adjust the memory of a process owned by another account.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeAudit"></span><span id="wbemprivilegeaudit"></span><span id="WBEMPRIVILEGEAUDIT"></span>**wbemPrivilegeAudit**
</dt> <dd> <dl> <dt>

20 (0x14)
</dt> <dt>



C++ constant: **SE\_AUDIT\_NAME** string: **SeAuditPrivilege**

Scripting short name: **Audit**

Required to generate audit entries in the NT Security log. Only secure servers should have this privilege.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeSystemEnvironment"></span><span id="wbemprivilegesystemenvironment"></span><span id="WBEMPRIVILEGESYSTEMENVIRONMENT"></span>**wbemPrivilegeSystemEnvironment**
</dt> <dd> <dl> <dt>

21 (0x15)
</dt> <dt>



C++ constant: **SE\_SYSTEM\_ENVIRONMENT\_NAME** string: **SeSystemEnvironmentPrivilege**

Scripting short name: **SystemEnvironment**

Required to modify the nonvolatile RAM of systems that use this type of memory to store configuration data.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeChangeNotify"></span><span id="wbemprivilegechangenotify"></span><span id="WBEMPRIVILEGECHANGENOTIFY"></span>**wbemPrivilegeChangeNotify**
</dt> <dd> <dl> <dt>

22 (0x16)
</dt> <dt>



C++ constant: **SE\_CHANGE\_NOTIFY\_NAME** string: **SeChangeNotifyPrivilege**

Scripting short name: **ChangeNotify**

Required to receive notifications of changes to files or directories and bypass traversal access checks. This privilege is enabled by default for all users.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeRemoteShutdown"></span><span id="wbemprivilegeremoteshutdown"></span><span id="WBEMPRIVILEGEREMOTESHUTDOWN"></span>**wbemPrivilegeRemoteShutdown**
</dt> <dd> <dl> <dt>

23 (0x17)
</dt> <dt>



C++ constant: **SE\_REMOTE\_SHUTDOWN\_NAME** string: **SeRemoteShutdownPrivilege**

Scripting short name: **RemoteShutdown**

Required to shut down a remote computer.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeUndock"></span><span id="wbemprivilegeundock"></span><span id="WBEMPRIVILEGEUNDOCK"></span>**wbemPrivilegeUndock**
</dt> <dd> <dl> <dt>

24 (0x18)
</dt> <dt>



C++ constant: **SE\_UNDOCK\_NAME** string: **SeUndockPrivilege**

Scripting short name: **Undock**

Required to remove a laptop from a docking station.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeSyncAgent"></span><span id="wbemprivilegesyncagent"></span><span id="WBEMPRIVILEGESYNCAGENT"></span>**wbemPrivilegeSyncAgent**
</dt> <dd> <dl> <dt>

25 (0x19)
</dt> <dt>



C++ constant: **SE\_SYNC\_AGENT\_NAME** string: **SeSyncAgentPrivilege**

Scripting short name: **SyncAgent**

Required to synchronize directory service data.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeEnableDelegation"></span><span id="wbemprivilegeenabledelegation"></span><span id="WBEMPRIVILEGEENABLEDELEGATION"></span>**wbemPrivilegeEnableDelegation**
</dt> <dd> <dl> <dt>

26 (0x1A)
</dt> <dt>



C++ constant: **SE\_ENABLE\_DELEGATION\_NAME** string: **SeEnableDelegationPrivilege**

Scripting short name: **EnableDelegation**

Required to enable computer and user accounts to be trusted for delegation.


</dt> </dl> </dd> <dt>

<span id="wbemPrivilegeManageVolume"></span><span id="wbemprivilegemanagevolume"></span><span id="WBEMPRIVILEGEMANAGEVOLUME"></span>**wbemPrivilegeManageVolume**
</dt> <dd> <dl> <dt>

27 (0x1B)
</dt> <dt>



C++ constant: **SE\_MANAGE\_VOLUME\_NAME** string: **SeManageVolumePrivilege**

Scripting short name: **ManageVolume**

Required to perform volume maintenance tasks.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wbemdisp.idl</dt> </dl> |



## See also

<dl> <dt>

[Scripting API Constants](scripting-api-constants.md)
</dt> <dt>

[**SWbemSecurity**](swbemsecurity.md)
</dt> <dt>

[**WbemPrivilegeEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemprivilegeenum)
</dt> <dt>

[Executing Privileged Operations](executing-privileged-operations.md)
</dt> <dt>

[Executing Privileged Operations Using VBScript](executing-privileged-operations-using-vbscript.md)
</dt> </dl>

 

