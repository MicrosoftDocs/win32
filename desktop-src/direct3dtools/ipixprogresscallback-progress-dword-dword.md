---
description: A callback that notifies the host of the progress of an associated request.
MS-HAID: vspixengine.IPixProgressCallback\_Progress\_DWORD\_DWORD
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixProgressCallback::Progress method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: BE74599B-C98F-4BDB-ACDF-641F77A35EEB
api_name: 
 - IPixProgressCallback.Progress
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipixprogresscallback_progress_dword_dword"></span>IPixProgressCallback::Progress method

A callback that notifies the host of the progress of an associated request.

## Syntax


```C++
HRESULT Progress(
   DWORD current,
   DWORD maxSize
);
```

## Parameters

*current*   
The portion of a request completed, as a count of the number of steps completed.

*maxSize*   
The total number of steps to complete the request.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPixProgressCallback**](/windows/desktop/direct3dtools/ipixprogresscallback)

 

 
