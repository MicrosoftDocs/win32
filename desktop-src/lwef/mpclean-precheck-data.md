---
title: MPCLEAN_PRECHECK_DATA structure (MpClient.h)
description: Notification data passed to clean precheck callback function.
ms.assetid: 65B3B116-6E83-46F5-AE2B-92A41AE39480
keywords:
- MPCLEAN_PRECHECK_DATA structure Legacy Windows Environment Features
- PMPCLEAN_PRECHECK_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPCLEAN_PRECHECK_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPCLEAN\_PRECHECK\_DATA structure

Notification data passed to clean precheck callback function.

## Syntax


```C++
typedef struct tagMPCLEAN_PRECHECK_DATA {
  PMPRESOURCE_INFO     BlockedResourceInfo;
  BlockingResourceInfo PMPRESOURCE_INFO;
} MPCLEAN_PRECHECK_DATA, *PMPCLEAN_PRECHECK_DATA;
```



## Members

<dl> <dt>

**BlockedResourceInfo**
</dt> <dd>

Type: **PMPRESOURCE\_INFO**

</dd> <dd>

Resource information about the resource being blocked. For example, when progress is **MPNOTIFY\_PRECHECK\_RESOURCE\_BLOCKED**. See [**MPRESOURCE\_INFO**](mpresource-info.md).

</dd> <dt>

**PMPRESOURCE\_INFO**
</dt> <dd>

Type: **BlockingResourceInfo**

</dd> <dd>

Resource information about the resource that is blocking. For example, when progress is **MPNOTIFY\_PRECHECK\_RESOURCE\_BLOCKED**. See [**MPRESOURCE\_INFO**](mpresource-info.md).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



## See also

<dl> <dt>

[**MPRESOURCE\_INFO**](mpresource-info.md)
</dt> </dl>

 

 





