---
Description: 'Remotable version of the IMFTopologyNode::GetInputPrefType method.'
ms.assetid: 'b02cf739-97a9-4bb0-abb1-0da491857c50'
title: RemoteGetInputPrefType
---

# RemoteGetInputPrefType

Remotable version of the [**IMFTopologyNode::GetInputPrefType**](imftopologynode-getinputpreftype.md) method.

``` syntax
[call_as(GetInputPrefType)] 
HRESULT RemoteGetInputPrefType(
    DWORD dwInputIndex,
    DWORD *pcbData,
    BYTE **ppbData
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**GetInputPrefType**](imftopologynode-getinputpreftype.md) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Mfuuid.lib</dt> </dl>                    |



## See also

<dl> <dt>

[**IMFTopologyNode**](imftopologynode.md)
</dt> </dl>

 

 




