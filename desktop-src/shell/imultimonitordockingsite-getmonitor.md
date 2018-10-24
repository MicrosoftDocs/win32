---
Description: Gets the current default monitor.
title: IMultiMonitorDockingSite::GetMonitor method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMultiMonitorDockingSite.GetMonitor
api_type: 
- COM
api_location: 
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

Type: **[**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx)\***

A pointer to the object implementing the [**IDockingWindow**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idockingwindow) interface for which the monitor is being requested.

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



 

 




