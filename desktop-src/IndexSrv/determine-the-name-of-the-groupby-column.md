---
title: Determine the Name of the GroupBy Column
description: Determine the Name of the GroupBy Column
ms.assetid: '508e23ee-14d9-48c5-a2e2-c3ed127c7926'
---

# Determine the Name of the GroupBy Column

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment iterates through all the fields of the objRS\_Parent [**Recordset**](mdobjodbrec) object and concatenates the names of the columns in the parent recordset, excluding any chaptered columns.


```VB
strGroupBy = ""
For intI = 0 to objRS_Parent.Fields.Count - 1
    If objRS_Parent(intI).Name <> "Chapter" Then
        If strGroupBy <> "" Then
            strGroupBy = strGroupBy & "    " & objRS_Parent(intI).Name
        Else
            strGroupBy = objRS_Parent(intI).Name
        End If
    End If
Next
```



For the properties set in this example, the *strGroupBy* variable is "DIRECTORY".

 

 




