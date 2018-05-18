---
title: IIMAPTransport2 EnableFetchEx method
description: Enables extended support for the FETCH command responses.
ms.assetid: 'ccc5ec41-a52e-4de0-a0e1-03e4161b9a85'
keywords: ["EnableFetchEx method Windows Mail (formerly Outlook Express)", "EnableFetchEx method Windows Mail (formerly Outlook Express) , IIMAPTransport2 interface", "IIMAPTransport2 interface Windows Mail (formerly Outlook Express) , EnableFetchEx method"]
topic_type:
- apiref
api_name:
- IIMAPTransport2.EnableFetchEx
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IIMAPTransport2::EnableFetchEx method

\[**IIMAPTransport2::EnableFetchEx** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Enables extended support for the FETCH command responses.

## Syntax


```C++
HRESULT EnableFetchEx(
  [in] DWORD dwFetchExFlags
);
```



## Parameters

<dl> <dt>

*dwFetchExFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that indicates whether to enable the FETCH command extensions. Sets a persisted IMAPTransport flag.



| Value                                                                                                                                                                                                                                               | Meaning                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <span id="IMAP_FETCHEX_DISABLE"></span><span id="imap_fetchex_disable"></span><dl> <dt>**IMAP\_FETCHEX\_DISABLE**</dt> <dt>0x00000000</dt> </dl> | Disable the FETCH command extensions. <br/> |
| <span id="IMAP_FETCHEX_ENABLE"></span><span id="imap_fetchex_enable"></span><dl> <dt>**IMAP\_FETCHEX\_ENABLE**</dt> <dt>0x00000001</dt> </dl>    | Enable the FETCH command extensions. <br/>  |



 

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

IMAPTransport initializes the persisted flag as **IMAP\_FETCHEX\_DISABLE**.

This method enables a larger set of FETCH command responses to be read. Server responses populate into the [**FETCH\_CMD\_RESULTS\_EX**](oe-fetch-cmd-results-ex.md) structure when *dwFetchExFlags* is equal to **IMAP\_FETCHEX\_ENABLE** and into the [**FETCH\_CMD\_RESULTS**](oe-fetch-cmd-results.md) structure when *dwFetchExFlags* is equal to **IMAP\_FETCHEX\_DISABLE**. The **FETCH\_CMD\_RESULTS\_EX** structure can accomodate ENVELOPE response data that the **FETCH\_CMD\_RESULTS** structure does not.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





