---
title: IDatabaseStream GetFileAddress method
description: Retrieves a locally-unique identifier for this stream.
ms.assetid: 3cc13767-6fb2-43d3-9ee4-17591d355cba
keywords:
- GetFileAddress method Windows Mail (formerly Outlook Express)
- GetFileAddress method Windows Mail (formerly Outlook Express) , IDatabaseStream interface
- IDatabaseStream interface Windows Mail (formerly Outlook Express) , GetFileAddress method
topic_type:
- apiref
api_name:
- IDatabaseStream.GetFileAddress
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

# IDatabaseStream::GetFileAddress method

Retrieves a locally-unique identifier for this stream.

## Syntax


```C++
HRESULT GetFileAddress(
  [out] LPFILEADDRESS pfaStream
);
```



## Parameters

<dl> <dt>

*pfaStream* \[out\]
</dt> <dd>

Type: **LPFILEADDRESS**

On success, will contain an identifier that can used with Stream functions on an IDatabase. This identifier is not portable across databases and should not be treated as a pointer. (It is a 32-bit value even on 64-bit systems.)

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                          | Description                                                          |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The locally-unique identifier was successfully retrieved.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





