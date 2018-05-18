---
Description: 'This topic introduces the Fax Service Extended COM APIs.'
ms.assetid: 'df15bad0-8f68-4eea-9cb3-439078239398'
title: About the Fax Service Extended COM API
---

# About the Fax Service Extended COM API

The fax service for Windows XP introduces a new set of Component Object Model (COM) dual interfaces, the Fax Service Extended COM API. The Fax Service Extended COM API allows you to incorporate fax functionality for users in client applications.

The extended COM objects and their interfaces can be classified into the following groups.

-   **Root objects**. Includes the [**FaxServer**](-mfax-faxserver.md) root object.
-   **Messaging objects**. Includes objects used to create, track, and manage fax documents, messages, and jobs.
-   **Configuration objects**. Includes objects used to configure the fax server.
-   **Notification objects**. Includes the [**FaxServerNotify**](-mfax-ifaxservernotify.md) interface and the [**FaxJobStatus**](-mfax-faxjobstatus.md) object for event notification callbacks.

For more information, see [Fax Service Extended COM Objects](-mfax-fax-service-extended-com-objects.md).

> [!Note]  
> The [Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md) includes both Microsoft Win32 functions and an implementation of COM dual interfaces. New fax client applications written for Windows XP and later, including Windows Vista, should use the extended COM interfaces rather than the C/C++ functions or COM interfaces that shipped with the Windows 2000 Windows Software Development Kit (SDK).

 

This section includes the following topics:

-   [Fax Service Extended COM Object Model](-mfax-fax-service-extended-com-object-model.md)
-   [Fax Broadcasts](-mfax-fax-broadcasts.md)
-   [Fax Folders](-mfax-fax-folders.md)
-   [Outbound Routing](-mfax-outbound-routing.md)
-   [Fax Service Extended COM Samples](-mfax-fax-service-extended-com-samples.md)

 

 



