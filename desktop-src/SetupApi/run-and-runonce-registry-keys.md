---
Description: Run and RunOnce registry keys cause programs to run each time that a user logs on.
ms.assetid: 5a6c17f1-d4c0-4005-9b26-036d8b27703a
title: Run and RunOnce Registry Keys
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Run and RunOnce Registry Keys

Run and RunOnce registry keys cause programs to run each time that a user logs on. The data value for a key is a command line no longer than 260 characters. Register programs to run by adding entries of the form *description*-*string*=*commandline*. You can write multiple entries under a key. If more than one program is registered under any particular key, the order in which those programs run is indeterminate.

The Windows registry includes the following four keys:

-   **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run**
-   **HKEY\_CURRENT\_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run**
-   **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce**
-   **HKEY\_CURRENT\_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce**

By default, the value of a RunOnce key is deleted before the command line is run. You can prefix a RunOnce value name with an exclamation point (!) to defer deletion of the value until after the command runs. Without the exclamation point prefix, if the RunOnce operation fails the associated program will not be asked to run the next time you start the computer.

By default, these keys are ignored when the computer is started in Safe Mode. The value name of RunOnce keys can be prefixed with an asterisk (\*) to force the program to run even in Safe mode.

A program run from any of these keys should not write to the key during its execution because this will interfere with the execution of other programs registered under the key. Applications should use the RunOnce or RunOnceServices keys only for transient conditions, such as to complete application setup. An application must not continually recreate entries under RunOnce or RunOnceServices because this will interfere with Windows Setup.

Run and RunOnce keys are run each time a new user logs in. RunServices and RunServicesOnce are run in the background when the logon dialog box first appears or at this stage of the boot process if there is no logon. These keys are for background services such as remote registry service and are run only once per boot. The Setup key is run only by Setup's first-boot activities, or after you use the Add/Remove Programs Wizard. This key displays the progress dialog box as the keys are run one at a time. For the Setup key, the name of the value is the name that is displayed in the dialog box.

 

 



