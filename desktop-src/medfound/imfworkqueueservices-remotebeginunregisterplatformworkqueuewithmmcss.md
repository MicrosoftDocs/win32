---
Description: Remotable version of the IMFWorkQueueServicesBeginUnregisterPlatformWorkQueueWithMMCSS method.
ms.assetid: c3117086-268e-4e52-acfb-2c8167adaa07
title: RemoteBeginUnregisterPlatformWorkQueueWithMMCSS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RemoteBeginUnregisterPlatformWorkQueueWithMMCSS

Remotable version of the [**IMFWorkQueueServices::BeginUnregisterPlatformWorkQueueWithMMCSS**](/windows/win32/mfidl/nf-mfidl-imfworkqueueservices-beginunregisterplatformworkqueuewithmmcss?branch=master) method.

``` syntax
[call_as(BeginUnregisterPlatformWorkQueueWithMMCSS)]
HRESULT RemoteBeginUnregisterPlatformWorkQueueWithMMCSS(
    DWORD dwPlatformWorkQueue,
    IMFRemoteAsyncCallback *pCallback
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**BeginUnregisterPlatformWorkQueueWithMMCSS**](/windows/win32/mfidl/nf-mfidl-imfworkqueueservices-beginunregisterplatformworkqueuewithmmcss?branch=master) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Mfuuid.lib</dt> </dl>                    |



## See also

<dl> <dt>

[**IMFWorkQueueServices**](/windows/win32/mfidl/nn-mfidl-imfworkqueueservices?branch=master)
</dt> </dl>

 

 




