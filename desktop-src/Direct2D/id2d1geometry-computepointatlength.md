---
title: ID2D1Geometry ComputePointAtLength methods
description: Calculates the point and tangent vector at the specified distance along the \ 160;geometry.
ms.assetid: b76aa3db-2967-4baa-a449-f664b080fb74
keywords:
- ComputePointAtLength methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID2D1Geometry::ComputePointAtLength methods

Calculates the point and tangent vector at the specified distance along the geometry.

### Overload list



| Method                                                                                                                                                                                                        | Description                                                                                                                                                                                        |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ComputePointAtLength(FLOAT,D2D1\_MATRIX\_3X2\_F&,D2D1\_POINT\_2F\*,D2D1\_POINT\_2F\*)**](https://msdn.microsoft.com/en-us/library/Dd316686(v=VS.85).aspx)              | Calculates the point and tangent vector at the specified distance along the geometry after it has been transformed by the specified matrix and flattened using the default tolerance.<br/>   |
| [**ComputePointAtLength(FLOAT,D2D1\_MATRIX\_3X2\_F\*,D2D1\_POINT\_2F\*,D2D1\_POINT\_2F\*)**](https://msdn.microsoft.com/en-us/library/Dd316680(v=VS.85).aspx)             | Calculates the point and tangent vector at the specified distance along the geometry after it has been transformed by the specified matrix and flattened using the default tolerance.<br/>   |
| [**ComputePointAtLength(FLOAT,D2D1\_MATRIX\_3X2\_F&,FLOAT,D2D1\_POINT\_2F\*,D2D1\_POINT\_2F\*)**](https://msdn.microsoft.com/en-us/library/Dd316683(v=VS.85).aspx)  | Calculates the point and tangent vector at the specified distance along the geometry after it has been transformed by the specified matrix and flattened using the specified tolerance.<br/> |
| [**ComputePointAtLength(FLOAT,D2D1\_MATRIX\_3X2\_F\*,FLOAT,D2D1\_POINT\_2F\*,D2D1\_POINT\_2F\*)**](https://msdn.microsoft.com/en-us/library/Dd316676(v=VS.85).aspx) | Calculates the point and tangent vector at the specified distance along the geometry after it has been transformed by the specified matrix and flattened using the specified tolerance.<br/> |



## Examples

The following code example shows how to use **ComputePointAtLength** to calculate the point and tangent vector at the specified distance along the geometry.


```C++
D2D1_POINT_2F point;
D2D1_POINT_2F tangent;
```




```C++
// Ask the geometry to give us the point that corresponds with the
// length at the current time.
hr = m_pPathGeometry->ComputePointAtLength(
    length, 
    NULL, 
    &amp;point, 
    &amp;tangent); 
```



## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1Geometry**](https://msdn.microsoft.com/en-us/library/Dd316578(v=VS.85).aspx)
</dt> </dl>

 

 





