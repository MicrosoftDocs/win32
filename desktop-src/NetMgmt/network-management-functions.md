---
title: Network Management Functions
description: The network management functions can be grouped as follows.
ms.assetid: 'dd159e2e-f37e-46b2-b980-008b73d40b39'
ms.topic: article
ms.date: 05/31/2018
---

# Network Management Functions

The network management functions can be grouped as follows.

## Alert Functions



| Function                                   | Description                                                                                                                                                                                            |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetAlertRaise**](/windows/desktop/api/Lmalert/nf-lmalert-netalertraise)     | Notifies all registered clients that a particular event has occurred.                                                                                                                                  |
| [**NetAlertRaiseEx**](/windows/desktop/api/Lmalert/nf-lmalert-netalertraiseex) | Simplifies notifying registered clients that a particular event has occurred, because, unlike **NetAlertRaise**, **NetAlertRaiseEx** does not require a [**STD\_ALERT**](/windows/desktop/api/Lmalert/ns-lmalert-std_alert) structure. |



 

## API Buffer Functions



| Function                                                 | Description                                                                                                               |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**NetApiBufferAllocate**](/windows/desktop/api/Lmapibuf/nf-lmapibuf-netapibufferallocate)     | Allocates memory from the heap. Call this function when you require compatibility with the **NetApiBufferFree** function. |
| [**NetApiBufferFree**](/windows/desktop/api/Lmapibuf/nf-lmapibuf-netapibufferfree)             | Frees memory allocated by the **NetApiBufferAllocate** function and other network management functions.                   |
| [**NetApiBufferReallocate**](/windows/desktop/api/Lmapibuf/nf-lmapibuf-netapibufferreallocate) | Changes the size of a buffer allocated by a call to the **NetApiBufferAllocate** function.                                |
| [**NetApiBufferSize**](/windows/desktop/api/Lmapibuf/nf-lmapibuf-netapibuffersize)             | Returns the size, in bytes, of a buffer allocated by a call to the **NetApiBufferAllocate** function.                     |



 

## Azure Active Directory Join Information Functions



| Function                                                       | Description                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetFreeAadJoinInformation**](/windows/desktop/api/lmjoin/nf-lmjoin-netfreeaadjoininformation) | Frees the memory allocated for the specified [**DSREG\_JOIN\_INFO**](/windows/desktop/api/lmjoin/ns-lmjoin-dsreg_join_info) structure, which contains join information for a tenant and which you retrieved by calling the [**NetGetAadJoinInformation**](/windows/desktop/api/lmjoin/nf-lmjoin-netgetaadjoininformation) function. |
| [**NetGetAadJoinInformation**](/windows/desktop/api/lmjoin/nf-lmjoin-netgetaadjoininformation)   | Retrieves the join information for the specified tenant. This function examines the join information for Microsoft Azure Active Directory and the work account that the current user added.                                                                     |



 

## Directory Service and Domain Join Functions



