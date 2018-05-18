---
Description: 'Remotable version of the IMFSourceResolver::EndCreateObjectFromURL method.'
ms.assetid: '42764869-9cbc-4f41-a3af-f2d869db9f99'
title: RemoteEndCreateObjectFromURL
---

# RemoteEndCreateObjectFromURL

Remotable version of the [**IMFSourceResolver::EndCreateObjectFromURL**](imfsourceresolver-endcreateobjectfromurl.md) method.

``` syntax
[call_as(EndCreateObjectFromURL)]
HRESULT RemoteEndCreateObjectFromURL(
    IUnknown *pResult,
    MF_OBJECT_TYPE *pObjectType,
    IUnknown **ppObject
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**EndCreateObjectFromURL**](imfsourceresolver-endcreateobjectfromurl.md) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                              |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Mfuuid.lib</dt> </dl>                    |



## See also

<dl> <dt>

[**IMFSourceResolver**](imfsourceresolver.md)
</dt> </dl>

 

 




