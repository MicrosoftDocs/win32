---
Description: Retrieves the number of cryptographic service providers (CSPs).
ms.assetid: 7e0c1613-85ad-4f25-837e-d7b0f11e654a
title: ISCrdEnr::CSPCount property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISCrdEnr::CSPCount property

The **CSPCount** property retrieves the number of [*cryptographic service providers*](security.c_gly#-security-cryptographic-service-provider-gly) (CSPs).

This property is read-only.

## Syntax


```C++
HRESULT get_CSPCount(
   LONG *pVal
);
```



## Property value

The number of CSPs.

## Error codes

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Scrdenrl.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCrdEnr is defined as 753988a1-1357-436d-9cf5-f089bdd67d64<br/>             |



## See also

<dl> <dt>

[**ISCrdEnr**](iscrdenr.md)
</dt> <dt>

[**ISCrdEnr::CSPName**](iscrdenr-cspname.md)
</dt> <dt>

[**ISCrdEnr::enumCSPName**](iscrdenr-enumcspname.md)
</dt> </dl>

 

 




