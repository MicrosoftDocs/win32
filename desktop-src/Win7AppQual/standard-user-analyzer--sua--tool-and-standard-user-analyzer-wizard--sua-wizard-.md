---
Description: .
ms.assetid: 229ee531-32b9-4e11-b64c-3ce5b5ab6530
title: Standard User Analyzer (SUA) Tool and Standard User Analyzer Wizard (SUA Wizard)
ms.topic: article
ms.date: 05/31/2018
---

# Standard User Analyzer (SUA) Tool and Standard User Analyzer Wizard (SUA Wizard)

## Affected Platforms

<dl> **Clients:** Windows XP \| Windows Vista \| Windows 7  
**Servers:** Windows Server 2003 \| Windows Server 2008 \| Windows Server 2008 R2  
</dl>

## Description

The Application Compatibility Toolkit includes the Standard User Analyzer (SUA) tool and the Standard User Analyzer Wizard (SUA Wizard). These tools enable you to test your applications and to monitor API calls in order to detect potential compatibility issues due to the User Account Control (UAC) feature in the Windows 7 operating system.

UAC, formerly known as Limited User Account (LUA), requires that all users (including members of the Administrator group) run as Standard Users by using the security prompt dialog box until the application is deliberately elevated. However, applications that require access and privileges for locations that are unavailable to a Standard User cannot run properly with the Standard User role.

## Usage

The following sections provide detailed information about how to use the SUA and SUA Wizard tools.

**SUA Tool**

The SUA tool enables you to analyze an application, review a detailed report about the UAC-related issues, and then apply the suggested and selected application mitigations, as shown in the following flowchart.

![](images/act-suaflowchart-appcookbook.gif)

*SUA Tool and Virtualization*

Only the SUA tool enables you to turn on and off the virtualization feature. By turning off the virtualization feature, the tested application will behave more like when it is functioning on the Windows XP operating system.

*SUA Tool and Elevated Privileges*

Only the SUA tool enables you to turn on and off the **Launch Elevated** feature. The Launch Elevated feature enables the selected application to run as an Administrator or as a Standard User. Depending on your selection, you will locate different types of UAC-related issues. If you clear the **Launch Elevated** check box, your application will run with full Administrator privileges, which enables SUA to predict the issues that might occur for a Standard User. If you select the Launch Elevated check box, you will see errors that result from the application actually running and generating errors.

**SUA Wizard**

The SUA Wizard enables you to follow a guided, step-by-step process by which you can analyze an application and then apply the suggested and selected application mitigations, as shown in the following flowchart. Unlike the SUA tool, the wizard does not enable a review of the detailed UAC-related issues.

![](images/act-suaflowchart-appcookbook.gif)

## Links to Other Resources

-   [Application Compatibility Toolkit Download](https://www.microsoft.com/downloads/details.aspx?FamilyId=24DA89E9-B581-47B0-B45E-492DD6DA2971)
-   [Understanding the Standard User Analyzer Tools](https://technet.microsoft.com/library/cc838047.aspx)
-   [Standard User Analyzer Technical Reference](https://technet.microsoft.com/library/cc765948.aspx)
-   [Testing and Mitigating Issues by Using the Development Tools](https://technet.microsoft.com/pt-pt/library/cc766461(WS.10).aspx)
-   [Application Compatibility and User Account Control](https://technet.microsoft.com/windows/aa905066.aspx)

> [!Note]  
> These resources may not be available in some languages and countries/regions.

 

 

 



