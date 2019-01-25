---
title: D2D1_COLOR_F
description: Describes the red, green, blue, and alpha components of a color.
ms.assetid: 564d4f41-2da7-49ed-b85a-d1070d662b40
keywords:
- D2D1_COLOR_F
ms.topic: article
ms.date: 05/31/2018
---

# D2D1\_COLOR\_F

Describes the red, green, blue, and alpha components of a color.


```C++
typedef D2D_COLOR_F D2D1_COLOR_F;
```



## Remarks

**D2D1\_COLOR\_F** is a typedef for [**D2D\_COLOR\_F**](d2d-color-f.md), which is itself a typedef for [D3DCOLORVALUE](https://msdn.microsoft.com/library/bb172520(VS.85).aspx). For information about the members provided by **D2D1\_COLOR\_F**, see [D3DCOLORVALUE](https://msdn.microsoft.com/library/bb172520(VS.85).aspx).

The [**ColorF**](https://msdn.microsoft.com/en-us/library/Dd370907(v=VS.85).aspx) class provides a set of predefined colors and helper functions for defining colors. For more information, see the [**ColorF**](https://msdn.microsoft.com/en-us/library/Dd370907(v=VS.85).aspx) reference.

## Examples

The following example uses the [**ColorF**](https://msdn.microsoft.com/en-us/library/Dd370907(v=VS.85).aspx) class to specify a predefined color (black) when creating an [**ID2D1SolidColorBrush**](https://msdn.microsoft.com/en-us/library/Dd372207(v=VS.85).aspx).


```C++
hr = m_pRenderTarget->CreateSolidColorBrush(
    D2D1::ColorF(D2D1::ColorF::Black, 1.0f),
    &m_pBlackBrush
    );
```



The following example uses the [**ColorF**](https://msdn.microsoft.com/en-us/library/Dd370907(v=VS.85).aspx) class to specify a color using red, green, blue, and alpha values.


```C++
ID2D1SolidColorBrush *pGridBrush = NULL;
hr = pCompatibleRenderTarget->CreateSolidColorBrush(
    D2D1::ColorF(D2D1::ColorF(0.93f, 0.94f, 0.96f, 1.0f)),
    &pGridBrush
    );
```



## Requirements



|                                     |                                                                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7, Windows Vista with SP2 and Platform Update for Windows Vista \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported server<br/> | Windows Server 2008 R2, Windows Server 2008 with SP2 and Platform Update for Windows Server 2008 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/>                                                  |
| Header<br/>                   | <dl> <dt>D2DBaseTypes.h (include D2d1.h)</dt> </dl>                               |



## See also

<dl> <dt>

[D3DCOLORVALUE](https://msdn.microsoft.com/library/bb172520(VS.85).aspx)
</dt> <dt>

[**ColorF**](https://msdn.microsoft.com/en-us/library/Dd370907(v=VS.85).aspx)
</dt> </dl>

 

 





