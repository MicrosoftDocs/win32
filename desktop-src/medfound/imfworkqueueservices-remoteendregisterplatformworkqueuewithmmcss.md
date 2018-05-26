---
Description: Remotable version of the IMFWorkQueueServicesEndRegisterPlatformWorkQueueWithMMCSS method.
ms.assetid: cb15129e-a3ad-4351-a7d6-dd4b883437bd
title: RemoteEndRegisterPlatformWorkQueueWithMMCSS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RemoteEndRegisterPlatformWorkQueueWithMMCSS

Remotable version of the [**IMFWorkQueueServices::EndRegisterPlatformWorkQueueWithMMCSS**](/windows/win32/mfidl/nf-mfidl-imfworkqueueservices-endregisterplatformworkqueuewithmmcss?branch=master) method.

``` syntax
[call_as(EndRegisterPlatformWorkQueueWithMMCSS)]
HRESULT RemoteEndRegisterPlatformWorkQueueWithMMCSS(
    IUnknown *pResult,
    DWORD *pdwTaskId
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**EndRegisterPlatformWorkQueueWithMMCSS**](/windows/win32/mfidl/nf-mfidl-imfworkqueueservices-endregisterplatformworkqueuewithmmcss?branch=master) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

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

 

 




