---
description: The Windows password filter DLL, Passfilt.dll, runs in the security context of the local system account and helps you filter domain or local account passwords.
ms.assetid: 12a6fe6d-5b37-4fcf-bd04-0a22d84ba323
title: Installing and Registering a Password Filter DLL
ms.topic: article
ms.date: 05/31/2018
---

# Installing and Registering a Password Filter DLL

You can use the Windows password filter to filter domain or local account passwords. To use the password filter for domain accounts, install and register the DLL on each domain controller in the domain.

Perform the following steps to install your password filter. You can perform these steps manually, or you can write an installer to perform these steps. You need to be an Administrator or belong to the Administrator Group to perform these steps.

**To install and register a Windows password filter DLL**

1.  Copy the DLL to the Windows installation directory on the domain controller or local computer. On standard installations, the default folder is \\Windows\\System32. Make sure that you create a 32-bit password filter DLL for 32-bit computers and a 64-bit password filter DLL for 64-bit computers, and then copy them to the appropriate location.
2.  To register the password filter, update the following system registry key:

    ```
    HKEY_LOCAL_MACHINE
       SYSTEM
          CurrentControlSet
             Control
                Lsa
    ```

    If the **Notification Packages** value of type *REG_MULTI_SZ* exists, add the name of your DLL to the existing value data. Do not overwrite the existing values, and do not include the .dll extension.

    If the **Notification Packages** value does not exist, create it, give it the *REG_MULTI_SZ* type and then specify the name of the DLL for the value data. Do not include the .dll extension.

    The **Notification Packages** value can add multiple packages.

3.  Find the password complexity setting.

    In Control Panel, click **Performance and Maintenance**, click **Administrative Tools**, double-click **Local Security Policy**, double-click **Account Policies**, and then double-click **Password Policy**.

4.  To enforce both the default Windows password filter and the custom password filter, ensure that the **Passwords must meet complexity requirements** policy setting is enabled. Otherwise, disable the **Passwords must meet complexity requirements** policy setting.

## Related topics

<dl> <dt>

[Password Filter Programming Considerations](password-filter-programming-considerations.md)
</dt> <dt>

[Strong Password Enforcement and Passfilt.dll](strong-password-enforcement-and-passfilt-dll.md)
</dt> <dt>

[Password Filter Functions](management-functions.md)
</dt> </dl>

 

 



