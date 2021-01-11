---
description: The Installer writes the following values into the log when an action returns these error codes. For the entire list of error codes returned by the Windows Installer function calls MsiExec.exe, and InstMsi.exe, see Error Codes.
ms.assetid: 653bbf45-ac2c-4f8a-a978-960e0c42e6e4
title: Logging of Action Return Values
ms.topic: article
ms.date: 05/31/2018
---

# Logging of Action Return Values

The Installer writes the following values into the log when an action returns these error codes. For the entire list of error codes returned by the Windows Installer function calls MsiExec.exe, and InstMsi.exe, see [Error Codes](error-codes.md).



| Error Code                       | Values returned by function calls MsiExec.exe, and InstMsi.exe | Values that appear in the Log. | Description                                                                                                                                                                                                                                                                     |
|----------------------------------|----------------------------------------------------------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERROR\_FUNCTION\_NOT\_CALLED     | 1626                                                           | 0                              | A function could not be executed.                                                                                                                                                                                                                                               |
| ERROR\_SUCCESS                   | 0                                                              | 1                              | An action completed successfully.                                                                                                                                                                                                                                               |
| ERROR\_INSTALL\_USEREXIT         | 1602                                                           | 2                              | A user canceled installation.                                                                                                                                                                                                                                                   |
| ERROR\_INSTALL\_FAILURE          | 1603                                                           | 3                              | A fatal error.                                                                                                                                                                                                                                                                  |
| ERROR\_INSTALL\_SUSPEND          | 1604                                                           | 4                              | The installation suspended, incomplete.                                                                                                                                                                                                                                         |
| ERROR\_SUCCESS                   | 0                                                              | 5                              | The action completed successfully.                                                                                                                                                                                                                                              |
| ERROR\_INVALID\_HANDLE\_STATE    | 1609                                                           | 6                              | The handle is in an invalid state.                                                                                                                                                                                                                                              |
| ERROR\_INVALID\_DATA             | 1626                                                           | 7                              | The data is invalid.                                                                                                                                                                                                                                                            |
| ERROR\_INSTALL\_ALREADY\_RUNNING | 1618                                                           | 8                              | Another installation is in progress. Only one installation at a time can run actions in the [InstallExecuteSequence](installexecutesequence-table.md), [AdminExecuteSequence](adminexecutesequence-table.md), or [AdvtExecuteSequence](advtexecutesequence-table.md) tables. |



 

## Related topics

<dl> <dt>

[Windows Installer Logging](windows-installer-logging.md)
</dt> </dl>

 

 



