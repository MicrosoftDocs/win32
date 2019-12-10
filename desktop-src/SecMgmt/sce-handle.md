---
Description: The SCE\_HANDLE data type is an opaque handle provided by the Security Configuration tool set. It is used by PFSCE\_QUERY\_INFO and PFSCE\_SET\_INFO support functions to pass information between the attachment and the security database.
ms.assetid: 8db91e6f-b31e-40c6-a158-b4b3b00ba0c0
title: SCE_HANDLE (Scesvc.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SCE\_HANDLE

The **SCE\_HANDLE** data type is an opaque handle provided by the Security Configuration tool set. It is used by [**PFSCE\_QUERY\_INFO**](https://msdn.microsoft.com/library/ms721890(v=VS.85).aspx) and [**PFSCE\_SET\_INFO**](https://msdn.microsoft.com/library/ms721892(v=VS.85).aspx) support functions to pass information between the attachment and the security database.


```C++
typedef PVOID SCE_HANDLE;
```



## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Scesvc.h</dt> </dl> |



## See also

<dl> <dt>

[**PFSCE\_QUERY\_INFO**](https://msdn.microsoft.com/library/ms721890(v=VS.85).aspx)
</dt> <dt>

[**PFSCE\_SET\_INFO**](https://msdn.microsoft.com/library/ms721892(v=VS.85).aspx)
</dt> </dl>

 

 




