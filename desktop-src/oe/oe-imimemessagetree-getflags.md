---
title: IMimeMessageTree GetFlags method
description: Gets a bitmask of flags that describe the contents of the message.
ms.assetid: 0ca55a89-1f90-48e8-b8ea-0dde22277485
keywords:
- GetFlags method Windows Mail (formerly Outlook Express)
- GetFlags method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , GetFlags method
topic_type:
- apiref
api_name:
- IMimeMessageTree.GetFlags
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

# IMimeMessageTree::GetFlags method

Gets a bitmask of flags that describe the contents of the message.

## Syntax


```C++
HRESULT GetFlags(
  [out] DWORD *pdwFlags
);
```



## Parameters

<dl> <dt>

*pdwFlags* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to the bitmask of [**IMSGFLAGS**](oe-imsgflags.md) flags.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                              |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                            |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that an unknown error has occurred.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pdwFlags* is **NULL**. <br/>       |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





