---
title: MimeOleSMimeCapRelease function
description: Do not use. Clears allocated capabilities memory.
ms.assetid: 9278da72-ed2b-4230-9449-627c74d05c32
keywords:
- MimeOleSMimeCapRelease function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleSMimeCapRelease
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MimeOleSMimeCapRelease function

Do not use. Clears allocated capabilities memory.

## Syntax


```C++
HRESULT MimeOleSMimeCapRelease(
  _In_ LPVOID pv
);
```



## Parameters

<dl> <dt>

*pv* \[in\]
</dt> <dd>

Type: **LPVOID**

Specifies pointer to capabilities memory to clear.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                          | Description                       |
|--------------------------------------------------------------------------------------|-----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Always returns S\_OK. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





