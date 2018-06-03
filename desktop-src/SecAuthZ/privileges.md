---
Description: A privilege is the right of an account, such as a user or group account, to perform various system-related operations on the local computer, such as shutting down the system, loading device drivers, or changing the system time.
ms.assetid: 8e3f70cd-814e-4aab-8f48-0ca482beef2e
title: Privileges
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Privileges

A [*privilege*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-privilege-gly) is the right of an account, such as a user or group account, to perform various system-related operations on the local computer, such as shutting down the system, loading device drivers, or changing the system time. Privileges differ from access rights in two ways:

-   Privileges control access to system resources and system-related tasks, whereas access rights control access to [securable objects](securable-objects.md).
-   A system administrator assigns privileges to user and group accounts, whereas the system grants or denies access to a securable object based on the access rights granted in the ACEs in the object's DACL.

Each system has an account database that stores the privileges held by user and group accounts. When a user logs on, the system produces an [access token](access-tokens.md) that contains a list of the user's privileges, including those granted to the user or to groups to which the user belongs. Note that the privileges apply only to the local computer; a domain account can have different privileges on different computers.

When the user tries to perform a privileged operation, the system checks the user's access token to determine whether the user holds the necessary privileges, and if so, it checks whether the privileges are enabled. If the user fails these tests, the system does not perform the operation.

To determine the privileges held in an access token, call the [**GetTokenInformation**](https://www.bing.com/search?q=**GetTokenInformation**) function, which also indicates which privileges are enabled. Most privileges are disabled by default.

The Windows API defines a set of string constants, such as SE\_ASSIGNPRIMARYTOKEN\_NAME, to identify the various privileges. These constants are the same on all systems and are defined in Winnt.h. For a table of the privileges defined by Windows, see [Privilege Constants](https://www.bing.com/search?q=Privilege Constants). However, the functions that get and adjust the privileges in an access token use the [**LUID**](/windows/desktop/api/Winnt/ns-winnt-_luid) type to identify privileges. The **LUID** values for a privilege can differ from one computer to another, and from one boot to another on the same computer. To get the current **LUID** that corresponds to one of the string constants, use the [**LookupPrivilegeValue**](/windows/desktop/api/Winbase/nf-winbase-lookupprivilegevaluea) function. Use the [**LookupPrivilegeName**](/windows/desktop/api/Winbase/nf-winbase-lookupprivilegenamea) function to convert a **LUID** to its corresponding string constant.

The system provides a set of display names that describe each of the privileges. These are useful when you need to display a description of a privilege to the user. Use the [**LookupPrivilegeDisplayName**](/windows/desktop/api/Winbase/nf-winbase-lookupprivilegedisplaynamea) function to retrieve a description string that corresponds to the string constant for a privilege. For example, on systems that use U.S. English, the display name for the SE\_SYSTEMTIME\_NAME privilege is "Change the system time".

You can use the [**PrivilegeCheck**](/windows/desktop/api/Winbase/nf-ntifs-ntprivilegecheck) function to determine whether an access token holds a specified set of privileges. This is useful primarily to server applications that are impersonating a client.

A system administrator can use administrative tools, such as User Manager, to add or remove privileges for user and group accounts. Administrators can programmatically use the [*Local Security Authority*](https://msdn.microsoft.com/library/windows/desktop/ms721592#-security-local-security-authority-gly) (LSA) functions to work with privileges. The [**LsaAddAccountRights**](https://msdn.microsoft.com/library/windows/desktop/ms721786) and [**LsaRemoveAccountRights**](https://msdn.microsoft.com/library/windows/desktop/ms721809) functions add or remove privileges from an account. The [**LsaEnumerateAccountRights**](https://msdn.microsoft.com/library/windows/desktop/ms721790) function enumerates the privileges held by a specified account. The [**LsaEnumerateAccountsWithUserRight**](https://msdn.microsoft.com/library/windows/desktop/ms721792) function enumerates the accounts that hold a specified privilege.

## Related topics

<dl> <dt>

[Authorization Constants](https://www.bing.com/search?q=Authorization Constants)
</dt> <dt>

[Enabling and Disabling Privileges in C++](enabling-and-disabling-privileges-in-c--.md)
</dt> </dl>

 

 



