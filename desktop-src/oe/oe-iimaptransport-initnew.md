---
title: IIMAPTransport InitNew method
description: Initializes the new IIMAPTransport object.
ms.assetid: 78d1b31f-27b1-455b-9942-f9a1cf0a94f2
keywords:
- InitNew method Windows Mail (formerly Outlook Express)
- InitNew method Windows Mail (formerly Outlook Express) , IIMAPTransport interface
- IIMAPTransport interface Windows Mail (formerly Outlook Express) , InitNew method
topic_type:
- apiref
api_name:
- IIMAPTransport.InitNew
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

# IIMAPTransport::InitNew method

\[**IIMAPTransport::InitNew** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Initializes the new [**IIMAPTransport**](oe-iimaptransport.md) object.

## Syntax


```C++
HRESULT InitNew(
  [in] LPCSTR        pszLogFilePath,
  [in] IIMAPCallback *pCBHandler
);
```



## Parameters

<dl> <dt>

*pszLogFilePath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the path to a log file where all IMAP can be logged.

</dd> <dt>

*pCBHandler* \[in\]
</dt> <dd>

Type: **[**IIMAPCallback**](oe-iimapcallback.md)\***

Specifies a pointer to the [**IIMAPCallback**](oe-iimapcallback.md) object. The callback object allows the [**IIMAPTransport**](oe-iimaptransport.md) object to report all IMAP response results to its user.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                               | Description                                                      |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Indicates success. <br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>              | Indicates that an error occurred. <br/>                    |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>             | Indicates that an attempt to allocate memory failed. <br/> |
| <dl> <dt>**IXP\_E\_ALREADY\_CONNECTED**</dt> </dl> | Indicates that the transport is currently connected. <br/> |



 

## Remarks

This function should be called immediately after instantiating the new [**IIMAPTransport**](oe-iimaptransport.md) object.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





