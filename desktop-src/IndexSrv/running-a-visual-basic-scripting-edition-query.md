---
title: Running a Visual Basic Scripting Edition Query
description: Running a Visual Basic Scripting Edition Query
ms.assetid: 'c77eec47-1ed2-47b6-a710-8d8b3d4365e5'
---

# Running a Visual Basic Scripting Edition Query

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

You can run a script written in Visual Basic Scripting Edition (VBScript) to submit a query (or to perform a managing task) with Windows Script Host in several ways, which include the following.

**To execute a query such as VBScript.vbs as a command-prompt application**

1.  Open a command window and change the directory to the path of the script.
2.  Submit the query by entering, at the command-line prompt, **cscript vbscript.vbs**

The output of the script appears in the command window.

**To execute a query such as VBScript.vbs as a Windows application**

1.  Select **Start**, **Run...** from the Windows toolbar.
2.  Submit the query by entering the absolute path of the script in the **Open** dialog box or by clicking the **Browse** button to find the appropriate directory and select the script file.

The output of each **Echo** method in the script appears in a separate dialog box. This is handy for debugging, but for a query with a large number of matches you will need to close each dialog box to proceed.

 

 




