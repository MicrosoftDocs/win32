---
title: Windows Event Log Data Types (WinEvt.h)
description: Windows Event Log defines the following data types
ms.assetid: 1aad25fe-7503-4ef8-a40a-63457bd9a007
keywords:
- EVT_HANDLE
- PEVT_HANDLE
- EVT_OBJECT_ARRAY_PROPERTY_HANDLE
ms.topic: reference
ms.date: 05/31/2018
---

# Windows Event Log Data Types

Windows Event Log defines the following data types:


```C++
typedef HANDLE EVT_HANDLE;
typedef HANDLE* PEVT_HANDLE;
typedef HANDLE EVT_OBJECT_ARRAY_PROPERTY_HANDLE;
```



<dl> <dt>

**EVT\_HANDLE**
</dt> <dd>

A handle to a Windows Event Log object.

</dd> <dt>

**PEVT\_HANDLE**
</dt> <dd>

A pointer to the handle of a Windows Event Log object.

</dd> <dt>

**EVT\_OBJECT\_ARRAY\_PROPERTY\_HANDLE**
</dt> <dd>

A handle to an array of Windows Event Log objects.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>WinEvt.h</dt> </dl> |



 

 





