---
title: IStoreFolder CreateStream method
description: Creates a data stream that can be used to store a new message.
ms.assetid: dde1b2c2-0008-4dcd-b04a-938fbd75ff4b
keywords:
- CreateStream method Windows Mail (formerly Outlook Express)
- CreateStream method Windows Mail (formerly Outlook Express) , IStoreFolder interface
- IStoreFolder interface Windows Mail (formerly Outlook Express) , CreateStream method
topic_type:
- apiref
api_name:
- IStoreFolder.CreateStream
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IStoreFolder::CreateStream method

Creates a data stream that can be used to store a new message.

## Syntax


```C++
HRESULT CreateStream(
  [in]  HBATCHLOCK  hBatchLock,
  [in]  DWORD       dwReserved,
  [out] IStream     **ppStream,
  [out] LPMESSAGEID pdwMessageId
);
```



## Parameters

<dl> <dt>

*hBatchLock* \[in\]
</dt> <dd>

Type: **HBATCHLOCK**

Not used.

</dd> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be 0.

</dd> <dt>

*ppStream* \[out\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\*\***

Reference to a pointer that receives a stream that can be used to write message data to.

</dd> <dt>

*pdwMessageId* \[out\]
</dt> <dd>

Type: **LPMESSAGEID**

Pointer that receives an ID value associated with the new message.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or the following error code.



| Return code                                                                                  | Description                                                                                                                |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The value of *ppStream* is **NULL**, the value of *pdwMessageId* is **NULL**, or *dwReserved* does not equal 0.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





