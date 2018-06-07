---
Description: Returns the number of certification authorities (CAs) willing to issue a certificate based on the specified certificate template.
ms.assetid: 377121a8-3895-4308-a803-4a62580c6de0
title: ISCrdEnr::getCACount method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISCrdEnr::getCACount method

The **getCACount** method returns the number of [*certification authorities*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (CAs) willing to issue a certificate based on the specified certificate template.

## Syntax


```C++
HRESULT getCACount(
  [in]  BSTR     bstrCertTemplateName,
  [out] LONG *pdwCACount
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>SCrdEnr.getCACount( _
  ByVal bstrCertTemplateName, _
  ByRef pdwCACount _
)</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*bstrCertTemplateName* \[in\]
</dt> <dd>

A string that represents the name of the certificate template.

</dd> <dt>

*pdwCACount* \[out\]
</dt> <dd>

A pointer to a **LONG** that returns the number of available CAs that will issue a certificate for the certificate template specified in *bstrCertTemplateName*.

</dd> </dl>

## Return value

### C++

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

### VB

A **Long** value that represents the number of available CAs that will issue a certificate for the certificate template specified in *bstrCertTemplateName*.

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

[**ISCrdEnr::enumCAName**](iscrdenr-enumcaname.md)
</dt> <dt>

[**ISCrdEnr::getCAName**](iscrdenr-getcaname.md)
</dt> </dl>

 

 




