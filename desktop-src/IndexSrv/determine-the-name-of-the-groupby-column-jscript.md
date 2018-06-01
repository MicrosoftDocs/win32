---
Description: Determine the Name of the GroupBy Column
ms.assetid: 9e0c5136-2177-4641-8214-9a2bd0097c38
title: Determine the Name of the GroupBy Column
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Determine the Name of the GroupBy Column

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment iterates through all the fields of the objRS\_Parent [**Recordset**](https://www.bing.com/search?q=**Recordset**) object and concatenates the names of the columns in the parent recordset, excluding any chaptered columns.


```JScript
strGroupBy = "";
for (intI=0; intI<objRS_Parent.Fields.Count; intI++) {
    if (objRS_Parent(intI).Name != "Chapter") {
        if (strGroupBy != "")
            strGroupBy = strGroupBy + "    " + objRS_Parent(intI).Name;
        else
            strGroupBy = objRS_Parent(intI).Name;
    );
);
```



For the properties set in this example, the *strGroupBy* variable is "DIRECTORY".

 

 



