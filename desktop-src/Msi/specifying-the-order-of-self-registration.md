---
description: Note that you cannot specify the order in which the installer registers or unregisters self-registering DLLs by using the SelfRegModules and SelfUnRegModules actions.
ms.assetid: 46ee5ea2-35fd-4352-8a45-572d6fb5e080
title: Specifying the Order of Self Registration
ms.topic: article
ms.date: 05/31/2018
---

# Specifying the Order of Self Registration

Note that you cannot specify the order in which the installer registers or unregisters self-registering DLLs by using the [SelfRegModules](selfregmodules-action.md) and [SelfUnRegModules](selfunregmodules-action.md) actions. These actions register all the modules listed in the [SelfReg table](selfreg-table.md). The installer does not self-register .exe files.

To specify the order in which the installer registers or unregisters modules, you must use two [custom actions](custom-actions.md) for each module. One custom action for DllRegisterServer and a second for DllUnregisterServer. These custom actions must then be authored in the [InstallExecuteSequence table](installexecutesequence-table.md) at the point in the sequence wherever the DLL is to be registered or unregistered.

The following example illustrates how to author the database to schedule the self-registration of a DLL at a particular point in the action sequence.

[File Table](file-table.md) (partial)



| File  | Component\_ | FileName  | Sequence |
|-------|-------------|-----------|----------|
| mydll | myComponent | Mydll.dll | 13       |



 

[Component Table](component-table.md) (partial)



| Component   | ComponentId | Directory\_ | KeyPath |
|-------------|-------------|-------------|---------|
| myComponent | {*a GUID*}  | myFolder    | mydll   |



 

[Directory Table](directory-table.md)



| Directory | Directory\_Parent | DefaultDir          |
|-----------|-------------------|---------------------|
| TARGETDIR |                   | SourceDir           |
| myFolder  | TARGETDIR         | myFolder\|My Folder |



 

[CustomAction Table](customaction-table.md)



| Action     | Type | Source   | Target                                     |
|------------|------|----------|--------------------------------------------|
| mydllREG   | 3170 | myFolder | "\[SystemFolder\]msiexec" /y "\[\#mydll\]" |
| mydllUNREG | 3170 | myFolder | "\[SystemFolder\]msiexec" /z "\[\#mydll\]" |



 

[InstallExecuteSequence Table](installexecutesequence-table.md) (partial)



| Action           | Condition         | Sequence |
|------------------|-------------------|----------|
| SelfUnregModules |                   | 2200     |
| mydllUNREG       | $myComponent=2    | 2201     |
| RemoveFiles      |                   | 3500     |
| InstallFiles     |                   | 4000     |
| SelfRegModules   |                   | 6500     |
| mydllREG         | $myComponent>2 | 6501     |



 

 

 



