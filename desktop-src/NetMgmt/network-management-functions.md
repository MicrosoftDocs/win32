---
title: Network Management Functions
description: The network management functions can be grouped as follows.
ms.assetid: 'dfa81c58-3ce4-40ee-8bfc-a19a13781992'
---

# Network Management Functions

The network management functions can be grouped as follows.

## Alert Functions



| Function                                   | Description                                                                                                                                                                                            |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetAlertRaise**](netalertraise.md)     | Notifies all registered clients that a particular event has occurred.                                                                                                                                  |
| [**NetAlertRaiseEx**](netalertraiseex.md) | Simplifies notifying registered clients that a particular event has occurred, because, unlike **NetAlertRaise**, **NetAlertRaiseEx** does not require a [**STD\_ALERT**](std-alert-str.md) structure. |



 

## API Buffer Functions



| Function                                                 | Description                                                                                                               |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**NetApiBufferAllocate**](netapibufferallocate.md)     | Allocates memory from the heap. Call this function when you require compatibility with the **NetApiBufferFree** function. |
| [**NetApiBufferFree**](netapibufferfree.md)             | Frees memory allocated by the **NetApiBufferAllocate** function and other network management functions.                   |
| [**NetApiBufferReallocate**](netapibufferreallocate.md) | Changes the size of a buffer allocated by a call to the **NetApiBufferAllocate** function.                                |
| [**NetApiBufferSize**](netapibuffersize.md)             | Returns the size, in bytes, of a buffer allocated by a call to the **NetApiBufferAllocate** function.                     |



 

## Azure Active Directory Join Information Functions



| Function                                                       | Description                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetFreeAadJoinInformation**](netfreeaadjoininformation.md) | Frees the memory allocated for the specified [**DSREG\_JOIN\_INFO**](dsreg-join-info.md) structure, which contains join information for a tenant and which you retrieved by calling the [**NetGetAadJoinInformation**](netgetaadjoininformation.md) function. |
| [**NetGetAadJoinInformation**](netgetaadjoininformation.md)   | Retrieves the join information for the specified tenant. This function examines the join information for Microsoft Azure Active Directory and the work account that the current user added.                                                                     |



 

## Directory Service and Domain Join Functions



| Function                                                                             | Description                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetAddAlternateComputerName**](netaddalternatecomputername.md)                   | Adds an alternate name for the specified computer.                                                                                                                                                                                                                      |
| [**NetCreateProvisioningPackage**](netprovisioncomputeraccount.md)                  | Provisions a computer account for later use in an offline domain join operation.                                                                                                                                                                                        |
| [**NetEnumerateComputerNames**](netenumeratecomputernames.md)                       | Enumerates names for the specified computer.                                                                                                                                                                                                                            |
| [**NetGetJoinableOUs**](netgetjoinableous.md)                                       | Retrieves a list of organizational units (OUs) in which a computer account can be created.                                                                                                                                                                              |
| [**NetGetJoinInformation**](netgetjoininformation.md)                               | Retrieves join status information for the specified computer.                                                                                                                                                                                                           |
| [**NetJoinDomain**](netjoindomain.md)                                               | Joins a computer to a workgroup or domain.                                                                                                                                                                                                                              |
| [**NetLogonSetServiceBits**](netlogonsetservicebits.md)                             | Notifies the Netlogon service of the running state of the services on a domain controller. The caller must be running in the context of either the LocalSystem or the LocalService account.                                                                             |
| [**NetProvisionComputerAccount**](netprovisioncomputeraccount.md)                   | Provisions a computer account for later used in an offline domain join operation.                                                                                                                                                                                       |
| [**NetRemoveAlternateComputerName**](netremovealternatecomputername.md)             | Removes an alternate name for the specified computer.                                                                                                                                                                                                                   |
| [**NetRenameMachineInDomain**](netrenamemachineindomain.md)                         | Changes the name of a computer in a domain.                                                                                                                                                                                                                             |
| [**NetRequestOfflineDomainJoin**](netrequestofflinedomainjoin.md)                   | Executes locally on a machine to modify a Windows operating system image mounted on a volume. The registry is loaded for the image and provisioning blob data is written where it can be retrieved during the completion phase of an offline domain join operation.     |
| [**NetRequestProvisioningPackageInstall**](netrequestprovisioningpackageinstall.md) | Executes locally on a machine to modify a Windows operating system image mounted on a volume. The registry is loaded from the image and provisioning package data is written where it can be retrieved during the completion phase of an offline domain join operation. |
| [**NetSetPrimaryComputerName**](netsetprimarycomputername.md)                       | Sets the primary computer name for the specified computer.                                                                                                                                                                                                              |
| [**NetUnjoinDomain**](netunjoindomain.md)                                           | Unjoins a computer from a workgroup or a domain.                                                                                                                                                                                                                        |
| [**NetValidateName**](netvalidatename.md)                                           | Verifies the validity of a computer name, workgroup name, or domain name.                                                                                                                                                                                               |



 

