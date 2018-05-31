---
title: Declare Variables
description: Declare Variables
ms.assetid: fdca9b81-981b-4fb5-9509-be59a8194bc1
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Declare Variables

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment declares all the (global) variables for the script, because the script doesn't contain any **Sub** or **Function** procedures with local variables. Although it is optional to declare variables before you use them in VBScript, it is good programming practice to use the **Option Explicit** statement and to declare variables that the script uses.


```VB
Option Explicit
 
Dim strGroupBy          ' Name of GroupBy column.
Dim intI, intJ          ' Index variables.
Dim objQ                ' Query object.
Dim strRecord           ' Output record of query results.
Dim objRS_Child         ' Child Recordset object.
Dim objRS_Parent        ' Parent Recordset object.
Dim intRS_Child_Count   ' Number of current record of child Recordset.
Dim intRS_Parent_Count  ' Number of current record of parent Recordset.
Dim objU                ' Utility object.
```



 

 




