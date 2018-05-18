---
Description: 'Remotable version of the IMFWorkQueueServices::EndRegisterTopologyWorkQueuesWithMMCSS method.'
ms.assetid: '94dce412-6a72-4ddf-86a3-5176ee1eb6d2'
title: RemoteEndRegisterTopologyWorkQueuesWithMMCSS
---

# RemoteEndRegisterTopologyWorkQueuesWithMMCSS

Remotable version of the [**IMFWorkQueueServices::EndRegisterTopologyWorkQueuesWithMMCSS**](imfworkqueueservices-endregistertopologyworkqueueswithmmcss.md) method.

``` syntax
[call_as(EndRegisterTopologyWorkQueuesWithMMCSS)]
HRESULT RemoteEndRegisterTopologyWorkQueuesWithMMCSS(
    IUnknown *pResult
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**EndRegisterTopologyWorkQueuesWithMMCSS**](imfworkqueueservices-endregistertopologyworkqueueswithmmcss.md) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

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

 

 




