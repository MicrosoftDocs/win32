---
Description: 'Sets or retrieves the PCCERT\_CHAIN\_CONTEXT of a certificate.'
ms.assetid: '1b33ecd5-88c9-4654-9d2d-95a0be4283c6'
title: 'IChainContext::ChainContext property'
---

# IChainContext::ChainContext property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP.\]

The **ChainContext** property sets or retrieves the PCCERT\_CHAIN\_CONTEXT of a certificate.

This property is read/write.

## Syntax


```VB
' Data type: Long

ChainContext.ChainContext As Long
```



## Property value

The PCCERT\_CHAIN\_CONTEXT of the certificate.

## Error codes

If the property access methods **put\_ChainContext** and **get\_ChainContext** succeed, they return S\_OK.

Any other **HRESULT** value indicates that the call failed.

## Remarks

You must call either the [**FreeContext**](ichaincontext-freecontext.md) method or the [**CertFreeCertificateChain**](certfreecertificatechain.md) function to free the context.

If you set the **ChainContext** property, the state of the entire [**Chain**](chain.md) object is reset.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**IChainContext**](ichaincontext.md)
</dt> </dl>

 

 




