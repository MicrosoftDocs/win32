---
title: IAccessibilityDockingService GetAvailableSize method
description: Gets the dimensions available for docking an accessibility window on a monitor.
ms.assetid: 1C838B01-EF26-4FCC-878F-A36DEFBA3142
keywords:
- GetAvailableSize method COM
- GetAvailableSize method COM , IAccessibilityDockingService interface
- IAccessibilityDockingService interface COM , GetAvailableSize method
topic_type:
- apiref
api_name:
- IAccessibilityDockingService.GetAvailableSize
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IAccessibilityDockingService::GetAvailableSize method

Gets the dimensions available for docking an accessibility window on a monitor.

## Syntax


```C++
HRESULT GetAvailableSize(
  [in]  HMONITOR hMonitor,
  [out] UINT     *puMaxHeight,
  [out] UINT     *puFixedWidth
);
```



## Parameters

<dl> <dt>

*hMonitor* \[in\]
</dt> <dd>

Specifies the monitor for which the available docking size will be retrieved.

</dd> <dt>

*puMaxHeight* \[out\]
</dt> <dd>

On success, set to the maximum height available for docking on the specified *hMonitor*, in pixels.

On failure, set to zero.

</dd> <dt>

*puFixedWidth* \[out\]
</dt> <dd>

On success, set to the fixed width available for docking on the specified *hMonitor*, in pixels. Any window docked to this *hMonitor* will be sized to this width.

On failure, set to zero.

</dd> </dl>

## Return value



| Return code                                                                                                                          | Description                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                                 | Success.<br/>                                                              |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_INVALID\_MONITOR\_HANDLE)**</dt> </dl> | The monitor specified by the monitor handle does not support docking.<br/> |



 

If either *puMaxHeight* or *puFixedWidth* are null, an access violation will occur.

## Remarks

Accessibility windows can only be docked to a monitor that has at least 768 vertical screen pixels. This API will not allow such windows to be docked with a height that would cause Windows Store apps to have less than 768 vertical screen pixels.

## Examples


```
IAccessibilityDockingService *pDockingService;
HRESULT hr = CoCreateInstance(CLSID_AccessibilityDockingService, CLSCTX_INPROV_SERVER, nullptr, IID_PPV_ARGS(&pDockingService));
if (SUCCEEDED(hr))
{
    UINT uMaxHeight;
    UINT uFixedWidth;

    HMONITOR hMonitor = MonitorFromWindow(_hwndMyApplication, MONITOR_DEFAULTTONULL);
    if (hMonitor != nullptr)
    {
        hr = pDockingService->GetAvailableSize(hMonitor, &uMaxHeight, &uFixedWidth);
    }
}
```



## See also

<dl> <dt>

[**IAccessibilityDockingService**](/windows/desktop/api/shobjidl/nn-shobjidl-iaccessibilitydockingservice)
</dt> </dl>

 

 





