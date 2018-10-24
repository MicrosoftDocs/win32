---
Description: Sets the current playback machine for the specified graphics log.
MS-HAID: vspixengine.IPixEngine2\_SetPlaybackMachine\_BSTR\_BOOL\_BSTR
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine2::SetPlaybackMachine method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.ipixengine2_setplaybackmachine_bstr_bool_bstr"></span>IPixEngine2::SetPlaybackMachine method

Sets the current playback machine for the specified graphics log.

## Syntax


```C++
);
```

## Parameters

*logFile*   
A COM string contianing the name of the graphics log.

*bUseAuthentication*   
true to use authentication; otherwise, false.

*machine*   
A COM string containing the name of the playback machine.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPixEngine2**](https://msdn.microsoft.com/library/windows/desktop/mt432746)

 

 



