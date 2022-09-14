---
description: Vsdiagview and Vssagent are tools that you can use to troubleshoot VSS applications.Note  These tools are included in the Microsoft Windows Software Development Kit (SDK) for Windows Vista and later.
ms.assetid: 2c1270a6-38c7-40d5-a194-0a6795557b9f
title: Using VSS Diagnostics
ms.topic: article
ms.date: 05/31/2018
---

# Using VSS Diagnostics

Vsdiagview and Vssagent are tools that you can use to troubleshoot VSS applications.

> [!Note]  
> These tools are included in the Microsoft Windows Software Development Kit (SDK) for Windows Vista and later. You can download the Windows SDK from [https://msdn.microsoft.com/windowsvista](https://msdn.microsoft.com/windows/default.aspx).

 

In the Windows SDK installation, these tools can be found in `%Program Files(x86)%\Windows Kits\8.1\bin\x64` (for 64-bit Windows) and `%Program Files(x86)%\Windows Kits\8.1\bin\x86` (for 32-bit Windows).

## Gathering Data

You can gather data by using the Vssagent command.

**To gather data using Vssagent**

1.  To gather data from the command line, use the Vssagent command as follows:

    **vssagent -gather** *XmlFileName***.xml**

2.  To view the output file, see the following Viewing Data section.

## Viewing Data

The Vsdiagview application can be used to view data that was gathered by using the Vssagent command. Vsdiagview displays the following information about the computer:

-   Information about the computer, such as the operating system version, total available memory, and CPU speed
-   The names and version numbers of the VSS binaries
-   The names and properties of the disk and volume devices
-   The names and properties of any COM+ applications
-   The names of event logs that can be used for diagnosing VSS problems
-   The names of any VSS writers and the events that they handle
-   Information about other operating system files

**To view data using Vsdiagview**

1.  In the File menu, choose **Open** to browse for a file. (The default location is C:\\vssdiag.)
2.  Click **Open** to view the data.

 

 



