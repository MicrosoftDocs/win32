---
title: Debugging Extension DLLs
description: Procedure to debug a cluster administrator extension DLL.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ccbac97f-7507-4350-8cff-d66d379f0a1e'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Cluster Administrator Failover Cluster ,extension DLLs,debugging"]
---

# Debugging Extension DLLs

The following procedure describes how to debug a [Cluster Administrator](cluster-administrator.md) extension DLL:

**To debug a Cluster Administrator extension DLL**

1.  Run your debugger and load the project workspace that contains your Cluster Administrator extension DLL project.
2.  Select the debug version of your Cluster Administrator extension DLL project.
3.  On the **Build** menu, click **Settings**.
4.  In the **Settings For** box, click the entry that represents the debug version of your Cluster Administrator extension DLL project.
5.  Click the **Debug** tab to switch to the **Debug** property page.
6.  Type the full path to Cluster Administrator (typically C:\\Windows\\Cluster\\CluAdmin.exe) in the **Executable for debug session** box and click **OK**.
7.  Set a breakpoint in the project, such as at the **OnInitDialog** method for the parameter page in the ResProp.cpp source file.
8.  Press **F5** to start Cluster Administrator in the debugger.
9.  View the properties of a resource of the type supported by your Cluster Administrator extension DLL.
10. Click the **Parameters** tab to switch to the **Parameters** page. This should cause the debugger to halt at the breakpoint set in step 7.

    The debugger should also halt when you create a new resource of the type supported by your extension DLL.

> \[!Warning\]  
> If you are not running the [Cluster service](cluster-service.md) interactively (that is, from the command line), trying to debug a resource DLL with the MSDEV debugger causes the appearance of an error dialog box.

 

 

 




