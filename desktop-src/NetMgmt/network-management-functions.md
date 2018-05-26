---
title: Network Management Functions
description: The network management functions can be grouped as follows.
ms.assetid: dfa81c58-3ce4-40ee-8bfc-a19a13781992
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Network Management Functions

The network management functions can be grouped as follows.

## Alert Functions



| Function                                   | Description                                                                                                                                                                                            |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetAlertRaise**](/windows/win32/Lmalert/nf-lmalert-netalertraise?branch=master)     | Notifies all registered clients that a particular event has occurred.                                                                                                                                  |
| [**NetAlertRaiseEx**](/windows/win32/Lmalert/nf-lmalert-netalertraiseex?branch=master) | Simplifies notifying registered clients that a particular event has occurred, because, unlike **NetAlertRaise**, **NetAlertRaiseEx** does not require a [**STD\_ALERT**](/windows/win32/Lmalert/ns-lmalert-_std_alert?branch=master) structure. |



 

## API Buffer Functions



| Function                                                 | Description                                                                                                               |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**NetApiBufferAllocate**](/windows/win32/Lmapibuf/nf-lmapibuf-netapibufferallocate?branch=master)     | Allocates memory from the heap. Call this function when you require compatibility with the **NetApiBufferFree** function. |
| [**NetApiBufferFree**](/windows/win32/Lmapibuf/nf-lmapibuf-netapibufferfree?branch=master)             | Frees memory allocated by the **NetApiBufferAllocate** function and other network management functions.                   |
| [**NetApiBufferReallocate**](/windows/win32/Lmapibuf/nf-lmapibuf-netapibufferreallocate?branch=master) | Changes the size of a buffer allocated by a call to the **NetApiBufferAllocate** function.                                |
| [**NetApiBufferSize**](/windows/win32/Lmapibuf/nf-lmapibuf-netapibuffersize?branch=master)             | Returns the size, in bytes, of a buffer allocated by a call to the **NetApiBufferAllocate** function.                     |



 

## Azure Active Directory Join Information Functions



| Function                                                       | Description                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetFreeAadJoinInformation**](/windows/win32/lmjoin/nf-lmjoin-netfreeaadjoininformation?branch=master) | Frees the memory allocated for the specified [**DSREG\_JOIN\_INFO**](/windows/win32/lmjoin/ns-lmjoin-_dsreg_join_info?branch=master) structure, which contains join information for a tenant and which you retrieved by calling the [**NetGetAadJoinInformation**](/windows/win32/lmjoin/nf-lmjoin-netgetaadjoininformation?branch=master) function. |
| [**NetGetAadJoinInformation**](/windows/win32/lmjoin/nf-lmjoin-netgetaadjoininformation?branch=master)   | Retrieves the join information for the specified tenant. This function examines the join information for Microsoft Azure Active Directory and the work account that the current user added.                                                                     |



 

## Directory Service and Domain Join Functions



