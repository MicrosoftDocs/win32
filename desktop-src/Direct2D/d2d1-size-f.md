---
title: D2D1_SIZE_F
description: Stores an ordered pair of floats, typically the width and height of a rectangle.
ms.assetid: c2fd41fb-72b3-418b-ad87-65549b04657d
keywords:
- D2D1_SIZE_F
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D2D1\_SIZE\_F

Stores an ordered pair of floats, typically the width and height of a rectangle.


```C++
typedef D2D_SIZE_F D2D1_SIZE_F;
```



## Remarks

Like points, sizes are another important graphics concept. In Direct2D, sizes are represented by the **D2D1\_SIZE\_F** or [**D2D1\_SIZE\_U**](d2d1-size-u.md) structures. Both contain an ordered pair of numbers, typically the width and height of a rectangle. The **D2D1\_SIZE\_F** structure contains an ordered pair of **FLOAT** values, and the **D2D1\_SIZE\_U** structure contains an ordered pair of **UINT32** values.

**D2D1\_SIZE\_F** is a new name for an already defined type **D2D\_SIZE\_F**. For a list of the fields provided by **D2D1\_SIZE\_F**, see **D2D\_SIZE\_F**.

## Requirements



|                                     |                                                                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7, Windows Vista with SP2 and Platform Update for Windows Vista \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported server<br/> | Windows Server 2008 R2, Windows Server 2008 with SP2 and Platform Update for Windows Server 2008 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/>                                                  |
| Header<br/>                   | <dl> <dt>D2DBaseTypes.h (include D2d1.h)</dt> </dl>                               |



## See also

<dl> <dt>

[**D2D\_SIZE\_F**](https://msdn.microsoft.com/library/windows/desktop/dd368189)
</dt> <dt>

[**D2D1\_SIZE\_U**](d2d1-size-u.md)
</dt> <dt>

[**D2D1\_POINT\_2F**](d2d1-point-2f.md)
</dt> </dl>

 

 





