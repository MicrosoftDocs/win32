---
title: User Functions
description: The network management user functions control a user's account in the security database, which is the security accounts manager (SAM) database or, in the case of domain controllers, the Active Directory. The user functions are listed following.
ms.assetid: 'cf0e5102-3924-46c0-8124-0aa04e95f48d'
---

# User Functions

The network management user functions control a user's account in the security database, which is the security accounts manager (SAM) database or, in the case of domain controllers, the Active Directory. The user functions are listed following.



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



 

Each user or application that accesses network resources must have an account in the security database. The directory services use this account to verify that the user or application has permission to connect to a resource. When a user or an application requests access to a resource, the Windows security system checks for an appropriate user account or group account to permit the access.

Once you remove a user account by calling the [**NetUserDel**](netuserdel.md) function, the user can no longer access the server except by using the guest account.

Because a user's password is confidential, it is not returned by the [**NetUserEnum**](netuserenum.md) function or the [**NetUserGetInfo**](netusergetinfo.md) function. The password is initially assigned when you call [**NetUserAdd**](netuseradd.md).

User account information is available at the following levels:

-   [**USER\_INFO\_0**](user-info-0-str.md)
-   [**USER\_INFO\_1**](user-info-1-str.md)
-   [**USER\_INFO\_2**](user-info-2-str.md)
-   [**USER\_INFO\_3**](user-info-3-str.md)
-   [**USER\_INFO\_4**](user-info-4-str.md)
-   [**USER\_INFO\_10**](user-info-10-str.md)
-   [**USER\_INFO\_11**](user-info-11-str.md)
-   [**USER\_INFO\_20**](user-info-20-str.md)
-   [**USER\_INFO\_21**](user-info-21-str.md)
-   [**USER\_INFO\_22**](user-info-22-str.md)
-   [**USER\_INFO\_23**](user-info-23-str.md)

In addition, the following information levels are valid when you call the [**NetUserSetInfo**](netusersetinfo.md) function:

-   [**USER\_INFO\_1003**](user-info-1003-str.md)
-   [**USER\_INFO\_1005**](user-info-1005-str.md)
-   [**USER\_INFO\_1006**](user-info-1006-str.md)
-   [**USER\_INFO\_1007**](user-info-1007-str.md)
-   [**USER\_INFO\_1008**](user-info-1008-str.md)
-   [**USER\_INFO\_1009**](user-info-1009-str.md)
-   [**USER\_INFO\_1010**](user-info-1010-str.md)
-   [**USER\_INFO\_1011**](user-info-1011-str.md)
-   [**USER\_INFO\_1012**](user-info-1012-str.md)
-   [**USER\_INFO\_1014**](user-info-1014-str.md)
-   [**USER\_INFO\_1017**](user-info-1017-str.md)
-   [**USER\_INFO\_1020**](user-info-1020-str.md)
-   [**USER\_INFO\_1024**](user-info-1024-str.md)
-   [**USER\_INFO\_1051**](user-info-1051-str.md)
-   [**USER\_INFO\_1052**](user-info-1052-str.md)
-   [**USER\_INFO\_1053**](user-info-1053-str.md)

The following functions enable applications to check password compliance.



| Function                                                               | Description                                                                                                |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**NetValidatePasswordPolicyFree**](netvalidatepasswordpolicyfree.md) | Frees the memory allocated by the [**NetValidatePasswordPolicy**](netvalidatepasswordpolicy.md) function. |
| [**NetValidatePasswordPolicy**](netvalidatepasswordpolicy.md)         | Verifies that passwords meet complexity, aging, minimum length, and history reuse requirements.            |



 

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management user functions. For more information, see [**IADsUser**](https://msdn.microsoft.com/library/aa746340) and [**IADsComputer**](https://msdn.microsoft.com/library/aa705980).

 

 




