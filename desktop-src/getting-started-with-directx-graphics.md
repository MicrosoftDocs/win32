---
Description: .
ms.assetid: 49E0D0C2-E6EC-4849-A44F-36FDEFBB9838
title: Getting Started with DirectX Graphics
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting Started with DirectX Graphics

Microsoft DirectX graphics provides a set of APIs that you can use to create games and other high-performance multimedia applications. DirectX graphics includes support for high-performance 2-D and 3-D graphics.

For 3-D graphics, use the Microsoft Direct3D 11 API. Even if you have Microsoft Direct3D 9-level or Microsoft Direct3D 10-level hardware, you can use the Direct3D 11 API and target a [feature level](https://msdn.microsoft.com/5ad0525c-249f-452d-950b-df8fa2addde2) 9\_x or feature level 10\_x device. For info about how to develop 3-D graphics with DirectX, see [An introduction to 3-D graphics with DirectX](https://msdn.microsoft.com/C7A96F26-620F-41E9-BEFD-BD8C3BE055FB).

For 2-D graphics and text, use Direct2D and [DirectWrite](https://msdn.microsoft.com/62a8d723-ae1c-4cbc-a9da-3177e80d4a3a) rather than Windows Graphics Device Interface (GDI).

To compose bitmaps that Direct3D 11 or Direct2D populated, use [DirectComposition](https://msdn.microsoft.com/40e2d02b-77e8-425f-ac5e-3dcddef08173).

To learn about how to create a Windows Store app that uses DirectX, see [Create your first Windows Store app using DirectX](1F023B01-41CD-4D8C-9C0F-9E06C5C0861A). You can use the [**Windows.UI::Xaml::Controls::SwapChainPanel**](https://msdn.microsoft.com/Windows.UI.Xaml.Controls.SwapChainPanel) class to create high-performance DirectX apps with a XAML UI overlay. For more info about combining XAML and DirectX in a Windows Store app, see [DirectX and XAML interop](https://msdn.microsoft.com/17987EEA-6771-423C-9B68-6B9AEADC7B7F).

To learn about how to build a display driver for Windows 8, see [Roadmap for Developing Drivers for the Windows Vista Display Driver Model (WDDM)](https://www.bing.com/search?q=Roadmap+for+Developing+Drivers+for+the+Windows+Vista+Display+Driver+Model+(WDDM)).

If you need the documentation for previous DirectX versions, see [Classic DirectX Graphics](https://www.bing.com/search?q=Classic+DirectX+Graphics).

 

 



