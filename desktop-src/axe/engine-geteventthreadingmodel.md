---
title: Engine GetEventThreadingModel method
description: Retrieve the threading model that is being used to call the solution’s native events that have been registered with the Engine.
ms.assetid: '2B5A1D7E-0A1F-4D0F-8A2B-BB3B7ABD34FF'
keywords: ["GetEventThreadingModel method Access Execution Engine", "GetEventThreadingModel method Access Execution Engine , Engine interface", "Engine interface Access Execution Engine , GetEventThreadingModel method"]
topic_type:
- apiref
api_name:
- Engine.GetEventThreadingModel
api_location:
- AxeCore.dll
api_type:
- COM
---

# Engine::GetEventThreadingModel method

Retrieve the threading model that is being used to call the solution’s native events that have been registered with the Engine.

## Syntax


```C++
virtual HRESULT GetEventThreadingModel(
  [out] ThreadingModel *eventThreadingModel
) = 0;
```



## Parameters

<dl> <dt>

*eventThreadingModel* \[out\]
</dt> <dd>

The threading model being used when invoking the solution’s callbacks. See the [**ThreadingModel**](threadingmodel.md) enumeration for details.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

This method retrieves the threading model that was specified in a successful call to [**SetEventThreadingModel**](job-seteventthreadingmodel.md). This method is only available in the native API. In managed code, .NET events are used instead of callbacks.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Engine**](engine-if.md)
</dt> </dl>

 

 





