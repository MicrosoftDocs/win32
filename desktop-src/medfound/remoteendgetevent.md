---
Description: 'Remotable version of the IMFMediaEventGenerator::EndGetEvent method.'
ms.assetid: '5b793760-546c-43d4-8251-d89d8d7152ad'
title: RemoteEndGetEvent
---

# RemoteEndGetEvent

Remotable version of the [**IMFMediaEventGenerator::EndGetEvent**](imfmediaeventgenerator-endgetevent.md) method.

``` syntax
[call_as(EndGetEvent)]
HRESULT RemoteEndGetEvent(
    IUnknown *pResult,
    DWORD *pcbEvent,
    BYTE **ppbEvent
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**EndGetEvent**](imfmediaeventgenerator-endgetevent.md) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

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

 

 




