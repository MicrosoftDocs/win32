---
title: RAS User Administration
description: A RAS server uses a user account database that contains information about a set of user accounts.
ms.assetid: b58767b0-9b76-4d43-953a-ea772643745e
keywords:
- RAS Administration RRAS , user administration
ms.topic: article
ms.date: 05/31/2018
---

# RAS User Administration

A RAS server uses a user account database that contains information about a set of user accounts. The information includes a user's RAS privileges, which are a set of bit flags that determine how the RAS server responds when the user calls to connect. The RAS server administration functions locate the user account database, and get and set the RAS privileges for user accounts.

A RAS server can be part of an operating system domain or it can be a stand-alone machine that runs the server or professional version of the operating system. For a server that is part of a domain, the user account database is stored on the server that is the primary domain controller (PDC). A stand-alone server stores its own local user account database. To get the name of the server that stores the user account database used by a specified RAS server, you can call the [**MprAdminGetPDCServer**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmingetpdcserver) function. You can then use the name of the user account server in a call to the [**NetQueryDisplayInformation**](/windows/win32/api/lmaccess/nf-lmaccess-netquerydisplayinformation) function to enumerate the users in a user account database. You can also use the server name in calls to the [**MprAdminUserGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminusergetinfo) and [**MprAdminUserSetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminusersetinfo) functions to get and set the RAS privileges for a specified user account.

The [**MprAdminUserGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminusergetinfo) and [**MprAdminUserSetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminusersetinfo) functions use the [**RAS\_USER\_0**](/windows/desktop/api/Mprapi/ns-mprapi-ras_user_0) structure to specify a user's RAS privileges and call-back phone number. The RAS privileges indicate the following information:

-   Whether the user can make a remote connection to the server or the domain to which the server belongs.
-   Whether the user establishes a connection through a call back, in which the RAS server hangs up and then calls back to the user to establish the connection.

Each user account specifies one of the following flags to indicate the user's call-back privileges.



| Value                      | Meaning                                                                                                                                                                                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RASPRIV\_NoCallback        | The RAS server does not call back the user to establish a connection.                                                                                                                                                                                                          |
| RASPRIV\_AdminSetCallback  | When the user calls, the RAS server hangs up and calls a preset call-back phone number stored in the user account database. The **szPhoneNumber** member of the [**RAS\_USER\_0**](/windows/desktop/api/Mprapi/ns-mprapi-ras_user_0) structure contains the user's call-back phone number.                       |
| RASPRIV\_CallerSetCallback | When the user calls, the RAS server provides the option of specifying a phone number at which to call back the user. The user can also choose to connect immediately without the call back. The **szPhoneNumber** member contains a default number that the user can override. |



 

 

 