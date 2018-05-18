---
Description: 'Remotable version of the IMFMediaSource::CreatePresentationDescriptor method.'
ms.assetid: '9ad6793e-32ca-471b-8639-41098b3e8216'
title: RemoteCreatePresentationDescriptor
---

# RemoteCreatePresentationDescriptor

Remotable version of the [**IMFMediaSource::CreatePresentationDescriptor**](imfmediasource-createpresentationdescriptor.md) method.

``` syntax
[call_as(CreatePresentationDescriptor)]
HRESULT RemoteCreatePresentationDescriptor(
    DWORD *pcbPD,
    BYTE **pbPD,
    IMFPresentationDescriptor **ppRemotePD
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**CreatePresentationDescriptor**](imfmediasource-createpresentationdescriptor.md) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                              |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Mfuuid.lib</dt> </dl>                    |



## See also

<dl> <dt>

[**IMFMediaSource**](imfmediasource.md)
</dt> </dl>

 

 




