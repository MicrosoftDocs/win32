---
title: IStoreFolder CommitStream method
description: Commits or reverts changes to a stream associated with a message object.
ms.assetid: 834a142d-2127-4a02-83db-58b1edc82312
keywords:
- CommitStream method Windows Mail (formerly Outlook Express)
- CommitStream method Windows Mail (formerly Outlook Express) , IStoreFolder interface
- IStoreFolder interface Windows Mail (formerly Outlook Express) , CommitStream method
topic_type:
- apiref
api_name:
- IStoreFolder.CommitStream
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IStoreFolder::CommitStream method

Commits or reverts changes to a stream associated with a message object.

## Syntax


```C++
HRESULT CommitStream(
  [in] HBATCHLOCK   hBatchLock,
  [in] DWORD        dwFlags,
  [in] DWORD        dwMsgFlags,
  [in] IStream      *pStream,
  [in] MESSAGEID    dwMessageId,
  [in] IMimeMessage *pMessage
);
```



## Parameters

<dl> <dt>

*hBatchLock* \[in\]
</dt> <dd>

Type: **HBATCHLOCK**

Handle to the folder interface. Set to (HBATCHLOCK)this.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies whether to commit or revert the stream. Set to 0 to commit and save the stream, or COMMITSTREAM\_REVERT to revert and discard changes to the stream.

</dd> <dt>

*dwMsgFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a combination of state flags to apply to the message associated with the stream. For a list of flags, see [**Message State Flags**](oe-message-state-flags.md).

</dd> <dt>

*pStream* \[in\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

Pointer to an open data stream received from [**IStoreFolder::CreateStream**](oe-istorefolder-createstream.md).

</dd> <dt>

*dwMessageId* \[in\]
</dt> <dd>

Type: **MESSAGEID**

Specifies the message that the stream is associated with; received from [**IStoreFolder::CreateStream**](oe-istorefolder-createstream.md).

</dd> <dt>

*pMessage* \[in\]
</dt> <dd>

Type: **[**IMimeMessage**](oe-imimemessage.md)\***

Pointer to a MIME message object that will be stored. If **NULL**, message data will be read from the stream specified by *pStream*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or the following error value.



| Return code                                                                                  | Description                                                                              |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The value of *pStream* is **NULL**, or the value of *dwMessageId* is invalid.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