| Function                                                                             | Description                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetAddAlternateComputerName**](/windows/win32/Lmjoin/nf-lmjoin-netaddalternatecomputername?branch=master)                   | Adds an alternate name for the specified computer.                                                                                                                                                                                                                      |
| [**NetCreateProvisioningPackage**](/windows/win32/Lmjoin/nf-lmjoin-netprovisioncomputeraccount?branch=master)                  | Provisions a computer account for later use in an offline domain join operation.                                                                                                                                                                                        |
| [**NetEnumerateComputerNames**](/windows/win32/Lmjoin/nf-lmjoin-netenumeratecomputernames?branch=master)                       | Enumerates names for the specified computer.                                                                                                                                                                                                                            |
| [**NetGetJoinableOUs**](/windows/win32/Lmjoin/nf-lmjoin-netgetjoinableous?branch=master)                                       | Retrieves a list of organizational units (OUs) in which a computer account can be created.                                                                                                                                                                              |
| [**NetGetJoinInformation**](/windows/win32/Lmjoin/nf-lmjoin-netgetjoininformation?branch=master)                               | Retrieves join status information for the specified computer.                                                                                                                                                                                                           |
| [**NetJoinDomain**](/windows/win32/Lmjoin/nf-lmjoin-netjoindomain?branch=master)                                               | Joins a computer to a workgroup or domain.                                                                                                                                                                                                                              |
| [**NetLogonSetServiceBits**](netlogonsetservicebits.md)                             | Notifies the Netlogon service of the running state of the services on a domain controller. The caller must be running in the context of either the LocalSystem or the LocalService account.                                                                             |
| [**NetProvisionComputerAccount**](/windows/win32/Lmjoin/nf-lmjoin-netprovisioncomputeraccount?branch=master)                   | Provisions a computer account for later used in an offline domain join operation.                                                                                                                                                                                       |
| [**NetRemoveAlternateComputerName**](/windows/win32/Lmjoin/nf-lmjoin-netremovealternatecomputername?branch=master)             | Removes an alternate name for the specified computer.                                                                                                                                                                                                                   |
| [**NetRenameMachineInDomain**](/windows/win32/Lmjoin/nf-lmjoin-netrenamemachineindomain?branch=master)                         | Changes the name of a computer in a domain.                                                                                                                                                                                                                             |
| [**NetRequestOfflineDomainJoin**](/windows/win32/Lmjoin/nf-lmjoin-netrequestofflinedomainjoin?branch=master)                   | Executes locally on a machine to modify a Windows operating system image mounted on a volume. The registry is loaded for the image and provisioning blob data is written where it can be retrieved during the completion phase of an offline domain join operation.     |
| [**NetRequestProvisioningPackageInstall**](/windows/win32/Lmjoin/nf-lmjoin-netrequestprovisioningpackageinstall?branch=master) | Executes locally on a machine to modify a Windows operating system image mounted on a volume. The registry is loaded from the image and provisioning package data is written where it can be retrieved during the completion phase of an offline domain join operation. |
| [**NetSetPrimaryComputerName**](/windows/win32/Lmjoin/nf-lmjoin-netsetprimarycomputername?branch=master)                       | Sets the primary computer name for the specified computer.                                                                                                                                                                                                              |
| [**NetUnjoinDomain**](/windows/win32/Lmjoin/nf-lmjoin-netunjoindomain?branch=master)                                           | Unjoins a computer from a workgroup or a domain.                                                                                                                                                                                                                        |
| [**NetValidateName**](/windows/win32/Lmjoin/nf-lmjoin-netvalidatename?branch=master)                                           | Verifies the validity of a computer name, workgroup name, or domain name.                                                                                                                                                                                               |



 

## Get Functions



| Function                                                               | Description                                                                                                                              |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetGetAnyDCName**](/windows/win32/Lmaccess/nf-lmaccess-netgetanydcname?branch=master)                             | Returns the name of any domain controller for a domain that is directly trusted by a specified server.                                   |
| [**NetGetDCName**](/windows/win32/Lmaccess/nf-lmaccess-netgetdcname?branch=master)                                   | Returns the name of the primary domain controller (PDC) for the specified domain.                                                        |
| [**NetGetDisplayInformationIndex**](/windows/win32/Lmaccess/nf-lmaccess-netgetdisplayinformationindex?branch=master) | Returns the index of the first display information entry whose name begins with a specified string or alphabetically follows the string. |
| [**NetQueryDisplayInformation**](/windows/win32/Lmaccess/nf-lmaccess-netquerydisplayinformation?branch=master)       | Returns user, computer, or global group account information.                                                                             |



 

## Group Functions



