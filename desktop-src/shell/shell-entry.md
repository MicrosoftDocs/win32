---
description: The Windows UI provides users with access to a wide variety of objects necessary for running applications and managing the operating system.
title: Windows Shell
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 1d0d4ed7-9b85-4d70-bf1f-82567a1687fb
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Windows Shell

The Windows UI provides users with access to a wide variety of objects necessary for running applications and managing the operating system. The most numerous and familiar of these objects are the folders and files that reside on computer disk drives. There are also a number of virtual objects that allow the user to perform tasks such as sending files to remote printers or accessing the Recycle Bin. The Shell organizes these objects into a hierarchical namespace and provides users and applications with a consistent and efficient way to access and manage objects.

## Shell Development Scenarios

The following development scenarios relate to application development:

-   Extending the Shell, which consists of creating a data source (versus consuming the Shell data model)
-   Implementing a subset of the Shell data source tasks
-   Supporting libraries and item views in Windows Explorer
-   Using the common file dialog
-   Implementing Control Panel items
-   Managing notifications

The following development scenarios relate to file format ownership:

-   Implementing a subset of the Shell data source tasks
-   Implementing any handler
-   Supporting desktop search

The following development scenarios relate to data storage ownership:

-   Supporting desktop search and OpenSearch
-   Implementing a subset of the Shell data source tasks (virtual folders)
-   Supporting libraries in Windows Explorer

The following development scenario relates to device support:

-   Auto run and auto play

## Windows Shell SDK Documentation

This documentation is broken into three major sections:

-   The [Shell Developer's Guide](intro.md) provides conceptual material about how the Shell works and how to use the Shell's API in your application.
-   The [Shell Reference](shell-reference-bumper.md) section documents programming elements that make up the various Shell APIs.
- [Shell Samples](samples-entry.md) provides links to related code samples.

The following table provides an outline of the Shell Reference section. Unless otherwise noted, all programming elements are documented in unmanaged C++.



| Section                                                               | Description                                                                                                          |
|-----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [Shell Classes](classes.md)                                          | This section describes select Windows Shell classes.                                                                 |
| [Shell Interfaces](interfaces.md)                                    | This section describes the Windows Shell Component Object Model (COM) interfaces.                                    |
| [Shell Functions](functions.md)                                      | This section describes the Windows Shell functions.                                                                  |
| [Shell Callback Functions](callbacks.md)                             | This section describes the Windows Shell callback functions templates.                                               |
| [Shell Constants, Enumerations, and Flags](consts-enums-flags.md)    | This section describes the Windows Shell constants, enumerations, and flags used in the Shell APIs.                  |
| [Shell Lightweight Utility Functions](shlwapi.md)                    | This section describes the Windows Shell lightweight utility functions provided in Shlwapi.dll.                      |
| [Shell Macros](macros.md)                                            | This section describes the Windows Shell utility macros.                                                             |
| [Shell Messages and Notifications](messages.md)                      | This section describes the messages and notifications sent by elements of the Windows Shell.                         |
| [Shell Objects for Scripting and Microsoft Visual Basic](objects.md) | This section describes the Windows objects implemented by the Shell for use in scripting and Microsoft Visual Basic. |
| [Shell Objects for C++](objects-cpp.md)                              | This section describes the C++ Windows objects implemented by the Shell.                                             |
| [Shell Schemas](schemas.md)                                          | This section describes library, property, and transfer manifest schemas used by the Windows Shell.                   |
| [Shell Structures](structures.md)                                    | This section describes the Windows Shell structures used in the Shell APIs.                                          |



 

 

 



