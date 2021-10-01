---
description: Gets the remoting version of the engine.
MS-HAID: vspixengine.IPixEngine6\_GetRemotingVersion\_RemotingVersion\_ptr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine6::GetRemotingVersion method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 065FC3A7-ECFB-4551-B4B0-CA0E6B8676F8
api_name: 
 - IPixEngine6.GetRemotingVersion
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipixengine6_getremotingversion_remotingversion_ptr"></span>IPixEngine6::GetRemotingVersion method

Gets the remoting version of the engine.

## Syntax


```C++
HRESULT GetRemotingVersion(
   RemotingVersion * pRemoteVersion
);
```

## Parameters

*pRemoteVersion*   
The remoting version of the engine.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPixEngine6**](/windows/desktop/direct3dtools/ipixengine6)

 

 
