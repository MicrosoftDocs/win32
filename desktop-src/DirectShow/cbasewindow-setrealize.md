---
Description: 'The SetRealize method specifies whether the window realizes palettes.'
ms.assetid: 'ab4a6069-c11f-4126-93bf-6de5277970a1'
title: 'CBaseWindow.SetRealize method'
---

# CBaseWindow.SetRealize method

The `SetRealize` method specifies whether the window realizes palettes.

## Syntax


```C++
void SetRealize(
   BOOL bRealize
);
```



## Parameters

<dl> <dt>

*bRealize* 
</dt> <dd>

Boolean value that specifies whether to realize palettes. If **TRUE**, the [**CBaseWindow::SetPalette**](cbasewindow-setpalette.md) method realizes palettes.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

By default, the **SetPalette** method realizes the specified palette. Call this method to change the default behavior, so that palettes are selected but not realized. This method sets the [**CBaseWindow::m\_bNoRealize**](cbasewindow-m-bnorealize.md) member variable.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




