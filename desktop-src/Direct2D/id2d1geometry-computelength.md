---
title: ID2D1Geometry ComputeLength methods
description: Calculates the length of the geometry as though each segment were unrolled into a line.
ms.assetid: '4659d880-0aa3-485d-ac71-044d9ace6759'
keywords: ["ComputeLength methods Direct2D"]
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
---

# ID2D1Geometry::ComputeLength methods

Calculates the length of the geometry as though each segment were unrolled into a line.

### Overload list



| Method                                                                                                                          | Description                                                                                         |
|:--------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------|
| [**ComputeLength(D2D1\_MATRIX\_3X2\_F&,FLOAT\*)**](id2d1geometry-computelength-ref-d2d-matrix-3x2-f-ptr-float.md)              | Calculates the length of the geometry as though each segment were unrolled into a line.<br/>  |
| [**ComputeLength(D2D1\_MATRIX\_3X2\_F\*,FLOAT\*)**](id2d1geometry-computelength-ptr-d2d-matrix-3x2-f-ptr-float.md)             | Calculates the length of the geometry as though each segment were unrolled into a line.<br/>  |
| [**ComputeLength(D2D1\_MATRIX\_3X2\_F&,FLOAT,FLOAT\*)**](id2d1geometry-computelength-ref-d2d-matrix-3x2-f-float-ptr-float.md)  | Calculates the length of the geometry as though each segment were unrolled into a line.<br/>  |
| [**ComputeLength(D2D1\_MATRIX\_3X2\_F\*,FLOAT,FLOAT\*)**](id2d1geometry-computelength-ptr-d2d-matrix-3x2-f-float-ptr-float.md) | Calculates the length of the geometry as though each segment were unrolled into a line. <br/> |



## Examples

The following code shows how to use **ComputeLength** to compute the length of a specified path geometry.


```C++
float length = 0;
hr = m_pPathGeometry->ComputeLength(
    NULL, //no transform
    &amp;length
    );

if (SUCCEEDED(hr))
{
    m_Animation.SetStart(0);        //start at beginning of path
    m_Animation.SetEnd(length);     //length at end of path
    m_Animation.SetDuration(5.0f);  //seconds

    ZeroMemory(&amp;m_DwmTimingInfo, sizeof(m_DwmTimingInfo));
    m_DwmTimingInfo.cbSize = sizeof(m_DwmTimingInfo);

    // Get the composition refresh rate. If the DWM isn't running,
    // get the refresh rate from GDI -- probably going to be 60Hz
    if (FAILED(DwmGetCompositionTimingInfo(NULL, &amp;m_DwmTimingInfo)))
    {
        HDC hdc = GetDC(m_hwnd);
        m_DwmTimingInfo.rateCompose.uiDenominator = 1;
        m_DwmTimingInfo.rateCompose.uiNumerator = GetDeviceCaps(hdc, VREFRESH);
        ReleaseDC(m_hwnd, hdc);
    }

    ShowWindow(m_hwnd, SW_SHOWNORMAL);

    UpdateWindow(m_hwnd);
}
```



## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1Geometry**](id2d1geometry.md)
</dt> </dl>

 

 





