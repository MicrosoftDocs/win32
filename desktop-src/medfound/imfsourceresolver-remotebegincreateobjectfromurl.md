---
Description: 'Remotable version of the IMFSourceResolver::BeginCreateObjectFromURL method.'
ms.assetid: '3c0b0aaf-832b-4708-bed9-6f448770ee77'
title: RemoteBeginCreateObjectFromURL
---

# RemoteBeginCreateObjectFromURL

Remotable version of the [**IMFSourceResolver::BeginCreateObjectFromURL**](imfsourceresolver-begincreateobjectfromurl.md) method.

``` syntax
[call_as(BeginCreateObjectFromURL)]
HRESULT RemoteBeginCreateObjectFromURL(
    LPCWSTR pwszURL,
    DWORD dwFlags,
    IPropertyStore *pProps,
    IMFRemoteAsyncCallback *pCallback
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**BeginCreateObjectFromURL**](imfsourceresolver-begincreateobjectfromurl.md) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

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

 

 