| Function                                                                             | Description                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetAddAlternateComputerName**](/windows/desktop/api/Lmjoin/nf-lmjoin-netaddalternatecomputername)                   | Adds an alternate name for the specified computer.                                                                                                                                                                                                                      |
| [**NetCreateProvisioningPackage**](/windows/desktop/api/Lmjoin/nf-lmjoin-netprovisioncomputeraccount)                  | Provisions a computer account for later use in an offline domain join operation.                                                                                                                                                                                        |
| [**NetEnumerateComputerNames**](/windows/desktop/api/Lmjoin/nf-lmjoin-netenumeratecomputernames)                       | Enumerates names for the specified computer.                                                                                                                                                                                                                            |
| [**NetGetJoinableOUs**](/windows/desktop/api/Lmjoin/nf-lmjoin-netgetjoinableous)                                       | Retrieves a list of organizational units (OUs) in which a computer account can be created.                                                                                                                                                                              |
| [**NetGetJoinInformation**](/windows/desktop/api/Lmjoin/nf-lmjoin-netgetjoininformation)                               | Retrieves join status information for the specified computer.                                                                                                                                                                                                           |
| [**NetJoinDomain**](/windows/desktop/api/Lmjoin/nf-lmjoin-netjoindomain)                                               | Joins a computer to a workgroup or domain.                                                                                                                                                                                                                              |
| [**NetProvisionComputerAccount**](/windows/desktop/api/Lmjoin/nf-lmjoin-netprovisioncomputeraccount)                   | Provisions a computer account for later used in an offline domain join operation.                                                                                                                                                                                       |
| [**NetRemoveAlternateComputerName**](/windows/desktop/api/Lmjoin/nf-lmjoin-netremovealternatecomputername)             | Removes an alternate name for the specified computer.                                                                                                                                                                                                                   |
| [**NetRenameMachineInDomain**](/windows/desktop/api/Lmjoin/nf-lmjoin-netrenamemachineindomain)                         | Changes the name of a computer in a domain.                                                                                                                                                                                                                             |
| [**NetRequestOfflineDomainJoin**](/windows/desktop/api/Lmjoin/nf-lmjoin-netrequestofflinedomainjoin)                   | Executes locally on a machine to modify a Windows operating system image mounted on a volume. The registry is loaded for the image and provisioning blob data is written where it can be retrieved during the completion phase of an offline domain join operation.     |
| [**NetRequestProvisioningPackageInstall**](/windows/desktop/api/Lmjoin/nf-lmjoin-netrequestprovisioningpackageinstall) | Executes locally on a machine to modify a Windows operating system image mounted on a volume. The registry is loaded from the image and provisioning package data is written where it can be retrieved during the completion phase of an offline domain join operation. |
| [**NetSetPrimaryComputerName**](/windows/desktop/api/Lmjoin/nf-lmjoin-netsetprimarycomputername)                       | Sets the primary computer name for the specified computer.                                                                                                                                                                                                              |
| [**NetUnjoinDomain**](/windows/desktop/api/Lmjoin/nf-lmjoin-netunjoindomain)                                           | Unjoins a computer from a workgroup or a domain.                                                                                                                                                                                                                        |
| [**NetValidateName**](/windows/desktop/api/Lmjoin/nf-lmjoin-netvalidatename)                                           | Verifies the validity of a computer name, workgroup name, or domain name.                                                                                                                                                                                               |



 

## Get Functions



| Function                                                               | Description                                                                                                                              |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetGetAnyDCName**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgetanydcname)                             | Returns the name of any domain controller for a domain that is directly trusted by a specified server.                                   |
| [**NetGetDCName**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgetdcname)                                   | Returns the name of the primary domain controller (PDC) for the specified domain.                                                        |
| [**NetGetDisplayInformationIndex**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgetdisplayinformationindex) | Returns the index of the first display information entry whose name begins with a specified string or alphabetically follows the string. |
| [**NetQueryDisplayInformation**](/windows/desktop/api/Lmaccess/nf-lmaccess-netquerydisplayinformation)       | Returns user, computer, or global group account information.                                                                             |



 

## Group Functions



| Function                                     | Description                                                                       |
|----------------------------------------------|-----------------------------------------------------------------------------------|
| [**NetGroupAdd**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupadd)           | Creates a global group.                                                           |
| [**NetGroupAddUser**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupadduser)   | Adds one user to an existing global group.                                        |
| [**NetGroupDel**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupdel)           | Removes a global group whether or not the group has any members.                  |
| [**NetGroupDelUser**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupdeluser)   | Removes one user name from a global group.                                        |
| [**NetGroupEnum**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupenum)         | Lists all global groups on a server.                                              |
| [**NetGroupGetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupgetinfo)   | Returns information about a particular global group.                              |
| [**NetGroupGetUsers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupgetusers) | Lists all members of a particular global group.                                   |
| [**NetGroupSetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupsetinfo)   | Sets general information about a global group.                                    |
| [**NetGroupSetUsers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupsetusers) | Assigns members to a new global group; replaces the members of an existing group. |



 

## Local Group Functions



| Function                                                   | Description                                                             |
|------------------------------------------------------------|-------------------------------------------------------------------------|
| [**NetLocalGroupAdd**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupadd)               | Creates a local group.                                                  |
| [**NetLocalGroupAddMembers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupaddmembers) | Adds one or more users or global groups to an existing local group.     |
| [**NetLocalGroupDel**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupdel)               | Deletes a local group, removing all existing members from the group.    |
| [**NetLocalGroupDelMembers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupdelmembers) | Removes one or more members from an existing local group.               |
| [**NetLocalGroupEnum**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupenum)             | Returns information about each local group account on a server.         |
| [**NetLocalGroupGetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupgetinfo)       | Returns information about a particular local group account on a server. |
| [**NetLocalGroupGetMembers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupgetmembers) | Lists all members of a specified local group.                           |
| [**NetLocalGroupSetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupsetinfo)       | Sets general information about a local group.                           |
| [**NetLocalGroupSetMembers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupsetmembers) | Assigns members to a local group.                                       |



 

