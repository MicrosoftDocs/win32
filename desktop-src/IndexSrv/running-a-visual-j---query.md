---
title: Running a Visual J++ Query
description: Running a Visual J++ Query
ms.assetid: 783e71a0-bd2f-433b-b1a5-89b84b5fbcf5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Running a Visual J++ Query

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

You can run a Visual J++ application to submit a query in several ways, which include the following.

**To execute a Visual J++ query for a command-prompt application**

1.  Set the PATH environment variable to include "D:\\mssdk\\Bin", where D: is the drive on which you installed the Platform SDK.

2.  Open a command window and change the directory to the path of the Visual J++ application.

3.  Submit a query by entering, at the command-line prompt:

    **jview /p /cp:p "&lt;JAVAPACKAGES&gt;"** *query-application-command*

    where *query-application-command* is the command line for the application. For appropriate values of *query-application-command* for the [VJQuery Sample](vjquery-sample.md), see the User's Guide for that sample.

    The output of the script appears in the command window in which you run Jview.

**To execute a Visual J++ query for a Windows application**

1.  Select **Start**, **Run...** from the Windows toolbar.

2.  Submit the query by entering, at the command prompt:

    **wjview /p /cp:p "&lt;JAVAPACKAGES&gt;"** *query-application-command*

    where *query-application-command* is the command line for the application.

    Wjview spawns a separate window process for windows-based applications, and is inappropriate for Visual J++ command applications (like VJQuery) that require input from or output to a command window.

 

 




