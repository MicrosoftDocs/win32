---
Description: Remotable version of IMFWorkQueueServicesEXBeginRegisterPlatformWorkQueueWithMMCSSEx.
ms.assetid: 75af7ce6-9b74-4d61-b7f2-5d07538f91cf
title: RemoteBeginRegisterPlatformWorkQueueWithMMCSSEx
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RemoteBeginRegisterPlatformWorkQueueWithMMCSSEx

Remotable version of [**IMFWorkQueueServicesEX::BeginRegisterPlatformWorkQueueWithMMCSSEx**](/windows/win32/mfidl/nf-mfidl-imfworkqueueservicesex-beginregisterplatformworkqueuewithmmcssex?branch=master).

``` syntax
[call_as(BeginRegisterPlatformWorkQueueWithMMCSSEx)]
HRESULT RemoteBeginRegisterPlatformWorkQueueWithMMCSSEx(
    DWORD dwPlatformWorkQueue,
    LPCWSTR wszClass,
    DWORD dwTaskId, 
    LONG lPriority,
    IMFRemoteAsyncCallback *pCallback
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**BeginRegisterPlatformWorkQueueWithMMCSSEx**](/windows/win32/mfidl/nf-mfidl-imfworkqueueservicesex-beginregisterplatformworkqueuewithmmcssex?branch=master) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Mfidl.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMFWorkQueueServicesEx**](/windows/win32/mfidl/nn-mfidl-imfworkqueueservicesex?branch=master)
</dt> </dl>

 

 




