---
title: IMimeMessageTree LoadOffsetTable method
description: Loads an offset table into the message object for quicker loading.
ms.assetid: 1dba8269-a5d1-4585-8f50-5dc3f35dd93e
keywords:
- LoadOffsetTable method Windows Mail (formerly Outlook Express)
- LoadOffsetTable method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , LoadOffsetTable method
topic_type:
- apiref
api_name:
- IMimeMessageTree.LoadOffsetTable
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

# IMimeMessageTree::LoadOffsetTable method

Loads an offset table into the message object for quicker loading.

## Syntax


```C++
HRESULT LoadOffsetTable(
  [in] IStream *pStream
);
```



## Parameters

<dl> <dt>

*pStream* \[in\]
</dt> <dd>

Type: **[**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034)\***

Specifies a pointer to an [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034) that contains the offset table. This stream, which MimeOLE reads from, needs to be positioned at the beginning of the offset table data. When the method returns, the position of the stream is at the end of the offset table. If this method fails, the position of this stream is undefined.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                        | Description                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                               | Indicates success.<br/>                                                                                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>                             | Indicates that an unknown error has occurred.<br/>                                                                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                       | Indicates that *pStream* is **NULL**. <br/>                                                                              |
| <dl> <dt>**MIME\_E\_CORRUPT\_CACHE\_TREE**</dt> </dl>       | Indicates that the offset table is invalid or corrupt. <br/>                                                             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                      | Indicates that an attempt to allocate memory failed.<br/>                                                                |
| <dl> <dt>**IStream::Read**</dt> </dl>                       | This method may return a failure result from the [**ISequentialStream::Read**](https://msdn.microsoft.com/library/windows/desktop/aa380011) method. <br/> |
| <dl> <dt>**MIME\_E\_UNKNOWN\_BODYTREE\_VERSION**</dt> </dl> | Indicates that the version of the offset table is invalid or not supported. <br/>                                        |



 

## Remarks

Offset tables are used to improve performance when loading a message. The offset table contains information about the message that enables MimeOLE to quickly load the message. Typically, the first time a client loads a message, they should call [**IMimeMessageTree::SaveOffsetTable**](oe-imimemessagetree-saveoffsettable.md). Then, the next time the client loads the message, they should first call **IMimeMessageTree::LoadOffsetTable** before loading the actual message into the message object.

For robustness, if a call to **IMimeMessageTree::LoadOffsetTable** fails, the client should ignore the failure and continue to load the message. If calls to LoadOffsetTable are consistently failing, there is most likely a problem that needs further investigation.

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

[**SaveOffsetTable**](oe-imimemessagetree-saveoffsettable.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**IPersistStreamInit::Load**](https://msdn.microsoft.com/library/windows/desktop/ms680730)
</dt> </dl>

 

 





