---
title: IMimeMessageTree SaveOffsetTable method
description: Saves the offset table of a message for quicker loading.
ms.assetid: 87f54c6a-d352-4a80-ad95-f6dcfb3d9fa5
keywords:
- SaveOffsetTable method Windows Mail (formerly Outlook Express)
- SaveOffsetTable method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , SaveOffsetTable method
topic_type:
- apiref
api_name:
- IMimeMessageTree.SaveOffsetTable
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

# IMimeMessageTree::SaveOffsetTable method

Saves the offset table of a message for quicker loading.

## Syntax


```C++
HRESULT SaveOffsetTable(
  [in] IStream *pStream,
  [in] DWORD   dwFlags
);
```



## Parameters

<dl> <dt>

*pStream* \[in\]
</dt> <dd>

Type: **[**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034)\***

Specifies a pointer to an [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034) to save the offset table to.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies how an [**IMimeMessageTree**](oe-imimemessagetree.md) object should be committed.



| Value                                                                                                                                                                                                                                                                | Meaning                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="COMMIT_ONLYIFDIRTY"></span><span id="commit_onlyifdirty"></span><dl> <dt>**COMMIT\_ONLYIFDIRTY**</dt> <dt>0x00000001</dt> </dl>                         | Indicates that if the message object is dirty, the message should internally commit all changes so that the method being called reflects the committed state of the message. <br/>                                                                                                |
| <span id="COMMIT_REUSESTORAGE"></span><span id="commit_reusestorage"></span><dl> <dt>**COMMIT\_REUSESTORAGE**</dt> <dt>0x00000002</dt> </dl>                      | Indicates that if the message object needs to commit itself, it should reuse its current storage object. For example, if a message object is loaded from a client provided [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034), the message object saves itself back into that original **IStream**. <br/> |
| <span id="COMMIT_SMIMETRANSFERENCODE"></span><span id="commit_smimetransferencode"></span><dl> <dt>**COMMIT\_SMIMETRANSFERENCODE**</dt> <dt>0x00000004</dt> </dl> | Indicates secure messaging.<br/>                                                                                                                                                                                                                                                  |



 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                        | Description                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                               | Indicates success.<br/>                                                                                                                                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>                             | Indicates that an unknown error has occurred.<br/>                                                                                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                       | Indicates that *pStream* is **NULL**. <br/>                                                                                                                            |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                      | Indicates that an attempt to allocate memory failed.<br/>                                                                                                              |
| <dl> <dt>**IStream::Write**</dt> </dl>                      | This method may return a failure result from the [ISequentialStream::Write](http://msdn.microsoft.com/library/stg/stg/isequentialstream_write.asp) method. <br/> |
| <dl> <dt>**MIME\_E\_UNKNOWN\_BODYTREE\_VERSION**</dt> </dl> | Indicates that the version of the offset table is invalid or not supported. <br/>                                                                                      |



 

## Remarks

Offset tables are used to improve performance when loading a message. The offset table contains information about the message, which enables MimeOLE to quickly load the message. Typically, the first time a client loads a message, they should call **IMimeMessageTree::SaveOffsetTable**. Then, the next time the client loads the message, they should first call [**IMimeMessageTree::LoadOffsetTable**](oe-imimemessagetree-loadoffsettable.md) before loading the actual message into the message object.

Using offset tables is optional.

## Examples

The following code demonstrates how to save the offset table.


```C++
IMimeMessageTree::Load(*pMessageSource);
IMimeMessageTree::SaveOffsetTable(*pOffsetTable);
```



The following code demonstrates how to load a message with an offset table.


```C++
IMimeMessageTree::LoadOffsetTable(*pOffsetTable);
IMimeMessageTree::Load(*pMessageSource);
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**IMimeMessageTree**](oe-imimemessagetree.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**LoadOffsetTable**](oe-imimemessagetree-loadoffsettable.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**IPersistStreamInit::Load**](https://msdn.microsoft.com/library/windows/desktop/ms680730)
</dt> </dl>

 

 





