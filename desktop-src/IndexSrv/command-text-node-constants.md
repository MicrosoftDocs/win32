---
title: Command-Text Node Constants
description: Command-Text Node Constants
ms.assetid: f13c22a8-27d6-4dd2-a65c-c6db2068731b
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Command-Text Node Constants

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The command-text node constants are a collection of globally unique identifiers (GUIDs) for the dialect of a command-text node.

``` syntax
DBGUID_SQL92       // Reserved for future use.
DBGUID_DBSQL       // This covers SQL used by OLE DB and ODBC.
                   // Deprecated; use DBGUID_DEFAULT instead.
extern const OLEDBDECLSPEC GUID DBGUID_DEFAULT = \
    {0xc8b521fb,0x5cf3,0x11ce, \
        {0xad,0xe5,0x00,0xaa,0x00,0x44,0x77,0x3d}};
DBGUID_TSQL        // Reserved for future use.
DBGUID_ACCESSSQL   // Reserved for future use.
```

### Remarks

To determine which dialects a provider supports, call [**IDBProperties::GetProperties**](https://msdn.microsoft.com/windows/desktop/5011f2ab-2131-49ed-bd8c-afd3b0daa32a) for the DBPROP\_SQLDIALECTS property. (For more information on using the **IDBProperties** interface, see the [OLE DB Programmer's Reference](https://msdn.microsoft.com/windows/desktop/3c5e2dd5-35e5-4a93-ac3a-3818bb43bbf8) in the Platform SDK.)

 

 