| Function                                     | Description                                                                       |
|----------------------------------------------|-----------------------------------------------------------------------------------|
| [**NetGroupAdd**](/windows/win32/Lmaccess/nf-lmaccess-netgroupadd?branch=master)           | Creates a global group.                                                           |
| [**NetGroupAddUser**](/windows/win32/Lmaccess/nf-lmaccess-netgroupadduser?branch=master)   | Adds one user to an existing global group.                                        |
| [**NetGroupDel**](/windows/win32/Lmaccess/nf-lmaccess-netgroupdel?branch=master)           | Removes a global group whether or not the group has any members.                  |
| [**NetGroupDelUser**](/windows/win32/Lmaccess/nf-lmaccess-netgroupdeluser?branch=master)   | Removes one user name from a global group.                                        |
| [**NetGroupEnum**](/windows/win32/Lmaccess/nf-lmaccess-netgroupenum?branch=master)         | Lists all global groups on a server.                                              |
| [**NetGroupGetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netgroupgetinfo?branch=master)   | Returns information about a particular global group.                              |
| [**NetGroupGetUsers**](/windows/win32/Lmaccess/nf-lmaccess-netgroupgetusers?branch=master) | Lists all members of a particular global group.                                   |
| [**NetGroupSetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netgroupsetinfo?branch=master)   | Sets general information about a global group.                                    |
| [**NetGroupSetUsers**](/windows/win32/Lmaccess/nf-lmaccess-netgroupsetusers?branch=master) | Assigns members to a new global group; replaces the members of an existing group. |



 

## Local Group Functions



| Function                                                   | Description                                                             |
|------------------------------------------------------------|-------------------------------------------------------------------------|
| [**NetLocalGroupAdd**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupadd?branch=master)               | Creates a local group.                                                  |
| [**NetLocalGroupAddMembers**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupaddmembers?branch=master) | Adds one or more users or global groups to an existing local group.     |
| [**NetLocalGroupDel**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupdel?branch=master)               | Deletes a local group, removing all existing members from the group.    |
| [**NetLocalGroupDelMembers**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupdelmembers?branch=master) | Removes one or more members from an existing local group.               |
| [**NetLocalGroupEnum**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupenum?branch=master)             | Returns information about each local group account on a server.         |
| [**NetLocalGroupGetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupgetinfo?branch=master)       | Returns information about a particular local group account on a server. |
| [**NetLocalGroupGetMembers**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupgetmembers?branch=master) | Lists all members of a specified local group.                           |
| [**NetLocalGroupSetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupsetinfo?branch=master)       | Sets general information about a local group.                           |
| [**NetLocalGroupSetMembers**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupsetmembers?branch=master) | Assigns members to a local group.                                       |



 

## Message Functions



| Function                                               | Description                                                                     |
|--------------------------------------------------------|---------------------------------------------------------------------------------|
| [**NetMessageBufferSend**](/windows/win32/Lmmsg/nf-lmmsg-netmessagebuffersend?branch=master)   | Sends a message to a registered message alias.                                  |
| [**NetMessageNameAdd**](/windows/win32/Lmmsg/nf-lmmsg-netmessagenameadd?branch=master)         | Registers a message alias in the message name table.                            |
| [**NetMessageNameDel**](/windows/win32/Lmmsg/nf-lmmsg-netmessagenamedel?branch=master)         | Deletes a message alias from the message name table.                            |
| [**NetMessageNameEnum**](/windows/win32/Lmmsg/nf-lmmsg-netmessagenameenum?branch=master)       | Lists all the message aliases stored in the message name table.                 |
| [**NetMessageNameGetInfo**](/windows/win32/Lmmsg/nf-lmmsg-netmessagenamegetinfo?branch=master) | Returns information about a particular message alias in the message name table. |



 

## NetFile Functions



