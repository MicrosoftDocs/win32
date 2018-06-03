---
title: Scripting Example
description: The following scripting example uses XML, Windows Script Host, and Microsoft Visual Basic Scripting Edition (VBScript) to create an extensible command-line interface for Network Load Balancing.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bb0ec401-dc84-4d49-a611-678237e5999a
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Scripting Example

The following scripting example uses XML, Windows Script Host, and Microsoft Visual Basic Scripting Edition (VBScript) to create an extensible command-line interface for Network Load Balancing. The code is presented in three sections:



| Section                                             | Description                                                                                                           |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [Nlb.xml](nlb-xml.md)<br/>                   | Contains configuration data in an XML document.<br/>                                                            |
| [NlbScriptLib.vbs](nlbscriptlib-vbs.md)<br/> | Contains common functions and constants (VBScript) used by all of the jobs in Nlb.wsf.<br/>                     |
| [Nlb.wsf](nlb-wsf.md)<br/>                   | A Windows Script Host (WSH) script that defines a number of jobs that can be called from the command line.<br/> |



 

 

 





