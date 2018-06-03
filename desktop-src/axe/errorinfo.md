---
title: ErrorInfo structure
description: This structure defines an AXE error.
ms.assetid: 52788B75-8638-47D6-A01A-10CD8F25A032
keywords:
- ErrorInfo structure Access Execution Engine
topic_type:
- apiref
api_name:
- ErrorInfo
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ErrorInfo structure

This structure defines an AXE error.

## Syntax


```C++
struct ErrorInfo {
  DWORD     size;
  UINT      index;
  UINT      assessmentIndex;
  ErrorType errorType;
  HRESULT   errorValue;
  WCHAR     file[MAX_PATH];
};
```



## Members

<dl> <dt>

**size**
</dt> <dd>

The number of bytes in the structure. Used to detect different versions of structure.

</dd> <dt>

**index**
</dt> <dd>

The zero-based index of this error in the error list.

</dd> <dt>

**assessmentIndex**
</dt> <dd>

The zero-based index of the assessment in the job manifest. If the *errorType* and *errorValue* parameters indicate this error does not pertain to an assessment, this value will be ((unsigned int)-1) and should be ignored.

</dd> <dt>

**errorType**
</dt> <dd>

The type of error that occurred.

</dd> <dt>

**errorValue**
</dt> <dd>

The **HRESULT** error value that occurred during the operation.

</dd> <dt>

**file**
</dt> <dd>

The absolute path to the file that caused the failure. If there is no file associated with the error then this value will contain the empty string.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





