---
Description: 'Information about Winlogon notification packages is stored in the registry. Registry entries specify the name of the notification package, the name of the DLL that implements the package, and the names of the functions that handle Winlogon events.'
ms.assetid: 'dbe8d5a3-8927-4b95-a1a0-82c8e12ba8c1'
title: Registering a Winlogon Notification Package
---

# Registering a Winlogon Notification Package

Information about [*Winlogon*](security.w_gly#-security-winlogon-gly) notification packages is stored in the registry. Registry entries specify the name of the notification package, the name of the DLL that implements the package, and the names of the functions that handle Winlogon events.

When Winlogon starts, it checks the registry and loads any registered notification packages. When an event occurs, Winlogon calls the designated event handler function for each package. Multiple event notification packages may be registered on a system.

To register your notification package, create a registry key named **Notify** as a subkey of the following registry key and add the values detailed in [Registry Entries](registry-entries.md).

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**Winlogon**

 

 



