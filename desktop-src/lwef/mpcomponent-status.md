---
title: MPCOMPONENT_STATUS structure (MpClient.h)
description: Component status information.
ms.assetid: 0E589E52-A204-425C-880B-CF13C16893F3
keywords:
- MPCOMPONENT_STATUS structure Legacy Windows Environment Features
- PMPCOMPONENT_STATUS structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPCOMPONENT_STATUS
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPCOMPONENT\_STATUS structure

Component status information.

## Syntax


```C++
typedef struct tagMPCOMPONENT_STATUS {
  BOOL    fEnable;
  HRESULT hResult;
} MPCOMPONENT_STATUS, *PMPCOMPONENT_STATUS;
```



## Members

<dl> <dt>

**fEnable**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Status for the component.

</dd> <dt>

**hResult**
</dt> <dd>

Type: **HRESULT**

</dd> <dd>

Success or failure code associated with the status.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





