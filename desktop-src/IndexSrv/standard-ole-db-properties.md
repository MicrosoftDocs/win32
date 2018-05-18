---
title: Standard OLE DB Properties
description: Standard OLE DB Properties
ms.assetid: 'c6d3964a-a7c4-48ad-84c3-4cd4669ab735'
---

# Standard OLE DB Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The OLE DB Provider for Indexing Service supports the standard OLE DB properties in the following table. The provider does not support other OLE DB properties. For a complete description of these properties, refer to the [OLE DB Programmer's Reference](3c5e2dd5-35e5-4a93-ac3a-3818bb43bbf8).



| Property                       | Settable | Default                                                                                                        |
|--------------------------------|----------|----------------------------------------------------------------------------------------------------------------|
| DBPROP\_BLOCKINGSTORAGEOBJECTS | FALSE    | VARIANT\_FALSE                                                                                                 |
| DBPROP\_BOOKMARKS              | TRUE     | VARIANT\_TRUE if the rowset is locatable.                                                                      |
| DBPROP\_BOOKMARKSKIPPED        | FALSE    | VARIANT\_FALSE                                                                                                 |
| DBPROP\_BOOKMARKTYPE           | FALSE    | Bookmarks are DBPROPVAL\_BMK\_NUMERIC                                                                          |
| DBPROP\_CACHEDEFERRED          | TRUE     | VARIANT\_FALSE                                                                                                 |
| DBPROP\_CANFETCHBACKWARDS      | FALSE    | VARIANT\_FALSE                                                                                                 |
| DBPROP\_CANHOLDROWS            | TRUE     | VARIANT\_TRUE if the rowset is locatable                                                                       |
| DBPROP\_CANSCROLLBACKWARDS     | FALSE    | VARIANT\_TRUE if the rowset is locatable                                                                       |
| DBPROP\_COLUMNRESTRICT         | FALSE    | VARIANT\_FALSE                                                                                                 |
| DBPROP\_COMMANDTIMEOUT         | TRUE     | The default is 0, which means no time-out.                                                                     |
| DBPROP\_DEFERRED               | TRUE     | VARIANT\_FALSE                                                                                                 |
| DBPROP\_FIRSTROWS              | TRUE     | The default is 0, which means this property will be disregarded and the DBPROP\_MAXROWS property will be used. |
| DBPROP\_LITERALBOOKMARKS       | FALSE    | VARIANT\_FALSE                                                                                                 |
| DBPROP\_LITERALIDENTITY        | FALSE    | VARIANT\_TRUE if the rowset is locatable                                                                       |
| DBPROP\_MAXOPENROWS            | FALSE    | The default is 0, which means no limit.                                                                        |
| DBPROP\_MAXROWS                | TRUE     | The default is 0, which means no limit.                                                                        |
| DBPROP\_MEMORYUSAGE            | TRUE     | The default is 0, which means no limit. Not implemented.                                                       |
| DBPROP\_ORDEREDBOOKMARKS       | FALSE    | VARIANT\_TRUE if the rowset is locatable                                                                       |
| DBPROP\_OTHERINSERT            | FALSE    | VARIANT\_TRUE if the rowset is asynchronous                                                                    |
| DBPROP\_OTHERUPDATEDELETE      | FALSE    | VARIANT\_TRUE if the rowset is asynchronous                                                                    |
| DBPROP\_QUICKRESTART           | FALSE    | VARIANT\_TRUE if the rowset is locatable                                                                       |
| DBPROP\_REENTRANTEVENTS        | FALSE    | VARIANT\_FALSE                                                                                                 |
| DBPROP\_REMOVEDELETED          | FALSE    | VARIANT\_TRUE                                                                                                  |
| DBPROP\_ROWRESTRICT            | FALSE    | VARIANT\_TRUE                                                                                                  |
| DBPROP\_ROWSET\_ASYNCH         | TRUE     | The default is 0, which means synchronous processing.                                                          |
| DBPROP\_ROWTHREADMODEL         | FALSE    | The default is DBPROPVAL\_RT\_FREETHREAD.                                                                      |
| DBPROP\_SERVERCURSOR           | FALSE    | VARIANT\_TRUE                                                                                                  |
| DBPROP\_STRONGIDENTITY         | FALSE    | VARIANT\_TRUE if the rowset is locatable                                                                       |
| DBPROP\_UPDATABILITY           | FALSE    | The default is 0, which means updates aren't supported.                                                        |



 

 

 




