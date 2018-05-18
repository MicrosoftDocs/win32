---
Description: 'Remotable version of the IMFWorkQueueServices::BeginRegisterPlatformWorkQueueWithMMCSS method.'
ms.assetid: '158497a9-9d66-4e58-919d-e35765fd29e4'
title: RemoteBeginRegisterPlatformWorkQueueWithMMCSS
---

# RemoteBeginRegisterPlatformWorkQueueWithMMCSS

Remotable version of the [**IMFWorkQueueServices::BeginRegisterPlatformWorkQueueWithMMCSS**](imfworkqueueservices-beginregisterplatformworkqueuewithmmcss.md) method.

``` syntax
[call_as(BeginRegisterPlatformWorkQueueWithMMCSS)]
HRESULT RemoteBeginRegisterPlatformWorkQueueWithMMCSS(
    DWORD dwPlatformWorkQueue,
    LPCWSTR wszClass,
    DWORD dwTaskId,
    IMFRemoteAsyncCallback *pCallback
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**BeginRegisterPlatformWorkQueueWithMMCSS**](imfworkqueueservices-beginregisterplatformworkqueuewithmmcss.md) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Mfuuid.lib</dt> </dl>                    |



## See also

<dl> <dt>

[**IMFWorkQueueServices**](imfworkqueueservices.md)
</dt> </dl>

 

 




