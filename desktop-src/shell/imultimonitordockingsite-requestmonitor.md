---
Description: 'Verifies that the monitor is active and available.'
title: 'IMultiMonitorDockingSite::RequestMonitor method'
---

# IMultiMonitorDockingSite::RequestMonitor method

Verifies that the monitor is active and available.

## Syntax


```C++
HRESULT RequestMonitor(
  [in] IUnknown *punkSrc,
  [in] HMONITOR *phMon
);
```



## Parameters

<dl> <dt>

*punkSrc* \[in\]
</dt> <dd>

Type: **[**IUnknown**](com.iunknown)\***

A pointer to the object implementing the [**IDockingWindow**](idockingwindow.md) interface.

</dd> <dt>

*phMon* \[in\]
</dt> <dd>

Type: **HMONITOR\***

A pointer to the default monitor's handle.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                        |
|-------------------------------------|------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                   |



 

 




