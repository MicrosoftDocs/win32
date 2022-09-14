---
title: User Functions
description: The network management user functions control a user's account in the security database, which is the security accounts manager (SAM) database or, in the case of domain controllers, the Active Directory. The user functions are listed following.
ms.assetid: cf0e5102-3924-46c0-8124-0aa04e95f48d
ms.topic: article
ms.date: 05/31/2018
---

# User Functions

The network management user functions control a user's account in the security database, which is the security accounts manager (SAM) database or, in the case of domain controllers, the Active Directory. The user functions are listed following.



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



 

Each user or application that accesses network resources must have an account in the security database. The directory services use this account to verify that the user or application has permission to connect to a resource. When a user or an application requests access to a resource, the Windows security system checks for an appropriate user account or group account to permit the access.

Once you remove a user account by calling the [**NetUserDel**](/windows/desktop/api/Lmaccess/nf-lmaccess-netuserdel) function, the user can no longer access the server except by using the guest account.

Because a user's password is confidential, it is not returned by the [**NetUserEnum**](/windows/desktop/api/Lmaccess/nf-lmaccess-netuserenum) function or the [**NetUserGetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusergetinfo) function. The password is initially assigned when you call [**NetUserAdd**](/windows/desktop/api/Lmaccess/nf-lmaccess-netuseradd).

User account information is available at the following levels:

-   [**USER\_INFO\_0**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_0)
-   [**USER\_INFO\_1**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1)
-   [**USER\_INFO\_2**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_2)
-   [**USER\_INFO\_3**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_3)
-   [**USER\_INFO\_4**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_4)
-   [**USER\_INFO\_10**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_10)
-   [**USER\_INFO\_11**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_11)
-   [**USER\_INFO\_20**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_20)
-   [**USER\_INFO\_21**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_21)
-   [**USER\_INFO\_22**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_22)
-   [**USER\_INFO\_23**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_23)

In addition, the following information levels are valid when you call the [**NetUserSetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusersetinfo) function:

-   [**USER\_INFO\_1003**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1003)
-   [**USER\_INFO\_1005**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1005)
-   [**USER\_INFO\_1006**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1006)
-   [**USER\_INFO\_1007**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1007)
-   [**USER\_INFO\_1008**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1008)
-   [**USER\_INFO\_1009**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1009)
-   [**USER\_INFO\_1010**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1010)
-   [**USER\_INFO\_1011**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1011)
-   [**USER\_INFO\_1012**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1012)
-   [**USER\_INFO\_1014**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1014)
-   [**USER\_INFO\_1017**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1017)
-   [**USER\_INFO\_1020**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1020)
-   [**USER\_INFO\_1024**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1024)
-   [**USER\_INFO\_1051**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1051)
-   [**USER\_INFO\_1052**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1052)
-   [**USER\_INFO\_1053**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_1053)

The following functions enable applications to check password compliance.



| Function                                                               | Description                                                                                                |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**NetValidatePasswordPolicyFree**](/windows/desktop/api/Lmaccess/nf-lmaccess-netvalidatepasswordpolicyfree) | Frees the memory allocated by the [**NetValidatePasswordPolicy**](/windows/desktop/api/Lmaccess/nf-lmaccess-netvalidatepasswordpolicy) function. |
| [**NetValidatePasswordPolicy**](/windows/desktop/api/Lmaccess/nf-lmaccess-netvalidatepasswordpolicy)         | Verifies that passwords meet complexity, aging, minimum length, and history reuse requirements.            |



 

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management user functions. For more information, see [**IADsUser**](/windows/desktop/api/iads/nn-iads-iadsuser) and [**IADsComputer**](/windows/desktop/api/iads/nn-iads-iadscomputer).

 

 