## Get Functions



| Function                                                               | Description                                                                                                                              |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetGetAnyDCName**](netgetanydcname.md)                             | Returns the name of any domain controller for a domain that is directly trusted by a specified server.                                   |
| [**NetGetDCName**](netgetdcname.md)                                   | Returns the name of the primary domain controller (PDC) for the specified domain.                                                        |
| [**NetGetDisplayInformationIndex**](netgetdisplayinformationindex.md) | Returns the index of the first display information entry whose name begins with a specified string or alphabetically follows the string. |
| [**NetQueryDisplayInformation**](netquerydisplayinformation.md)       | Returns user, computer, or global group account information.                                                                             |



 

## Group Functions



| Function                                     | Description                                                                       |
|----------------------------------------------|-----------------------------------------------------------------------------------|
| [**NetGroupAdd**](netgroupadd.md)           | Creates a global group.                                                           |
| [**NetGroupAddUser**](netgroupadduser.md)   | Adds one user to an existing global group.                                        |
| [**NetGroupDel**](netgroupdel.md)           | Removes a global group whether or not the group has any members.                  |
| [**NetGroupDelUser**](netgroupdeluser.md)   | Removes one user name from a global group.                                        |
| [**NetGroupEnum**](netgroupenum.md)         | Lists all global groups on a server.                                              |
| [**NetGroupGetInfo**](netgroupgetinfo.md)   | Returns information about a particular global group.                              |
| [**NetGroupGetUsers**](netgroupgetusers.md) | Lists all members of a particular global group.                                   |
| [**NetGroupSetInfo**](netgroupsetinfo.md)   | Sets general information about a global group.                                    |
| [**NetGroupSetUsers**](netgroupsetusers.md) | Assigns members to a new global group; replaces the members of an existing group. |



 

## Local Group Functions



| Function                                                   | Description                                                             |
|------------------------------------------------------------|-------------------------------------------------------------------------|
| [**NetLocalGroupAdd**](netlocalgroupadd.md)               | Creates a local group.                                                  |
| [**NetLocalGroupAddMembers**](netlocalgroupaddmembers.md) | Adds one or more users or global groups to an existing local group.     |
| [**NetLocalGroupDel**](netlocalgroupdel.md)               | Deletes a local group, removing all existing members from the group.    |
| [**NetLocalGroupDelMembers**](netlocalgroupdelmembers.md) | Removes one or more members from an existing local group.               |
| [**NetLocalGroupEnum**](netlocalgroupenum.md)             | Returns information about each local group account on a server.         |
| [**NetLocalGroupGetInfo**](netlocalgroupgetinfo.md)       | Returns information about a particular local group account on a server. |
| [**NetLocalGroupGetMembers**](netlocalgroupgetmembers.md) | Lists all members of a specified local group.                           |
| [**NetLocalGroupSetInfo**](netlocalgroupsetinfo.md)       | Sets general information about a local group.                           |
| [**NetLocalGroupSetMembers**](netlocalgroupsetmembers.md) | Assigns members to a local group.                                       |



 

## Message Functions



| Function                                               | Description                                                                     |
|--------------------------------------------------------|---------------------------------------------------------------------------------|
| [**NetMessageBufferSend**](netmessagebuffersend.md)   | Sends a message to a registered message alias.                                  |
| [**NetMessageNameAdd**](netmessagenameadd.md)         | Registers a message alias in the message name table.                            |
| [**NetMessageNameDel**](netmessagenamedel.md)         | Deletes a message alias from the message name table.                            |
| [**NetMessageNameEnum**](netmessagenameenum.md)       | Lists all the message aliases stored in the message name table.                 |
| [**NetMessageNameGetInfo**](netmessagenamegetinfo.md) | Returns information about a particular message alias in the message name table. |



 

## NetFile Functions



