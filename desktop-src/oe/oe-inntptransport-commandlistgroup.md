---
title: INNTPTransport CommandLISTGROUP method
description: Retrieves a list of all the article numbers in a particular news group.
ms.assetid: 'e653bd8e-2998-4122-9055-1d6ac94ff345'
keywords: ["CommandLISTGROUP method Windows Mail (formerly Outlook Express)", "CommandLISTGROUP method Windows Mail (formerly Outlook Express) , INNTPTransport interface", "INNTPTransport interface Windows Mail (formerly Outlook Express) , CommandLISTGROUP method"]
topic_type:
- apiref
api_name:
- INNTPTransport.CommandLISTGROUP
api_location:
- Inetcomm.dll
api_type:
- COM
---

# INNTPTransport::CommandLISTGROUP method

\[**INNTPTransport::CommandLISTGROUP** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves a list of all the article numbers in a particular news group. If the caller specifies a newsgroup name, then the articles are listed for the specified newsgroup. Otherwise, the currently-selected newsgroup is listed.

## Syntax


```C++
HRESULT CommandLISTGROUP(
  [in] LPSTR pszGroup
);
```



## Parameters

<dl> <dt>

*pszGroup* \[in\]
</dt> <dd>

Type: **LPSTR**

Optional newsgroup name to list articles for.

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



 

 





