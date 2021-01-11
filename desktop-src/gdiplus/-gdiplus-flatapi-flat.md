---
description: Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h.
ms.assetid: afd8cf81-8a20-4592-bd0a-46341742cc9b
title: GDI+ Flat API
ms.topic: article
ms.date: 05/31/2018
---

# GDI+ Flat API

Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h. The functions in the GDI+ flat API are wrapped by a collection of about 40 C++ classes. It is recommended that you do not directly call the functions in the flat API. Whenever you make calls to GDI+, you should do so by calling the methods and functions provided by the C++ wrappers. Microsoft Product Support Services will not provide support for code that calls the flat API directly.

As an alternative to the C++ wrappers, the Microsoft .NET Framework provides a set of managed-code wrapper classes for GDI+. The managed-code wrappers for GDI+ belong to the following namespaces.

-   [System.Drawing](/dotnet/api/system.drawing?view=dotnet-plat-ext-3.1&preserve-view=true)
-   [System.Drawing.Drawing2D](/dotnet/api/system.drawing.drawing2d?view=dotnet-plat-ext-3.1&preserve-view=true)
-   [System.Drawing.Imaging](/dotnet/api/system.drawing.imaging?view=dotnet-plat-ext-3.1&preserve-view=true)
-   [System.Drawing.Text](/dotnet/api/system.drawing.text?view=dotnet-plat-ext-3.1&preserve-view=true)

Both sets of wrappers (C++ and managed code) use an object-oriented approach, so there are some differences between the way parameters are passed to the wrapper methods and the way parameters are passed to functions in the flat API. For example, one of the C++ wrappers is the [**Matrix**](/windows/win32/api/gdiplusmatrix/nl-gdiplusmatrix-matrix) class. Each **Matrix** object has a field, **nativeMatrix**, that points to an internal variable of type **GpMatrix**. When you pass parameters to a method of a **Matrix** object, that method passes those parameters (or a set of related parameters) along to one of the functions in the GDI+ flat API. But that method also passes the **nativeMatrix** field (as an input parameter) to the flat API function. The following code shows how the [**Matrix::Shear**](/windows/win32/api/Gdiplusmatrix/nf-gdiplusmatrix-matrix-shear) method calls the **GdipShearMatrix(GpMatrix \*matrix, REAL shearX, REAL shearY, GpMatrixOrder order)** function.


```
Status Shear(
      IN REAL shearX, 
      IN REAL shearY,
      IN MatrixOrder order = MatrixOrderPrepend)
{
   ...
   GdipShearMatrix(nativeMatrix, shearX, shearY, order);
   ...
}
```



The [**Matrix**](/windows/win32/api/gdiplusmatrix/nl-gdiplusmatrix-matrix) constructors pass the address of a **GpMatrix** pointer variable (as an output parameter) to the **GdipCreateMatrix(GpMatrix \*\*matrix)** function. **GdipCreateMatrix** creates and initializes an internal **GpMatrix** variable and then assigns the address of the **GpMatrix** to the pointer variable. Then the constructor copies the value of the pointer to the **nativeMatrix** field.


```
Matrix()
{
   GpMatrix *matrix = NULL;
   lastResult = DllExports::GdipCreateMatrix(&matrix);
   SetNativeMatrix(matrix);
}

VOID SetNativeMatrix(GpMatrix *nativeMatrix)
{
   this->nativeMatrix = nativeMatrix;
}
```



Clone methods in the wrapper classes receive no parameters but often pass two parameters to the underlying function in the GDI+ flat API. For example, the [**Matrix::Clone**](/windows/win32/api/Gdiplusmatrix/nf-gdiplusmatrix-matrix-clone) method passes **nativeMatrix** (as an input parameter) and the address of a **GpMatrix** pointer variable (as an output parameter) to the **GdipCloneMatrix** function. The following code shows how the **Matrix::Clone** method calls the **GdipCloneMatrix(GpMatrix \*matrix, GpMatrix \*\*cloneMatrix)** function.


```
Matrix *Clone() const
{
   GpMatrix *cloneMatrix = NULL;
   ...
   GdipCloneMatrix(nativeMatrix, &cloneMatrix));
   ...
   return new Matrix(cloneMatrix);
 }
```



