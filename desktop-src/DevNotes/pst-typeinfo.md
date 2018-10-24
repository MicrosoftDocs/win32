---
Description: Describes a type or a subtype.
ms.assetid: 4b6b77d9-54ea-4101-9c8b-e525f9aa3816
title: PST_TYPEINFO structure
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PST_TYPEINFO
api_type: 
- HeaderDef
api_location: 
- Pstore.h
---

# PST\_TYPEINFO structure

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](https://msdn.microsoft.com/en-us/library/Aa380261(v=VS.85).aspx) and [**CryptUnprotectData**](https://msdn.microsoft.com/en-us/library/Aa380882(v=VS.85).aspx) functions.\]

Describes a type or a subtype.

## Syntax


```C++
typedef struct {
  DWORD  cbSize;
  LPWSTR szDisplayName;
} PST_TYPEINFO, *PPST_TYPEINFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size of this structure.

</dd> <dt>

**szDisplayName**
</dt> <dd>

A pointer to a wide character string that represents the display name for the type.

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl> |



## See also

<dl> <dt>

[**CreateSubtype**](ipstore-createsubtype.md)
</dt> <dt>

[**CreateType**](ipstore-createtype.md)
</dt> <dt>

[**GetSubtypeInfo**](ipstore-getsubtypeinfo.md)
</dt> <dt>

[**GetTypeInfo**](ipstore-gettypeinfo.md)
</dt> </dl>

 

 




