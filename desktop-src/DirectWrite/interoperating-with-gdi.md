---
title: Interoperating with GDI
description: DirectWrite provides a migration path from, and some interoperability with, GDI's font model, as well as interfaces for rendering text to a bitmap that can then be drawn on a window.
ms.assetid: fb73e07b-60fb-4726-bd5b-c14d61ace186
keywords:
- DirectWrite,GDI interoperation
- DirectWrite,interoperability
- interoperability
- Graphics Device Interface (GDI)
- GDI (Graphics Device Interface)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Interoperating with GDI

[DirectWrite](direct-write-portal.md) provides a migration path from, and some interoperability with, GDI's font model, as well as interfaces for rendering text to a bitmap that can then be drawn on a window.

This overview contains the following parts:

-   [Introduction](#introduction)
-   [Part 1: IDWriteGdiInterop](#part-1-idwritegdiinterop)
-   [Part 2: Font Objects](#part-2-font-objects)
-   [Part 3: Rendering](#part-3-rendering)

## Introduction

[DirectWrite](direct-write-portal.md) provides methods for converting between GDI's LOGFONT structure and DirectWrite font interfaces. This allows you to use GDI for some or all of the font enumeration and selection, while taking advantage of the improved functionality and performance of DirectWrite. DirectWrite also has interfaces for rendering to a bitmap if you want to display text on a GDI surface.

## Part 1: IDWriteGdiInterop

The [**IDWriteGdiInterop**](https://msdn.microsoft.com/en-us/library/Dd371172(v=VS.85).aspx) interface is used to convert between GDI font structures and [DirectWrite](direct-write-portal.md) font interfaces, and also to create an [**IDWriteBitmapRenderTarget**](https://msdn.microsoft.com/en-us/library/Dd368165(v=VS.85).aspx) object. Get an **IDWriteGdiInterop** object by using the [**IDWriteFactory::GetGdiInterop**](https://msdn.microsoft.com/en-us/library/Dd368207(v=VS.85).aspx) method, as shown in the following code.


```C++
// Create a GDI interop interface.
if (SUCCEEDED(hr))
{
    hr = g_pDWriteFactory->GetGdiInterop(&amp;g_pGdiInterop);
}
```



## Part 2: Font Objects

GDI uses the LOGFONT structure to store information about the font and style of text. The [**IDWriteGdiInterop::CreateFontFromLOGFONT**](https://msdn.microsoft.com/en-us/library/Dd371187(v=VS.85).aspx) method will convert a LOGFONT structure to an [**IDWriteFont**](https://msdn.microsoft.com/en-us/library/Dd368213(v=VS.85).aspx) object, as seen in the following code.


```C++
// Convert to a DirectWrite font.
if (SUCCEEDED(hr))
{
    hr = g_pGdiInterop->CreateFontFromLOGFONT(&amp;lf, &amp;pFont);
}
```



However, [**IDWriteFont**](https://msdn.microsoft.com/en-us/library/Dd368213(v=VS.85).aspx) does not encapsulate all of the same information that a LOGFONT does. A LOGFONT structure contains the font size, weight, style, underline, strikeout, font face name, and some other information. **IDWriteFont** objects contain information about a font and its weight and style, but not the font size, underline, and so on. With [DirectWrite](direct-write-portal.md), formatting information elements such as these are encapsulated by an [**IDWriteTextFormat**](https://msdn.microsoft.com/en-us/library/Dd316628(v=VS.85).aspx) object or, for specific ranges of text, an [**IDWriteTextLayout**](https://msdn.microsoft.com/en-us/library/Dd316718(v=VS.85).aspx) object.

You do have the option to convert a [**IDWriteFont**](https://msdn.microsoft.com/en-us/library/Dd368213(v=VS.85).aspx) to a LOGFONT by using the [**IDWriteGdiInterop::ConvertFontToLOGFONT**](https://msdn.microsoft.com/en-us/library/Dd371177(v=VS.85).aspx).

## Part 3: Rendering

To render DirectWrite text to a GDI surface you use a custom text renderer. See the [Render to a GDI Surface](render-to-a-gdi-surface.md) topic.

 

 




