---
Description: The data types for Protected Storage methods.
ms.assetid: 4d494326-6d0f-4a12-83a2-3c3dd3ca9c1b
title: PStore Types
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# PStore Types

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](https://msdn.microsoft.com/en-us/library/Aa380261(v=VS.85).aspx) and [**CryptUnprotectData**](https://msdn.microsoft.com/en-us/library/Aa380882(v=VS.85).aspx) functions.\]

The data types for Protected Storage methods.


```C++
typedef DWORD PST_ACCESSMODE;
typedef DWORD PST_ACCESSCLAUSETYPE;
typedef DWORD PST_KEY;
```



<dl> <dt>

**PST\_ACCESSMODE**
</dt> <dd>

Defines the read or write mode of the access rule.

</dd> <dt>

**PST\_ACCESSCLAUSETYPE**
</dt> <dd>

Defines the clause type of the access rule.

</dd> <dt>

**PST\_KEY**
</dt> <dd>

Defines the key for the stored item.

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl> |



 

 




