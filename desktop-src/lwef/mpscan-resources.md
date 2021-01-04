---
title: MPSCAN_RESOURCES structure (MpClient.h)
description: Resource information passed during a scan operation.
ms.assetid: D97712A6-547D-44CC-B55D-039A5CCE20BF
keywords:
- MPSCAN_RESOURCES structure Legacy Windows Environment Features
- PMPSCAN_RESOURCES structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPSCAN_RESOURCES
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPSCAN\_RESOURCES structure

Resource information passed during a scan operation.

## Syntax


```C++
typedef struct tagMPSCAN_RESOURCES {
  DWORD            dwResourceCount;
  PMPRESOURCE_INFO pResourceList;
} MPSCAN_RESOURCES, *PMPSCAN_RESOURCES;
```



## Members

<dl> <dt>

**dwResourceCount**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Count of resources.

</dd> <dt>

**pResourceList**
</dt> <dd>

Type: **PMPRESOURCE\_INFO**

</dd> <dd>

Array of resources. See [**MPRESOURCE\_INFO**](mpresource-info.md).

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

 

 





