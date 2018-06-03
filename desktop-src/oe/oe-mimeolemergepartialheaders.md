---
title: MimeOleMergePartialHeaders function
description: Do not use. Merges partial headers. The resulting stream should contain the headers for the first message (using normal RFC822 rules), then a blank line, and then the headers for the second message (again following RFC822 rules).
ms.assetid: 488fa372-45e3-49cd-8cca-fe7bae93733c
keywords:
- MimeOleMergePartialHeaders function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleMergePartialHeaders
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MimeOleMergePartialHeaders function

Do not use. Merges partial headers. The resulting stream should contain the headers for the first message (using normal RFC822 rules), then a blank line, and then the headers for the second message (again following RFC822 rules).

## Syntax


```C++
HRESULT MimeOleMergePartialHeaders(
  _In_ IStream *pstmIn,
  _In_ IStream *pstmOut
);
```



## Parameters

<dl> <dt>

*pstmIn* \[in\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

Specifies a pointer to the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object for message source.

</dd> <dt>

*pstmOut* \[in\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

Specifies a pointer to the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object for message destination.

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

All of the header fields from the initial enclosing entity (part one), except those that start with "Content-" and the specific header fields "Message-ID", "Encrypted", and "MIME-Version", must be copied, in order, to the new message.

Only those header fields in the enclosed message which start with "Content-" and "Message-ID", "Encrypted", and "MIME-Version" must be appended, in order, to the header fields of the new message. Any header fields in the enclosed message which do not start with "Content-" (except for "Message-ID", "Encrypted", and "MIME-Version") will be ignored.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





