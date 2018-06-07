---
Description: Describes a rule for access to items stored in protected storage.
ms.assetid: 22aebac3-46e9-4c66-bfaf-e82cf9d494cb
title: PST\_ACCESSRULE structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# PST\_ACCESSRULE structure

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](https://msdn.microsoft.com/765a68fd-f105-49fc-a738-4a8129eb0770) and [**CryptUnprotectData**](https://msdn.microsoft.com/54eab3b0-d341-47c6-9c32-79328d7a7155) functions.\]

Describes a rule for access to items stored in protected storage.

## Syntax


```C++
typedef struct {
  DWORD            cbSize;
  PST_ACCESSMODE   AccessModeFlags;
  DWORD            cClauses;
  PST_ACCESSCLAUSE *rgClauses;
} PST_ACCESSRULE, *PPST_ACCESSRULE;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size of this structure.

</dd> <dt>

**AccessModeFlags**
</dt> <dd>

The access modes to which a specified set of access clauses pertain.



| Value                                                                                                                                                                                                         | Meaning                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| <span id="PST_READ"></span><span id="pst_read"></span><dl> <dt>**PST\_READ**</dt> <dt>0x0001</dt> </dl>    | Read access mode.<br/>  |
| <span id="PST_WRITE"></span><span id="pst_write"></span><dl> <dt>**PST\_WRITE**</dt> <dt>0x0002</dt> </dl> | Write access mode.<br/> |



 

</dd> <dt>

**cClauses**
</dt> <dd>

The number of structures in the **rgClauses** array.

</dd> <dt>

**rgClauses**
</dt> <dd>

A pointer to an array of [**PST\_ACCESSCLAUSE**](pst-accessclause.md) structures.

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl> |



## See also

<dl> <dt>

[**PST\_ACCESSCLAUSE**](pst-accessclause.md)
</dt> <dt>

[**PST\_ACCESSRULESET**](pst-accessruleset.md)
</dt> </dl>

 

 




