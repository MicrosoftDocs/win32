---
Description: The RefreshDisplayType method updates the object's video format to match the specified display.
ms.assetid: cc2bdfeb-80f1-4fb6-859d-977d644a5e08
title: CImageDisplay.RefreshDisplayType method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CImageDisplay.RefreshDisplayType method

The `RefreshDisplayType` method updates the object's video format to match the specified display.

## Syntax


```C++
HRESULT RefreshDisplayType(
   LPSTR szDeviceName
);
```



## Parameters

<dl> <dt>

*szDeviceName* 
</dt> <dd>

Pointer to a string that contains the name of the display device, as returned by the GDI **EnumDisplayDevices** function. To use the main display device, set this parameter to **NULL**.

</dd> </dl>

## Return value

Returns S\_OK if successful, or E\_FAIL if unsuccessful.

## Remarks

This method initializes the **m\_Display** member to a video type that corresponds to the display mode on the specified device.

Call this method whenever a WM\_DISPLAYCHANGED message is received, or to specify a secondary display device.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageDisplay Class**](cimagedisplay.md)
</dt> </dl>

 

 




