---
title: ADSI Interfaces
description: This topic describes the categories used for ADSI interfaces.
ms.assetid: 8c735dbf-41d7-4fbb-b372-9abe4e1b8fdd
ms.tgt_platform: multiple
keywords:
- ADSI Interfaces ADSI
- ADSI ADSI , reference,interfaces
- interfaces ADSI
ms.topic: article
ms.date: 05/31/2018
---

# ADSI Interfaces

Active Directory Service Interfaces (ADSI) supports a rich set of interfaces that can be classified according to the following categories:

-   [Core](core-interfaces.md). These interfaces provide the basic object management functions of ADSI objects. The core functions include providing an entry point into a directory store, loading properties into the property cache, and committing changes to the underlying directory.
-   [Schema](schema-interfaces.md). These interfaces provide methods for managing and extending the directory schema.
-   [Property Cache](property-cache-interfaces.md). These interfaces define methods for manipulating properties in the property cache.
-   [Persistent Object](persistent-object-interfaces.md). These interfaces manipulate persistent data in the namespace of the underlying directory service. ADSI objects implement these types of interfaces to provide access to their persistent data, including user accounts, file shares, organizational hierarchies, and job listings in a print queue.
-   [Dynamic Object](dynamic-object-interfaces.md). These interfaces work with dynamic data in a directory service. Directory objects not represented in the underlying directory service implement such interfaces. Examples of dynamic data include commands issued over a network.
-   [Security](security-interfaces.md). These interfaces enable an ADSI client to establish its credentials to a server and use security features that the directory service supports, such as the access control list or security descriptors.
-   [Non-Automation](non-automation-interfaces.md). These interfaces allow non-Automation clients (for example, C/C++ applications) low-overhead access to directory objects by providing Vtable access to methods for managing and searching directory service objects.
-   [Extension](extension-interfaces.md). These interfaces allow ADSI clients to extend the features of existing ADSI classes to offer customized solutions to directory services.
-   [Utility](utility-interfaces.md). These interfaces provide advanced helper functions for managing ADSI objects.
-   [Data Type](data-type-interfaces.md). These interfaces provide methods to access ADSI data types.

 

 




