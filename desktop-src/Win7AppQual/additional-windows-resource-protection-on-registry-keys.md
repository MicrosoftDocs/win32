---
description: Additional Windows Resource Protection on Registry Keys
ms.assetid: 25d07e42-b5eb-4f72-b4b1-0ebb881644ba
title: Additional Windows Resource Protection on Registry Keys
ms.topic: article
ms.date: 05/31/2018
---

# Additional Windows Resource Protection on Registry Keys

## Platform

**Clients** - Windows 7  
**Servers** - Windows Server 2008 R2  









## Feature Impact

**Severity** - Medium  
**Frequency** - Low  


## Description

Additional system resources have added Windows Resource Protection (WRP) settings in Windows 7, making them read-only settings. The vast majority of resources that received added protection are system COM server keys, although some features have added targeted resource protection. Microsoft changed these resources in order to protect the system and other applications from breaking each other and to provide a consistent, stable platform upon which applications can reliably run. In the past, applications could provide custom files and use the unprotected COM registration to change the system. In the case of older applications, this can downgrade system runtimes or change the interface upon which other applications needed to work properly. In the worst case, such installations could cause system failure or degradation over time. To provide a better experience and a more stable application platform, we locked down these registrations so that only Microsoft updates could change system components.

Since most resources changed are COM keys used by the system, this change will not affect the majority of applications. While we expect most applications to have a better experience on Windows 7 as a result of these changes, a small subset of applications may be negatively affected. The system's application compatibility layers will automatically resolve setup problems by always telling the application that it succeeded in changing a setting, even if it failed due to it being a protected resource. This prevents application setups from breaking but may cause problems if the setting needed to be changed in order for the application to function properly.

## Manifestation

Applications may have modified these settings prior to Windows 7. Upon installing on Windows 7, applications may find certain features no longer work because the settings did not reflect what the application expected.

There are two scenarios in which applications may encounter problems related to this added protection:

-   Applications that may have been using the now-protected settings as a data store or as a rare or unintended extensibility point
-   In rare cases, the detection mechanism used to identify application setups may not recognize a particular setup and so the application compatibility mitigation layer may not be applied

## Mitigation

The primary means of mitigation is the system's application compatibility layer, which is automatically applied to application setups when detected. You can also manually apply it to any application using the compatibility tab in the application's properties.

This layer resolves the problem by intercepting registry operations. In the case where the application was attempting to modify a read-only (WRP) setting, the layer always returns success, even though the setting was not really changed. For most applications, this will cause no problems. However, there is a possibility that the application needed that setting changed in order to function properly, which is the first scenario described above.

## Solution

For the two scenarios identified above:

-   If the application requires the key to be writable in order to function or use the data store, there is no solution other than changing the application so that it no longer writes to that location.
-   If the compatibility layer was not applied to a setup, the setup failure should be detected and offered to be applied and re-run. Applications can also run in compatibility mode, in which case the mitigation layer is always applied.

## Compatibility Tests

How to detect if an application had WRP mitigation applied to it:

-   Windows Installer is aware of WRP; it automatically and silently ignores attempts to write or modify a protected resource. If the application was installed with Windows Installer and logging was enabled, then a warning will be logged for each registry key write operation that was ignored due to its being a WRP-protected resource.
-   The WRP API incorporates SfCIsKeyProtected, which can query if a registry key is WRP-protected on the current system. See the WRP entry in MSDN in the links below for additional information on using this API.

## Links to Other Resources

<dl>

[Windows Resource Protection](/windows/desktop/Wfp/windows-resource-protection-portal)  
</dl>

 

 
