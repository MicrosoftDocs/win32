---
title: IMimePropertySet BindToObject method
description: Obtains an IMimeAddressTable or IMimeHeaderTable interface from the current object.
ms.assetid: 'f20e46d8-9e34-4a3e-9791-b470bf85dcc5'
keywords: ["BindToObject method Windows Mail (formerly Outlook Express)", "BindToObject method Windows Mail (formerly Outlook Express) , IMimePropertySet interface", "IMimePropertySet interface Windows Mail (formerly Outlook Express) , BindToObject method"]
topic_type:
- apiref
api_name:
- IMimePropertySet.BindToObject
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimePropertySet::BindToObject method

Obtains an [**IMimeAddressTable**](oe-imimeaddresstable.md) or [**IMimeHeaderTable**](oe-imimeheadertable.md) interface from the current object.

## Syntax


```C++
HRESULT BindToObject(
  [in]  REFIID riid,
  [out] void   **ppvObject
);
```



## Parameters

<dl> <dt>

*riid* \[in\]
</dt> <dd>

Type: **REFIID**

Specifies the interface ID to return.



| Value                                                                                                                                                   | Meaning                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <dl> <dt></dt> <dt>IID\_IMimeAddressTable</dt> </dl> | Indicates the [**IMimeAddressTable**](oe-imimeaddresstable.md) interface for a body. <br/> |
| <dl> <dt></dt> <dt>IID\_IMimeHeaderTable</dt> </dl>  | Indicates the [**IMimeHeaderTable**](oe-imimeheadertable.md) interface for a body. <br/>   |



 

</dd> <dt>

*ppvObject* \[out\]
</dt> <dd>

Type: **void\*\***

Receives the address of a pointer to the requested object. The client is responsible for releasing the object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                  |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that the *ppvObject* is **NULL**.<br/>                       |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | Indicates that the interface ID specified by *riid* is not valid.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





