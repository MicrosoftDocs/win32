---
title: Output Query Properties
description: Output Query Properties
ms.assetid: 3740e3ce-a452-4362-a4a9-9c80985f0f27
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Output Query Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the **Echo** method of the **WScript** object to output the properties of the query that the script set earlier. When the script is run as a Windows application using wscript.exe, each **Echo** method produces a dialog box with its specified output. When run with cscript.exe at the command prompt, each **Echo** method produces a line of output.


```VB
WScript.Echo " Columns = " & objQ.Columns
WScript.Echo " Query = " & objQ.Query
WScript.Echo " GroupBy = " & objQ.GroupBy
WScript.Echo " Catalog = " & objQ.Catalog
WScript.Echo " CiScope = " & objQ.CiScope
WScript.Echo " CiFlags = " & objQ.CiFlags
WScript.Echo " OptimizeFor = " & objQ.OptimizeFor)
WScript.Echo " AllowEnumeration = " & CStr(objQ.AllowEnumeration)
WScript.Echo " MaxRecords = " & objQ.MaxRecords
```



Up to this point, the output when running the script with cscript.exe is the following.

``` syntax
 Columns = filename, directory, size, write
 Query = #filename *.asp
 GroupBy = directory[a]
 Catalog = system
 CiScope = \
 CiFlags = DEEP
 OptimizeFor = recall,hitcount
 AllowEnumeration = TRUE
 MaxRecords = 20000
```

 

 




