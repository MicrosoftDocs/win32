---
Description: 'Remotable version of the IMFMediaEventGenerator::BeginGetEvent method.'
ms.assetid: '96a16fd3-10bc-4cd9-967a-ceb92e26ccc8'
title: RemoteBeginGetEvent
---

# RemoteBeginGetEvent

Remotable version of the [**IMFMediaEventGenerator::BeginGetEvent**](imfmediaeventgenerator-begingetevent.md) method.

``` syntax
[call_as(BeginGetEvent)]
HRESULT RemoteBeginGetEvent(
    IMFRemoteAsyncCallback* pCallback
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**BeginGetEvent**](imfmediaeventgenerator-begingetevent.md) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                              |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Mfuuid.lib</dt> </dl>                    |



## See also

<dl> <dt>

[**IMFMediaEventGenerator**](imfmediaeventgenerator.md)
</dt> </dl>

 

 




