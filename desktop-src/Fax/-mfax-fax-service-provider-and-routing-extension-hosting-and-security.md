---
Description: 'Beginning with Windows Server 2003, FSPs and Routing Extensions are loaded into a provider subsystem with the NetworkService security account.'
ms.assetid: 'd0a91e09-a71c-4e6b-a015-5f89e2e4d314'
title: Fax Service Provider and Routing Extension Hosting and Security
---

# Fax Service Provider and Routing Extension Hosting and Security

In earlier versions of Windows, fax service providers (FSPs) and Routing Extensions were loaded in-process with the fax service process address space, running under the [LocalSystem](http://msdn.microsoft.com/library/en-us/dllproc/base/localsystem_account.asp) security account. Beginning with Windows Server 2003, FSPs and Routing Extensions are loaded into a provider subsystem with the [NetworkService](http://msdn.microsoft.com/library/en-us/dllproc/base/networkservice_account.asp) security account. The [NetworkService](http://msdn.microsoft.com/library/en-us/dllproc/base/networkservice_account.asp) account is for services that have no real need for extensive privileges but do need to remotely communicate with other systems. Using this account in the subsystem eliminates the potential risk of a corrupted or compromised extension affecting the entire system.

This change will affect the following aspects of your FSP or Routing Extension:

-   Registry keys must be created using the [RegCreateKeyEx](http://msdn.microsoft.com/library/en-us/sysinfo/base/regcreatekeyex.asp) function, not the **RegCreateKey** function.

-   When you create a registry key, you cannot use the KEY\_ALL\_ACCESS access mask.

-   When you use [RegOpenKeyEx](http://msdn.microsoft.com/library/en-us/sysinfo/base/regopenkeyex.asp), you cannot set the *samDesired* parameter equal to KEY\_ALL\_ACCESS. If you do, the function will fail.

-   FSPs and Routing Extensions will not be able to create or access folders in the WINDOWS directory. This includes the WINDOWS/Temp directory.

-   If a dialog that states, "Click Cancel to debug the program" appears, note that a debugger will not be automatically attached to the process if you click **Cancel**. First attach a debugger, then click **Cancel**.

-   Fax service has more restrictive access rights to **HKLM**\\**Software**\\**Microsoft**\\**Fax**. If you write code that opens a registry key you must use the appropriate access rights. You cannot use KEY\_ALL\_ACCESS. The fax service access rights are as follows:

-   -   Query value
    -   Set value
    -   Create subkey
    -   Enumerate subkeys
    -   Notify
    -   Delete
    -   Read control

-   There is a new subkey called **Client** that gives users read rights. All debugging registry values were relocated to the **Client** subkey. If, for example, you want to change the DebugLevel you will have to do so under the **Fax**\\**Client** subkey.

 

 



