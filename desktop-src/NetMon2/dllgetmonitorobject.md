---
Description: The DllGetMonitorObject function must be implemented by the monitor. The MCSVC calls this function to create an instance of the monitor.
ms.assetid: 2c39f752-264c-4ab9-8710-a0d660c4772f
title: DllGetMonitorObject callback function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DllGetMonitorObject callback function

The **DllGetMonitorObject** function must be implemented by the monitor. The MCSVC calls this function to create an instance of the monitor.

## Syntax


```C++
HRESULT DllGetMonitorObject(
  _In_  REFIID riid,
  _Out_ LPVOID *ppObj
);
```



## Parameters

<dl> <dt>

*riid* \[in\]
</dt> <dd>

UUID of monitors, shown below, as defined in the IMonitor.h header file. If an invalid UUID is provided, the function fails, and the monitor must return E\_NOINTERFACE.

``` syntax
IID_IMonitor
```

</dd> <dt>

*ppObj* \[out\]
</dt> <dd>

Pointer to a pointer that receives the interface requested in *riid*.

</dd> </dl>

## Return value

If the function is successful, the return value is S\_OK (which is the same as NOERROR).

If the function is unsuccessful, the return value is a failure code. When a failure code is returned, the MCSVC does not create the monitor object, and the [IUnknown::Release](https://msdn.microsoft.com/windows/desktop/4b494c6f-f0ee-4c35-ae45-ed956f40dc7a) method is not called on the interface pointer.

## Remarks

The **DllGetMonitorObject** function is called each time the MCSVC tries to create an instance of the monitor. This function intentionally bears a strong resemblance to the more common [**DllGetClassObject**](https://msdn.microsoft.com/windows/desktop/42c08149-c251-47f7-a81f-383975d7081c) function. The main difference is that a CLSID is not passed in to **DllGetMonitorObject**.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




