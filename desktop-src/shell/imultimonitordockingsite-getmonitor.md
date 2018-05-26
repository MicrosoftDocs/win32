---
Description: Gets the current default monitor.
title: IMultiMonitorDockingSiteGetMonitor method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMultiMonitorDockingSite::GetMonitor method

Gets the current default monitor.

## Syntax


```C++
HRESULT GetMonitor(
  [in]  IUnknown *punkSrc,
  [out] HMONITOR *phMon
);
```



## Parameters

<dl> <dt>

*punkSrc* \[in\]
</dt> <dd>

Type: **[**IUnknown**](com.iunknown)\***

A pointer to the object implementing the [**IDockingWindow**](/windows/win32/shobjidl_core/nn-shobjidl_core-idockingwindow?branch=master) interface for which the monitor is being requested.

</dd> <dt>

*phMon* \[out\]
</dt> <dd>

Type: **HMONITOR\***

When the function returns, contains a pointer to the default monitor's handle.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                        |
|-------------------------------------|------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                   |



 

 




