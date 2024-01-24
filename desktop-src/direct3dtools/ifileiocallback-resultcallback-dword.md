---
description: A callback function used to notify the host of errors while during capture or playback.
MS-HAID: vspixengine.IFileIOCallback\_ResultCallback\_DWORD
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IFileIOCallback::ResultCallback method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: E4418A63-47C6-4F12-94FA-0F1B5465FE84
api_name: 
 - IFileIOCallback.ResultCallback
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ifileiocallback_resultcallback_dword"></span>IFileIOCallback::ResultCallback method

A callback function used to notify the host of errors while during capture or playback.

## Syntax


```C++
HRESULT ResultCallback(
   DWORD resultState
);
```

## Parameters

*resultState*   
Indicates the kind of error encountered.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IFileIOCallback**](/windows/desktop/direct3dtools/ifileiocallback)

 

 
