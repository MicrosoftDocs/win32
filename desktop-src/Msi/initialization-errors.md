---
description: This table describes initialization error codes and values.
ms.assetid: 5cce27ff-1143-4fe6-b4bd-727581431c07
title: Initialization Errors
ms.topic: article
ms.date: 05/31/2018
---

# Initialization Errors

This table describes initialization error codes and values.



| Error code                            | Value | Error                                                                                                                                                                                                                                                                         |
|---------------------------------------|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERROR\_SUCCESS                        | 0     | Initialization complete                                                                                                                                                                                                                                                       |
| ERROR\_ALREADY\_INITIALIZED           | 1247  | The installer is already initialized                                                                                                                                                                                                                                          |
| ERROR\_INSTALL\_SERVICE\_FAILURE      | 1601  | Install server could not be accessed                                                                                                                                                                                                                                          |
| ERROR\_BAD\_CONFIGURATION             | 1610  | Configuration data is corrupt                                                                                                                                                                                                                                                 |
| ERROR\_INSTALL\_PACKAGE\_VERSION      | 1613  | Installer version does not support database format                                                                                                                                                                                                                            |
| ERROR\_INSTALL\_ALREADY\_RUNNING      | 1618  | An installation is already in progress                                                                                                                                                                                                                                        |
| ERROR\_INSTALL\_PACKAGE\_OPEN\_FAILED | 1619  | Database could not be opened                                                                                                                                                                                                                                                  |
| ERROR\_INSTALL\_PACKAGE\_INVALID      | 1620  | Incompatible database                                                                                                                                                                                                                                                         |
| ERROR\_INSTALL\_UI\_FAILURE           | 1621  | Could not initialize handler interface                                                                                                                                                                                                                                        |
| ERROR\_INSTALL\_LOG\_FAILURE          | 1622  | Could not open log file in requested mode                                                                                                                                                                                                                                     |
| ERROR\_INSTALL\_LANGUAGE\_UNSUPPORTED | 1623  | No acceptable language could be found                                                                                                                                                                                                                                         |
| ERROR\_INSTALL\_TRANSFORM\_FAILURE    | 1624  | Database transform failed to merge                                                                                                                                                                                                                                            |
| ERROR\_INSTALL\_PACKAGE\_REJECTED     | 1625  | This installation is forbidden by system policy. Contact your system administrator.                                                                                                                                                                                           |
| ERROR\_INSTALL\_PLATFORM\_UNSUPPORTED | 1633  | The platform specified by the [**Template Summary**](template-summary.md) property is not supported.                                                                                                                                                                         |
| ERROR\_PATCH\_PACKAGE\_OPEN\_FAILED   | 1635  | Patch package could not be opened                                                                                                                                                                                                                                             |
| ERROR\_PATCH\_PACKAGE\_INVALID        | 1636  | Patch package invalid.                                                                                                                                                                                                                                                        |
| ERROR\_PATCH\_PACKAGE\_UNSUPPORTED    | 1637  | Patch package unsupported                                                                                                                                                                                                                                                     |
| ERROR\_INVALID\_COMMAND\_LINE         | 1639  | Invalid command line syntax                                                                                                                                                                                                                                                   |
| ERROR\_INSTALL\_REMOTE\_DISALLOWED    | 1640  | Installation from a Terminal Services client session not permitted for current user.                                                                                                                                                                                          |
| ERROR\_PATCH\_TARGET\_NOT\_FOUND      | 1642  | The installer cannot install the upgrade patch because the program being upgraded may be missing or the upgrade patch updates a different version of the program. Verify that the program to be upgraded exists on your computer and that you have the correct upgrade patch. |
| ERROR\_INSTALL\_REJECTED              | 1654  | The app that you are trying to run is not supported on this version of Windows. A Windows Installer package, patch, or transform that has not been signed by Microsoft cannot be installed on an ARM computer.                                                                |



 

 

 



