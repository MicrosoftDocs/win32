---
title: IMimeEnumAddressTypes Count method
description: Gets the total number of elements in the enumerator object.
ms.assetid: 457efa3f-66fd-42bf-9282-2db3eadc1995
keywords:
- Count method Windows Mail (formerly Outlook Express)
- Count method Windows Mail (formerly Outlook Express) , IMimeEnumAddressTypes interface
- IMimeEnumAddressTypes interface Windows Mail (formerly Outlook Express) , Count method
topic_type:
- apiref
api_name:
- IMimeEnumAddressTypes.Count
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

# IMimeEnumAddressTypes::Count method

Gets the total number of elements in the enumerator object.

## Syntax


```C++
HRESULT Count(
  [out] ULONG *pcItems
);
```



## Parameters

<dl> <dt>

*pcItems* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the total number of elements in the enumerator.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                       |
|----------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pcItems* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





