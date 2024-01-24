---
description: Sets or retrieves the name of the cryptographic service provider (CSP).
ms.assetid: 34fde7b0-747d-4592-a89a-207f82369f52
title: ISCrdEnr::CSPName property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCrdEnr.CSPName
- ISCrdEnr.get_CSPName
- ISCrdEnr.put_CSPName
- SCrdEnr.CSPName
api_type: 
- COM
api_location: 
- Scrdenrl.dll
---

# ISCrdEnr::CSPName property

The **CSPName** property sets or retrieves the name of the [*cryptographic service provider*](../secgloss/c-gly.md) (CSP).

This property is read/write.

## Syntax


```C++
HRESULT put_CSPName(
   BSTR newVal
);

HRESULT get_CSPName(
   BSTR *pVal
);
```



## Property value

The name of the CSP.

## Error codes

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

## Remarks

Set this property to specify the name of the CSP to use with the Smart Card Enrollment Control. Get this property to retrieve the name of the specified CSP. If you do not specify a value for this property, the **CSPName** property defaults to the first name in the available list of CSPs.

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

[**ISCrdEnr::enumCSPName**](iscrdenr-enumcspname.md)
</dt> </dl>

 

 
