---
description: If you are writing a GINA to replace the Microsoft standard GINA DLL (MSGina.dll), you may want to provide some or all of the standard GINA functionality.
ms.assetid: cd2ce7b7-6167-4451-9f6e-881676a2145c
title: MSGina.dll Features
ms.topic: article
ms.date: 05/31/2018
---

# MSGina.dll Features

If you are writing a [*GINA*](../secgloss/g-gly.md) to replace the Microsoft standard GINA DLL (MSGina.dll), you may want to provide some or all of the standard GINA functionality. Following is a list of standard features and a brief description of how they are controlled.

> [!Note]  
> GINA DLLs are ignored in Windows Vista.

 

Registry key values control the availability or behavior of many of these standard GINA features. Unless otherwise noted, these key values belong to the Winlogon registry key and have a value type of \[REG\_SZ\]. The actual path of the [*Winlogon*](../secgloss/w-gly.md) key is:

**\\HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon**

-   **Legal Notification Dialog Box**

    In some places, it is legal for anyone who has access to a workstation to log on and begin working unless there is a notice that indicates that the system is for authorized users only. Also, many users want company-specific messages displayed before normal logon. The standard GINA uses two Winlogon registry key values to allow a system to display information before logon. If either key value is present and contains a non-null string, then a Legal Notice dialog box is displayed before the usual Welcome screen. These key value names are shown in the following table.

    

    | Key value name         | Contents                                                            |
    |------------------------|---------------------------------------------------------------------|
    | **LegalNoticeCaption** | The string to display as the caption of the legal notice dialog box |
    | **LegalNoticeText**    | The string to display as the message of the legal notice dialog box |

    

     

-   **Display Last User Name**

    By default, the logon screen displays the name of the last user to successfully log on to the workstation. This feature is controlled by the **DontDisplayLastUserName** registry key value. When this key value is set to one, the user name is not displayed in the logon dialog box.

-   **Automatic Logon**

    This feature allows a system to log on a user automatically every time the system starts by using default information and disabling the CTRL+ALT+DEL logon box.

    This feature uses the following values of the Winlogon key.

    

    | Value                 | Contents                                           |
    |-----------------------|----------------------------------------------------|
    | **AutoAdminLogon**    | 1                                                  |
    | **AutoLogonCount**    | The number of times to do an automatic logon       |
    | **DefaultUserName**   | The name of the user account                       |
    | **DefaultDomainName** | The name of the domain that the user account is in |

    

     

    If the **AutoAdminLogon** key value is present and contains a one, and the **AutoLogonCount** key value is not present, an automatic logon will occur every time the current user logs off or the system is restarted. The account being logged onto is specified using the **DefaultUserName** and **DefaultDomainName** key values. The password for the account can be specified in one of two ways. For computers running one of the Windows Server 2003 or Windows XP operating systems, the password should be stored as a secret using the [**LsaStorePrivateData**](/windows/win32/api/ntsecapi/nf-ntsecapi-lsastoreprivatedata) function. For details, see [Protecting the Automatic Logon Password](protecting-the-automatic-logon-password.md). The other way to store the password is in plaintext in the **DefaultPassword** entry of the Winlogon key; for security purposes, this technique should be avoided. If you store the password using the **LsaStorePrivateData** function, then do not provide a **DefaultPassword** entry in the Winlogon key.

    If the **AutoAdminLogon** key value is present and contains a one, and if the **AutoLogonCount** key value is present and is not zero, **AutoLogonCount** will determine the number of automatic logons that occur. Each time the system is restarted, the value of **AutoLogonCount** will be decremented by one, until it reaches zero. When **AutoLogonCount** reaches zero, no account will be logged on automatically, the **AutoLogonCount** key value and **DefaultPassword** key value, if used, will be deleted from the registry, and **AutoAdminLogon** will be set to zero.

    There is one additional caveat to using **AutoAdminLogon**: By default, MSGina.dll checks the state of the SHIFT key when **AutoAdminLogon** is one. If the SHIFT key is held down during the boot process, MSGina.dll will ignore the **AutoAdminLogon** key value and prompt the user for identification and authentication information interactively. This is a useful feature when you are debugging a dedicated application. To disable the meaning of the SHIFT key, set the **IgnoreShiftOverride** key value to one.

-   **Allow Unauthenticated Shutdown**

    You can configure the default [*GINA*](../secgloss/g-gly.md) to include a **Shutdown** button in the logon dialog box. This lets users shut down the system without first logging on. The following key value controls whether this button is included.

    

    | Value                    | Description                                           |
    |--------------------------|-------------------------------------------------------|
    | **ShutdownWithoutLogon** | One to include the button; zero to exclude the button |

    

     

-   **Userinit.exe Activation**

    Userinit.exe is an application that is executed by MSGina.dll when the user has logged on. It runs in the newly logged-on user's [*context*](../secgloss/c-gly.md) and on the application desktop. Its purpose is to set up the user's environment, including restoring network uses, establishing profile settings such as fonts and screen colors, and running logon scripts. After completing those tasks, Userinit.exe executes the user shell programs. The shell programs inherit the environment that Userinit.exe sets up. The specific shell programs that Userinit.exe executes are stored in the **Shell** key value under the Winlogon registry key.

    The **Shell** key value can contain a comma-separated list of programs to be executed. Windows Explorer is the default shell program and will be executed if the **Shell** key value is null or not present. By default, Windows Explorer is listed.

-   **Logged-On Security Options**

    When logged on, if a user enters a [*secure attention sequence*](../secgloss/s-gly.md) (SAS), the user is presented with a security options screen. Among the options listed are:

    -   Shut down the system.
    -   Log off.
    -   Change the password.
    -   Go to the task list.
    -   Lock the workstation.

    A replacement GINA can provide similar options when a SAS event is received while a user is logged on.

 

 
