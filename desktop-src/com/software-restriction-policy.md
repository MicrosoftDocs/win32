---
title: Software Restriction Policy
description: The software restriction policy (SRP) settings were introduced with the release of Windows XP to help protect systems from unknown and possibly dangerous code.
ms.assetid: 44b4e448-f5b4-4483-b53b-506938b36857
ms.topic: article
ms.date: 05/31/2018
---

# Software Restriction Policy

The software restriction policy (SRP) settings were introduced with the release of Windows XP to help protect systems from unknown and possibly dangerous code. The SRP provides a mechanism where only trusted code is given unrestricted access to a user's privileges. Unknown code, which might contain viruses or code that conflicts with currently installed programs, is allowed to run only in a constrained environment (often called a *sandbox*) where it is disallowed from accessing any security-sensitive user privileges. Properly using the SRP can make your business more agile because it provides a proactive framework for preventing problems, rather than a reactive framework that relies on the costly alternative of restoring a system after a problem has occurred.

The SRP depends upon assigning trust levels to the code that can run on a system. Currently, two trust levels exist: Unrestricted and Disallowed. Code that has an Unrestricted trust level is given unrestricted access to the user's privileges, so this trust level should be applied only to fully trusted code. Code with a Disallowed trust level is disallowed from accessing any security-sensitive user privileges and can run only in a sandbox so that Unrestricted code cannot load the Disallowed code into its address space.

The SRP configuration of individual COM applications is done through the [SRPTrustLevel](srptrustlevel.md) value in the application's [AppID](appid-key.md) key in the registry. If the SRP trust level is not specified for a COM application, the default value of Disallowed is used. A COM application that has an Unrestricted trust level has unrestricted access to the user's privileges but can load only components with an Unrestricted trust level, while a Disallowed COM application can load components with any trust level but cannot access any security-sensitive user privileges.

In addition to the SRP trust levels of individual COM applications, two other SRP properties determine how the SRP is used for all COM applications. If [SRPRunningObjectChecks](srprunningobjectchecks.md) is enabled, attempts to connect to running objects will be checked for appropriate SRP trust levels. The running object cannot have a less stringent SRP trust level than the client object. For example, the running object cannot have a Disallowed trust level if the client object has an Unrestricted trust level.

The second property determines how the SRP handles activate-as-activator connections. If [SRPActivateAsActivatorChecks](srpactivateasactivatorchecks.md) is enabled, the SRP trust level that is configured for the server object is compared with the SRP trust level of the client object and the more stringent trust level will be used to run the server object. If **SRPActivateAsActivatorChecks** is not enabled, the server object runs with the SRP trust level of the client object, regardless of the SRP trust level with which it was configured. By default, both **SRPRunningObjectChecks** and **SRPActivateAsActivatorChecks** are enabled.

 

 




