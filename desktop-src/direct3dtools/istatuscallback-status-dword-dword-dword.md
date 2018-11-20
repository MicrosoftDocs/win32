---
Description: A callback function used to notify the host of the engines progress. This also serves as a way for the host to determine that the engine is still running.
title: "IStatusCallback::Status method"
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.istatuscallback_status_dword_dword_dword"></span>IStatusCallback::Status method

A callback function used to notify the host of the engine's progress. This also serves as a way for the host to determine that the engine is still running.

## Syntax


```C++
);
```

## Parameters

*dwMillisecondsElapsed*   
The time elapsed since the last call to Status, in milliseconds.

*dwFramesCaptured*   
The number of frames that have been captures since the last call to Status.

*dwFramesElapsed*   
The number of frames elapsed since the last call to Status.

## Return value

If this method succeeds, it returns **S_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IStatusCallback**](https://msdn.microsoft.com/library/windows/desktop/mt432807)

 

 



