---
description: Learn how to use the Standard User Analyzer (SUA) tool and SUA Wizard to test your applications and detect potential compatibility issues.
ms.assetid: 229ee531-32b9-4e11-b64c-3ce5b5ab6530
title: Standard User Analyzer (SUA) Tool and Standard User Analyzer Wizard (SUA Wizard)
ms.topic: article
ms.date: 05/31/2018
---

# Standard User Analyzer (SUA) Tool and Standard User Analyzer Wizard (SUA Wizard)

## Affected Platforms

**Clients:** Windows XP, Windows Vista, Windows 7  
**Servers:** Windows Server 2003, Windows Server 2008, Windows Server 2008 R2  

## Description

The Application Compatibility Toolkit includes the Standard User Analyzer (SUA) tool and the Standard User Analyzer Wizard (SUA Wizard). These tools enable you to test your applications and to monitor API calls in order to detect potential compatibility issues due to the User Account Control (UAC) feature in the Windows 7 operating system.

UAC, formerly known as Limited User Account (LUA), requires that all users (including members of the Administrator group) run as Standard Users by using the security prompt dialog box until the application is deliberately elevated. However, applications that require access and privileges for locations that are unavailable to a Standard User cannot run properly with the Standard User role.

## Usage

The following sections provide detailed information about how to use the SUA and SUA Wizard tools.

**SUA Tool**

The SUA tool enables you to analyze an application, review a detailed report about the UAC-related issues, and then apply the suggested and selected application mitigations, as shown in the following flowchart.

![Diagram that shows the flow of the S U A tool.](images/act-suaflowchart-appcookbook.gif)

*SUA Tool and Virtualization*

Only the SUA tool enables you to turn on and off the virtualization feature. By turning off the virtualization feature, the tested application will behave more like when it is functioning on the Windows XP operating system.

*SUA Tool and Elevated Privileges*

Only the SUA tool enables you to turn on and off the **Launch Elevated** feature. The Launch Elevated feature enables the selected application to run as an Administrator or as a Standard User. Depending on your selection, you will locate different types of UAC-related issues. If you clear the **Launch Elevated** check box, your application will run with full Administrator privileges, which enables SUA to predict the issues that might occur for a Standard User. If you select the Launch Elevated check box, you will see errors that result from the application actually running and generating errors.

**SUA Wizard**

The SUA Wizard enables you to follow a guided, step-by-step process by which you can analyze an application and then apply the suggested and selected application mitigations, as shown in the following flowchart. Unlike the SUA tool, the wizard does not enable a review of the detailed UAC-related issues.

![Diagram that shows the flow of the S U A Wizard.](images/act-suaflowchart-appcookbook.gif)

## Links to Other Resources

-   [Application Compatibility Toolkit Download](/windows-hardware/get-started/adk-install)
-   [Understanding the Standard User Analyzer Tools](/previous-versions/windows/it-pro/windows-7/cc838047(v=ws.10))
-   [Standard User Analyzer Technical Reference](/previous-versions/windows/it-pro/windows-7/cc765948(v=ws.10))
-   [Testing and Mitigating Issues by Using the Development Tools](/previous-versions/orphan-topics/ws.10/cc766461(v=ws.10))
-   [Application Compatibility and User Account Control](/previous-versions/windows/)

> [!Note]  
> These resources may not be available in some languages and countries/regions.

 

 

 
