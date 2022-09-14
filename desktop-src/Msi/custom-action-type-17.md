---
description: Developers of Windows Installer packages may choose to use a custom action type 17 when the standard actions are insufficient to execute the installation.
ms.assetid: 99efd6d5-e0a3-4e66-ae55-252d19090d31
title: Custom Action Type 17
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Type 17

This custom action calls a dynamic link library (DLL) written in C or C++.

## Source

The DLL is installed with the application during the current session. The Source field of the [CustomAction table](customaction-table.md) contains a key to the [File table](file-table.md). The location of the custom action code is determined by the resolution of the target path for this file; therefore this custom action must be called after that file has been installed and before it is removed.

## Type Value

Include the following value in the Type column of the [CustomAction table](customaction-table.md) to specify the basic numeric type.



| Constants                                                          | Hexadecimal | Decimal |
|--------------------------------------------------------------------|-------------|---------|
| **msidbCustomActionTypeDll** + **msidbCustomActionTypeSourceFile** | 0x011       | 17      |



 

## Target

The DLL is called through the entry point named in the Target field of the [CustomAction table](customaction-table.md), passing a single argument that is the handle to the current install session. The entry point name specified in the table must match that exported from the DLL. Note that if the entry function is not specified by a .DEF file or by a /EXPORT: linker specification, the name may have a leading underscore and a "@4" suffix. The called function must specify the \_\_stdcall calling convention.

## Return Processing Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify return processing options. For a description of the options and the values, see [Custom Action Return Processing Options](custom-action-return-processing-options.md).

## Execution Scheduling Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify execution scheduling options. These options control the multiple execution of custom actions. For a description of the options, see [Custom Action Execution Scheduling Options](custom-action-execution-scheduling-options.md).

## In-Script Execution Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify an in-script execution option. These options copy the action code into the execution, rollback, or commit script. For a description of the options, see [Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md).

## Return Values

See [Custom Action Return Values](custom-action-return-values.md).

## Remarks

A custom action that calls a dynamic-link library (DLL) requires a handle to the installation session. If this is also a deferred execution custom action, the session may no longer exist during execution of the installation script. For information on how a custom action of this type can obtain context information, see [Obtaining Context Information for Deferred Execution Custom Actions](obtaining-context-information-for-deferred-execution-custom-actions.md).

Custom actions execute in a separate thread, and may have limited access to the system. Custom actions that run asynchronously block the main thread at the termination of either the current sequence or the install session until they return.

Custom actions that reference an installed file as their source, such as Custom Action Type 17 (DLL), must adhere to the following sequencing restrictions:

-   The custom action must be sequenced after the [CostFinalize action](costfinalize-action.md). This is so that the custom action can resolve the path needed to locate the DLL.
-   If the source file is not already installed on the computer, deferred (in-script) custom actions of this type must be sequenced after the [InstallFiles action](installfiles-action.md).
-   If the source file is not already installed on the computer, non-deferred custom actions of this type must be sequenced after the [InstallFinalize action](installfinalize-action.md).

## Related topics

<dl> <dt>

[Custom\_Actions](custom-actions.md)
</dt> <dt>

[Deferred Execution Custom Actions](deferred-execution-custom-actions.md)
</dt> <dt>

[Dynamic-Link Libraries](dynamic-link-libraries.md)
</dt> </dl>

 

 



