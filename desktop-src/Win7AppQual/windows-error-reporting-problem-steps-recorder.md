---
description: Windows Error Reporting Problem Steps Recorder
ms.assetid: ce5db84a-53b6-4a7f-bee4-d198d8a6781e
title: Windows Error Reporting Problem Steps Recorder
ms.topic: article
ms.date: 05/31/2018
---

# Windows Error Reporting Problem Steps Recorder

## Affected Platforms

**Clients** – Windows 7  
**Servers** – Windows Server 2008 R2  


## Description

Prior to Windows 7, Windows Error Reporting (WER) collected error reports that indicated problems in need of repair. These error reports contain helpful information that describes the general nature of a problem, but not enough information to determine its root cause. For that, developers need a tool to reproduce the crash/hang scenario for debugging.

A new application, Problem Steps Recorder (PSR.exe), is shipping on all builds of Windows 7. This feature enables the collection of the actions performed by a user while encountering a crash so that testers and developers can reproduce the situation for analysis and debugging.

## Usage

Currently, a Windows Error Reporting service developer must request PSR enablement for an application; Microsoft support organizations also use this tool while troubleshooting with end users. Plans are in place to make PSR available at Windows Quality Online Services (Winqual) after the release of Windows 7.

**Note:** With PSR enabled for an application, the application may see some performance degradation.

## Links to Other Resources

-   [Windows Error Reporting blog entry](/archive/blogs/wer/)
-   [Windows Quality Online Services (Winqual)](https://winqual.microsoft.com)

 

 
