---
title: D2D1_POINT_2F (D2DBaseTypes.h)
description: Represents an x-coordinate and y-coordinate pair in two-dimensional space. | D2D1_POINT_2F (D2DBaseTypes.h)
ms.assetid: b317ae75-d738-4e1a-bcd1-adf3e95b197e
keywords:
- D2D1_POINT_2F
ms.topic: reference
ms.date: 05/31/2018
---

# D2D1\_POINT\_2F

Represents an x-coordinate and y-coordinate pair in two-dimensional space.


```C++
typedef D2D_POINT_2F D2D1_POINT_2F;
```



## Remarks

Points in Direct2D are represented by the **D2D1\_POINT\_2F** or [**D2D1\_POINT\_2U**](d2d1-point-2u.md) structures. Both contain an x-coordinate and y-coordinate pair in two-dimensional space. The **D2D1\_POINT\_2F** structure stores the coordinates as **FLOAT** values, and the **D2D1\_POINT\_2U** structure stores them as **UINT32** values.

**D2D1\_POINT\_2F** is a new name for the already defined type [**D2D\_POINT\_2F**](/windows/desktop/api/dcommon/ns-dcommon-d2d_point_2f).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7, Windows Vista with SP2 and Platform Update for Windows Vista \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported server<br/> | Windows Server 2008 R2, Windows Server 2008 with SP2 and Platform Update for Windows Server 2008 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/>                                                  |
| Header<br/>                   | <dl> <dt>D2DBaseTypes.h (include D2d1.h)</dt> </dl>                               |



## See also

<dl> <dt>

[**D2D1\_POINT\_2U**](/windows/desktop/Direct2D/d2d1-point-2u)
</dt> <dt>

[**D2D\_POINT\_2F**](/windows/desktop/api/dcommon/ns-dcommon-d2d_point_2f)
</dt> </dl>

 

