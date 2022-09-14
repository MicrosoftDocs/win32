---
title: Command Blocking
description: To preserve integrity of operations, certain TPM commands are not allowed to be executed by software on the platform.
ms.assetid: 47402a4a-5f8d-4648-b3ea-06c95b2a1fc1
ms.topic: article
ms.date: 05/31/2018
---

# Command Blocking

To preserve integrity of operations, certain TPM commands are not allowed to be executed by software on the platform. For example, some commands are only executed by system software. When the TBS blocks a command, an error is returned as appropriate. By default, the TBS blocks commands that could impact system privacy, security, and stability. The TBS also assumes that other parts of the software stack may restrict access to certain commands to authorized entities.

For TPM version 1.2 commands, there are three lists of blocked commands: a list controlled by group policy, a list controlled by local administrators, and a default list. A TPM command is blocked if it is on any of the lists. However, there are group policy flags to allow the TBS to ignore the local list and the default list. The group policy flags can be edited directly or accessed through the Group Policy Object Editor.

> [!Note]  
> The list of locally blocked commands is not preserved after an upgrade to the operating system. Commands that are blocked on the Group Policy list are preserved.

 

For TPM version 2.0 commands, the logic for blocking is inverted; it uses a list of allowed commands. This logic will automatically block commands that were not known when the list was first made. When commands are added to the TPM specification after a version of Windows has shipped, these new commands are automatically blocked. Only an update of the registry will add these new commands to the list of allowed commands.

Starting with Windows 10 1809 (Windows Server 2019), allowed TPM 2.0 commands can no longer be manipulated through registry settings. For these Windows 10 versions, the allowed TPM 2.0 commands are fixed in the TPM driver. TPM 1.2 commands can still be blocked and unblocked through registry changes. 

## Direct Registry Access

The Group Policy flags are under registry key **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Tpm**\\**BlockedCommands**.

To determine which lists should be used to block TPM commands, there are two **DWORD** values that are used as Boolean flags:

-   "IgnoreDefaultList"

    If set (value exists and is nonzero), the TBS ignores the default blocked-commands list.

-   "IgnoreLocalList"

    If set (value exists and is nonzero), the TBS ignores the local blocked-commands list.

## Group Policy Object Editor

**To access the Group Policy object editor**

1.  Click **Start**.
2.  Click **Run**.
3.  In the **Open** box, type **gpedit.msc**. Click **OK**. The Group Policy object editor opens.
4.  Expand **Computer Configuration**.
5.  Expand **Administrative Templates**.
6.  Expand **System**.
7.  Expand **Trusted Platform Module Services**.

The lists of specific blocked TPM1.2 commands can be edited directly in the following locations.

-   Group policy list:

    ```
    HKEY_LOCAL_MACHINE
       Software
          Policies
             Microsoft
                Tpm
                   BlockedCommands
                      List
    ```

-   Local list:

    ```
    HKEY_LOCAL_MACHINE
       SYSTEM
          CurrentControlSet
             Services
                SharedAccess
                   Parameters
                      Tpm
                         BlockedCommands
                            List
    ```

-   Default list:

    ```
    HKEY_LOCAL_MACHINE
       Software
          Microsoft
             Tpm
                BlockedCommands
                   List
    ```

Under each of these registry keys, there is a list of registry values of REG\_SZ type. Each value represents a blocked TPM command. Each registry key has a "Value name" field and a "Value data" field. Both fields ("Value Name" and "Value data"), should exactly match the decimal value of the TPM command ordinal to be blocked.

The list of specific allowed TPM 2.0 commands can be edited directly in the following location. Under the registry key, there is a list of registry values of REG\_DWORD type. Each value represents an allowed TPM 2.0 command. Each registry value has a **name** and a **value** field. The **name** matches the hexadecimal TPM 2.0 command ordinal that should be allowed. The **value** has a value of 1 if the command is allowed. If a command ordinal is not present or has a value of 0, the command will be blocked.

-   Default list:

    ```
    HKEY_LOCAL_MACHINE
       Software
          Microsoft
             Tpm
                AllowedW8Commands
                   List
    ```

For Windows 8, Windows Server 2012 and later, the **BlockedCommands** and **AllowedW8Commands** registry keys respectively determine the blocked or allowed TPM commands for administrator accounts. User accounts have a list of blocked or allowed TPM commands in the **BlockedUserCommands** and **AllowedW8UserCommands** registry keys respectively. In Windows 10, version 1607, new registry keys have been introduces for AppContainer applications: **BlockedAppContainerCommands** and **AllowedW8AppContainerCommands**.

 

 




