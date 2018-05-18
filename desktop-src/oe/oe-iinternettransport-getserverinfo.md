---
title: IInternetTransport GetServerInfo method
description: Gets the server information for the transport.
ms.assetid: 'aa6dd4f7-09ae-4201-9518-277e582932a8'
keywords: ["GetServerInfo method Windows Mail (formerly Outlook Express)", "GetServerInfo method Windows Mail (formerly Outlook Express) , IInternetTransport interface", "IInternetTransport interface Windows Mail (formerly Outlook Express) , GetServerInfo method"]
topic_type:
- apiref
api_name:
- IInternetTransport.GetServerInfo
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IInternetTransport::GetServerInfo method

\[**IInternetTransport::GetServerInfo** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Gets the server information for the transport.

## Syntax


```C++
HRESULT GetServerInfo(
  [in, out] LPINETSERVER pInetServer
);
```



## Parameters

<dl> <dt>

*pInetServer* \[in, out\]
</dt> <dd>

Type: **LPINETSERVER**

Receives a pointer to the [**INETSERVER**](oe-inetserver.md) structure that contains the current server information for the transport.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                           |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pInetServer* is **NULL**. <br/> |



 

## Remarks

The data in the [**INETSERVER**](oe-inetserver.md) structure is valid only after [**IInternetTransport::Connect**](oe-iinternettransport-connect.md) is called.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