The functions in the flat API return a value of type GpStatus. The GpStatus enumeration is identical to the [**Status**](/windows/win32/api/Gdiplustypes/ne-gdiplustypes-status) enumeration used by the wrapper methods. In GdiplusGpStubs.h, GpStatus is defined as follows:

`typedef Status GpStatus;`

Most of the methods in the wrapper classes return a status value that indicates whether the method succeeded. However, some of the wrapper methods return state values. When you call a wrapper method that returns a state value, the wrapper method passes the appropriate parameters to the underlying function in the GDI+ flat API. For example, the [**Matrix**](/windows/win32/api/gdiplusmatrix/nl-gdiplusmatrix-matrix) class has an [**Matrix::IsInvertible**](/windows/win32/api/Gdiplusmatrix/nf-gdiplusmatrix-matrix-isinvertible) method that passes the **nativeMatrix** field and and the address of a **BOOL** variable (as an output parameter) to the **GdipIsMatrixInvertible** function. The following code shows how the **Matrix::IsInvertible** method calls the **GdipIsMatrixInvertible(GDIPCONST GpMatrix \*matrix, BOOL \*result)** function.


```
BOOL IsInvertible() const
{
   BOOL result = FALSE;
   ...
   GdipIsMatrixInvertible(nativeMatrix, &result);
   return result;
}
```



Another one of the wrappers is the [**Color**](/windows/win32/api/gdipluscolor/nl-gdipluscolor-color) class. A **Color** object has a single field of type **ARGB**, which is defined as a **DWORD**. When you pass a **Color** object to one of the wrapper methods, that method passes the **ARGB** field along to the underlying function in the GDI+ flat API. The following code shows how the [**Pen::SetColor**](/windows/win32/api/Gdipluspen/nf-gdipluspen-pen-setcolor) method calls the **GdipSetPenColor(GpPen \*pen, ARGB argb)** function. The [**Color::GetValue**](/windows/win32/api/Gdipluscolor/nf-gdipluscolor-color-getvalue) method returns the value of the **ARGB** field.


```
Status SetColor(IN const Color& color)
{
   ...
   GdipSetPenColor(nativePen, color.GetValue());
}
```



The following topics show the relationship between the GDI+ flat API and the C++ wrapper methods.

-   [AdjustableArrowCap Functions](-gdiplus-adjustablearrowcap-flat.md)
-   [Bitmap Functions](-gdiplus-bitmap-flat.md)
-   [Brush Functions](-gdiplus-brush-flat.md)
-   [CachedBitmap Functions](-gdiplus-cachedbitmap-flat.md)
-   [CustomLineCap Functions](-gdiplus-customlinecap-flat.md)
-   [Font Functions](-gdiplus-font-flat.md)
-   [FontFamilyFunctions](-gdiplus-fontfamily-flat.md)
-   [Graphics Functions](-gdiplus-graphics-flat.md)
-   [GraphicsPath Functions](-gdiplus-graphicspath-flat.md)
-   [HatchBrush Functions](-gdiplus-hatchbrush-flat.md)
-   [Image Functions](-gdiplus-image-flat.md)
-   [ImageAttributes Functions](-gdiplus-imageattributes-flat.md)
-   [LinearGradientBrush Functions](-gdiplus-lineargradientbrush-flat.md)
-   [Matrix Functions](-gdiplus-matrix-flat.md)
-   [Memory Functions](-gdiplus-memory-flat.md)
-   [Notification Functions](-gdiplus-notification-flat.md)
-   [PathGradientBrush Functions](-gdiplus-pathgradientbrush-flat.md)
-   [PathIterator Functions](-gdiplus-pathiterator-flat.md)
-   [Pen Functions](-gdiplus-pen-flat.md)
-   [Region Functions](-gdiplus-region-flat.md)
-   [SolidBrush Functions](-gdiplus-solidbrush-flat.md)
-   [String Format Functions](-gdiplus-stringformat-flat.md)
-   [Text Functions](-gdiplus-text-flat.md)
-   [Texture Brush Functions](-gdiplus-texturebrush-flat.md)

 

 
