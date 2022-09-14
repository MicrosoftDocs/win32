---
title: IMsTscNonScriptable PortablePassword property
description: This property is no longer available for use. | IMsTscNonScriptable PortablePassword property
ms.assetid: 8d831ed3-1f4a-41a9-b283-507c5d9eea22
ms.tgt_platform: multiple
keywords:
- PortablePassword property Remote Desktop Services
- PortablePassword property Remote Desktop Services , IMsTscNonScriptable interface
- IMsTscNonScriptable interface Remote Desktop Services , PortablePassword property
- PortablePassword property Remote Desktop Services , MsTscAx object
- MsTscAx object Remote Desktop Services , PortablePassword property
- PortablePassword property Remote Desktop Services , IMsRdpClientNonScriptable interface
- IMsRdpClientNonScriptable interface Remote Desktop Services , PortablePassword property
- PortablePassword property Remote Desktop Services , IMsRdpClientNonScriptable2 interface
- IMsRdpClientNonScriptable2 interface Remote Desktop Services , PortablePassword property
- PortablePassword property Remote Desktop Services , IMsRdpClientNonScriptable3 interface
- IMsRdpClientNonScriptable3 interface Remote Desktop Services , PortablePassword property
- PortablePassword property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , PortablePassword property
- PortablePassword property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , PortablePassword property
topic_type:
- apiref
api_name:
- IMsTscNonScriptable.PortablePassword
- IMsTscNonScriptable.get_PortablePassword
- IMsTscNonScriptable.put_PortablePassword
- MsTscAx.PortablePassword
- IMsRdpClientNonScriptable.PortablePassword
- IMsRdpClientNonScriptable.get_PortablePassword
- IMsRdpClientNonScriptable.put_PortablePassword
- IMsRdpClientNonScriptable2.PortablePassword
- IMsRdpClientNonScriptable2.get_PortablePassword
- IMsRdpClientNonScriptable2.put_PortablePassword
- IMsRdpClientNonScriptable3.PortablePassword
- IMsRdpClientNonScriptable3.get_PortablePassword
- IMsRdpClientNonScriptable3.put_PortablePassword
- IMsRdpClientNonScriptable4.PortablePassword
- IMsRdpClientNonScriptable4.get_PortablePassword
- IMsRdpClientNonScriptable4.put_PortablePassword
- IMsRdpClientNonScriptable5.PortablePassword
- IMsRdpClientNonScriptable5.get_PortablePassword
- IMsRdpClientNonScriptable5.put_PortablePassword
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscNonScriptable::PortablePassword property

This property is no longer available for use.

This property is read/write.

## Syntax


```C++
HRESULT put_PortablePassword(
  [in]  BSTR newPortablePassVal
);

HRESULT get_PortablePassword(
  [out] BSTR *pPortablePass
);
```



## Property value

The new password part, in portable encoded format.

## Error codes

Returns **E\_NOTIMPL**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | None supported<br/>                                                              |
| End of client support<br/>    | None supported<br/>                                                              |
| End of server support<br/>    | None supported<br/>                                                              |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsTscNonScriptable is defined as c1e6743a-41c1-4a74-832a-0dd06c1c7a0e<br/> |



## See also

<dl> <dt>

[**IMsRdpClientNonScriptable**](imsrdpclientnonscriptable-interface.md)
</dt> <dt>

[**IMsRdpClientNonScriptable2**](imsrdpclientnonscriptable2.md)
</dt> <dt>

[**IMsRdpClientNonScriptable3**](imsrdpclientnonscriptable3.md)
</dt> <dt>

[**IMsRdpClientNonScriptable4**](imsrdpclientnonscriptable4.md)
</dt> <dt>

[**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
</dt> <dt>

[**IMsTscNonScriptable**](imstscnonscriptable-interface.md)
</dt> </dl>

 

 





