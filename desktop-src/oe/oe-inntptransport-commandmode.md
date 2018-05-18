---
title: INNTPTransport CommandMODE method
description: Issues a MODE command to the server.
ms.assetid: '59560881-367d-4677-9427-92c2bb9ada95'
keywords: ["CommandMODE method Windows Mail (formerly Outlook Express)", "CommandMODE method Windows Mail (formerly Outlook Express) , INNTPTransport interface", "INNTPTransport interface Windows Mail (formerly Outlook Express) , CommandMODE method"]
topic_type:
- apiref
api_name:
- INNTPTransport.CommandMODE
api_location:
- Inetcomm.dll
api_type:
- COM
---

# INNTPTransport::CommandMODE method

\[**INNTPTransport::CommandMODE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Issues a `MODE` command to the server.*pszMode* is a required argument, an example of which are "MODE READER" to tell the server that the connection is for a user instead of another server. Refer to RFC977 for more details.

## Syntax


```C++
HRESULT CommandMODE(
  [in] LPSTR pszMode
);
```



## Parameters

<dl> <dt>

*pszMode* \[in\]
</dt> <dd>

Type: **LPSTR**

Required argument to the MODE command.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | An invalid parameter was passed in<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | A memory allocation failed<br/>         |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





