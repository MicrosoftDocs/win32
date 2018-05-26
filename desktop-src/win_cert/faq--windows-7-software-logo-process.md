---
title: FAQ Windows 7 software logo process
description: FAQ Windows 7 software logo process
ms.assetid: BD152E61-EF56-4525-9F6A-117936D2E46A
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FAQ: Windows 7 software logo process

## What is the cost to get a product certified as compatible with Windows 7?

There is no cost associated to test your app for the Compatible with Windows 7 Software Logo Program. You only need to have a Dashboard account to create the submission. However, to create a new Dashboard account, you need a code signing certificate. Find more details about getting a [code-signing certificate.](https://msdn.microsoft.com/library/windows/hardware/mt786451)

## Why is code signing required?

Signing the app files (.exe, .dll, .ocx, .sys, .cpl, .drv, .scr) using an Authenticode digital signature allows users to be sure that the software is genuine. It also allows detection if a file has been tampered with; for example, infected by a virus. Kernel-mode code signing enforcement is a Windows feature known as code integrity (CI) that improves the security of the operating system (OS), by verifying the integrity of a file each time the image of the file is loaded into memory. CI detects whether malicious code has modified a system binary file. It also generates diagnostic and system-audit log events when the signature of a kernel module fails to verify correctly.

## How do I code-sign files with my code signing certificate using SignTool.exe?

You can follow the Readme document that comes as part of the zip package that you get from the Sysdev signup process. You can also refer to Sysdev Help.

## Do we need to retest for compatible with Windows 7 if we have a version change?

Just as you should validate your app’s eligibility before testing it with the toolkit, you should also validate the eligibility for major and minor version changes. The **Windows 7 Client Software Logo Program** considers apps distinct when they have differing major or minor versions. In general, app version numbers are broken down to **Major, Minor, Build, and Revision**. In your app, if the major and minor versions are not same, then you must retest and resubmit these apps. **Updates only to the build or revision do not require retesting and resubmission**. For more details, see [Windows 7 Client Software Logo Program Technical Requirements](http://go.microsoft.com/fwlink/p/?LinkId=708306).

Example of version changes that do not require resubmission:

-   1.0.0.0 To 1.0.1.1
-   2.1 To 2.1.1

Example of version changes that require resubmission:

-   1.0.1.1 To 1.1.1.1
-   2.0.1 To 2.1
-   2.1 To 3

## How can we apply for a waiver for the Windows 7 Client Software Logo Program?

The waiver process is now built into the automated Windows 7 Client Software Logo Toolkit itself. After you run through the tests using the toolkit, it will provide you with an option to apply for a waiver on your failed test cases.

## Can we use the same waiver for all the submissions?

A waiver is valid for only one submission. In the future, if you submit another version of the same app, you must apply for a waiver again.

## Are plug-ins eligible for the Compatible with Windows 7 Logo Program?

Plug-ins/add-ins are not eligible for the software logo program. To be eligible for the Windows 7 Client Software Logo Program, an app should be able to run on its own and be detected by the OS (make an ARP entry/footprint on the system). For further requirements on app eligibility, check the Technical Requirements and Program Eligibility document.

## Are ClickOnce apps eligible for the software logo program?

Online-only (network deployed, no physical existence in the system) ClickOnce apps are currently not eligible for the logo program because they don’t have any footprint in the system and therefore are not detected by the OS (in ARP) or by the logo toolkit.

Offline ClickOnce apps (detected by both the OS and the toolkit) are eligible for the program.

## Do we receive any confirmation mail after a successful submission?

You might not receive any confirmation email after a successful submission to the Dashboard. In the Windows 7 Client Software Logo Program, the submission status itself is the confirmation.

## How do we map drivers to WER?

Log in to the Dashboard, navigate to Hardware, and then Manage Driver Mapping (in the far-left menu).

 

 




