---
title: RAS User Account Administration
description: A Windows NT 4.0 RAS server uses a user account database that contains information about a set of user accounts.
ms.assetid: 653307f8-3b14-474a-9094-03a2d4c89092
ms.topic: article
ms.date: 05/31/2018
---

# RAS User Account Administration

A Windows NT 4.0 RAS server uses a user account database that contains information about a set of user accounts. The information includes a user's RAS privileges, which are a set of bit flags that determine how the RAS server responds when the user calls to connect. The RAS server administration functions enable you to locate the user account database, and to get and set the RAS privileges for user accounts.

A Windows NT 4.0 RAS server can be part of a Windows NT/Windows 2000 domain, or it can be a stand-alone Windows NT Server or Workstation that is not part of a domain. For a server that is part of a domain, the user account database is stored on the server that is the primary domain controller (PDC). A stand-alone server stores its own local user account database. To get the name of the server that stores the user account database used by a specified RAS server, you can call the [**RasAdminGetUserAccountServer**](rasadmingetuseraccountserver.md) function. You can then use the name of the user account server in a call to the [**NetQueryDisplayInformation**](/windows/win32/api/lmaccess/nf-lmaccess-netquerydisplayinformation) function to enumerate the users in a user account database. You can also use the server name in calls to the [**RasAdminUserGetInfo**](rasadminusergetinfo.md) and [**RasAdminUserSetInfo**](rasadminusersetinfo.md) functions to get and set the RAS privileges for a specified user account.

The [**RasAdminUserGetInfo**](rasadminusergetinfo.md) and [**RasAdminUserSetInfo**](rasadminusersetinfo.md) functions use the [**RAS\_USER\_0**](ras-user-0-str.md) structure to specify a user's RAS privileges and call-back phone number. The RAS privileges indicate the following information:

-   Whether the user can make a remote connection to the server or the domain to which the server belongs.
-   Whether the user can establish a connection through a call-back, in which the RAS server hangs up and then calls back to the user to establish the connection.

Each user account specifies one of the following flags to indicate the user's call-back privilege.



| Value                      | Meaning                                                                                                                                                                                                                                                      |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RASPRIV\_NoCallback        | The RAS server will not call back the user to establish a connection.                                                                                                                                                                                        |
| RASPRIV\_AdminSetCallback  | When the user calls, the RAS server hangs up and calls a preset call-back phone number stored in the user account database. The **szPhoneNumber** member of the [**RAS\_USER\_0**](ras-user-0-str.md) structure contains the user's call-back phone number. |
| RASPRIV\_CallerSetCallback | When the user calls, the RAS server provides the option of specifying a call-back phone number. The user can also choose to connect immediately without a call back. The **szPhoneNumber** member contains a default number that the user can override.      |



 

 

 