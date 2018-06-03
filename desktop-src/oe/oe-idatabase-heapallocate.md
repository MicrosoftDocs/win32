---
title: IDatabase HeapAllocate method
description: Allocates memory.
ms.assetid: e2885f74-1fd0-4a3d-ba80-09ae1e299eb7
keywords:
- HeapAllocate method Windows Mail (formerly Outlook Express)
- HeapAllocate method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , HeapAllocate method
topic_type:
- apiref
api_name:
- IDatabase.HeapAllocate
api_location:
- Directdb.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IDatabase::HeapAllocate method

\[**HeapAllocate** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Allocates memory.

## Syntax


```C++
HRESULT HeapAllocate(
  [in]  DWORD  dwFlags,
  [in]  DWORD  cbSize,
  [out] LPVOID *ppBuffer
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies options for the way the memory is allocated. Should be the same as the values passed to HeapAlloc's dwFlags.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the size of the buffer to allocate.

</dd> <dt>

*ppBuffer* \[out\]
</dt> <dd>

Type: **LPVOID\***

Specifies the pointer that will receive the location of the new buffer.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                         |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The function succeeded.<br/>                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates memory could not be allocated.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





