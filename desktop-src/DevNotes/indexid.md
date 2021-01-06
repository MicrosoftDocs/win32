---
description: The identifier of the index to be accessed in a database.
ms.assetid: 559e73bf-91c2-4dbf-a667-e5c0431aaffa
title: INDEXID
ms.topic: reference
ms.date: 05/31/2018
---

# INDEXID

The identifier of the index to be accessed in a database.


```C++
typedef DWORD INDEXID;
```



## Remarks

An **INDEXID** can be an integer value that represents the index, or the following value:

<dl> <dt>

<span id="INDEXID_NULL___INDEXID_-1_"></span><span id="indexid_null___indexid_-1_"></span>INDEXID\_NULL ((INDEXID)-1)
</dt> <dd>

An invalid **INDEXID**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SdbDeclareIndex**](sdbdeclareindex.md)
</dt> <dt>

[**SdbStartIndexing**](sdbstartindexing.md)
</dt> <dt>

[**SdbStopIndexing**](sdbstopindexing.md)
</dt> </dl>

 

 




