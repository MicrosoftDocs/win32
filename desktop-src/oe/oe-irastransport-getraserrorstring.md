---
title: IRASTransport GetRasErrorString method
description: Returns error messages while establishing a Remote Access Service (RAS) connection.
ms.assetid: 'fbd7532d-543f-40ec-bbd6-7dfa6708dfda'
keywords: ["GetRasErrorString method Windows Mail (formerly Outlook Express)", "GetRasErrorString method Windows Mail (formerly Outlook Express) , IRASTransport interface", "IRASTransport interface Windows Mail (formerly Outlook Express) , GetRasErrorString method"]
topic_type:
- apiref
api_name:
- IRASTransport.GetRasErrorString
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IRASTransport::GetRasErrorString method

\[**IRASTransport::GetRasErrorString** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns error messages while establishing a Remote Access Service (RAS) connection.

## Syntax


```C++
HRESULT GetRasErrorString(
  [in]  UINT  uRasErrorValue,
  [out] LPSTR pszErrorString,
  [in]  ULONG cchMax,
  [out] DWORD *pdwRASResult
);
```



## Parameters

<dl> <dt>

*uRasErrorValue* \[in\]
</dt> <dd>

Type: **UINT**

Specifies a **UINT** that contains the numeric value of the error.

</dd> <dt>

*pszErrorString* \[out\]
</dt> <dd>

Type: **LPSTR**

Specifies an **LPSTR** that contains the error message.

</dd> <dt>

*cchMax* \[in\]
</dt> <dd>

Type: **ULONG**

Contains a **ULONG** that contains the size in bytes of *pszErrorString*.

</dd> <dt>

*pdwRASResult* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to a **DWORD** that contains the **HRESULT** of this method.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                   | Description                                                                                                             |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                          | Indicates success. <br/>                                                                                          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                  | Indicates that *pszErrorString* or *pdwRASResult* is **NULL** or that *uRasErrorValue* or *cchMax* is zero. <br/> |
| <dl> <dt>**IXP\_E\_RAS\_ERROR**</dt> </dl>             | Indicates that an error has occurred. <br/>                                                                       |
| <dl> <dt>**IXP\_E\_RAS\_NOT\_INSTALLED**</dt> </dl>    | Indicates that RASAPI32.DLL is not installed on the client machine. <br/>                                         |
| <dl> <dt>**IXP\_E\_RAS\_PROCS\_NOT\_FOUND**</dt> </dl> | Indicates that the RAS connection did not start up properly. <br/>                                                |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





