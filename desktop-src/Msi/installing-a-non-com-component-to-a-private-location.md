---
description: To force a client application to always use the same copy of a non-COM server, author the application's installation package to specify an isolated components relationship between the server and client.
ms.assetid: 3ca9cad7-6848-4483-b5e3-2b7bbdefe605
title: Installing a non-COM Component to a Private Location
ms.topic: article
ms.date: 05/31/2018
---

# Installing a non-COM Component to a Private Location

To force a client application to always use the same copy of a non-COM server, author the application's installation package to specify an [isolated components](isolated-components.md) relationship between the server and client. This installs a private copy of the server component to a location used exclusively by the client application. Do the following when authoring the package:

-   Put the server DLL and the .exe client in separate components.
-   Enter a record in the [IsolatedComponent table](isolatedcomponent-table.md) with the client component in the Component\_Shared column and the client application in the Component\_Application column. Include the [IsolateComponents action](isolatecomponents-action.md) in the sequence tables.
-   Set the msidbComponentAttributesSharedDllRefCount bit in the [Component table](component-table.md) record for Component\_Shared. The installer requires this global refcount on the shared location to protect the shared files and registration in cases where there is sharing with other installation technologies.
-   Avoid authoring a shared registered path across components.

 

 



