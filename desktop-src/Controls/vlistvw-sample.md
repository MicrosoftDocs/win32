---
title: VListVW Sample
ms.assetid: 5e1d13a6-ae11-4729-b0fc-0a1620cf0738
description: "Learn more about: VListVW Sample"
ms.topic: article
ms.date: 05/31/2018
---

# VListVW Sample

This topic describes the VListVW Sample code sample. It contains the following sections:

-   [Description](#description)
-   [Minimum Requirements](#minimum-requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Related topics](#related-topics)

## Description

The VListVW Sample shows how to implement a simple virtual list-view control in an application. A virtual list-view control is a standard list-view control with the **LVS\_OWNERDATA** style. This example creates a list-view control that "virtually" holds 100,000 items. The items are never actually added. Instead, the virtual list-view control is "told" how many items it contains with the [**LVM\_SETITEMCOUNT**](lvm-setitemcount.md) message. When an item needs to be drawn, the list-view control queries the parent window for display information with the [LVN\_GETDISPINFO](lvn-getdispinfo.md) notification.

## Minimum Requirements



| Product          | Version                               |
|------------------|---------------------------------------|
| DLL              | comctl32.dll version 4.70             |
| Operating System | Windows 95, Microsoft Windows NT 3.51 |



 

## Downloading the Sample

The VListVW Sample is available on on github in the [Windows Classic Samples repository](https://github.com/microsoft/Windows-classic-samples). The list view control items examples can be found at [here](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/controls/common/vlistvw)

 

## Building the Sample

To build the sample using the command prompt:

1.  Open the Command Prompt window and navigate to the project directory.
2.  Enter `msbuild [project file]`.

To build the sample using Visual Studio:

1.  Open Windows Explorer and navigate to the project directory.
2.  Double-click the icon for the .vcproj file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution** to build the solution.

## Related topics

<dl> <dt>

[About List-View Controls](list-view-controls-overview.md)
</dt> </dl>

 

 




