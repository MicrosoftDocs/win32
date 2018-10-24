---
Description: .
ms.assetid: 49E0D0C2-E6EC-4849-A44F-36FDEFBB9838
title: Getting Started with DirectX Graphics
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting Started with DirectX Graphics

Microsoft DirectX graphics provides a set of APIs that you can use to create games and other high-performance multimedia applications. DirectX graphics includes support for high-performance 2-D and 3-D graphics.

For 3-D graphics, use the Microsoft Direct3D 11 API. Even if you have Microsoft Direct3D 9-level or Microsoft Direct3D 10-level hardware, you can use the Direct3D 11 API and target a [feature level](https://msdn.microsoft.com/en-us/library/Ff476876(v=VS.85).aspx) 9\_x or feature level 10\_x device. For info about how to develop 3-D graphics with DirectX, see [An introduction to 3-D graphics with DirectX](https://msdn.microsoft.com/en-us/library/Hh465137(v=Win.10).aspx).

For 2-D graphics and text, use Direct2D and [DirectWrite](https://msdn.microsoft.com/en-us/library/Dd368038(v=VS.85).aspx) rather than Windows Graphics Device Interface (GDI).

To compose bitmaps that Direct3D 11 or Direct2D populated, use [DirectComposition](https://msdn.microsoft.com/en-us/library/Hh437371(v=VS.85).aspx).

To learn about how to create a Windows Store app that uses DirectX, see [Create your first Windows Store app using DirectX](https://msdn.microsoft.com/en-us/library/BR229580(v=Win.10).aspx). You can use the [**Windows.UI::Xaml::Controls::SwapChainPanel**](https://msdn.microsoft.com/en-us/library/Dn252834(v=WIN.10).aspx) class to create high-performance DirectX apps with a XAML UI overlay. For more info about combining XAML and DirectX in a Windows Store app, see [DirectX and XAML interop](https://msdn.microsoft.com/en-us/library/Hh825871(v=WIN.10).aspx).

To learn about how to build a display driver for Windows 8, see [Roadmap for Developing Drivers for the Windows Vista Display Driver Model (WDDM)](https://msdn.microsoft.com/library/Ff569513(v=VS.85).aspx).

If you need the documentation for previous DirectX versions, see [Classic DirectX Graphics](https://msdn.microsoft.com/en-us/library/Hh309465(v=VS.85).aspx).

 

 



