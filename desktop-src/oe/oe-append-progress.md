---
title: APPEND\_PROGRESS structure
description: Returns the progress of the current APPEND command.
ms.assetid: f810c774-4d52-4bf6-a1d7-ff535d15b2a8
keywords:
- APPEND_PROGRESS structure Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- APPEND_PROGRESS
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# APPEND\_PROGRESS structure

\[**APPEND\_PROGRESS** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the progress of the current APPEND command.

## Syntax


```C++
typedef struct tagAPPEND_PROGRESS {
  DWORD dwUploaded;
  DWORD dwTotal;
} APPEND_PROGRESS;
```



## Members

<dl> <dt>

**dwUploaded**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the number of bytes that have been uploaded.

</dd> <dt>

**dwTotal**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the total number of bytes to be uploaded.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





