---
title: AxeErrorInfo structure
description: This structure defines an AXE error.
ms.assetid: 52788B75-8638-47D6-A01A-10CD8F25A032
keywords:
- AxeErrorInfo structure Access Execution Engine
topic_type:
- apiref
api_name:
- AxeErrorInfo
api_location:
- AxeCore.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AxeErrorInfo structure

This structure defines an AXE error.

## Syntax


```C++
struct AxeErrorInfo {
  DWORD       size;
  IssueType   Kind;
  HRESULT     ErrorValue;
  const WCHAR *Message;
};
```



## Members

<dl> <dt>

**size**
</dt> <dd>

The number of bytes in the structure. Used to detect different versions of structure.

</dd> <dt>

**Kind**
</dt> <dd>

The type of issue, an [**IssueType**](issuetype-enum.md).

</dd> <dt>

**ErrorValue**
</dt> <dd>

The **HRESULT** error value that occurred during the operation.

</dd> <dt>

**Message**
</dt> <dd>

Describes the error.

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl> |



 

 





