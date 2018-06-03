---
title: IDatabase HeapFree method
description: Free the memory allocated using HeapAllocated.
ms.assetid: 77ea422a-df9d-4d6c-896a-30f20715b6e4
keywords:
- HeapFree method Windows Mail (formerly Outlook Express)
- HeapFree method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , HeapFree method
topic_type:
- apiref
api_name:
- IDatabase.HeapFree
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

# IDatabase::HeapFree method

\[**HeapFree** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Free the memory allocated using HeapAllocated.

## Syntax


```C++
HRESULT HeapFree(
  [out] LPVOID pBuffer
);
```



## Parameters

<dl> <dt>

*pBuffer* \[out\]
</dt> <dd>

Type: **LPVOID**

The buffer to be freed.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns the following value.



| Return code                                                                          | Description                        |
|--------------------------------------------------------------------------------------|------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The function succeeded.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Heapapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





