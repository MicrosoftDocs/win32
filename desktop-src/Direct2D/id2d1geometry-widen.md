---
title: ID2D1Geometry Widen methods
description: Widens the geometry by the specified stroke and writes the result to an ID2D1SimplifiedGeometrySink.
ms.assetid: c951ab85-7980-41e3-95c4-291d2fb046c8
keywords:
- Widen methods Direct2D
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
api_name: 
---

# ID2D1Geometry::Widen methods

Widens the geometry by the specified stroke and writes the result to an [**ID2D1SimplifiedGeometrySink**](https://msdn.microsoft.com/en-us/library/Dd316919(v=VS.85).aspx).

### Overload list



| Method                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                              |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Widen(FLOAT,ID2D1StrokeStyle\*,D2D1\_MATRIX\_3X2\_F\*,ID2D1SimplifiedGeometrySink\*)**](https://msdn.microsoft.com/en-us/library/Dd316770(v=VS.85).aspx)             | Widens the geometry by the specified stroke and writes the result to an [**ID2D1SimplifiedGeometrySink**](https://msdn.microsoft.com/en-us/library/Dd316919(v=VS.85).aspx) after it has been transformed by the specified matrix and flattened using the default tolerance.<br/>   |
| [**Widen(FLOAT,ID2D1StrokeStyle\*,D2D1\_MATRIX\_3X2\_F&,ID2D1SimplifiedGeometrySink\*)**](https://msdn.microsoft.com/en-us/library/Dd316779(v=VS.85).aspx)              | Widens the geometry by the specified stroke and writes the result to an [**ID2D1SimplifiedGeometrySink**](https://msdn.microsoft.com/en-us/library/Dd316919(v=VS.85).aspx) after it has been transformed by the specified matrix and flattened using the default tolerance.<br/>   |
| [**Widen(FLOAT,ID2D1StrokeStyle\*,D2D1\_MATRIX\_3X2\_F\*,FLOAT,ID2D1SimplifiedGeometrySink\*)**](https://msdn.microsoft.com/en-us/library/Dd316766(v=VS.85).aspx) | Widens the geometry by the specified stroke and writes the result to an [**ID2D1SimplifiedGeometrySink**](https://msdn.microsoft.com/en-us/library/Dd316919(v=VS.85).aspx) after it has been transformed by the specified matrix and flattened using the specified tolerance.<br/> |
| [**Widen(FLOAT,ID2D1StrokeStyle\*,D2D1\_MATRIX\_3X2\_F&,FLOAT,ID2D1SimplifiedGeometrySink\*)**](https://msdn.microsoft.com/en-us/library/Dd316774(v=VS.85).aspx)  | Widens the geometry by the specified stroke and writes the result to an [**ID2D1SimplifiedGeometrySink**](https://msdn.microsoft.com/en-us/library/Dd316919(v=VS.85).aspx) after it has been transformed by the specified matrix and flattened using the specified tolerance.<br/> |



## Examples

The following code example shows how to use **Widen** to widen the geometry by the specified stroke and then write the result to an [**ID2D1SimplifiedGeometrySink**](https://msdn.microsoft.com/en-us/library/Dd316919(v=VS.85).aspx) object.


```C++
 ID2D1GeometrySink *pGeometrySink = NULL;
 hr = pPathGeometry->Open(&amp;pGeometrySink);
 if (SUCCEEDED(hr))
 {
     hr = pGeometry->Widen(
             strokeWidth,
             pIStrokeStyle,
             pWorldTransform,
             pGeometrySink
             );

     if (SUCCEEDED(hr))
     {
         hr = pGeometrySink->Close();
         if (SUCCEEDED(hr))
         {
             ID2D1Mesh *pMesh = NULL;
             hr = m_pRT->CreateMesh(&amp;pMesh);
             if (SUCCEEDED(hr))
             {
                 ID2D1TessellationSink *pSink = NULL;
                 hr = pMesh->Open(&amp;pSink);
                 if (SUCCEEDED(hr))
                 {
                     hr = pPathGeometry->Tessellate(
                             NULL, // world transform (already handled in Widen)
                             pSink
                             );
                     if (SUCCEEDED(hr))
                     {
                         hr = pSink->Close();
                         if (SUCCEEDED(hr))
                         {
                             SafeReplace(&amp;m_pStrokeMesh, pMesh);
                         }
                     }
                     pSink->Release();
                 }
                 pMesh->Release();
             }
         }
     }
     pGeometrySink->Release();
 }
 pPathGeometry->Release();
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

 

 





