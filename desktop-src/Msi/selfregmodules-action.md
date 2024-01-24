---
description: The SelfRegModules action processes all modules listed in the SelfReg table and registers all installed modules with the system. The installer does not self-register EXE files.
ms.assetid: b139ae28-e479-4915-909d-2449244e9fd6
title: SelfRegModules Action
ms.topic: article
ms.date: 05/31/2018
---

# SelfRegModules Action

The SelfRegModules action processes all modules listed in the [SelfReg](selfreg-table.md) table and registers all installed modules with the system. The installer does not self-register EXE files.

## Sequence Restrictions

The [InstallValidate](installvalidate-action.md) action must be called before calling the SelfRegModules action. If an [InstallFiles](installfiles-action.md) action is used, it must appear before the SelfRegModules action in the sequence. Because the SelfRegModules action changes the system, SelfRegModules should come after the [InstallInitialize action](installinitialize-action.md).

## ActionData Messages



| Field | Description of action data                           |
|-------|------------------------------------------------------|
| \[1\] | Identifier of registered module file.                |
| \[2\] | Identifier of folder holding registered module file. |



 

## Remarks

The SelfRegModules action attempts to call the [DllRegisterServer](/windows/win32/api/olectl/nf-olectl-dllregisterserver) function of the module scheduled to be registered. This action runs with elevated privileges when the installation is being run with elevated privileges, such as during a per-machine installation. During a per-user installation the installer runs this action with user privileges.

Note that you cannot specify the order in which the installer registers self-registering DLLs by using the [SelfUnRegModules action](selfunregmodules-action.md).

## Related topics

<dl> <dt>

[Specifying the Order of Self Registration](specifying-the-order-of-self-registration.md)
</dt> </dl>

 

 
