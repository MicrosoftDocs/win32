---
title: IMimePropertySchema RegisterAddressType method
description: Registers a new address type in the MimeOLE global property schema.
ms.assetid: 975c54df-0d60-4d93-b29f-d8d41f4a2361
keywords:
- RegisterAddressType method Windows Mail (formerly Outlook Express)
- RegisterAddressType method Windows Mail (formerly Outlook Express) , IMimePropertySchema interface
- IMimePropertySchema interface Windows Mail (formerly Outlook Express) , RegisterAddressType method
topic_type:
- apiref
api_name:
- IMimePropertySchema.RegisterAddressType
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

# IMimePropertySchema::RegisterAddressType method

Registers a new address type in the MimeOLE global property schema.

## Syntax


```C++
HRESULT RegisterAddressType(
  [in]  LPCSTR  pszName,
  [out] LPDWORD pdwAdrType
);
```



## Parameters

<dl> <dt>

*pszName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the name of the header for the new address type.

</dd> <dt>

*pdwAdrType* \[out\]
</dt> <dd>

Type: **LPDWORD**

Receives the value of the new address type.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                      | Description                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                             | Indicates success. <br/>                                                                                                                               |
| <dl> <dt>**E\_FAIL**</dt> </dl>                           | Indicates that an unknown error has occurred. <br/>                                                                                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                     | Indicates that *pszName* or *pdwAdrType* is **NULL**. <br/>                                                                                            |
| <dl> <dt>**MIME\_E\_NO\_MORE\_ADDRESS\_TYPES**</dt> </dl> | Indicates that the maximum number of address types has been reached and no more new address types can be added. The maximum is 32 address types. <br/> |



 

## Remarks

MimeOLE defines a set of default address types in the IAT\_*xxx* bitmask (see [**ADDRESSPROPS**](oe-addressprops.md) for the list of bitmask values). However, a client may need to register a new type of address. Address types are used with the [**IMimeAddressTable**](oe-imimeaddresstable.md) interface. If this function tries to register a name that is already registered as an address type, this function succeeds and returns the value for the existing address type in *pdwAdrType*.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





