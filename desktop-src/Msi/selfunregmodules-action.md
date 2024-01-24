---
description: The SelfUnregModules action unregisters all modules listed in the SelfReg table that are scheduled to be uninstalled. The installer does not self-register .EXE files.
ms.assetid: fa5a5abb-ecd4-434c-b176-83cdca280a13
title: SelfUnregModules Action
ms.topic: article
ms.date: 05/31/2018
---

# SelfUnregModules Action

The SelfUnregModules action unregisters all modules listed in the [SelfReg table](selfreg-table.md) that are scheduled to be uninstalled. The installer does not self-register .EXE files.

## Sequence Restrictions

The [InstallValidate](installvalidate-action.md) action must appear before the SelfUnregModules action in the sequence. If a [SelfRegModules](selfregmodules-action.md) action is used it must appear after the SelfUnregModules action in the sequence. If a [RemoveFiles action](removefiles-action.md) is used it must appear after the SelfUnregModules action in the sequence.

## ActionData Messages



| Field | Description of action data                             |
|-------|--------------------------------------------------------|
| \[1\] | Identifier of unregistered module file.                |
| \[2\] | Identifier of folder holding unregistered module file. |



 

## Remarks

The SelfUnregModules action attempts to call the [**DllUnregisterServer**](/windows/win32/api/olectl/nf-olectl-dllunregisterserver) function of the module that is to be unregistered. This action runs with elevated privileges when the installation is being run with elevated privileges, such as during a per-machine installation. During a per-user installation, the installer runs this action with user privileges.

Note that you cannot specify the order in which the installer unregisters self-registering DLLs by using the SelfUnRegModules action.

## Related topics

<dl> <dt>

[Specifying the Order of Self Registration](specifying-the-order-of-self-registration.md)
</dt> </dl>

 

 
