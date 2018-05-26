---
title: IMimeBody SetCurrentEncoding method
description: Sets the current encoding type for the data that is stored in the body.
ms.assetid: 2a06871f-5fcf-4194-bae1-70356e2510ce
keywords:
- SetCurrentEncoding method Windows Mail (formerly Outlook Express)
- SetCurrentEncoding method Windows Mail (formerly Outlook Express) , IMimeBody interface
- IMimeBody interface Windows Mail (formerly Outlook Express) , SetCurrentEncoding method
topic_type:
- apiref
api_name:
- IMimeBody.SetCurrentEncoding
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

# IMimeBody::SetCurrentEncoding method

Sets the current encoding type for the data that is stored in the body.

## Syntax


```C++
HRESULT SetCurrentEncoding(
  [in] ENCODINGTYPE ietEncoding
);
```



## Parameters

<dl> <dt>

*ietEncoding* \[in\]
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

Specifies the new [**ENCODINGTYPE**](oe-encodingtype.md) value for data stored in the body.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                                                   |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                                                                                 |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *ietEncoding* is greater than or equal to [**IET\_UNKNOWN**](oe-encodingtype.md). <br/> |



 

## Remarks

Usually, a client does not need to set the encoding type. The actual data stored in the body is not affected when this method is called. This encoding type represents how the data stored in the body is currently encoded so a client must be careful that the current encoding type describes how the data is actually encoded.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





