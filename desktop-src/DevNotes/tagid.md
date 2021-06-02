---
description: Contains the index of an entry and its TAG information in a shim database.
ms.assetid: '2ff58e01-cc47-4612-a3bc-a87ccb343bd2'
title: TAGID
ms.topic: article
ms.date: 05/31/2018
---

# TAGID

Contains the index of an entry and its TAG information in a shim database.


```C++
typedef DWORD TAGID;
```



## Remarks

A **TAGID** is specific to a database. It can be an integer value that represents the index, or one of the following values:

<dl> <dt>

<span id="TAGID_NULL__0_"></span><span id="tagid_null__0_"></span>TAGID\_NULL (0)
</dt> <dd>

The **TAGID** does not exist. This value is returned from a function when it cannot return a valid **TAGID**.

</dd> <dt>

<span id="TAGID_ROOT__0_"></span><span id="tagid_root__0_"></span>TAGID\_ROOT (0)
</dt> <dd>

Indicates a root list TAG that can be used as a parent to obtain a child **TAGID**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**TAG**](tag.md)
</dt> <dt>

[TAG Types](tag-types.md)
</dt> <dt>

[**TAGREF**](tagref.md)
</dt> </dl>

 

 