## Message Functions



| Function                                               | Description                                                                     |
|--------------------------------------------------------|---------------------------------------------------------------------------------|
| [**NetMessageBufferSend**](/windows/desktop/api/Lmmsg/nf-lmmsg-netmessagebuffersend)   | Sends a message to a registered message alias.                                  |
| [**NetMessageNameAdd**](/windows/desktop/api/Lmmsg/nf-lmmsg-netmessagenameadd)         | Registers a message alias in the message name table.                            |
| [**NetMessageNameDel**](/windows/desktop/api/Lmmsg/nf-lmmsg-netmessagenamedel)         | Deletes a message alias from the message name table.                            |
| [**NetMessageNameEnum**](/windows/desktop/api/Lmmsg/nf-lmmsg-netmessagenameenum)       | Lists all the message aliases stored in the message name table.                 |
| [**NetMessageNameGetInfo**](/windows/desktop/api/Lmmsg/nf-lmmsg-netmessagenamegetinfo) | Returns information about a particular message alias in the message name table. |



 

## NetFile Functions



| Function                                | Description                                                          |
|-----------------------------------------|----------------------------------------------------------------------|
| [**NetFileClose**](/windows/desktop/api/lmshare/nf-lmshare-netfileclose)     | Forces a resource to close.                                          |
| [**NetFileEnum**](/windows/desktop/api/lmshare/nf-lmshare-netfileenum)       | Returns information about open files on a server.                    |
| [**NetFileGetInfo**](/windows/desktop/api/lmshare/nf-lmshare-netfilegetinfo) | Returns information about a particular opening of a server resource. |



 

## Remote Utility Functions



| Function                                                       | Description                                                                             |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**NetRemoteComputerSupports**](/windows/desktop/api/Lmremutl/nf-lmremutl-netremotecomputersupports) | Queries the redirector to retrieve the optional features that a remote system supports. |
| [**NetRemoteTOD**](/windows/desktop/api/Lmremutl/nf-lmremutl-netremotetod)                           | Enables applications to access the time-of-day information on a remote server.          |



 

## Schedule Functions



| Function                                                                     | Description                                                      |
|------------------------------------------------------------------------------|------------------------------------------------------------------|
| [**NetScheduleJobAdd**](/windows/desktop/api/Lmat/nf-lmat-netschedulejobadd)                               | Submits a job to run at a specified future date and time.        |
| [**NetScheduleJobDel**](/windows/desktop/api/Lmat/nf-lmat-netschedulejobdel)                               | Cancels a range of jobs queued to run on a computer.             |
| [**NetScheduleJobEnum**](/windows/desktop/api/Lmat/nf-lmat-netschedulejobenum)                             | Lists the jobs queued on a specified computer.                   |
| [**NetScheduleJobGetInfo**](/windows/desktop/api/Lmat/nf-lmat-netschedulejobgetinfo)                       | Returns information about a particular job queued on a computer. |
| [**GetNetScheduleAccountInformation**](/windows/desktop/api/AtAcct/nf-atacct-getnetscheduleaccountinformation) | Retrieves the AT Service account name.                           |
| [**SetNetScheduleAccountInformation**](/windows/desktop/api/AtAcct/nf-atacct-setnetscheduleaccountinformation) | Sets the AT Service account name and password.                   |



 

## Server Functions



| Function                                       | Description                                                                        |
|------------------------------------------------|------------------------------------------------------------------------------------|
| [**NetServerDiskEnum**](/windows/desktop/api/Lmserver/nf-lmserver-netserverdiskenum) | Returns a list of local disk drives on a server.                                   |
| [**NetServerEnum**](/windows/desktop/api/Lmserver/nf-lmserver-netserverenum)         | Lists all visible servers of a particular type (or types) in the specified domain. |
| [**NetServerGetInfo**](/windows/desktop/api/Lmserver/nf-lmserver-netservergetinfo)   | Returns configuration information about a specified server.                        |
| [**NetServerSetInfo**](/windows/desktop/api/Lmserver/nf-lmserver-netserversetinfo)   | Sets the operating parameters for a server.                                        |



 

