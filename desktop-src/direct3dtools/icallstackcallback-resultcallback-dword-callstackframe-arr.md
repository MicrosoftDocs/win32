---
Description: A callback function used to notify the host of call stack information.
MS-HAID: vspixengine.ICallStackCallback\_ResultCallback\_DWORD\_CallStackFrame\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: ICallStackCallback::ResultCallback method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.icallstackcallback_resultcallback_dword_callstackframe_arr"></span>ICallStackCallback::ResultCallback method

A callback function used to notify the host of call stack information.

## Syntax


```C++
);
```

## Parameters

*count*   
The number of callstack framebuffers returned.

*count0\_callStackFrameBuffer*   
The callstack information.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**ICallStackCallback**](https://msdn.microsoft.com/library/windows/desktop/mt422650)

 

 



