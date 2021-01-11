---
description: Remotable version of the IMFPMPHost::CreateObjectByCLSID method.
ms.assetid: be96be6d-47de-4d2b-81fc-13079de33888
title: RemoteCreateObjectByCLSID (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# RemoteCreateObjectByCLSID

Remotable version of the [**IMFPMPHost::CreateObjectByCLSID**](/windows/desktop/api/mfidl/nf-mfidl-imfpmphost-createobjectbyclsid) method.

``` syntax
[call_as(CreateObjectByCLSID)]
HRESULT RemoteCreateObjectByCLSID( 
    REFCLSID clsid,
    BYTE *pbData, 
    DWORD cbData, 
    REFIID riid,
    void **ppv
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**CreateObjectByCLSID**](/windows/desktop/api/mfidl/nf-mfidl-imfpmphost-createobjectbyclsid) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Mfuuid.lib</dt> </dl>                    |



## See also

<dl> <dt>

[**IMFPMPHost**](/windows/desktop/api/mfidl/nn-mfidl-imfpmphost)
</dt> <dt>

[PMP Media Session](pmp-media-session.md)
</dt> <dt>

[Protected Media Path](protected-media-path.md)
</dt> </dl>

 

 