| Function                                | Description                                                          |
|-----------------------------------------|----------------------------------------------------------------------|
| [**NetFileClose**](https://msdn.microsoft.com/library/windows/desktop/bb525377)     | Forces a resource to close.                                          |
| [**NetFileEnum**](https://msdn.microsoft.com/library/windows/desktop/bb525378)       | Returns information about open files on a server.                    |
| [**NetFileGetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525379) | Returns information about a particular opening of a server resource. |



 

## Remote Utility Functions



| Function                                                       | Description                                                                             |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**NetRemoteComputerSupports**](netremotecomputersupports.md) | Queries the redirector to retrieve the optional features that a remote system supports. |
| [**NetRemoteTOD**](netremotetod.md)                           | Enables applications to access the time-of-day information on a remote server.          |



 

## Schedule Functions



| Function                                                                     | Description                                                      |
|------------------------------------------------------------------------------|------------------------------------------------------------------|
| [**NetScheduleJobAdd**](netschedulejobadd.md)                               | Submits a job to run at a specified future date and time.        |
| [**NetScheduleJobDel**](netschedulejobdel.md)                               | Cancels a range of jobs queued to run on a computer.             |
| [**NetScheduleJobEnum**](netschedulejobenum.md)                             | Lists the jobs queued on a specified computer.                   |
| [**NetScheduleJobGetInfo**](netschedulejobgetinfo.md)                       | Returns information about a particular job queued on a computer. |
| [**GetNetScheduleAccountInformation**](getnetscheduleaccountinformation.md) | Retrieves the AT Service account name.                           |
| [**SetNetScheduleAccountInformation**](setnetscheduleaccountinformation.md) | Sets the AT Service account name and password.                   |



 

## Server Functions



| Function                                       | Description                                                                        |
|------------------------------------------------|------------------------------------------------------------------------------------|
| [**NetServerDiskEnum**](netserverdiskenum.md) | Returns a list of local disk drives on a server.                                   |
| [**NetServerEnum**](netserverenum.md)         | Lists all visible servers of a particular type (or types) in the specified domain. |
| [**NetServerGetInfo**](netservergetinfo.md)   | Returns configuration information about a specified server.                        |
| [**NetServerSetInfo**](netserversetinfo.md)   | Sets the operating parameters for a server.                                        |



 

## Server and Workstation Transport Functions



| Function                                                     | Description                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetServerComputerNameAdd**](netservercomputernameadd.md) | Binds an emulated server name to each of the transport protocols on which a server is active. (Combines the functionality of the [**NetServerTransportEnum**](netservertransportenum.md) function and the [**NetServerTransportAddEx**](netservertransportaddex.md) function.)                                            |
| [**NetServerComputerNameDel**](netservercomputernamedel.md) | Disconnects each network transport protocol from an emulated server name set by a previous call to the **NetServerComputerNameAdd** function.                                                                                                                                                                               |
| [**NetServerTransportAdd**](netservertransportadd.md)       | Binds the specified server to the transport protocol. (This function supports only the [**SERVER\_TRANSPORT\_INFO\_0**](server-transport-info-0-str.md) information level.)                                                                                                                                                |
| [**NetServerTransportAddEx**](netservertransportaddex.md)   | Binds the specified server to the transport protocol. (This extended function supports the [**SERVER\_TRANSPORT\_INFO\_1**](server-transport-info-1-str.md), [**SERVER\_TRANSPORT\_INFO\_2**](server-transport-info-2-str.md), and [**SERVER\_TRANSPORT\_INFO\_3**](server-transport-info-3-str.md) information levels.) |
| [**NetServerTransportDel**](netservertransportdel.md)       | Disconnects the transport protocol from the server.                                                                                                                                                                                                                                                                         |
| [**NetServerTransportEnum**](netservertransportenum.md)     | Enumerates the transport protocols managed by the server.                                                                                                                                                                                                                                                                   |
| [**NetWkstaTransportEnum**](netwkstatransportenum.md)       | Lists the transport protocols that are managed by the redirector.                                                                                                                                                                                                                                                           |



 

## Use Functions



| Function                               | Description                                                                               |
|----------------------------------------|-------------------------------------------------------------------------------------------|
| [**NetUseAdd**](netuseadd.md)         | Creates a connection between a local computer and a server.                               |
| [**NetUseDel**](netusedel.md)         | Ends a connection to a shared resource.                                                   |
| [**NetUseEnum**](netuseenum.md)       | Lists all current connections between the local computer and resources on remote servers. |
| [**NetUseGetInfo**](netusegetinfo.md) | Returns information about a connection to a shared resource.                              |



 

## User Functions



