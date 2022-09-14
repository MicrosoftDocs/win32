---
description: Performance counters specific to your application can help you tune performance while you develop and debug the application.
ms.assetid: 016386f6-4675-409e-8446-599e4ff96109
title: Adding Performance Counters
ms.topic: article
ms.date: 05/31/2018
---

# Adding Performance Counters

> [!IMPORTANT]
> Due to significant performance and reliability limitations, the method for providing performance counter data that this topic describes may be altered or unavailable in the future. Instead, Microsoft recommends that you use the method described in [Providing Counter Data Using Version 2.0](providing-counter-data-using-version-2-0.md) for creating new performance counters, and that you migrate existing performance counters to use that method as well.

Performance counters specific to your application can help you tune performance while you develop and debug the application. After your application is complete and installed on target systems, the counters can help system administrators adjust configurable settings for your application.

## Adding a performance object and its counters

1. Design the object types and counters for the application. For details, see [Object and Counter Design](object-and-counter-design.md).
2. Create an initialization (.ini) file containing the names and descriptions of the performance objects and counters that you provide. For details, see [Adding Counter Names and Descriptions to the Registry](adding-counter-names-and-descriptions-to-the-registry.md).
3. Create a header (.h) file containing the relative offsets at which the counter objects and counters will be installed in the registry. For details, see [Adding Counter Names and Descriptions to the Registry](adding-counter-names-and-descriptions-to-the-registry.md).
4. Set up the necessary performance monitoring entries in the registry. This includes the following steps.
    1. Create a registry key in the **Services** key for the application. If you do not have such a node, create it under the following registry key: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services`. For details, see [Creating the Application's Performance Key](creating-the-applications-performance-key.md).
    2. Use the **lodctr** utility with the .ini and .h files to install the information in the registry. This utility succeeds only if a performance key exists in the **Services** key for the application. For details, see [Adding Counter Names and Descriptions to the Registry](adding-counter-names-and-descriptions-to-the-registry.md).
5. Create a performance DLL containing a set of exported functions that provide the queried counter data to the consumer. For details, see [Creating a Performance Extension DLL](creating-a-performance-extension-dll.md).
6. Modify the application's setup file to automate adding information to the registry (as described in step 4) and copy your performance DLL to your application's directory at setup.

For information about additional registry entries, see [Creating Other Registry Entries](creating-other-registry-entries.md).
