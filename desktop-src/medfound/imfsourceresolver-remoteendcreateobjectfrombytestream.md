---
Description: Remotable version of the IMFSourceResolverEndCreateObjectFromByteStream method.
ms.assetid: 6e4e9ace-e18a-45df-b20c-28e352fcdee7
title: RemoteEndCreateObjectFromByteStream
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RemoteEndCreateObjectFromByteStream

Remotable version of the [**IMFSourceResolver::EndCreateObjectFromByteStream**](/windows/win32/mfidl/nf-mfidl-imfsourceresolver-endcreateobjectfrombytestream?branch=master) method.

``` syntax
[call_as(EndCreateObjectFromByteStream)]
HRESULT RemoteEndCreateObjectFromByteStream(
    IUnknown *pResult,
    MF_OBJECT_TYPE *pObjectType,
    IUnknown **ppObject
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**EndCreateObjectFromByteStream**](/windows/win32/mfidl/nf-mfidl-imfsourceresolver-endcreateobjectfrombytestream?branch=master) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                              |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Mfuuid.lib</dt> </dl>                    |



## See also

<dl> <dt>

[**IMFSourceResolver**](/windows/win32/mfidl/nn-mfidl-imfsourceresolver?branch=master)
</dt> </dl>

 

 




