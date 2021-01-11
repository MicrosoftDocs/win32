---
description: To help maintain secure a software installation, adhere to these guidelines when authoring a Windows Installer custom action.
ms.assetid: f7081b0c-bfa2-47a1-840b-28881ad97071
title: Guidelines for Securing Custom Actions
ms.topic: article
ms.date: 05/31/2018
---

# Guidelines for Securing Custom Actions

Adherence to the following guidelines when authoring a Windows Installer package with custom actions helps maintain a secure environment during installation:

-   Secure any additional files written by your custom action.
-   Check buffer lengths and validity of all data read by your custom action. This includes properties that may supply data to your custom action, particularly those that use public properties provided by a user.
-   Do not rely on external DLLs that are not trusted by the system on all platforms on which your installation package is intended to run.
-   Carefully consider whether to use custom actions that use [*elevated*](e-gly.md) privileges or impersonation. Custom actions such as “open a URL after installation is completed,” “launch the software after installation is complete,” or “launch ReadMe after installation is complete” would not usually require elevated privileges to function. If your custom action must run with *elevated* privileges, be sure that the custom action code guards against buffer overruns and inadvertent loading of unsafe code. Note that during the execution phase of the installation, the installer passes information to a process with *elevated* privileges and runs the script. Any custom actions that run during the execution phase may run with *elevated* privileges.
-   Gather all information provided by the user during the UI sequence. Do not prompt the user for any information that can't be set using a public property.
-   If your script custom action expands properties, take precautions that the custom action is secured against the possibility of script injection. Script may be logged in clear text.

See also [Custom Action Security](custom-action-security.md).

 

 



