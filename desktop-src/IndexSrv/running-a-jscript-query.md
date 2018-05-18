---
title: Running a JScript Query
description: Running a JScript Query
ms.assetid: '88c2c618-88e4-4c88-b445-173115a073c8'
---

# Running a JScript Query

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

You can run a script written in JScript to submit a query (or to perform a managing task) with Windows Script Host in several ways, which include the following.

**To execute a query like JScript.js as a command-prompt application**

1.  Open a command window and change the directory to the path of the script.
2.  Submit the query by entering, at the command-line prompt, **cscript jscript.js**

The output of the script appears in the command window.

**To execute a query like JScript.vbs as a Windows application**

1.  Select **Start**, **Run...** from the Windows toolbar.
2.  Submit the query by entering the absolute path of the script in the **Open** dialog box or by clicking the **Browse** button to find the appropriate directory and select the script file.

The output of each **Echo** method in the script appears in a separate dialog. This is handy for debugging, but for a query with a large number of matches, you will need to close each dialog box to proceed.

 

 




