---
title: Read Through the Parent Recordset Object
description: Read Through the Parent Recordset Object
ms.assetid: 598a4c05-29f2-4eed-81d6-235e3d0dba23
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Read Through the Parent Recordset Object

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment steps through the parent objRS\_Parent [Recordset](https://www.bing.com/search?q=Recordset) object until an end of file occurs. For each parent recordset (directory for this example), the code segment outputs the values of the child recordsets (file names, sizes, and writes for this example).

The following pseudo-code divides the segment into sub-segments and shows the structure of the complete segment. The individual topic for each sub-segment describes the details of the code for that sub-segment.


```JScript
intRS_Parent_Count = 0;
while (!objRS_Parent.EOF) {
    intRS_Parent_Count = intRS_Parent_Count + 1;
    strRecord = (intRS_Parent_Count + ".      ").slice(0, 4);
 
    // Extract and Output Values for Non-Chaptered Columns.
    // Create a Child Recordset Object for Chaptered Columns.
    // Read through the Child Recordset Object, Extracting and Outputting Values for Chaptered Columns.
    // Close the Child Recordset Object.
 
    objRS_Parent.MoveNext;
);
```



The output when running the script with cscript.exe is similar to the following.

``` syntax
1.    c:\inetpub\iissamples\default
1.1.      learn.asp  4859  9/17/98 1:48:10 AM
1.2.      exair.asp  4641  6/16/98 6:22:58 AM
2.    c:\inetpub\iissamples\sdk\asp\applications
2.1.      session_vbscript.asp  1553  5/30/98 2:52:24 AM
2.2.      session_jscript.asp  1568  5/30/98 2:52:24 AM
2.3.      application_vbscript.asp  2011  5/30/98 2:52:24 AM
2.4.      application_jscript.asp  2017  5/30/98 2:52:24 AM
...
```

## Related topics

<dl> <dt>

[Extract and Output Values for Non-Chaptered Columns](extract-and-output-values-for-non-chaptered-columns-jscript.md)
</dt> <dt>

[Create a Child Recordset Object for Chaptered Columns](create-a-child-recordset-object-for-chaptered-columns-jscript.md)
</dt> <dt>

[Read through the Child Recordset Object, Extracting and Outputting Values for Chaptered Columns](read-through-the-child-recordset-object--extracting-and-outputting-values-for-chaptered-columns-jscript.md)
</dt> <dt>

[Close the Child Recordset Object](close-the-child-recordset-object-jscript.md)
</dt> </dl>

 

 




