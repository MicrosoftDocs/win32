---
description: When creating your own side-by-side assemblies, follow the Guidelines for Creating Side-by-side Assemblies.
ms.assetid: e5fc3bae-0646-4418-a8f7-369856f03cd5
title: Authoring DLLs for Side-by-side Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# Authoring DLLs for Side-by-side Assemblies

When creating your own side-by-side assemblies, follow the [Guidelines for Creating Side-by-side Assemblies](guidelines-for-creating-side-by-side-assemblies.md) and author any DLLs used in the assembly according to the following guidelines:

-   Your DLLs should be designed so that multiple versions can run at the same time and in the same process without interfering with each other. For example, many applications host multiple plug-ins that each require a different version of one component. The developer the side-by-side assembly needs to design and test to ensure that multiple versions of the component work correctly when run at the same time in the same process.

-   If you plan to provide your component as a shared component on systems earlier than Windows XP, you need to continue to install the component on these systems as a single-instance shared component. In this case, you need to ensure your component is backward compatible.

-   Evaluate the use of objects when more than one version of your assembly is run on the system. Determine whether different versions of the assembly require separate data structures, such as memory-mapped files, named pipes, registered Windows messages and classes, shared memory, semaphores, mutexes, and hardware drivers. Any data structures used across assembly versions must be backward-compatible. Decide which data structures can be used across versions, and which data structures must be private to a version. Determine whether shared data structures require separate synchronization objects, such as semaphores and mutexes.

-   Some objects, such as window classes and Atoms, are uniquely named for each process. Objects such as window classes should be versioned for each assembly using the manifest. For objects such as Atoms, use version-specific identifiers unless you plan to share across versions. If you use version-specific identifiers, use the four-part versioning number.

-   Include no self-registering code in any DLL. A DLL in a side-by-side assembly cannot be self-registering.

-   Define all version-specific names in your DLL with \#define statements. This enables all registry keys to be changed from one location. When you release a new version of your assembly, you only need to change this \#define statement. For example:

    `#define MyRegistryKey "MyAssembly1.0.0.0"`

-   Store any nonpersistent data in the Temp directory.

-   Do not put user data into global locations. Keep application data separate from user data.

-   Assign all shared files a file version that depends upon the application's name.

-   Assign all messages and data structures used across processes a version to prevent unintentional cross-process sharing.

-   Your DLL should not depend upon sharing across versions that may not exist, such as shared memory sections that are not shared across different versions of your assembly.

-   If you add new functionality that does not follow the binary interface compatibility contract of the original DLL, you must assign a new CLSID, ProgId, and file name. Future versions of your side-by-side assembly is then required to use this CLSID, ProgId, and file name. This prevents a conflict when a version of the DLL that is not side-by-side is registered over a side-by-side version.

-   If you reuse the same CLSID or ProgId, test to ensure that the assembly is backward compatible.

-   Initialize and set the default settings for the assembly in the assembly code. Do not save the defaults settings in the registry.

-   Assign versions to all data structures.

-   Your DLL should store the state of the side-by-side assembly as described in [Authoring State Storage for Side-by-Side Assemblies](authoring-state-storage-for-side-by-side-assemblies.md).

 

 



