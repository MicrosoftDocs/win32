---
title: Query Status Properties
description: Query Status Properties
ms.assetid: b57534e0-f267-409d-9ac2-6f88a85fb82c
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Query Status Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following table includes dynamic properties for determining the status of queries using the ADO **Recordset** object.



| Property                                        | Data Type  | Property Group      | Read/Write | Description                        |
|-------------------------------------------------|------------|---------------------|------------|------------------------------------|
| Rowset Query Status (DBPROP\_RowsetQueryStatus) | DBTYPE\_I4 | DBPROPFLAGS\_ROWSET | RO         | Indicates the rowset query status. |



 

The status can be any of the following values.



| Status                           | Value     |
|----------------------------------|-----------|
| STAT\_BUSY                       | ( 0 )     |
| STAT\_ERROR                      | ( 0x1 )   |
| STAT\_DONE                       | ( 0x2 )   |
| STAT\_CONTENT\_OUT\_OF\_DATE     | ( 0x20 )  |
| STAT\_CONTENT\_QUERY\_INCOMPLETE | ( 0x80 )  |
| STAT\_TIME\_LIMIT\_EXCEEDED      | ( 0x100 ) |



 

 

 




