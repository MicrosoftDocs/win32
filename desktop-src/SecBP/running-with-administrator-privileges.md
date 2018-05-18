---
Description: 'To help prevent malicious attack, determine whether your application requires administrator privileges. For functions that require administrator permissions, create a separate application and use the Windows RunAs command line command.'
ms.assetid: 'afa520fc-c206-49de-8d73-8f6566ec4fb6'
title: Running with Administrator Privileges
---

# Running with Administrator Privileges

The first step in establishing which type of account your application needs to run under is to examine what resources the application will use and what privileged APIs it will call. You may find that the application, or large parts of it, do not require administrator privileges. *Writing Secure Code*, by Michael Howard and David LeBlanc offers an excellent description of how to carry out this assessment and is highly recommended. (This resource may not be available in some languages and countries.)

You can provide the privileges your application needs with less exposure to malicious attack by using one of the following approaches:

-   Run under an account with less privilege. One way to do this is to use [**PrivilegeCheck**](https://msdn.microsoft.com/library/windows/desktop/aa379304) to determine what privileges are enabled in a token. If the available privileges are not adequate for the current operation, you can disable that code and ask the user to logon to an account with administrator privileges.
-   Break into a separate application functions that require administrator permissions. You can provide for the user a shortcut that executes the RunAs command. For detailed instructions on how to set up the shortcut, search for "runas" in Help. Programmatically, you can configure the [RunAs](https://msdn.microsoft.com/library/windows/desktop/ms680046) command under the [AppId Key](https://msdn.microsoft.com/library/windows/desktop/ms682359) registry key for your application.
-   Authenticate the user by calling [**CredUIPromptForCredentials**](https://msdn.microsoft.com/library/windows/desktop/aa375177) (GUI) or [**CredUICmdLinePromptForCredentials**](https://msdn.microsoft.com/library/windows/desktop/aa375171) (command line) to obtain user name and password. For an example, see [Asking the User for Credentials](asking-the-user-for-credentials.md).
-   Impersonate the user. A process that starts under a highly privileged account like System can impersonate a user account by calling [**ImpersonateLoggedOnUser**](https://msdn.microsoft.com/library/windows/desktop/aa378612) or similar Impersonate functions, thus reducing privilege level. However, if a call to [**RevertToSelf**](https://msdn.microsoft.com/library/windows/desktop/aa379317) is injected into the thread, the process returns to the original System privileges.

If you have determined that your application must run under an account with administrator privileges and that an administrator password must be stored in the software system, see [Handling Passwords](handling-passwords.md) for methods of doing this safely.

 

 



