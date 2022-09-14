---
description: To force a COM-client application to always use the same copy of a COM-server, author the application's installation package to specify an isolated components relationship between the COM server and client.
ms.assetid: 387c1c4d-16f5-4f46-b868-c2be7cb3f942
title: Installing a COM Component to a Private Location
ms.topic: article
ms.date: 05/31/2018
---

# Installing a COM Component to a Private Location

To force a COM-client application to always use the same copy of a COM-server, author the application's installation package to specify an [isolated components](isolated-components.md) relationship between the COM server and client. This installs a private copy of the COM-server component to a location used exclusively by the client application. Do the following when authoring the package:

-   Put the COM server DLL and the .exe client in separate components.
-   Enter a record in the [IsolatedComponent table](isolatedcomponent-table.md) with the COM-client component in the Component\_Shared column and the client application in the Component\_Application column. Include the [IsolateComponents action](isolatecomponents-action.md) in the sequence tables.
-   Set the msidbComponentAttributesSharedDllRefCount bit in the [Component table](component-table.md) record for Component\_Shared. The installer requires this global refcount on the shared location to protect the shared files and registration in cases where there is sharing with other installation technologies.

 

 



