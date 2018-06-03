---
title: ISystemMediaTransportControlsInterop GetForWindow method
description: Gets an instance of the ISystemMediaTransportControls interface for the specified window.
ms.assetid: 7E878C3B-4CE9-4DED-8082-8E37266FE8AF
keywords:
- GetForWindow method
- GetForWindow method, ISystemMediaTransportControlsInterop interface
- ISystemMediaTransportControlsInterop interface, GetForWindow method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControlsInterop.GetForWindow
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISystemMediaTransportControlsInterop::GetForWindow method

Gets an instance of the [**ISystemMediaTransportControls**](isystemmediatransportcontrols.md) interface for the specified window.

## Syntax


```C++
HRESULT GetForWindow(
        HWND   appWindow,
        REFIID riid,
  [out] void   **mediaTransportControl
);
```



## Parameters

<dl> <dt>

*appWindow* 
</dt> <dd>

The top-level app window for which the [**ISystemMediaTransportControls**](isystemmediatransportcontrols.md) interface is retrieved.

</dd> <dt>

*riid* 
</dt> <dd>

A reference to the IID of the interface to retrieve.

</dd> <dt>

*mediaTransportControl* \[out\]
</dt> <dd>

The top-level app window for which the [**ISystemMediaTransportControls**](isystemmediatransportcontrols.md) interface is retrieved.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## See also

<dl> <dt>

[**ISystemMediaTransportControlsInterop**](/previous-versions/windows/desktop/api/systemmediatransportcontrolsinterop/nn-systemmediatransportcontrolsinterop-isystemmediatransportcontrolsinterop)
</dt> </dl>

 

 




