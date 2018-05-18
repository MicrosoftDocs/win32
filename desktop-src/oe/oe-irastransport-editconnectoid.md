---
title: IRASTransport EditConnectoid method
description: Displays a dialog box for editing the specified remote access phonebook entry.
ms.assetid: '32d99bcb-d36a-4da2-addb-baffe9a382f7'
keywords: ["EditConnectoid method Windows Mail (formerly Outlook Express)", "EditConnectoid method Windows Mail (formerly Outlook Express) , IRASTransport interface", "IRASTransport interface Windows Mail (formerly Outlook Express) , EditConnectoid method"]
topic_type:
- apiref
api_name:
- IRASTransport.EditConnectoid
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IRASTransport::EditConnectoid method

\[**IRASTransport::EditConnectoid** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Displays a dialog box for editing the specified remote access phonebook entry.

## Syntax


```C++
HRESULT EditConnectoid(
  [in]  HWND  hwndParent,
  [in]  LPSTR pszConnectoid,
  [out] DWORD *pdwRASResult
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **HWND**

Specifies an **HWND** that contains the handle to the parent window.

</dd> <dt>

*pszConnectoid* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies an **LPSTR** that contains the phone book entry used to establish the remote access connection.

</dd> <dt>

*pdwRASResult* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to a **DWORD** that contains more error information when this method returns IXP\_E\_RAS\_ERROR. Otherwise, it contains NO\_ERROR.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                       | Description                                             |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | Indicates success. <br/>                          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>      | Indicates that *pszConnectoid* is **NULL**. <br/> |
| <dl> <dt>**IXP\_E\_RAS\_ERROR**</dt> </dl> | Indicates that an error has occurred. <br/>       |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





