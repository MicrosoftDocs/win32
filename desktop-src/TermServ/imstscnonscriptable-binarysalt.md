---
title: IMsTscNonScriptable BinarySalt property
description: This property is no longer available for use. | IMsTscNonScriptable BinarySalt property
ms.assetid: 7af2e5be-9ddb-46ab-947c-f79ab890d7bc
ms.tgt_platform: multiple
keywords:
- BinarySalt property Remote Desktop Services
- BinarySalt property Remote Desktop Services , IMsTscNonScriptable interface
- IMsTscNonScriptable interface Remote Desktop Services , BinarySalt property
- BinarySalt property Remote Desktop Services , MsTscAx object
- MsTscAx object Remote Desktop Services , BinarySalt property
- BinarySalt property Remote Desktop Services , IMsRdpClientNonScriptable interface
- IMsRdpClientNonScriptable interface Remote Desktop Services , BinarySalt property
- BinarySalt property Remote Desktop Services , IMsRdpClientNonScriptable2 interface
- IMsRdpClientNonScriptable2 interface Remote Desktop Services , BinarySalt property
- BinarySalt property Remote Desktop Services , IMsRdpClientNonScriptable3 interface
- IMsRdpClientNonScriptable3 interface Remote Desktop Services , BinarySalt property
- BinarySalt property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , BinarySalt property
- BinarySalt property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , BinarySalt property
topic_type:
- apiref
api_name:
- IMsTscNonScriptable.BinarySalt
- IMsTscNonScriptable.get_BinarySalt
- IMsTscNonScriptable.put_BinarySalt
- MsTscAx.BinarySalt
- IMsRdpClientNonScriptable.BinarySalt
- IMsRdpClientNonScriptable.get_BinarySalt
- IMsRdpClientNonScriptable.put_BinarySalt
- IMsRdpClientNonScriptable2.BinarySalt
- IMsRdpClientNonScriptable2.get_BinarySalt
- IMsRdpClientNonScriptable2.put_BinarySalt
- IMsRdpClientNonScriptable3.BinarySalt
- IMsRdpClientNonScriptable3.get_BinarySalt
- IMsRdpClientNonScriptable3.put_BinarySalt
- IMsRdpClientNonScriptable4.BinarySalt
- IMsRdpClientNonScriptable4.get_BinarySalt
- IMsRdpClientNonScriptable4.put_BinarySalt
- IMsRdpClientNonScriptable5.BinarySalt
- IMsRdpClientNonScriptable5.get_BinarySalt
- IMsRdpClientNonScriptable5.put_BinarySalt
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscNonScriptable::BinarySalt property

This property is no longer available for use.

This property is read/write.

## Syntax


```C++
HRESULT put_BinarySalt(
  [in]  BSTR newSalt
);

HRESULT get_BinarySalt(
  [out] BSTR *pSalt
);
```



## Property value

The new binary salt part for a binary encoded password.

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

 

 





