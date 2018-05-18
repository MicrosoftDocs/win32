---
Description: Credential Management API
ms.assetid: 'e393041b-f10c-4053-bc6c-65a89f40e74f'
title: Credential Management API
---

# Credential Management API

The credential management functions constitute the set of functions that a credential manager must implement. These are:

-   [**NPLogonNotify**](nplogonnotify.md), an event-handler function that the MPR calls when a user logs on.
-   [**NPPasswordChangeNotify**](nppasswordchangenotify.md), an event-handler function the MPR calls when an account password is changed.

The credential management functions are always called in the system context (LocalSystem) rather than the user context.

For more information about how to create and register a credential manager application, see [Implementing a Credential Manager](implementing-a-credential-manager.md) and [Registering Network Providers and Credential Managers](registering-network-providers-and-credential-managers.md).

 

 



