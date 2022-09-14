---
description: Gets information about the current playback machine.
MS-HAID: vspixengine.IPixEngine2\_GetPlaybackMachine\_BSTR\_BOOL\_ptr\_BSTR\_ptr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine2::GetPlaybackMachine method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: D6C3C391-F039-4A5A-AA88-87A3624ECAD2
api_name: 
 - IPixEngine2.GetPlaybackMachine
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipixengine2_getplaybackmachine_bstr_bool_ptr_bstr_ptr"></span>IPixEngine2::GetPlaybackMachine method

Gets information about the current playback machine.

## Syntax


```C++
HRESULT GetPlaybackMachine(
   BSTR   logFile,
   BOOL * pUseAuthentication,
   BSTR * pMachine
);
```

## Parameters

*logFile*   
A COM string containing the name of the associated graphics log.

*pUseAuthentication*   
On return, true if the connection uses authentication; otherwise, false.

*pMachine*   
On return, a COM string containing the name of the playback machine.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPixEngine2**](/windows/desktop/direct3dtools/ipixengine2)

 

 
