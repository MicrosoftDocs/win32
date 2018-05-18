---
title: INNTPTransport ReleaseResponse method
description: Used to free data returned to the client's OnResponse callback.
ms.assetid: '896d3431-ffb3-45d8-89bf-ab099e699ceb'
keywords: ["ReleaseResponse method Windows Mail (formerly Outlook Express)", "ReleaseResponse method Windows Mail (formerly Outlook Express) , INNTPTransport interface", "INNTPTransport interface Windows Mail (formerly Outlook Express) , ReleaseResponse method"]
topic_type:
- apiref
api_name:
- INNTPTransport.ReleaseResponse
api_location:
- Inetcomm.dll
api_type:
- COM
---

# INNTPTransport::ReleaseResponse method

\[**INNTPTransport::ReleaseResponse** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Used to free data returned to the client's [**OnResponse**](oe-inntpcallback-onresponse.md) callback.

## Syntax


```C++
HRESULT ReleaseResponse(
  [in] LPNNTPRESPONSE pResponse
);
```



## Parameters

<dl> <dt>

*pResponse* \[in\]
</dt> <dd>

Type: **LPNNTPRESPONSE**

A pointer to the [**NNTPRESPONSE**](oe-nntpresponse.md) structure passed to the [**OnResponse**](oe-inntpcallback-onresponse.md) callback.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns the following value.



| Return code                                                                                  | Description                                   |
|----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | An invalid parameter was passed in<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





