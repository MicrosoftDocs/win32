---
description: The GetMaxIdealImageSize method retrieves the maximum ideal image size.
ms.assetid: 881c1c3d-7505-44a2-964d-3255e2072f6b
title: CBaseControlWindow.GetMaxIdealImageSize method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.GetMaxIdealImageSize
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.GetMaxIdealImageSize method

The `GetMaxIdealImageSize` method retrieves the maximum ideal image size.

## Syntax


```C++
HRESULT GetMaxIdealImageSize(
   long *pWidth,
   long *pHeight
);
```



## Parameters

<dl> <dt>

*pWidth* 
</dt> <dd>

Pointer to the maximum ideal width, in pixels.

</dd> <dt>

*pHeight* 
</dt> <dd>

Pointer to the maximum ideal height, in pixels.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

Various renderers have performance restrictions on the size of images they can display. Although they should still function properly when requested to display images larger than the specified maximum, renderers can nominate the minimum and maximum ideal sizes through the [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) interface. This interface can be called only when the filter graph is paused or running, because it is not until then that resources are allocated and the renderer can recognize its restrictions. If no restrictions exist, the renderer fills in the *pWidth* and *pHeight* parameters with the native video dimensions and returns S\_FALSE. If restrictions do exist, the restricted width and height are entered, and the member function returns S\_OK.

The dimensions apply to the size of the destination video and not to the overall window size. So, when calculating the size of the window to set, account for the current window styles (for example, WS\_CAPTION and WS\_BORDER).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




