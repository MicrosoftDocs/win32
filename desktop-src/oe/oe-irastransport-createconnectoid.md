---
title: IRASTransport CreateConnectoid method
description: Displays a dialog box for making a new remote access phonebook entry.
ms.assetid: 1bf0f6d8-aaa6-4188-a78a-bf91800a3da7
keywords:
- CreateConnectoid method Windows Mail (formerly Outlook Express)
- CreateConnectoid method Windows Mail (formerly Outlook Express) , IRASTransport interface
- IRASTransport interface Windows Mail (formerly Outlook Express) , CreateConnectoid method
topic_type:
- apiref
api_name:
- IRASTransport.CreateConnectoid
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

# IRASTransport::CreateConnectoid method

\[**IRASTransport::CreateConnectoid** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Displays a dialog box for making a new remote access phonebook entry.

## Syntax


```C++
HRESULT CreateConnectoid(
  [in]  HWND  hwndParent,
  [out] DWORD *pdwRASResult
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **HWND**

Specifies an **HWND** that contains the handle to the parent window.

</dd> <dt>

*pdwRASResult* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to a **DWORD** that contains more error information when this method returns IXP\_E\_RAS\_ERROR. Otherwise, it contains NO\_ERROR.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                       | Description                                       |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | Indicates success. <br/>                    |
| <dl> <dt>**IXP\_E\_RAS\_ERROR**</dt> </dl> | Indicates that an error has occurred. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





