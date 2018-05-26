---
Description: The SCESVC\_HANDLE data type is an opaque handle provided by the Security Configuration tool set.
ms.assetid: 478d7d4b-7983-4247-b8be-2e2cd3327533
title: SCESVC\_HANDLE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SCESVC\_HANDLE

The **SCESVC\_HANDLE** data type is an opaque handle provided by the Security Configuration tool set. It is used by methods of the [**ISceSvcAttachmentData**](/windows/win32/Scesvc/nn-scesvc-iscesvcattachmentdata?branch=master) and [**ISceSvcAttachmentPersistInfo**](/windows/win32/Scesvc/nn-scesvc-iscesvcattachmentpersistinfo?branch=master) interfaces to pass information between the Security Configuration snap-in and the snap-in extension.


```C++
typedef PVOID SCESVC_HANDLE;
```



## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Scesvc.h</dt> </dl> |



## See also

<dl> <dt>

[**ISceSvcAttachmentData**](/windows/win32/Scesvc/nn-scesvc-iscesvcattachmentdata?branch=master)
</dt> <dt>

[**ISceSvcAttachmentPersistInfo**](/windows/win32/Scesvc/nn-scesvc-iscesvcattachmentpersistinfo?branch=master)
</dt> </dl>

 

 




