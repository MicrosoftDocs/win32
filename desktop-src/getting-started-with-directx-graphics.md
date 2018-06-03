---
Description: '.'
ms.assetid: '49E0D0C2-E6EC-4849-A44F-36FDEFBB9838'
title: Getting Started with DirectX Graphics
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting Started with DirectX Graphics

Microsoft DirectX graphics provides a set of APIs that you can use to create games and other high-performance multimedia applications. DirectX graphics includes support for high-performance 2-D and 3-D graphics.

For 3-D graphics, use the Microsoft Direct3D 11 API. Even if you have Microsoft Direct3D 9-level or Microsoft Direct3D 10-level hardware, you can use the Direct3D 11 API and target a [feature level](direct3d11.overviews_direct3d_11_devices_downlevel_intro#overview) 9\_x or feature level 10\_x device. For info about how to develop 3-D graphics with DirectX, see [An introduction to 3-D graphics with DirectX](m_gamedev.an_introduction_to_3d_graphics_with_directx).

For 2-D graphics and text, use Direct2D and [DirectWrite](directwrite.direct_write_portal) rather than Windows Graphics Device Interface (GDI).

To compose bitmaps that Direct3D 11 or Direct2D populated, use [DirectComposition](directcomp.directcomposition_portal).

To learn about how to create a Windows Store app that uses DirectX, see [Create your first Windows Store app using DirectX](m_getstarted.building_your_first_directx_app). You can use the [**Windows.UI::Xaml::Controls::SwapChainPanel**](w_ui_xaml_ctrl.swapchainpanel) class to create high-performance DirectX apps with a XAML UI overlay. For more info about combining XAML and DirectX in a Windows Store app, see [DirectX and XAML interop](m_ca_coreui.directx_and_xaml_interop).

To learn about how to build a display driver for Windows 8, see [Roadmap for Developing Drivers for the Windows Vista Display Driver Model (WDDM)](display.roadmap_for_developing_drivers_for_the_windows_vista_display_driver_mo).

If you need the documentation for previous DirectX versions, see [Classic DirectX Graphics](classic-directx-graphics.md).

 

 



