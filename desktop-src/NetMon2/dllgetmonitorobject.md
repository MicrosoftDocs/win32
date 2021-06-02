---
description: The DllGetMonitorObject function must be implemented by the monitor. The MCSVC calls this function to create an instance of the monitor.
ms.assetid: 2c39f752-264c-4ab9-8710-a0d660c4772f
title: DllGetMonitorObject callback function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DllGetMonitorObject
api_type: 
- UserDefined
api_location: 
- Netmon.h
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

If the function is unsuccessful, the return value is a failure code. When a failure code is returned, the MCSVC does not create the monitor object, and the [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method is not called on the interface pointer.

## Remarks

The **DllGetMonitorObject** function is called each time the MCSVC tries to create an instance of the monitor. This function intentionally bears a strong resemblance to the more common [**DllGetClassObject**](/windows/win32/api/combaseapi/nf-combaseapi-dllgetclassobject) function. The main difference is that a CLSID is not passed in to **DllGetMonitorObject**.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

