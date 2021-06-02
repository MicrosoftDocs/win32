---
description: TAGREF - Contains the index of an entry and its TAG information in a shim database.
ms.assetid: e7d83dca-13a5-4396-b50b-0d068209c03c
title: TAGREF
ms.topic: reference
ms.date: 05/31/2018
---

# TAGREF

Contains the index of an entry and its TAG information in a shim database.


```C++
typedef DWORD TAGREF;
```



## Remarks

A **TAGREF** is specific to a shim database and valid across multiple databases. It can be an integer value that represents the index, or one of the following values:

<dl> <dt>

<span id="TAGREF_NULL__0_"></span><span id="tagref_null__0_"></span>TAGREF\_NULL (0)
</dt> <dd>

The **TAGREF** does not exist. This value is returned from a function when it cannot return a valid **TAGREF**.

</dd> <dt>

<span id="TAGREF_ROOT__0_"></span><span id="tagref_root__0_"></span>TAGREF\_ROOT (0)
</dt> <dd>

Indicates a root list TAG that can be used as a parent to obtain a child **TAGREF**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SdbTagRefToTagID**](sdbtagreftotagid.md)
</dt> <dt>

[**TAG**](tag.md)
</dt> <dt>

[TAG Types](tag-types.md)
</dt> <dt>

[**TAGID**](tagid.md)
</dt> </dl>

 

 




