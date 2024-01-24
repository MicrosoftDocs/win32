---
description: Enumerates the name of the available cryptographic service providers (CSPs).
ms.assetid: d0dc8a8a-afff-4ccc-96e0-2c52913c3322
title: ISCrdEnr::enumCSPName method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCrdEnr.enumCSPName
- SCrdEnr.enumCSPName
api_type: 
- COM
api_location: 
- Scrdenrl.dll
---

# ISCrdEnr::enumCSPName method

The **enumCSPName** method enumerates the name of the available [*cryptographic service providers*](../secgloss/c-gly.md) (CSPs).

## Syntax


```C++
HRESULT enumCSPName(
  [in]  DWORD     dwIndex,
  [in]  DWORD     dwFlags,
  [out] BSTR *pbstrCSPName
);
```


```VB

SCrdEnr.enumCSPName( _
  ByVal dwIndex, _
  ByVal dwFlags, _
  ByRef pbstrCSPName _
)
```





## Parameters

<dl> <dt>

*dwIndex* \[in\]
</dt> <dd>

The zero-based index for the enumeration sequence.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved for future use. Set this value to zero.

</dd> <dt>

*pbstrCSPName* \[out\]
</dt> <dd>

A pointer to a string that returns the name of the enumerated CSP.

</dd> </dl>

## Return value

### C++

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

### VB

A string that represents the name of the enumerated CSP.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Scrdenrl.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCrdEnr is defined as 753988a1-1357-436d-9cf5-f089bdd67d64<br/>             |



## See also

<dl> <dt>

[**ISCrdEnr**](iscrdenr.md)
</dt> <dt>

[**ISCrdEnr::CSPCount**](iscrdenr-cspcount.md)
</dt> <dt>

[**ISCrdEnr::CSPName**](iscrdenr-cspname.md)
</dt> </dl>

 

 
