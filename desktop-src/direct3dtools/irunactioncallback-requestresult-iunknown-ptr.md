---
Description: A callback function used to notify the host of results from an action (for example, capture a frame) that it requested.
MS-HAID: vspixengine.IRunActionCallback\_RequestResult\_IUnknown\_ptr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IRunActionCallback::RequestResult method
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.irunactioncallback_requestresult_iunknown_ptr"></span>IRunActionCallback::RequestResult method

A callback function used to notify the host of results from an action (for example, capture a frame) that it requested.

## Syntax


```C++
);
```

## Parameters

*actionResult*   
The result of the action.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IRunActionCallback**](https://msdn.microsoft.com/library/windows/desktop/mt432790)

 

 



