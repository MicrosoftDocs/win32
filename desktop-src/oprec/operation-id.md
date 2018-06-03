---
title: OPERATION\_ID
description: A identifier that corresponds to the operation having file access patterns recorded. The value should be unique for each operation that the developer intends to record.
ms.assetid: D5446D23-DBB5-4EB8-97E4-590537A33193
keywords:
- OPERATION_ID
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OPERATION\_ID

A identifier that corresponds to the operation having file access patterns recorded. The value should be unique for each operation that the developer intends to record.


```C++
typedef ULONG OPERATION_ID;
```



## Remarks

Each application has a dedicated **OPERATION\_ID** namespace. If two applications both use **OPERATION\_ID** value of 1 to identify an operation, the system will maintain separate context for each one.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>WinBase.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>


</dt> <dt>

[Operation Recorder](-operation-portal.md)
</dt> <dt>

[**OperationStart**](/windows/desktop/api/WinBase/nf-winbase-operationstart)
</dt> <dt>

[**OperationEnd**](/windows/desktop/api/WinBase/nf-winbase-operationend)
</dt> <dt>

[**\_OPERATION\_START\_PARAMETERS**](/windows/desktop/api/WinBase/ns-winbase-_operation_start_parameters)
</dt> <dt>

[**\_OPERATION\_END\_PARAMETERS**](/windows/desktop/api/WinBase/ns-winbase-_operation_end_parameters)
</dt> </dl>

 

 





