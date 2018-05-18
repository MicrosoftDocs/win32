---
title: INNTPTransport CommandGROUP method
description: Issues an GROUP command to the server.
ms.assetid: '2f290580-c72d-4773-8c5c-6e19b7e0bffe'
keywords: ["CommandGROUP method Windows Mail (formerly Outlook Express)", "CommandGROUP method Windows Mail (formerly Outlook Express) , INNTPTransport interface", "INNTPTransport interface Windows Mail (formerly Outlook Express) , CommandGROUP method"]
topic_type:
- apiref
api_name:
- INNTPTransport.CommandGROUP
api_location:
- Inetcomm.dll
api_type:
- COM
---

# INNTPTransport::CommandGROUP method

\[**INNTPTransport::CommandGROUP** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Issues an GROUP command to the server. The server's response string will be returned to the [**OnResponse**](oe-inntpcallback-onresponse.md).

## Syntax


```C++
HRESULT CommandGROUP(
  [in] LPSTR pszGroup
);
```



## Parameters

<dl> <dt>

*pszGroup* \[in\]
</dt> <dd>

Type: **LPSTR**

Name of the newsgroup to enter.

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



 

 





