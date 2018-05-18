---
title: IImnAccount ShowProperties method
description: Displays the property sheet for the account.
ms.assetid: '5d466071-5bd8-4df6-80c4-1450515dc2ec'
keywords: ["ShowProperties method Windows Mail (formerly Outlook Express)", "ShowProperties method Windows Mail (formerly Outlook Express) , IImnAccount interface", "IImnAccount interface Windows Mail (formerly Outlook Express) , ShowProperties method"]
topic_type:
- apiref
api_name:
- IImnAccount.ShowProperties
api_location:
- Msoeacct.dll
api_type:
- COM
---

# IImnAccount::ShowProperties method

\[**IImnAccount::ShowProperties** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Displays the property sheet for the account.

## Syntax


```C++
HRESULT ShowProperties(
  [in] HWND  hwnd,
  [in] DWORD dwFlags
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

Type: **HWND**

Specifies the handle to the parent window.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies flags for displaying the property sheet.



| Value                                                                                                                                                 | Meaning                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <span id="SP_NO_IMAP"></span><span id="sp_no_imap"></span><dl> <dt>**SP\_NO\_IMAP**</dt> </dl> | Disables the ability to create IMAP accounts.<br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                               |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                             |
| <dl> <dt>**S\_FALSE**</dt> </dl>      | Indicates that the account has no properties. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that an unknown error has occurred.<br/>  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *dwFlags* is invalid. <br/>          |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





