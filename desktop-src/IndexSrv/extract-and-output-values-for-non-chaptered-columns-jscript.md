---
title: Extract and Output Values for Non-Chaptered Columns
description: Extract and Output Values for Non-Chaptered Columns
ms.assetid: 4bdf0346-9871-46c2-a3b8-9abfecf8cc97
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extract and Output Values for Non-Chaptered Columns

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code sub-segment iterates through all the fields of the objRS\_Parent [**Recordset**](https://www.bing.com/search?q=**Recordset**) object and concatenates the values of the columns in the parent recordset, excluding any chaptered columns.


```JScript
for (intI=0; intI<objRS_Parent.Fields.Count; intI++) {
    if (objRS_Parent(intI).Name != "Chapter") 
        strRecord = strRecord + "  " + objRS_Parent(intI).Value;
};
 
WScript.Echo(strRecord);
```



For the query properties set in this example, the *strRecord* variable is, for example, the following.

``` syntax
1.    c:\inetpub\iissamples\default
```

 

 




