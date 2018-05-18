---
Description: 'Performance counters specific to your application can help you tune performance while you develop and debug the application.'
ms.assetid: '016386f6-4675-409e-8446-599e4ff96109'
title: Adding Performance Counters
---

# Adding Performance Counters

Performance counters specific to your application can help you tune performance while you develop and debug the application. After your application is complete and installed on target systems, the counters can help system administrators adjust configurable settings for your application.

**To add a performance object and its counters**

1.  Design the object types and counters for the application. For details, see [Object and Counter Design](object-and-counter-design.md).
2.  Create an initialization (.ini) file containing the names and descriptions of the performance objects and counters that you provide. For details, see [Adding Counter Names and Descriptions to the Registry](adding-counter-names-and-descriptions-to-the-registry.md).
3.  Create a header (.h) file containing the relative offsets at which the counter objects and counters will be installed in the registry. For details, see [Adding Counter Names and Descriptions to the Registry](adding-counter-names-and-descriptions-to-the-registry.md).
4.  Set up the necessary performance monitoring entries in the registry. This includes the following steps.
    1.  Create a registry key in the **Services** key for the application. If you do not have such a node, create it under the following registry key: **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services**. For details, see [Creating the Application's Performance Key](creating-the-applications-performance-key.md).
    2.  Use the **lodctr** utility with the .ini and .h files to install the information in the registry. This utility succeeds only if a performance key exists in the **Services** key for the application. For details, see [Adding Counter Names and Descriptions to the Registry](adding-counter-names-and-descriptions-to-the-registry.md).
5.  Create a performance DLL containing a set of exported functions that provide the queried counter data to the consumer. For details, see [Creating a Performance Extension DLL](creating-a-performance-extension-dll.md).
6.  Modify the application's setup file to automate adding information to the registry (as described in step 4) and move your performance DLL to the system directory at setup.

To view a performance object, its functions, and its counters, use the [extensible counter list utility](Http://go.microsoft.com/fwlink/p/?linkid=84423) (Exctrlst.exe). The utility is included with the Support Tools for Windows Server 2003 and Windows XP.

For information about additional registry entries, see [Creating Other Registry Entries](creating-other-registry-entries.md).

 

 



