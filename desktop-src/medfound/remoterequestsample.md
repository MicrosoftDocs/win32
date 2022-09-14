---
description: Remotable version of the IMFMediaStream::RequestSample method.
ms.assetid: 05ed4de0-fe5c-4183-8f1d-55d5a27e436a
title: RemoteRequestSample (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# RemoteRequestSample

Remotable version of the [**IMFMediaStream::RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample) method.

``` syntax
[call_as(RequestSample)]
HRESULT RemoteRequestSample();
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                              |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Mfuuid.lib</dt> </dl>                    |



## See also

<dl> <dt>

[**IMFMediaStream**](/windows/desktop/api/mfidl/nn-mfidl-imfmediastream)
</dt> </dl>

 

 




