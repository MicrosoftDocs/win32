---
Description: 'Changes which monitor is used for docked toolbars on a multiple monitor system.'
title: 'IMultiMonitorDockingSite::SetMonitor method'
---

# IMultiMonitorDockingSite::SetMonitor method

Changes which monitor is used for docked toolbars on a multiple monitor system.

## Syntax


```C++
HRESULT SetMonitor(
  [in]  IUnknown *punkSrc,
  [in]  HMONITOR hMonNew,
  [out] HMONITOR *phMonOld
);
```



## Parameters

<dl> <dt>

*punkSrc* \[in\]
</dt> <dd>

Type: **[**IUnknown**](com.iunknown)\***

A pointer to the object implementing the [**IDockingWindow**](idockingwindow.md) interface for which the monitor is being altered.

</dd> <dt>

*hMonNew* \[in\]
</dt> <dd>

Type: **HMONITOR**

A handle to the monitor that replaces the existing default monitor.

</dd> <dt>

*phMonOld* \[out\]
</dt> <dd>

Type: **HMONITOR\***

When this function returns, contains a pointer to the previous default monitor's handle.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                        |
|-------------------------------------|------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                   |



 

 




