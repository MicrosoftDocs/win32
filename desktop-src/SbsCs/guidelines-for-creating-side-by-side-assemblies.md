---
description: The following guidelines discuss how to author your own COM or Win32 side-by-side assemblies.
ms.assetid: e10fe92c-bce8-420e-a84c-2748e929eb1b
title: Guidelines for Creating Side-by-side Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# Guidelines for Creating Side-by-side Assemblies

The following guidelines discuss how to author your own COM or Win32 side-by-side assemblies. You may not need to create your own side-by-side assemblies if the functionality needed is provided by one of the [supported Microsoft side-by-side assemblies](supported-microsoft-side-by-side-assemblies.md). In this case, use the assemblies provided by Microsoft and follow the procedures for using side-by-side assemblies in [Using Isolated Applications and Side-by-side Assemblies](using-isolated-applications-and-side-by-side-assemblies.md).

First, consider whether your component makes a suitable candidate for a side-by-side assembly. For more information, see [Should you provide a shared component as a side-by-side assembly?](should-you-provide-a-shared-component-as-a-side-by-side-assembly.md)

To create a side-by-side assembly, follow these guidelines:

-   Decide which resources to include in the assembly. Keep in mind that an assembly consists of one or more files that are always provided to applications and customers together. The assembly serves as the fundamental unit used for naming, binding, versioning, deployment, and [default configuration](default-configuration.md). As a general rule, when uncertain about whether two resources belong in the same assembly, it is recommended that they be authored to go into separate assemblies. Typically, a side-by-side assembly consists of a single DLL.
-   Create an assembly [manifest](manifests.md) for the assembly. The manifest should describe the COM object or type libraries in the assembly. For more information about what should be authored into an assembly manifest, see [assembly manifests](assembly-manifests.md).
-   Evaluate the usage of objects when more than one version of your assembly is run on the system. Determine whether different versions of the assembly require separate data structures, such as memory-mapped files, named pipes, registered Windows messages and classes, shared memory, semaphores, mutexes, and hardware drivers. Any data structures used across assembly versions must be backward-compatible versions. Decide which data structures can be used across versions and which data structures must be private to a version. Determine whether shared data structures require separate synchronization objects such as semaphores and mutexes.
-   Author your DLL to work well as a side-by-side assembly by adhering to the guidelines in [Authoring a DLL for a Side-by-Side Assembly](authoring-a-dll-for-a-side-by-side-assembly.md).
-   Author a set of header files and helper functions to provide an easy way to version registry keys containing the assembly state. Assemblies commonly save their state settings in registry keys. Registry settings must be written on an individual version basis to isolate multiple assembly versions that may be run at the same time. Design your side-by-side assembly and DLL to correctly store and handle the state of the assembly during side-by-side sharing scenarios. Follow the guidelines in [Authoring State Storage for Side-by-Side Assemblies](authoring-state-storage-for-side-by-side-assemblies.md).
-   Developers of applications that use [private assemblies](/windows/desktop/Msi/private-assemblies) should secure the application directory. If the application is installed using the [Windows Installer](../msi/windows-installer-portal.md), then the application directory can be secured by using the LockPermissions table. Typically, the system is given read, write, and execute access to private assemblies; all other processes are given only execute and read access.
-   Test the assembly using scenarios with side-by-side sharing to ensure that it is a valid side-by-side assembly. Successful installation of the assembly is not sufficient to guarantee that it will work as expected.
-   Adopt a method for numbering updates for your assembly. Each assembly is associated with a four-part version number. Left-to-right, the major, minor, build, and revision parts are separated by periods. Change the major or minor number of an assembly for a version that is incompatible with earlier versions. Change only the build and revision parts for backward-compatible changes to the assembly. For example, a developer might adopt a numbering method in which all 1.0.0.\* version numbers refer to update versions to assembly version 1.0.0.0.

 

 
