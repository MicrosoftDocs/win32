---
title: Read through the Child Recordset Object, Extracting and Outputting Values for Chaptered Columns
description: Read through the Child Recordset Object, Extracting and Outputting Values for Chaptered Columns
ms.assetid: 40834941-b969-4ade-be82-aacd05ada5dc
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Read through the Child Recordset Object, Extracting and Outputting Values for Chaptered Columns

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code sub-segment steps through the child objRS\_Child [**Recordset**](https://www.bing.com/search?q=**Recordset**) object until an end of file occurs, and, for each child recordset (of filename, size, and write for this example), outputs the values in the child recordsets.


```JScript
intRS_Child_Count = 0;
while (!objRS_Child.EOF) {
    intRS_Child_Count = intRS_Child_Count + 1;
    strRecord = (intRS_Parent_Count + "." + intRS_Child_Count + ".      ").slice(0,8);
 
    for (intJ=0; intJ < objRS_Child.Fields.Count; intJ++) {
        if (objRS_Child(intJ).Name != "Chapter") {
            if (objRS_Child(intJ).Name != strGroupBy)
                strRecord = strRecord + "  " + objRS_Child(intJ).Value;
        };
    };
 
    WScript.Echo(strRecord);
    objRS_Child.MoveNext;
};
```



For the query properties set in this code example, the *strRecord* variable is, for example, the following.

``` syntax
1.1.      learn.asp  4859  Thu Sep 17 01:48:10 PDT 1998
1.2.      exair.asp  4641  Tue Jun 16 06:22:58 PDT 1998
...
```

 

 




