---
Description: 'The INSTALL action is a top-level action called to install or remove components.'
ms.assetid: 'bf290b59-1ecb-410f-b1f6-fdbeebebe3d3'
title: INSTALL Action
---

# INSTALL Action

The INSTALL action is a top-level action called to install or remove components. This action queries the [InstallUISequence Table](installuisequence-table.md) and [InstallExecuteSequence Table](installexecutesequence-table.md) for the action to execute, the condition for action execution, and the place of the action in the sequence:

## Sequence Restrictions

There are no sequence restrictions.

## ActionData Messages

There are no ActionData messages.

## Remarks

The INSTALL action is not called from within the action table sequence, it is passed to Windows Installer when [**MsiInstallProduct**](msiinstallproduct.md) is called, or the command line executable Msiexec.exe is called with the '**/i**' command line switch, or when any installer function is called that may perform an installation task, such as [**MsiConfigureFeature**](msiconfigurefeature.md), [**MsiProvideComponent**](msiprovidecomponent.md), or [**MsiInstallMissingFile**](msiinstallmissingfile.md).

 

 



