---
Description: Indexing Service Predefined Views
ms.assetid: 57193623-aeae-47cc-b053-b1e79e868d3d
title: Indexing Service Predefined Views
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Indexing Service Predefined Views

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The SQL extensions include several predefined views that you can use without writing an explicit [CREATE VIEW statement](create-view-statement.md). Because the predefined view names are permanent, they do not need to be preceded by the number sign (\#).

The following table lists the predefined views for Indexing Service, which are always available, regardless of the catalog you are currently using.



| Predefined View    | Properties                                                                                          | Description                             |
|--------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------|
| FILEINFO           | path, FileName, size, write, attrib                                                                 | Standard file result list               |
| FILEINFO\_ABSTRACT | path, FileName, size, write, attrib, Characterization                                               | Standard file result list plus abstract |
| EXTENDED\_FILEINFO | path, FileName, size, write, attrib, DocTitle, DocAuthor, DocSubject, DocKeywords, Characterization | Extended file result list               |
| WEBINFO            | Vpath, path, FileName, size, write, attrib, Characterization, DocTitle                              | Standard Web results                    |
| EXTENDED\_WEBINFO  | Vpath, path, FileName, size, Characterization, write, DocAuthor, DocSubject, DocKeywords, DocTitle  | Extended Web results                    |



 

### Example

The following example shows a conceptual SQL statement that defines the FILEINFO predefined view. All predefined views are constructed using the default scope.


```
CREATE VIEW FILEINFO AS
  SELECT path, FileName, size, write, attrib
  FROM SCOPE()
```



Without creating the FILEINFO view (it is predefined), you can issue queries such as the following.


```
SELECT * FROM FILEINFO
  WHERE size > 20000
SELECT path, FileName, attrib
  FROM FILEINFO
  WHERE attrib = ALL ARRAY [0x820]
  OR FileName LIKE 'arch%.xls'
```



## Related topics

<dl> <dt>

[CREATE VIEW Statement](create-view-statement.md)
</dt> <dt>

[Site Server Predefined Views](site-server-predefined-views.md)
</dt> </dl>

 

 



