---
title: INNTPTransport InitNew method
description: Initializes the Internet transport.
ms.assetid: bfe1f74e-4b35-49f6-88a6-ad7c52d45555
keywords:
- InitNew method Windows Mail (formerly Outlook Express)
- InitNew method Windows Mail (formerly Outlook Express) , INNTPTransport interface
- INNTPTransport interface Windows Mail (formerly Outlook Express) , InitNew method
topic_type:
- apiref
api_name:
- INNTPTransport.InitNew
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

# INNTPTransport::InitNew method

\[**INNTPTransport::InitNew** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Initializes the Internet transport. This method be called before the transport can doing anything.

## Syntax


```C++
HRESULT InitNew(
  [in] LPSTR         pszLogFilePath,
  [in] INNTPCallback *pCallback
);
```



## Parameters

<dl> <dt>

*pszLogFilePath* \[in\]
</dt> <dd>

Type: **LPSTR**

Full file path in which to log the protocol commands. **NULL** is a valid value (no logging)

</dd> <dt>

*pCallback* \[in\]
</dt> <dd>

Type: **[**INNTPCallback**](oe-inntpcallback.md)\***

Specifies the Transport callback interface.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | An invalid parameter was passed in<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | An memory allocation failed<br/>        |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





