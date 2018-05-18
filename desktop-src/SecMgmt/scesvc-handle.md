---
Description: 'The SCESVC\_HANDLE data type is an opaque handle provided by the Security Configuration tool set.'
ms.assetid: '478d7d4b-7983-4247-b8be-2e2cd3327533'
title: 'SCESVC\_HANDLE'
---

# SCESVC\_HANDLE

The **SCESVC\_HANDLE** data type is an opaque handle provided by the Security Configuration tool set. It is used by methods of the [**ISceSvcAttachmentData**](iscesvcattachmentdata.md) and [**ISceSvcAttachmentPersistInfo**](iscesvcattachmentpersistinfo.md) interfaces to pass information between the Security Configuration snap-in and the snap-in extension.


```C++
typedef PVOID SCESVC_HANDLE;
```



## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Scesvc.h</dt> </dl> |



## See also

<dl> <dt>

[**ISceSvcAttachmentData**](iscesvcattachmentdata.md)
</dt> <dt>

[**ISceSvcAttachmentPersistInfo**](iscesvcattachmentpersistinfo.md)
</dt> </dl>

 

 