| Function                                | Description                                                          |
|-----------------------------------------|----------------------------------------------------------------------|
| [**NetFileClose**](https://msdn.microsoft.com/library/windows/desktop/bb525377)     | Forces a resource to close.                                          |
| [**NetFileEnum**](https://msdn.microsoft.com/library/windows/desktop/bb525378)       | Returns information about open files on a server.                    |
| [**NetFileGetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525379) | Returns information about a particular opening of a server resource. |



 

## Remote Utility Functions



| Function                                                       | Description                                                                             |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**NetRemoteComputerSupports**](/windows/win32/Lmremutl/nf-lmremutl-netremotecomputersupports?branch=master) | Queries the redirector to retrieve the optional features that a remote system supports. |
| [**NetRemoteTOD**](/windows/win32/Lmremutl/nf-lmremutl-netremotetod?branch=master)                           | Enables applications to access the time-of-day information on a remote server.          |



 

## Schedule Functions



| Function                                                                     | Description                                                      |
|------------------------------------------------------------------------------|------------------------------------------------------------------|
| [**NetScheduleJobAdd**](/windows/win32/Lmat/nf-lmat-netschedulejobadd?branch=master)                               | Submits a job to run at a specified future date and time.        |
| [**NetScheduleJobDel**](/windows/win32/Lmat/nf-lmat-netschedulejobdel?branch=master)                               | Cancels a range of jobs queued to run on a computer.             |
| [**NetScheduleJobEnum**](/windows/win32/Lmat/nf-lmat-netschedulejobenum?branch=master)                             | Lists the jobs queued on a specified computer.                   |
| [**NetScheduleJobGetInfo**](/windows/win32/Lmat/nf-lmat-netschedulejobgetinfo?branch=master)                       | Returns information about a particular job queued on a computer. |
| [**GetNetScheduleAccountInformation**](/windows/win32/AtAcct/nf-atacct-getnetscheduleaccountinformation?branch=master) | Retrieves the AT Service account name.                           |
| [**SetNetScheduleAccountInformation**](/windows/win32/AtAcct/nf-atacct-setnetscheduleaccountinformation?branch=master) | Sets the AT Service account name and password.                   |



 

## Server Functions



| Function                                       | Description                                                                        |
|------------------------------------------------|------------------------------------------------------------------------------------|
| [**NetServerDiskEnum**](/windows/win32/Lmserver/nf-lmserver-netserverdiskenum?branch=master) | Returns a list of local disk drives on a server.                                   |
| [**NetServerEnum**](/windows/win32/Lmserver/nf-lmserver-netserverenum?branch=master)         | Lists all visible servers of a particular type (or types) in the specified domain. |
| [**NetServerGetInfo**](/windows/win32/Lmserver/nf-lmserver-netservergetinfo?branch=master)   | Returns configuration information about a specified server.                        |
| [**NetServerSetInfo**](/windows/win32/Lmserver/nf-lmserver-netserversetinfo?branch=master)   | Sets the operating parameters for a server.                                        |



 

## Server and Workstation Transport Functions



| Function                                                     | Description                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetServerComputerNameAdd**](/windows/win32/Lmserver/nf-lmserver-netservercomputernameadd?branch=master) | Binds an emulated server name to each of the transport protocols on which a server is active. (Combines the functionality of the [**NetServerTransportEnum**](/windows/win32/Lmserver/nf-lmserver-netservertransportenum?branch=master) function and the [**NetServerTransportAddEx**](/windows/win32/Lmserver/nf-lmserver-netservertransportaddex?branch=master) function.)                                            |
| [**NetServerComputerNameDel**](/windows/win32/Lmserver/nf-lmserver-netservercomputernamedel?branch=master) | Disconnects each network transport protocol from an emulated server name set by a previous call to the **NetServerComputerNameAdd** function.                                                                                                                                                                               |
| [**NetServerTransportAdd**](/windows/win32/Lmserver/nf-lmserver-netservertransportadd?branch=master)       | Binds the specified server to the transport protocol. (This function supports only the [**SERVER\_TRANSPORT\_INFO\_0**](/windows/win32/Lmserver/ns-lmserver-_server_transport_info_0?branch=master) information level.)                                                                                                                                                |
| [**NetServerTransportAddEx**](/windows/win32/Lmserver/nf-lmserver-netservertransportaddex?branch=master)   | Binds the specified server to the transport protocol. (This extended function supports the [**SERVER\_TRANSPORT\_INFO\_1**](/windows/win32/Lmserver/ns-lmserver-_server_transport_info_1?branch=master), [**SERVER\_TRANSPORT\_INFO\_2**](/windows/win32/Lmserver/ns-lmserver-_server_transport_info_2?branch=master), and [**SERVER\_TRANSPORT\_INFO\_3**](/windows/win32/Lmserver/ns-lmserver-_server_transport_info_3?branch=master) information levels.) |
| [**NetServerTransportDel**](/windows/win32/Lmserver/nf-lmserver-netservertransportdel?branch=master)       | Disconnects the transport protocol from the server.                                                                                                                                                                                                                                                                         |
| [**NetServerTransportEnum**](/windows/win32/Lmserver/nf-lmserver-netservertransportenum?branch=master)     | Enumerates the transport protocols managed by the server.                                                                                                                                                                                                                                                                   |
| [**NetWkstaTransportEnum**](/windows/win32/Lmwksta/nf-lmwksta-netwkstatransportenum?branch=master)       | Lists the transport protocols that are managed by the redirector.                                                                                                                                                                                                                                                           |



 

