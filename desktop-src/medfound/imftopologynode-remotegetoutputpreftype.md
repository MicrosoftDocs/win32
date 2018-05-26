---
Description: Remotable version of the IMFTopologyNodeGetOutputPrefType method.
ms.assetid: 56fbbf14-0c55-4f98-bcda-7f434cff803c
title: RemoteGetOutputPrefType
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RemoteGetOutputPrefType

Remotable version of the [**IMFTopologyNode::GetOutputPrefType**](/windows/win32/mfidl/nf-mfidl-imftopologynode-getoutputpreftype?branch=master) method.

``` syntax
[call_as(GetOutputPrefType)] 
HRESULT RemoteGetOutputPrefType(
    DWORD dwOutputIndex,
    DWORD *pcbData,
    BYTE **ppbData
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If **GetOutputPrefType** is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Mfuuid.lib</dt> </dl>                    |



## See also

<dl> <dt>

[**IMFTopologyNode**](/windows/win32/mfidl/nn-mfidl-imftopologynode?branch=master)
</dt> </dl>

 

 




