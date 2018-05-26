---
title: User Functions
description: The network management user functions control a users account in the security database, which is the security accounts manager (SAM) database or, in the case of domain controllers, the Active Directory. The user functions are listed following.
ms.assetid: cf0e5102-3924-46c0-8124-0aa04e95f48d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# User Functions

The network management user functions control a user's account in the security database, which is the security accounts manager (SAM) database or, in the case of domain controllers, the Active Directory. The user functions are listed following.



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



 

Each user or application that accesses network resources must have an account in the security database. The directory services use this account to verify that the user or application has permission to connect to a resource. When a user or an application requests access to a resource, the Windows security system checks for an appropriate user account or group account to permit the access.

Once you remove a user account by calling the [**NetUserDel**](/windows/win32/Lmaccess/nf-lmaccess-netuserdel?branch=master) function, the user can no longer access the server except by using the guest account.

Because a user's password is confidential, it is not returned by the [**NetUserEnum**](/windows/win32/Lmaccess/nf-lmaccess-netuserenum?branch=master) function or the [**NetUserGetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netusergetinfo?branch=master) function. The password is initially assigned when you call [**NetUserAdd**](/windows/win32/Lmaccess/nf-lmaccess-netuseradd?branch=master).

User account information is available at the following levels:

-   [**USER\_INFO\_0**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_0?branch=master)
-   [**USER\_INFO\_1**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1?branch=master)
-   [**USER\_INFO\_2**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_2?branch=master)
-   [**USER\_INFO\_3**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_3?branch=master)
-   [**USER\_INFO\_4**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_4?branch=master)
-   [**USER\_INFO\_10**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_10?branch=master)
-   [**USER\_INFO\_11**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_11?branch=master)
-   [**USER\_INFO\_20**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_20?branch=master)
-   [**USER\_INFO\_21**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_21?branch=master)
-   [**USER\_INFO\_22**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_22?branch=master)
-   [**USER\_INFO\_23**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_23?branch=master)

In addition, the following information levels are valid when you call the [**NetUserSetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netusersetinfo?branch=master) function:

-   [**USER\_INFO\_1003**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1003?branch=master)
-   [**USER\_INFO\_1005**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1005?branch=master)
-   [**USER\_INFO\_1006**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1006?branch=master)
-   [**USER\_INFO\_1007**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1007?branch=master)
-   [**USER\_INFO\_1008**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1008?branch=master)
-   [**USER\_INFO\_1009**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1009?branch=master)
-   [**USER\_INFO\_1010**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1010?branch=master)
-   [**USER\_INFO\_1011**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1011?branch=master)
-   [**USER\_INFO\_1012**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1012?branch=master)
-   [**USER\_INFO\_1014**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1014?branch=master)
-   [**USER\_INFO\_1017**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1017?branch=master)
-   [**USER\_INFO\_1020**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1020?branch=master)
-   [**USER\_INFO\_1024**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1024?branch=master)
-   [**USER\_INFO\_1051**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1051?branch=master)
-   [**USER\_INFO\_1052**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1052?branch=master)
-   [**USER\_INFO\_1053**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_1053?branch=master)

The following functions enable applications to check password compliance.



| Function                                                               | Description                                                                                                |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**NetValidatePasswordPolicyFree**](/windows/win32/Lmaccess/nf-lmaccess-netvalidatepasswordpolicyfree?branch=master) | Frees the memory allocated by the [**NetValidatePasswordPolicy**](/windows/win32/Lmaccess/nf-lmaccess-netvalidatepasswordpolicy?branch=master) function. |
| [**NetValidatePasswordPolicy**](/windows/win32/Lmaccess/nf-lmaccess-netvalidatepasswordpolicy?branch=master)         | Verifies that passwords meet complexity, aging, minimum length, and history reuse requirements.            |



 

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management user functions. For more information, see [**IADsUser**](https://msdn.microsoft.com/library/aa746340) and [**IADsComputer**](https://msdn.microsoft.com/library/aa705980).

 

 