## Use Functions



| Function                               | Description                                                                               |
|----------------------------------------|-------------------------------------------------------------------------------------------|
| [**NetUseAdd**](/windows/win32/Lmuse/nf-lmuse-netuseadd?branch=master)         | Creates a connection between a local computer and a server.                               |
| [**NetUseDel**](/windows/win32/Lmuse/nf-lmuse-netusedel?branch=master)         | Ends a connection to a shared resource.                                                   |
| [**NetUseEnum**](/windows/win32/Lmuse/nf-lmuse-netuseenum?branch=master)       | Lists all current connections between the local computer and resources on remote servers. |
| [**NetUseGetInfo**](/windows/win32/Lmuse/nf-lmuse-netusegetinfo?branch=master) | Returns information about a connection to a shared resource.                              |



 

## User Functions



| Function                                               | Description                                                         |
|--------------------------------------------------------|---------------------------------------------------------------------|
| [**NetUserAdd**](/windows/win32/Lmaccess/nf-lmaccess-netuseradd?branch=master)                       | Adds a user account and assigns a password and privilege level.     |
| [**NetUserChangePassword**](/windows/win32/Lmaccess/nf-lmaccess-netuserchangepassword?branch=master) | Changes a user's password for a specified network server or domain. |
| [**NetUserDel**](/windows/win32/Lmaccess/nf-lmaccess-netuserdel?branch=master)                       | Deletes a user account from the server.                             |
| [**NetUserEnum**](/windows/win32/Lmaccess/nf-lmaccess-netuserenum?branch=master)                     | Lists all user accounts on a server.                                |
| [**NetUserGetGroups**](/windows/win32/Lmaccess/nf-lmaccess-netusergetgroups?branch=master)           | Returns a list of global group names to which a user belongs.       |
| [**NetUserGetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netusergetinfo?branch=master)               | Returns information about a particular user account on a server.    |
| [**NetUserGetLocalGroups**](/windows/win32/Lmaccess/nf-lmaccess-netusergetlocalgroups?branch=master) | Returns a list of local group names to which a user belongs.        |
| [**NetUserSetGroups**](/windows/win32/Lmaccess/nf-lmaccess-netusersetgroups?branch=master)           | Sets global group memberships for a specified user account.         |
| [**NetUserSetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netusersetinfo?branch=master)               | Sets the password and other elements of a user account.             |



 

## User Modals Functions



| Function                                     | Description                                                                                                                                                                                             |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetUserModalsGet**](/windows/win32/Lmaccess/nf-lmaccess-netusermodalsget?branch=master) | Returns global information for all users and global groups in the security database, which is the security accounts manager (SAM) database or, in the case of domain controllers, the Active Directory. |
| [**NetUserModalsSet**](/windows/win32/Lmaccess/nf-lmaccess-netusermodalsset?branch=master) | Sets global information for all users and global groups in the security database.                                                                                                                       |



 

## Validation Functions



