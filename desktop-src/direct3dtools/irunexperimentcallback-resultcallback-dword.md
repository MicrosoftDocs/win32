---
description: Requests to run an experiment (capture) on the specified process.
MS-HAID: vspixengine.IRunExperimentCallback\_ResultCallback\_DWORD
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IRunExperimentCallback::ResultCallback method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: C00034DF-5F51-49A2-B49A-62F98EA48F46
api_name: 
 - IRunExperimentCallback.ResultCallback
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.irunexperimentcallback_resultcallback_dword"></span>IRunExperimentCallback::ResultCallback method

Requests to run an experiment (capture) on the specified process.

## Syntax


```C++
HRESULT ResultCallback(
   DWORD processId
);
```

## Parameters

*processId*   
The specified process.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IRunExperimentCallback**](/windows/desktop/direct3dtools/irunexperimentcallback)

 

 
