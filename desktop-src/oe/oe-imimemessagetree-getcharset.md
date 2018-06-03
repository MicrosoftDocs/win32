---
title: IMimeMessageTree GetCharset method
description: Gets the character set for the message.
ms.assetid: 51075fc7-bb30-4c86-9061-3646140e4274
keywords:
- GetCharset method Windows Mail (formerly Outlook Express)
- GetCharset method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , GetCharset method
topic_type:
- apiref
api_name:
- IMimeMessageTree.GetCharset
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

# IMimeMessageTree::GetCharset method

Gets the character set for the message.

## Syntax


```C++
HRESULT GetCharset(
  [out] LPHCHARSET phCharset
);
```



## Parameters

<dl> <dt>

*phCharset* \[out\]
</dt> <dd>

Type: **LPHCHARSET**

Receives the handle of the character set.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                              |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                            |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that an unknown error has occurred.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *phCharset* is **NULL**. <br/>      |



 

## Remarks

This method returns the character set value from the first body in the message that is marked with a charset parameter. If no body has a charset parameter, the method returns the default character set for the message.

This method does not support mixed character sets within a message.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





