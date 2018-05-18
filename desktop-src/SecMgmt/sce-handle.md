---
Description: 'The SCE\_HANDLE data type is an opaque handle provided by the Security Configuration tool set. It is used by PFSCE\_QUERY\_INFO and PFSCE\_SET\_INFO support functions to pass information between the attachment and the security database.'
ms.assetid: '8db91e6f-b31e-40c6-a158-b4b3b00ba0c0'
title: 'SCE\_HANDLE'
---

# SCE\_HANDLE

The **SCE\_HANDLE** data type is an opaque handle provided by the Security Configuration tool set. It is used by [**PFSCE\_QUERY\_INFO**](pfsce-query-info.md) and [**PFSCE\_SET\_INFO**](pfsce-set-info.md) support functions to pass information between the attachment and the security database.


```C++
typedef PVOID SCE_HANDLE;
```



## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Scesvc.h</dt> </dl> |



## See also

<dl> <dt>

[**PFSCE\_QUERY\_INFO**](pfsce-query-info.md)
</dt> <dt>

[**PFSCE\_SET\_INFO**](pfsce-set-info.md)
</dt> </dl>

 

 