## Server and Workstation Transport Functions



| Function                                                     | Description                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetServerComputerNameAdd**](/windows/desktop/api/Lmserver/nf-lmserver-netservercomputernameadd) | Binds an emulated server name to each of the transport protocols on which a server is active. (Combines the functionality of the [**NetServerTransportEnum**](/windows/desktop/api/Lmserver/nf-lmserver-netservertransportenum) function and the [**NetServerTransportAddEx**](/windows/desktop/api/Lmserver/nf-lmserver-netservertransportaddex) function.)                                            |
| [**NetServerComputerNameDel**](/windows/desktop/api/Lmserver/nf-lmserver-netservercomputernamedel) | Disconnects each network transport protocol from an emulated server name set by a previous call to the **NetServerComputerNameAdd** function.                                                                                                                                                                               |
| [**NetServerTransportAdd**](/windows/desktop/api/Lmserver/nf-lmserver-netservertransportadd)       | Binds the specified server to the transport protocol. (This function supports only the [**SERVER\_TRANSPORT\_INFO\_0**](/windows/desktop/api/Lmserver/ns-lmserver-server_transport_info_0) information level.)                                                                                                                                                |
| [**NetServerTransportAddEx**](/windows/desktop/api/Lmserver/nf-lmserver-netservertransportaddex)   | Binds the specified server to the transport protocol. (This extended function supports the [**SERVER\_TRANSPORT\_INFO\_1**](/windows/desktop/api/Lmserver/ns-lmserver-server_transport_info_1), [**SERVER\_TRANSPORT\_INFO\_2**](/windows/desktop/api/Lmserver/ns-lmserver-server_transport_info_2), and [**SERVER\_TRANSPORT\_INFO\_3**](/windows/desktop/api/Lmserver/ns-lmserver-server_transport_info_3) information levels.) |
| [**NetServerTransportDel**](/windows/desktop/api/Lmserver/nf-lmserver-netservertransportdel)       | Disconnects the transport protocol from the server.                                                                                                                                                                                                                                                                         |
| [**NetServerTransportEnum**](/windows/desktop/api/Lmserver/nf-lmserver-netservertransportenum)     | Enumerates the transport protocols managed by the server.                                                                                                                                                                                                                                                                   |
| [**NetWkstaTransportEnum**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstatransportenum)       | Lists the transport protocols that are managed by the redirector.                                                                                                                                                                                                                                                           |



 

## Use Functions



| Function                               | Description                                                                               |
|----------------------------------------|-------------------------------------------------------------------------------------------|
| [**NetUseAdd**](/windows/desktop/api/Lmuse/nf-lmuse-netuseadd)         | Creates a connection between a local computer and a server.                               |
| [**NetUseDel**](/windows/desktop/api/Lmuse/nf-lmuse-netusedel)         | Ends a connection to a shared resource.                                                   |
| [**NetUseEnum**](/windows/desktop/api/Lmuse/nf-lmuse-netuseenum)       | Lists all current connections between the local computer and resources on remote servers. |
| [**NetUseGetInfo**](/windows/desktop/api/Lmuse/nf-lmuse-netusegetinfo) | Returns information about a connection to a shared resource.                              |



 

## User Functions



| Function                                               | Description                                                         |
|--------------------------------------------------------|---------------------------------------------------------------------|
| [**NetUserAdd**](/windows/desktop/api/Lmaccess/nf-lmaccess-netuseradd)                       | Adds a user account and assigns a password and privilege level.     |
| [**NetUserChangePassword**](/windows/desktop/api/Lmaccess/nf-lmaccess-netuserchangepassword) | Changes a user's password for a specified network server or domain. |
| [**NetUserDel**](/windows/desktop/api/Lmaccess/nf-lmaccess-netuserdel)                       | Deletes a user account from the server.                             |
| [**NetUserEnum**](/windows/desktop/api/Lmaccess/nf-lmaccess-netuserenum)                     | Lists all user accounts on a server.                                |
| [**NetUserGetGroups**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusergetgroups)           | Returns a list of global group names to which a user belongs.       |
| [**NetUserGetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusergetinfo)               | Returns information about a particular user account on a server.    |
| [**NetUserGetLocalGroups**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusergetlocalgroups) | Returns a list of local group names to which a user belongs.        |
| [**NetUserSetGroups**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusersetgroups)           | Sets global group memberships for a specified user account.         |
| [**NetUserSetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusersetinfo)               | Sets the password and other elements of a user account.             |



 

