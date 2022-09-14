---
title: CustomAccServer Sample
description: CustomAccServer Sample
ms.assetid: 8c3636ef-0993-4ded-a3c0-05cf2de777bb
ms.topic: article
ms.date: 05/31/2018
---

# CustomAccServer Sample

This topic contains the following sections.

-   [Description](#description)
-   [Download Information](#download-information)
-   [Minimum Requirements](#minimum-requirements)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Related topics](#related-topics)

## Description

This sample shows how to implement a Microsoft Active Accessibility server for a simple custom control. The accessible object for the control consists of the root element (a list box) and its children (the list items.)

## Download Information

The CustomAccServer sample is installed as part of the [Microsoft Windows Software Development Kit (SDK)](https://msdn.microsoft.com/windowsvista/bb980924.aspx) and is available in the following location.



| Location    | Path/URL                                                                           |
|-------------|------------------------------------------------------------------------------------|
| Windows SDK | %Program Files%\\Microsoft SDKs\\Windows\\\[version number\]\\Samples\\winui\\msaa |



 

## Minimum Requirements



| Product          | Version                         |
|------------------|---------------------------------|
| Operating System | Windows XP, Windows Server 2003 |
| Windows SDK      | 7.0                             |
| Visual Studio    | 2008                            |



 

## Building the Sample

To build the sample using Visual Studio 2008:

1.  Run the Microsoft Windows Software Development Kit (SDK) Configuration Tool provided with the SDK to add SDK include directories to Visual Studio.
2.  Open Windows Explorer and navigate to the project directory.
3.  Double-click the icon for the .sln (solution) file to open the project in Visual Studio.
4.  On the **Build** menu, select **Build Solution** to build the solution. The application will be built in the default \\Debug or \\Release directory.

To build the sample from the command line, see Building Samples in the Windows SDK release notes at the following location: %Program Files%\\Microsoft SDKs\\Windows\\v7.0\\ReleaseNotes.htm

## Running the Sample

To run the sample:

1.  Navigate to the directory that contains the new executable, using the command prompt or Windows Explorer.
2.  Type AccServer.exe at the command line, or double-click the icon for AccServer.exe to launch it from Windows Explorer.

To run from Visual Studio, press F5 or click **Start Debugging** from the **Debug** menu.

## Related topics

<dl> <dt>

[Samples](samples.md)
</dt> </dl>

 

 




