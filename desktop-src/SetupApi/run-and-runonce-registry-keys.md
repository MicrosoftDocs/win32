---
description: Use Run or RunOnce registry keys to make a program run when a user logs on.
ms.assetid: 5a6c17f1-d4c0-4005-9b26-036d8b27703a
title: Run and RunOnce Registry Keys
ms.topic: article
ms.date: 01/04/2022
---

# Run and RunOnce Registry Keys

Use `Run` or `RunOnce` registry keys to make a program run when a user logs on. The `Run` key makes the program run every time the user logs on, while the `RunOnce` key makes the program run one time, and then the key is deleted. These keys can be set for the user or the machine.

The data value for a key is a command line no longer than 260 characters. Register programs to run by adding entries of the form *description*-*string*=*commandline*. You can write multiple entries under a key. If more than one program is registered under any particular key, the order in which those programs run is indeterminate.

The Windows registry includes the following four `Run` and `RunOnce` keys:

-   **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run**
-   **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce**
-   **HKEY\_CURRENT\_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run**
-   **HKEY\_CURRENT\_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce**

By default, the value of a `RunOnce` key is deleted before the command line is run. You can prefix a `RunOnce` value name with an exclamation point (!) to defer deletion of the value until after the command runs. Without the exclamation point prefix, if the `RunOnce` operation fails, the associated program will not be asked to run the next time you start the computer.

By default, these keys are ignored when the computer is started in Safe Mode. The value name of `RunOnce` keys can be prefixed with an asterisk (\*) to force the program to run even in Safe Mode.

A program that is run from any of these keys should not write to the key during its execution because this will interfere with the execution of other programs registered under the key. Applications should use the `RunOnce` key only for transient conditions, such as to complete application setup. An application must not continually recreate entries under `RunOnce` because this will interfere with Windows Setup.

## Related topics

[Windows Registry](../sysinfo/registry.md), [RunOnce Registry Key](/windows-hardware/drivers/install/runonce-registry-key)