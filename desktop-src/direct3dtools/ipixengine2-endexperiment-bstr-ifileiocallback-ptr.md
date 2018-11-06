---
Description: Ends the experiement and completes the graphics log.
MS-HAID: vspixengine.IPixEngine2\_EndExperiment\_BSTR\_IFileIOCallback\_ptr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine2::EndExperiment method
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.ipixengine2_endexperiment_bstr_ifileiocallback_ptr"></span>IPixEngine2::EndExperiment method

Ends the experiement and completes the graphics log.

## Syntax


```C++
);
```

## Parameters

*logFile*   
A COM string containing the name of the graphics log.

*pCallback*   
The address of a callback used to indicate that the experiement is ended.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPixEngine2**](https://msdn.microsoft.com/library/windows/desktop/mt432746)

 

 



