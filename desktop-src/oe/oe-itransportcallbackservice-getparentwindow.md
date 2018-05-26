---
title: ITransportCallbackService GetParentWindow method
description: Gets the handle of the parent applications window.
ms.assetid: f1667c10-3991-4e44-81dd-39cccf3483f6
keywords:
- GetParentWindow method Windows Mail (formerly Outlook Express)
- GetParentWindow method Windows Mail (formerly Outlook Express) , ITransportCallbackService interface
- ITransportCallbackService interface Windows Mail (formerly Outlook Express) , GetParentWindow method
topic_type:
- apiref
api_name:
- ITransportCallbackService.GetParentWindow
api_location:
- Msoe.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ITransportCallbackService::GetParentWindow method

\[**ITransportCallbackService::GetParentWindow** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Gets the handle of the parent application's window.

## Syntax


```C++
HRESULT GetParentWindow(
  [in]  DWORD dwReserved,
  [out] HWND  *phwndParent
);
```



## Parameters

<dl> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> <dt>

*phwndParent* \[out\]
</dt> <dd>

Type: **HWND\***

Receives a pointer to the handle of the parent window.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                            | Description                                               |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Indicates success. <br/>                            |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Indicates that an unknown error has occurred. <br/> |



 

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                      |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                    |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





