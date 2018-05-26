---
title: IMimeAddressTable GetProps method
description: Gets the properties for the specified address.
ms.assetid: b5723f36-5ef0-4e84-952b-692b0c458f03
keywords:
- GetProps method Windows Mail (formerly Outlook Express)
- GetProps method Windows Mail (formerly Outlook Express) , IMimeAddressTable interface
- IMimeAddressTable interface Windows Mail (formerly Outlook Express) , GetProps method
topic_type:
- apiref
api_name:
- IMimeAddressTable.GetProps
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

# IMimeAddressTable::GetProps method

Gets the properties for the specified address.

## Syntax


```C++
HRESULT GetProps(
  [in] HADDRESS       hAddress,
  [in] LPADDRESSPROPS pAddress
);
```



## Parameters

<dl> <dt>

*hAddress* \[in\]
</dt> <dd>

Type: **HADDRESS**

Specifies the handle of the address.

</dd> <dt>

*pAddress* \[in\]
</dt> <dd>

Type: **LPADDRESSPROPS**

Specifies a pointer to the [**ADDRESSPROPS**](oe-addressprops.md) structure that contains the address properties. The client is responsible for freeing this structure by calling [**FreeAddressProps**](oe-imimeallocator-freeaddressprops.md).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                         |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success. <br/>                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Indicates that an unknown error has occurred. <br/>           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *pAddress* is **NULL**. <br/>                  |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hAddress* is an invalid address handle. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>           | Indicates that an attempt to allocate memory failed.<br/>     |



 

## Remarks

The client should initialize *pAddress*-&gt;**dwProps** before calling this method to specify which properties to return.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





