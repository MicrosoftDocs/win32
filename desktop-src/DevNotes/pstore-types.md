---
Description: The data types for Protected Storage methods.
ms.assetid: 4d494326-6d0f-4a12-83a2-3c3dd3ca9c1b
title: PStore Types
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PStore Types

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](https://msdn.microsoft.com/windows/desktop/765a68fd-f105-49fc-a738-4a8129eb0770) and [**CryptUnprotectData**](https://msdn.microsoft.com/windows/desktop/54eab3b0-d341-47c6-9c32-79328d7a7155) functions.\]

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



 

 




