---
description: Verifies that the monitor is active and available.
title: IMultiMonitorDockingSite::RequestMonitor method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMultiMonitorDockingSite.RequestMonitor
api_type: 
- COM
api_location: 
ms.assetid: 9aa6eb20-de39-41f7-a17e-183f4088f972
api_name: 
 - IMultiMonitorDockingSite.RequestMonitor
api_type: 
 - COM
api_location: 
topic_type: 
 - APIRef
 - kbSyntax

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

Type: **[**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown)\***

A pointer to the object implementing the [**IDockingWindow**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idockingwindow) interface.

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



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                   |



 

 
