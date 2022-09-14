---
description: This topic identifies the option flags that you can use to control the processing of the custom action thread.
ms.assetid: a09b3a0e-564e-41aa-af0d-2e46776f291b
title: Custom Action Return Processing Options
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Return Processing Options

This topic identifies the option flags that you can use to control the processing of the custom action thread. The flags are used to specify that the main and custom action threads run synchronously (Windows Installer waits for the custom action thread to complete before resuming the main installation thread), or asynchronously (Windows Installer runs the custom action simultaneously while the main installation continues).

To enable the option flags, add the value that is identified in the following table to the value in the Type field of the [CustomAction Table](customaction-table.md).



| Constant                                                           | Hexadecimal             | Decimal | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------|-------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| (none)                                                             | 0x00000000              | +0      | A synchronous execution that fails if the exit code is not 0 (zero). <br/> If the flag msidbCustomActionTypeContinue is not set, then the custom action must return one of the return values that is described in [Custom Action Return Values](custom-action-return-values.md).<br/>                                                                                                                                                                                                                             |
| **msidbCustomActionTypeContinue**                                  | 0x00000040              | +64     | A synchronous execution that ignores exit code and continues.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **msidbCustomActionTypeAsync**                                     | 0x00000080              | +128    | An asynchronous execution that waits for exit code at the end of the sequence.<br/> This option cannot be used with [Concurrent Installations](concurrent-installations.md), [Rollback Custom Actions](rollback-custom-actions.md), or [Script Custom Actions](scripts.md).<br/>                                                                                                                                                                                                                                |
| **msidbCustomActionTypeAsync** + **msidbCustomActionTypeContinue** | 0x00000040 + 0x00000080 | +192    | An asynchronous execution that does not wait for completion.<br/> Execution continues after Windows Installer terminates.<br/> This option can only be used with the EXE type custom actions that is, [executable files](executable-files.md). <br/> All other types of custom actions can be asynchronous only within the install session, and must end for the installation to terminate.<br/> This option cannot be used with [Concurrent Installations](concurrent-installations.md).<br/> |



 

 

 