| Function                                                               | Description                                                                                                                                                                                                                     |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetValidatePasswordPolicyFree**](/windows/win32/Lmaccess/nf-lmaccess-netvalidatepasswordpolicyfree?branch=master) | Frees the memory that the [**NetValidatePasswordPolicy**](/windows/win32/Lmaccess/nf-lmaccess-netvalidatepasswordpolicy?branch=master) function allocates for the *OutputArg* parameter,                                                                                      |
| [**NetValidatePasswordPolicy**](/windows/win32/Lmaccess/nf-lmaccess-netvalidatepasswordpolicy?branch=master)         | Enables an application to check password compliance against an application-provided account database and verify that passwords meet the complexity, aging, minimum length, and history reuse requirements of a password policy. |



 

## Workstation and Workstation User Functions



| Function                                           | Description                                                                         |
|----------------------------------------------------|-------------------------------------------------------------------------------------|
| [**NetWkstaGetInfo**](/windows/win32/Lmwksta/nf-lmwksta-netwkstagetinfo?branch=master)         | Returns information about the configuration elements for a workstation.             |
| [**NetWkstaSetInfo**](/windows/win32/Lmwksta/nf-lmwksta-netwkstasetinfo?branch=master)         | Configures a workstation.                                                           |
| [**NetWkstaUserEnum**](/windows/win32/Lmwksta/nf-lmwksta-netwkstauserenum?branch=master)       | Lists information about all users currently logged on to the workstation.           |
| [**NetWkstaUserGetInfo**](/windows/win32/Lmwksta/nf-lmwksta-netwkstausergetinfo?branch=master) | Returns information about one currently logged-on user.                             |
| [**NetWkstaUserSetInfo**](/windows/win32/Lmwksta/nf-lmwksta-netwkstausersetinfo?branch=master) | Sets the user-specific information for the configuration elements of a workstation. |



 

## Obsolete Functions

-   [**NetAccessAdd**](/windows/win32/lmaccess/nf-lmaccess-netaccessadd?branch=master)
-   [**NetAccessCheck**](/windows/win32/Lmaccess/?branch=master)
-   [**NetAccessDel**](/windows/win32/lmaccess/nf-lmaccess-netaccessdel?branch=master)
-   [**NetAccessEnum**](/windows/win32/lmaccess/nf-lmaccess-netaccessenum?branch=master)
-   [**NetAccessGetInfo**](/windows/win32/lmaccess/nf-lmaccess-netaccessgetinfo?branch=master)
-   [**NetAccessGetUserPerms**](/windows/win32/lmaccess/nf-lmaccess-netaccessgetuserperms?branch=master)
-   [**NetAccessSetInfo**](/windows/win32/lmaccess/nf-lmaccess-netaccesssetinfo?branch=master)
-   [**NetAuditClear**](netauditclear.md)
-   [**NetAuditRead**](netauditread.md)
-   [**NetAuditWrite**](netauditwrite.md)
-   [**NetConfigGet**](netconfigget.md)
-   [**NetConfigGetAll**](netconfiggetall.md)
-   [**NetConfigSet**](netconfigset.md)
-   [**NetErrorLogClear**](neterrorlogclear.md)
-   [**NetErrorLogRead**](neterrorlogread.md)
-   [**NetErrorLogWrite**](neterrorlogwrite.md)
-   [**NetLocalGroupAddMember**](/windows/win32/lmaccess/nf-lmaccess-netlocalgroupaddmember?branch=master)
-   [**NetLocalGroupDelMember**](/windows/win32/lmaccess/nf-lmaccess-netlocalgroupdelmember?branch=master)
-   [**NetServiceControl**](netservicecontrol.md)
-   [**NetServiceEnum**](netserviceenum.md)
-   [**NetServiceGetInfo**](netservicegetinfo.md)
-   [**NetServiceInstall**](netserviceinstall.md)
-   [**NetWkstaTransportAdd**](/windows/win32/lmwksta/nf-lmwksta-netwkstatransportadd?branch=master)
-   [**NetWkstaTransportDel**](/windows/win32/lmwksta/nf-lmwksta-netwkstatransportdel?branch=master)

## Related topics

<dl> <dt>

[Windows Networking Functions](https://msdn.microsoft.com/library/windows/desktop/aa385391)
</dt> </dl>

 

 