## User Modals Functions



| Function                                     | Description                                                                                                                                                                                             |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetUserModalsGet**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusermodalsget) | Returns global information for all users and global groups in the security database, which is the security accounts manager (SAM) database or, in the case of domain controllers, the Active Directory. |
| [**NetUserModalsSet**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusermodalsset) | Sets global information for all users and global groups in the security database.                                                                                                                       |



 

## Validation Functions



| Function                                                               | Description                                                                                                                                                                                                                     |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetValidatePasswordPolicyFree**](/windows/desktop/api/Lmaccess/nf-lmaccess-netvalidatepasswordpolicyfree) | Frees the memory that the [**NetValidatePasswordPolicy**](/windows/desktop/api/Lmaccess/nf-lmaccess-netvalidatepasswordpolicy) function allocates for the *OutputArg* parameter,                                                                                      |
| [**NetValidatePasswordPolicy**](/windows/desktop/api/Lmaccess/nf-lmaccess-netvalidatepasswordpolicy)         | Enables an application to check password compliance against an application-provided account database and verify that passwords meet the complexity, aging, minimum length, and history reuse requirements of a password policy. |



 

## Workstation and Workstation User Functions



| Function                                           | Description                                                                         |
|----------------------------------------------------|-------------------------------------------------------------------------------------|
| [**NetWkstaGetInfo**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstagetinfo)         | Returns information about the configuration elements for a workstation.             |
| [**NetWkstaSetInfo**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstasetinfo)         | Configures a workstation.                                                           |
| [**NetWkstaUserEnum**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstauserenum)       | Lists information about all users currently logged on to the workstation.           |
| [**NetWkstaUserGetInfo**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstausergetinfo) | Returns information about one currently logged-on user.                             |
| [**NetWkstaUserSetInfo**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstausersetinfo) | Sets the user-specific information for the configuration elements of a workstation. |



 

## Obsolete Functions

-   [**NetAccessAdd**](/windows/desktop/api/lmaccess/nf-lmaccess-netaccessadd)
-   [**NetAccessCheck**](/previous-versions/windows/desktop/legacy/aa370291(v=vs.85))
-   [**NetAccessDel**](/windows/desktop/api/lmaccess/nf-lmaccess-netaccessdel)
-   [**NetAccessEnum**](/windows/desktop/api/lmaccess/nf-lmaccess-netaccessenum)
-   [**NetAccessGetInfo**](/windows/desktop/api/lmaccess/nf-lmaccess-netaccessgetinfo)
-   [**NetAccessGetUserPerms**](/windows/desktop/api/lmaccess/nf-lmaccess-netaccessgetuserperms)
-   [**NetAccessSetInfo**](/windows/desktop/api/lmaccess/nf-lmaccess-netaccesssetinfo)
-   [**NetAuditClear**](netauditclear.md)
-   [**NetAuditRead**](netauditread.md)
-   [**NetAuditWrite**](netauditwrite.md)
-   [**NetConfigGet**](netconfigget.md)
-   [**NetConfigGetAll**](netconfiggetall.md)
-   [**NetConfigSet**](netconfigset.md)
-   [**NetErrorLogClear**](neterrorlogclear.md)
-   [**NetErrorLogRead**](neterrorlogread.md)
-   [**NetErrorLogWrite**](neterrorlogwrite.md)
-   [**NetLocalGroupAddMember**](/windows/desktop/api/lmaccess/nf-lmaccess-netlocalgroupaddmember)
-   [**NetLocalGroupDelMember**](/windows/desktop/api/lmaccess/nf-lmaccess-netlocalgroupdelmember)
-   [**NetServiceControl**](netservicecontrol.md)
-   [**NetServiceEnum**](netserviceenum.md)
-   [**NetServiceGetInfo**](netservicegetinfo.md)
-   [**NetServiceInstall**](netserviceinstall.md)
-   [**NetWkstaTransportAdd**](/windows/desktop/api/lmwksta/nf-lmwksta-netwkstatransportadd)
-   [**NetWkstaTransportDel**](/windows/desktop/api/lmwksta/nf-lmwksta-netwkstatransportdel)

## Related topics

<dl> <dt>

[Windows Networking Functions](/windows/desktop/WNet/windows-networking-functions)
</dt> </dl>

 

 