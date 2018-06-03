---
title: IMimeMessageW DeletePropW method
description: Deletes a property from the root header of a message.
ms.assetid: 7067e781-267f-433c-9ad6-d0b65b5e69bd
keywords:
- DeletePropW method Windows Mail (formerly Outlook Express)
- DeletePropW method Windows Mail (formerly Outlook Express) , IMimeMessageW interface
- IMimeMessageW interface Windows Mail (formerly Outlook Express) , DeletePropW method
topic_type:
- apiref
api_name:
- IMimeMessageW.DeletePropW
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

# IMimeMessageW::DeletePropW method

\[**DeletePropW** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Deletes a property from the root header of a message.

## Syntax


```C++
HRESULT DeletePropW(
  [in] LPCWSTR pwszName
);
```



## Parameters

<dl> <dt>

*pwszName* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies the property name or ID.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                                     |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success.<br/>                                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Indicates that an unknown error has occurred. <br/>                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pwszName* is **NULL**.<br/>                               |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that the property specified by *pwszName* cannot be found.<br/> |



 

## Remarks

A property ID can also be passed into this method through the *pwszName* parameter using the PIDTOSTR macro.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





