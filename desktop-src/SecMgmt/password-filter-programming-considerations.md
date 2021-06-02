---
description: Explains considerations for implementation of password filter export functions.
ms.assetid: ec7c1e7e-844a-43d4-b756-02bc1062d7b8
title: Password Filter Programming Considerations
ms.topic: article
ms.date: 05/31/2018
---

# Password Filter Programming Considerations

When implementing [*password filter*](/windows/desktop/SecGloss/p-gly) export functions, keep the following considerations in mind:

-   Take great care when working with [*plaintext*](/windows/desktop/SecGloss/p-gly) passwords. Sending plaintext passwords over networks could compromise security. Network "sniffers" can easily watch for plaintext password traffic.
-   Erase all memory used to store passwords by calling the [**SecureZeroMemory**](/previous-versions/windows/desktop/legacy/aa366877(v=vs.85)) function before freeing memory.
-   All buffers passed into password notification and filter routines should be treated as read-only. Writing data to these buffers may cause unstable behavior.
-   All password notification and filter routines should be thread-safe. Use critical sections or other synchronous programming techniques to protect data where appropriate.
-   Password notification and filtering take place only on the computer that houses the account.
-   All domain controllers are writeable, therefore password filter packages must be present on all domain controllers.

    **Windows NT 4.0 domains:** Notification on domain accounts takes place only on the primary domain controller. In addition to the primary domain controller, the password filter packages should be installed on all backup domain controllers to allow notifications to continue in the event of server role changes.

-   All password filter DLLs run in the [*security context*](/windows/desktop/SecGloss/s-gly) of the local system account.



| For information about                                                                                                                     | See                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| How to install and register your own [*password filter*](/windows/desktop/SecGloss/p-gly) DLL. | [Installing and Registering a Password Filter DLL](installing-and-registering-a-password-filter-dll.md) |
| The password filter DLL provided by Microsoft.                                                                                            | [Strong Password Enforcement and Passfilt.dll](strong-password-enforcement-and-passfilt-dll.md)         |
| Export functions implemented by a password filter DLL.                                                                                    | [Password Filter Functions](management-functions.md)                          |



 

 

 
