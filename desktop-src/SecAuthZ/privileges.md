---
description: A privilege is the right of an account, such as a user or group account, to perform various system-related operations on the local computer, such as shutting down the system, loading device drivers, or changing the system time.
ms.assetid: 'fe6aae0f-93eb-4aba-a6ac-45e71c251c51'
title: Privileges
ms.topic: article
ms.date: 05/31/2018
---

# Privileges

A [*privilege*](/windows/desktop/SecGloss/p-gly) is the right of an account, such as a user or group account, to perform various system-related operations on the local computer, such as shutting down the system, loading device drivers, or changing the system time. Privileges differ from access rights in two ways:

-   Privileges control access to system resources and system-related tasks, whereas access rights control access to [securable objects](securable-objects.md).
-   A system administrator assigns privileges to user and group accounts, whereas the system grants or denies access to a securable object based on the access rights granted in the ACEs in the object's DACL.

Each system has an account database that stores the privileges held by user and group accounts. When a user logs on, the system produces an [access token](access-tokens.md) that contains a list of the user's privileges, including those granted to the user or to groups to which the user belongs. Note that the privileges apply only to the local computer; a domain account can have different privileges on different computers.

When the user tries to perform a privileged operation, the system checks the user's access token to determine whether the user holds the necessary privileges, and if so, it checks whether the privileges are enabled. If the user fails these tests, the system does not perform the operation.

To determine the privileges held in an access token, call the [**GetTokenInformation**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-gettokeninformation) function, which also indicates which privileges are enabled. Most privileges are disabled by default.

The Windows API defines a set of string constants, such as SE\_ASSIGNPRIMARYTOKEN\_NAME, to identify the various privileges. These constants are the same on all systems and are defined in Winnt.h. For a table of the privileges defined by Windows, see [Privilege Constants](authorization-constants.md). However, the functions that get and adjust the privileges in an access token use the [**LUID**](/windows/desktop/api/Winnt/ns-winnt-luid) type to identify privileges. The **LUID** values for a privilege can differ from one computer to another, and from one boot to another on the same computer. To get the current **LUID** that corresponds to one of the string constants, use the [**LookupPrivilegeValue**](/windows/desktop/api/Winbase/nf-winbase-lookupprivilegevaluea) function. Use the [**LookupPrivilegeName**](/windows/desktop/api/Winbase/nf-winbase-lookupprivilegenamea) function to convert a **LUID** to its corresponding string constant.

The system provides a set of display names that describe each of the privileges. These are useful when you need to display a description of a privilege to the user. Use the [**LookupPrivilegeDisplayName**](/windows/desktop/api/Winbase/nf-winbase-lookupprivilegedisplaynamea) function to retrieve a description string that corresponds to the string constant for a privilege. For example, on systems that use U.S. English, the display name for the SE\_SYSTEMTIME\_NAME privilege is "Change the system time".

You can use the [**PrivilegeCheck**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-privilegecheck) function to determine whether an access token holds a specified set of privileges. This is useful primarily to server applications that are impersonating a client.

A system administrator can use administrative tools, such as User Manager, to add or remove privileges for user and group accounts. Administrators can programmatically use the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) functions to work with privileges. The [**LsaAddAccountRights**](/windows/desktop/api/ntsecapi/nf-ntsecapi-lsaaddaccountrights) and [**LsaRemoveAccountRights**](/windows/desktop/api/ntsecapi/nf-ntsecapi-lsaremoveaccountrights) functions add or remove privileges from an account. The [**LsaEnumerateAccountRights**](/windows/desktop/api/ntsecapi/nf-ntsecapi-lsaenumerateaccountrights) function enumerates the privileges held by a specified account. The [**LsaEnumerateAccountsWithUserRight**](/windows/desktop/api/ntsecapi/nf-ntsecapi-lsaenumerateaccountswithuserright) function enumerates the accounts that hold a specified privilege.

## Related topics

<dl> <dt>

[Authorization Constants](authorization-constants.md)
</dt> <dt>

[Enabling and Disabling Privileges in C++](enabling-and-disabling-privileges-in-c--.md)
</dt> </dl>

 

 
