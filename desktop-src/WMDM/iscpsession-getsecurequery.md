---
title: ISCPSession GetSecureQuery method
description: The GetSecureQuery method is used to obtain a secure query object for the session.
ms.assetid: 'c725f0ae-1f37-412d-ac2b-0833989d1bd6'
keywords: ["GetSecureQuery method windows Media Device Manager", "GetSecureQuery method windows Media Device Manager , ISCPSession interface", "ISCPSession interface windows Media Device Manager , GetSecureQuery method"]
topic_type:
- apiref
api_name:
- ISCPSession.GetSecureQuery
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSession::GetSecureQuery method

The **GetSecureQuery** method is used to obtain a secure query object for the session.

## Syntax


```C++
HRESULT GetSecureQuery(
  [out] ISCPSecureQuery **ppSecureQuery
);
```



## Parameters

<dl> <dt>

*ppSecureQuery* \[out\]
</dt> <dd>

Pointer to a secure query object.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If the method fails, it returns an **HRESULT** error code.

## Remarks

This method should be used to obtain a secure query object when using secure content provider sessions for efficient transfer of multiple files.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSession Interface**](iscpsession.md)
</dt> </dl>

 

 





