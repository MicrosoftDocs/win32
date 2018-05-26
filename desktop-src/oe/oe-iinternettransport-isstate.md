---
title: IInternetTransport IsState method
description: Queries the transport for validity of the specified state.
ms.assetid: eaf9cecd-33fa-49d0-8cdf-2843ad091e28
keywords:
- IsState method Windows Mail (formerly Outlook Express)
- IsState method Windows Mail (formerly Outlook Express) , IInternetTransport interface
- IInternetTransport interface Windows Mail (formerly Outlook Express) , IsState method
topic_type:
- apiref
api_name:
- IInternetTransport.IsState
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

# IInternetTransport::IsState method

\[**IInternetTransport::IsState** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Queries the transport for validity of the specified state.

## Syntax


```C++
HRESULT IsState(
  [in] IXPISSTATE isstate
);
```



## Parameters

<dl> <dt>

*isstate* \[in\]
</dt> <dd>

Type: **[**IXPISSTATE**](oe-ixpisstate.md)**

Specifies the [**IXPISSTATE**](oe-ixpisstate.md) value to query.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                                           |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates that the state specified by *isstate* is true. <br/>  |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates that the state specified by *isstate* is false. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





