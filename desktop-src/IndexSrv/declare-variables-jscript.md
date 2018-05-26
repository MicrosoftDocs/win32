---
title: Declare Variables
description: Declare Variables
ms.assetid: 117d00b7-b11e-4d56-ab4a-c2b548352f2e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Declare Variables

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment declares all the (global) variables for the script, because the script doesn't contain any functions with local variables. Although it is optional to declare global variables before you use them in JScript, it is good programming practice to do so.


```JScript
var strGroupBy;         // Name of GroupBy column.
var intI, intJ;         // Index variables.
var objQ;               // Query object.
var strRecord;          // Output record of query results.
var objRS_Child;        // Child Recordset object.
var objRS_Parent;       // Parent Recordset object.
var intRS_Child_Count;  // Number of current record of child Recordset.
var intRS_Parent_Count; // Number of current record of parent Recordset.
var objU;               // Utility object.
```



 

 




