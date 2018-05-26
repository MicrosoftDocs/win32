---
Description: Remotable version of the IMFWorkQueueServicesBeginUnregisterTopologyWorkQueuesWithMMCSS method.
ms.assetid: 1a168462-400d-46c9-a489-7b861770469f
title: RemoteBeginUnregisterTopologyWorkQueuesWithMMCSS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RemoteBeginUnregisterTopologyWorkQueuesWithMMCSS

Remotable version of the [**IMFWorkQueueServices::BeginUnregisterTopologyWorkQueuesWithMMCSS**](/windows/win32/mfidl/nf-mfidl-imfworkqueueservices-beginunregistertopologyworkqueueswithmmcss?branch=master) method.

``` syntax
[call_as(BeginUnregisterTopologyWorkQueuesWithMMCSS)]
HRESULT RemoteBeginUnregisterTopologyWorkQueuesWithMMCSS(
    IMFRemoteAsyncCallback *pCallback
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**BeginUnregisterTopologyWorkQueuesWithMMCSS**](/windows/win32/mfidl/nf-mfidl-imfworkqueueservices-beginunregistertopologyworkqueueswithmmcss?branch=master) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

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

 

 




