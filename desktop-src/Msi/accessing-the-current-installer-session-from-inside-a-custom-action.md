---
description: Nondeferred custom actions that call dynamic-link libraries or scripts may access a running installation to query or modify the attributes of the current installation session.
ms.assetid: cf70b0b3-ac81-47ab-a4c8-4db53ed9dc84
title: Accessing the Current Installer Session from Inside a Custom Action
ms.topic: article
ms.date: 05/31/2018
---

# Accessing the Current Installer Session from Inside a Custom Action

Nondeferred custom actions that call [dynamic-link libraries](dynamic-link-libraries.md) or [scripts](scripts.md) may access a running installation to query or modify the attributes of the current installation session. Only one **Session** object can exist for each process, and custom action scripts must not attempt to create another session.

Custom actions can only add, modify, or remove temporary rows, columns, or tables from a database. Custom actions cannot modify persistent data in a database, for example, data that is a part of the database stored on disk.

[Dynamic-Link Libraries](dynamic-link-libraries.md)

To access a running installation, custom actions that call dynamic-link libraries (DLL) are passed a handle of the type MSIHANDLE for the current session as the only argument to the DLL entry point named in the Target column of the [CustomAction Table](customaction-table.md). Because the installer provides this handle, the custom action should not close it, for example, to receive the handle *hInstall* from the installer, the custom action function is declared as follows.


```C++
UINT __stdcall CustomAction(MSIHANDLE hInstall)
```



For read-only access to the current database obtain the database handle by calling [**MsiGetActiveDatabase**](/windows/desktop/api/Msiquery/nf-msiquery-msigetactivedatabase). For more information, see [Obtaining a Database Handle](obtaining-a-database-handle.md).

[Scripts](scripts.md)

Custom actions written in VBScript or JScript can access the current installation session by using the [**Session Object**](session-object.md). The installer creates a **Session** object named "Session" that references the current installation. For read-only access to the current database use the [**Database**](session-database.md) property of the **Session** object.

Because a script is run from the context of the [**Session**](session-object.md) object, it is not always necessary to fully qualify properties and methods. In the following example, when using VBScript, the Me reference can replace the **Session** object, for example, the following three lines are equivalent.


```VB
Session.SetInstallLevel 1
```




```VB
Me.SetInstallLevel 1
```




```VB
SetInstallLevel 1
```



[Executable Files](executable-files.md)

You cannot access the current installer session from custom actions that call executable files launched with a command-line, for example, [Custom Action Type 2](custom-action-type-2.md) and [Custom Action Type 18](custom-action-type-18.md).

[Deferred Execution Custom Actions](deferred-execution-custom-actions.md)

You cannot access the current installer session or all property data from a deferred execution custom action. For more information, see [Obtaining Context Information for Deferred Execution Custom Actions](obtaining-context-information-for-deferred-execution-custom-actions.md).

## Related topics

<dl> <dt>

[Accessing a Database or Session from Inside a Custom Action](accessing-a-database-or-session-from-inside-a-custom-action.md)
</dt> </dl>

 

 



