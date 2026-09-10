---
description: To help prevent malicious attack, determine whether your application requires administrator privileges. Use UAC manifests to declare the required execution level, and separate elevated operations from standard-user functionality.
ms.assetid: afa520fc-c206-49de-8d73-8f6566ec4fb6
title: Running with Administrator Privileges
ms.topic: reference
ms.date: 07/16/2026
---

# Running with Administrator Privileges

The first step in establishing which type of account your application needs to run under is to examine what resources the application will use and what privileged APIs it will call. You may find that the application, or large parts of it, do not require administrator privileges. *Writing Secure Code*, by Michael Howard and David LeBlanc offers an excellent description of how to carry out this assessment and is highly recommended.

> [!IMPORTANT]
> Most desktop applications should run at the **asInvoker** execution level. Only request elevation when your application genuinely requires write access to protected locations (like `%ProgramFiles%`) or must modify system-wide settings. Requesting unnecessary elevation increases your application's attack surface and trains users to dismiss UAC prompts without reading them.

## Declare required execution level with a UAC manifest

Windows uses the application manifest to determine the execution level your application needs. Embed a manifest with one of these `requestedExecutionLevel` values:

| Level | When to use |
|-------|-------------|
| `asInvoker` | Default. The application runs with the same token as the parent process. Use for most applications. |
| `highestAvailable` | The application runs with the highest privileges available to the current user. Use when some features need elevation but the application should still launch for standard users. |
| `requireAdministrator` | The application always requires full administrator privileges. UAC prompts the user for consent or credentials before launching. |

```xml
<!-- Example: embed in your application manifest (.exe.manifest or linker /MANIFEST) -->
<trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
  <security>
    <requestedPrivileges>
      <requestedExecutionLevel level="asInvoker" uiAccess="false" />
    </requestedPrivileges>
  </security>
</trustInfo>
```

> [!WARNING]
> An application without a manifest is treated as **asInvoker** on modern Windows, but may be subject to installer detection heuristics that cause unexpected elevation prompts. Always embed an explicit manifest.

## Approaches to minimize privilege

You can provide the privileges your application needs with less exposure to malicious attack by using one of the following approaches:

-   **Run under an account with less privilege.** Use [**PrivilegeCheck**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-privilegecheck) to determine what privileges are enabled in a token. If the available privileges are not adequate for the current operation, you can disable that code and ask the user to logon to an account with administrator privileges.
-   **Separate elevated operations into a helper process.** Keep your main application running as **asInvoker** and launch a separate elevated process only for the specific operations that need it. Use COM elevation moniker or [**ShellExecute**](/windows/win32/api/shellapi/nf-shellapi-shellexecutea) with the `runas` verb to trigger the UAC elevation prompt.
-   **Authenticate the user** by calling [**CredUIPromptForWindowsCredentials**](/windows/desktop/api/wincred/nf-wincred-creduipromptforwindowscredentialsa) (GUI) or [**CredUICmdLinePromptForCredentials**](/windows/desktop/api/wincred/nf-wincred-creduicmdlinepromptforcredentialsa) (command line) to obtain user name and password. For an example, see [Asking the User for Credentials](asking-the-user-for-credentials.md).
-   **Impersonate the user.** A process that starts under a highly privileged account like System can impersonate a user account by calling [**ImpersonateLoggedOnUser**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-impersonateloggedonuser) or similar Impersonate functions, thus reducing privilege level. However, if a call to [**RevertToSelf**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-reverttoself) is injected into the thread, the process returns to the original System privileges.

If you have determined that your application must run under an account with administrator privileges and that an administrator password must be stored in the software system, see [Handling Passwords](handling-passwords.md) for methods of doing this safely.

## Related topics

- [User Account Control](/windows/security/application-security/application-control/user-account-control/)
- [Running with Special Privileges](running-with-special-privileges.md)

