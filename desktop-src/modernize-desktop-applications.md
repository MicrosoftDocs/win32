---
Description: Add modern XAML user interfaces, create MSIX packages, and incorporate other modern components into your desktop application in an "alacart" fashion.
title: Desktop guide to the modern platform
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 08/21/2018
---

# Desktop guide to the modern platform

* The modern platform is being made available as stand-alone building blocks that you can adopt in your desktop applications ala cart without having to completely rewrite applications in UWP.

* Enhance existing investments in-place. No re-write required. No need to learn a whole new stack to modernize.

* Choose which stack to invest in (modern front-ends, MSIX deployment + opt-into security level, UWP APIs etc.).

## Modern application delivery with MSIX

MSIX is a new containerization package format that applies to all Windows applications including Win32, Windows Forms, WPF, and UWP. This new format inherits great features from UWP:

* Robust installation and updating.

* Managed security model with a flexible capability system.

* Support for the Microsoft Store, enterprise management, and many custom distribution models.

  Link to comprehensive topic about MSIX, it's benefits such as multilingual aware, network optimization, resource packages, automatic updates, etc. This topic not the right place to lay all of that out. Ownership of MSIX all up conceptual needs to be assigned.

* Use DAC or command-line. Visual Studio support coming.

* If you've got apps without source code, use IT Pro tool. Link to tool.

## User interfaces optimized for high DPI displays

* Update .NET Framework version to .NET 4.7 or .NET Core 3 and Windows Forms UIs render pixel perfect on high res laptops and displays.

* Not sure about WPF or Win32.

## Modern user interfaces with the Fluent design system

* Add Fluent UIs to a desktop application by using XAML Islands.

* For Windows Forms and WPF applications, use the XAML Island host control or any of the XAML Island wrapped controls.

* For Win32 applications, use the XAML Island API.

### XAML Island host control

>[!NOTE]
>This feature is in preview only.

* Host control is convenient way to add a XAML Island to Windows Forms and WPF apps.

  * Show simple example with screenshot.

  * Link to our XAML islands doc.

  * Link to host control doc on Community Toolkit Page.

### XAML Island wrapped controls

>[!NOTE]
>This feature is in preview only.

* Wrapped controls that you can use directly on design surfaces.

* Complete list going out with next refresh of the Toolkit is currently TBD.

#### WebView

* Code snippet of XAML Island assigned to WebView.

* Screenshot of WebView in win32 application.

* Link to WebView doc.

#### InkCanvas

* Code snippet of XAML Island assigned to WebView.

* Screenshot of WebView in win32 application.

* Link to WebView doc.

#### InkToolbar

* Code snippet of XAML Island assigned to WebView.

* Screenshot of WebView in win32 application.

* Link to WebView doc.

#### MediaPlayerElement

* Code snippet of XAML Island assigned to WebView.

* Screenshot of WebView in win32 application.

* Link to WebView doc.

#### WebViewCompatible

* Code snippet of XAML Island assigned to WebView.

* Screenshot of WebView in win32 application.

* Link to WebView doc.

### XAML Island API

>[!NOTE]
>This feature is in preview only.

* Win32 API for Win32 apps.

  * Show simple example with screenshot.

  * Link to code-first sample.

  * Link to Win32 API doc that McLean wrote.

### Fluent controls

* Add any Fluent control to your XAML Islands.

  * Link to Fluent controls in UWP content.

* There's several new desktop-grade controls available with Fluent.

* These controls render as expected on large desktop screens.

#### MenuBar

Code snippet of XAML Island assigned to MenuBar.
Screenshot of MenuBar in win32 application.

#### DropDownButton

Code snippet of XAML Island assigned to DropDownButton.
Screenshot of DropDownButton in win32 application.

#### SplitButtonMenuBar

Code snippet of XAML Island assigned to SplitButtonMenuBar.
Screenshot of SplitButtonMenuBar in win32 application.

#### CommandBarFlyout

Code snippet of XAML Island assigned to CommandBarFlyout.
Screenshot of CommandBarFlyout in win32 application.

#### EditableComboBox

Code snippet of XAML Island assigned to EditableComboBox.
Screenshot of EditableComboBox in win32 application.

#### DataGridView

Code snippet of XAML Island assigned to DataGridView.
Screenshot of DataGridView in win32 application.

### Win UI

* Value prop and example.

## Modern features with WinRT APIs

* Some sort of stake in the ground that clarifies that desktop applications have access to UWP APIs.

* Link to topic about adding references and using UWP APIs.

## Other Interesting technologies

* .NET Core 3
* Graph
* Sets
* Adaptive Cards
