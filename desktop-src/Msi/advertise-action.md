---
Description: The ADVERTISE action is a top-level action called to install or remove advertised components.
ms.assetid: d9c843e4-fcd9-4d47-9ca9-ffa83ed80574
title: ADVERTISE Action
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ADVERTISE Action

The ADVERTISE action is a top-level action called to install or remove advertised components.

## Sequence Restrictions

There are no sequence restrictions.

## ActionData Messages

There are no ActionData messages.

## Remarks

[*Advertising*](a-gly.md#-msi-advertising-gly) refers to the installer's ability to provide the loading and launching interfaces of an application without physically installing the application. The installer does not install the necessary components until a user or application activates an advertised interface. This concept is called [*install-on-demand*](i-gly.md#-msi-install-on-demand-gly).

The ADVERTISE action is not called from within the action table sequence, the Windows Installer executes this action when the command line executable Msiexec.exe is called with the '/j' command line switch or when [**MsiInstallProduct**](/windows/win32/Msi/nf-msi-msiinstallproducta?branch=master) is called with the *szCommandLine* parameter set to ACTION=ADVERTISE.

## Related topics

<dl> <dt>

[AdvtExecuteSequence Table](advtexecutesequence-table.md)
</dt> </dl>

 

 



