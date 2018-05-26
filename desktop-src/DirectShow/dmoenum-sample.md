---
Description: DMOEnum Sample
ms.assetid: afd7853e-b0ab-42f6-8c2e-c2b0b40d989b
title: DMOEnum Sample
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DMOEnum Sample

## Description

This sample application enumerates all of the [DirectX Media Objects](directx-media-objects.md) (DMOs) registered in the user's system, and displays information about them.

The sample uses the [**DMOEnum**](/windows/win32/Dmoreg/nf-dmoreg-dmoenum?branch=master) function and the [**IEnumDMO**](/windows/win32/Mediaobj/nn-mediaobj-ienumdmo?branch=master) interface to enumerate the DMOs. It uses the [**IMediaObject**](/windows/win32/Mediaobj/nn-mediaobj-imediaobject?branch=master) interface and other DMO interfaces to retrieve information about each DMO.

## Usage

When the application launches, it enumerates all of the installed DMOs. If you select a specific DMO category, the application displays only the DMOs in that category. To view information about a DMO, select the DMO from the list. The application displays the number of streams, the preferred media types, the DLL server for that DMO, and other information about the DMO. To include or exclude keyed DMOs, toggle the **Include Keyed DMOs?** checkbox.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](http://go.microsoft.com/fwlink/p/?linkid=129787).

This sample is installed under the following path: *\[SDK Root\]*\\Samples\\Multimedia\\DirectShow\\Misc\\DMOEnum.

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 