| Function                                               | Description                                                         |
|--------------------------------------------------------|---------------------------------------------------------------------|
| [**NetUserAdd**](netuseradd.md)                       | Adds a user account and assigns a password and privilege level.     |
| [**NetUserChangePassword**](netuserchangepassword.md) | Changes a user's password for a specified network server or domain. |
| [**NetUserDel**](netuserdel.md)                       | Deletes a user account from the server.                             |
| [**NetUserEnum**](netuserenum.md)                     | Lists all user accounts on a server.                                |
| [**NetUserGetGroups**](netusergetgroups.md)           | Returns a list of global group names to which a user belongs.       |
| [**NetUserGetInfo**](netusergetinfo.md)               | Returns information about a particular user account on a server.    |
| [**NetUserGetLocalGroups**](netusergetlocalgroups.md) | Returns a list of local group names to which a user belongs.        |
| [**NetUserSetGroups**](netusersetgroups.md)           | Sets global group memberships for a specified user account.         |
| [**NetUserSetInfo**](netusersetinfo.md)               | Sets the password and other elements of a user account.             |



 

## User Modals Functions



| Function                                     | Description                                                                                                                                                                                             |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetUserModalsGet**](netusermodalsget.md) | Returns global information for all users and global groups in the security database, which is the security accounts manager (SAM) database or, in the case of domain controllers, the Active Directory. |
| [**NetUserModalsSet**](netusermodalsset.md) | Sets global information for all users and global groups in the security database.                                                                                                                       |



 

## Validation Functions



| Function                                                               | Description                                                                                                                                                                                                                     |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetValidatePasswordPolicyFree**](netvalidatepasswordpolicyfree.md) | Frees the memory that the [**NetValidatePasswordPolicy**](netvalidatepasswordpolicy.md) function allocates for the *OutputArg* parameter,                                                                                      |
| [**NetValidatePasswordPolicy**](netvalidatepasswordpolicy.md)         | Enables an application to check password compliance against an application-provided account database and verify that passwords meet the complexity, aging, minimum length, and history reuse requirements of a password policy. |



 

## Workstation and Workstation User Functions



| Function                                           | Description                                                                         |
|----------------------------------------------------|-------------------------------------------------------------------------------------|
| [**NetWkstaGetInfo**](netwkstagetinfo.md)         | Returns information about the configuration elements for a workstation.             |
| [**NetWkstaSetInfo**](netwkstasetinfo.md)         | Configures a workstation.                                                           |
| [**NetWkstaUserEnum**](netwkstauserenum.md)       | Lists information about all users currently logged on to the workstation.           |
| [**NetWkstaUserGetInfo**](netwkstausergetinfo.md) | Returns information about one currently logged-on user.                             |
| [**NetWkstaUserSetInfo**](netwkstausersetinfo.md) | Sets the user-specific information for the configuration elements of a workstation. |



 

## Obsolete Functions

-   [**NetAccessAdd**](netaccessadd.md)
-   [**NetAccessCheck**](netaccesscheck.md)
-   [**NetAccessDel**](netaccessdel.md)
-   [**NetAccessEnum**](netaccessenum.md)
-   [**NetAccessGetInfo**](netaccessgetinfo.md)
-   [**NetAccessGetUserPerms**](netaccessgetuserperms.md)
-   [**NetAccessSetInfo**](netaccesssetinfo.md)
-   [**NetAuditClear**](netauditclear.md)
-   [**NetAuditRead**](netauditread.md)
-   [**NetAuditWrite**](netauditwrite.md)
-   [**NetConfigGet**](netconfigget.md)
-   [**NetConfigGetAll**](netconfiggetall.md)
-   [**NetConfigSet**](netconfigset.md)
-   [**NetErrorLogClear**](neterrorlogclear.md)
-   [**NetErrorLogRead**](neterrorlogread.md)
-   [**NetErrorLogWrite**](neterrorlogwrite.md)
-   [**NetLocalGroupAddMember**](netlocalgroupaddmember.md)
-   [**NetLocalGroupDelMember**](netlocalgroupdelmember.md)
-   [**NetServiceControl**](netservicecontrol.md)
-   [**NetServiceEnum**](netserviceenum.md)
-   [**NetServiceGetInfo**](netservicegetinfo.md)
-   [**NetServiceInstall**](netserviceinstall.md)
-   [**NetWkstaTransportAdd**](netwkstatransportadd.md)
-   [**NetWkstaTransportDel**](netwkstatransportdel.md)

## Related topics

<dl> <dt>

[Windows Networking Functions](https://msdn.microsoft.com/library/windows/desktop/aa385391)
</dt> </dl>

 

 




