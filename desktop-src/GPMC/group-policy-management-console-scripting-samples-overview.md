---
title: Group Policy Management Console Scripting Samples Overview
description: The Group Policy Management Console (GPMC) provides a set of sample scripts that use the GPMC interfaces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: df712beb-49ee-4688-859d-a857747e45f1
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
keywords:
- scripting overview
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Group Policy Management Console Scripting Samples Overview

The Group Policy Management Console (GPMC) provides a set of sample scripts that use the [GPMC interfaces](gpmc-interfaces.md). These samples were originally found in the %programfiles%\\Gpmc\\Scripts directory after you installed the GPMC, but can now be found on the [TechNet Code Gallery](https://gallery.technet.microsoft.com/Group-Policy-Management-17a5f840).

The sample scripts form the basis for a scripting toolkit that the Group Policy administrator can use to manage an organization. The scripts serve two purposes:

-   They address real-world scenarios and solve real-world administrative problems.
-   They illustrate the use of the key scripting objects and methods, and they provide an overview of the wide variety of tasks that administrators can accomplish with the GPMC.

The sample scripts can be modified to meet the needs of individual production environments, in accordance with the terms of the End User License Agreement.

The sample scripts were written using Microsoft Visual Basic Scripting Edition or Microsoft JScript. The sample scripts are designed to be executed using Windows Script Host (WSH). You execute all the scripts at the command prompt. To display the usage for a script, execute the script with the **/?** switch.

Because the sample scripts echo the output to the Command Prompt window, they should be executed using the CScript.exe application. If CScript.exe is not your default scripting host, you will need to explicitly specify CScript.exe at the command prompt, as shown in the following example:

**D:\\Program files\\gpmc\\scripts&gt;cscript listallgpos.wsf**

To make CScript.exe the default scripting host, run the following command:

**cscript //H:cscript**

Many of the sample scripts require a library of common helper functions from the Lib\_CommonGPMCFunctions.js file. If you copy the sample scripts to a different directory, you must also copy the Lib\_CommonGPMCFunctions.js file to that directory. Furthermore, many of the script samples have **Domain** or **DomainController** switches. If the **Domain** switch is not specified when the script is run, the domain of the user running the script is used. If the **Domain** switch is specified, it must be fully qualified, as follows:

example.microsoft.com

If the **DomainController** switch is also not specified, the script will be run using an available domain controller in the domain of the user.

For a brief description of the sample scripts, and an execution example, see [Group Policy Management Console Scripting Samples](group-policy-management-console-scripting-samples.md).

 

 




