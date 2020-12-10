---
title: IMsRdpClientNonScriptable4 PublisherCertificateChain property
description: Controls the publisher certificate chain. The chain is stored in a variant of type VT\_BYREF that contains a pointer to a CERT\_CHAIN\_CONTEXT structure. For information about VT\_BYREF structures, see VARIANT and VARIANTARG.
ms.assetid: 27ab0aff-1aef-4701-abe0-849bf32c9773
ms.tgt_platform: multiple
keywords:
- PublisherCertificateChain property Remote Desktop Services
- PublisherCertificateChain property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , PublisherCertificateChain property
- PublisherCertificateChain property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , PublisherCertificateChain property
- PublisherCertificateChain property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , PublisherCertificateChain property
- PublisherCertificateChain property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , PublisherCertificateChain property
- PublisherCertificateChain property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , PublisherCertificateChain property
- PublisherCertificateChain property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , PublisherCertificateChain property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable4.PublisherCertificateChain
- IMsRdpClientNonScriptable4.get_PublisherCertificateChain
- IMsRdpClientNonScriptable4.put_PublisherCertificateChain
- IMsRdpClientNonScriptable5.PublisherCertificateChain
- IMsRdpClientNonScriptable5.get_PublisherCertificateChain
- IMsRdpClientNonScriptable5.put_PublisherCertificateChain
- MsRdpClient6.PublisherCertificateChain
- MsRdpClient7.PublisherCertificateChain
- MsRdpClient8.PublisherCertificateChain
- MsRdpClient9.PublisherCertificateChain
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable4::PublisherCertificateChain property

Controls the publisher certificate chain. The chain is stored in a variant of type **VT\_BYREF** that contains a pointer to a [**CERT\_CHAIN\_CONTEXT**](/windows/desktop/api/wincrypt/ns-wincrypt-cert_chain_context) structure. For information about **VT\_BYREF** structures, see [VARIANT and VARIANTARG](/windows/win32/api/oaidl/ns-oaidl-variant).

This property is read/write.

## Syntax


```C++
HRESULT put_PublisherCertificateChain(
  [in]  VARIANT *pVarCert
);

HRESULT get_PublisherCertificateChain(
  [out] VARIANT *pVarCert
);
```



## Property value

Sets the publisher certificate chain. The chain is stored in a variant of type **VT\_BYREF** that contains a pointer to a [**CERT\_CHAIN\_CONTEXT**](/windows/desktop/api/wincrypt/ns-wincrypt-cert_chain_context) structure.

## Error codes

Returns **S\_OK** if successful.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| IID<br/>                      | IMsRdpClientNonScriptable4 is defined as f50fa8aa-1c7d-4f59-b15c-a90cacae1fcb<br/> |



## See also

<dl> <dt>

[**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
</dt> <dt>

[**IMsRdpClientNonScriptable4**](imsrdpclientnonscriptable4.md)
</dt> </dl>

 

