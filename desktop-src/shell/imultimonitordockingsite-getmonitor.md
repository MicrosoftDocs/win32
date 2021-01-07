---
description: Gets the current default monitor.
title: IMultiMonitorDockingSite::GetMonitor method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMultiMonitorDockingSite.GetMonitor
api_type: 
- COM
api_location: 
ms.assetid: 0bae75eb-ebd5-4de4-9249-0e9bb489f61f
api_name: 
 - IMultiMonitorDockingSite.GetMonitor
api_type: 
 - COM
api_location: 
topic_type: 
 - APIRef
 - kbSyntax

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

Type: **[**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown)\***

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



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                   |



 

 
