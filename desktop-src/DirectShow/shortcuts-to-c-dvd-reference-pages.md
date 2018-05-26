---
Description: Shortcuts to C++ DVD Reference Pages
ms.assetid: b37337b7-b3be-4f49-b350-df5e3c88e3cf
title: Shortcuts to C++ DVD Reference Pages
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Shortcuts to C++ DVD Reference Pages

The following interfaces are those typically used when writing a DVD application in C++.



| Interface                                    | Purpose                                                                                          |
|----------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**IAMLine21Decoder**](/windows/win32/il21dec/nn-il21dec-iamline21decoder?branch=master) | Controls closed captioning display.                                                              |
| [**IDvdCmd**](/windows/win32/Strmif/nn-strmif-idvdcmd?branch=master)                   | Used in advanced command synchronization techniques to control a command object.                 |
| [**IDvdControl2**](/windows/win32/Strmif/nn-strmif-idvdcontrol2?branch=master)         | Issues commands to the [DVD Navigator](dvd-navigator-filter.md) filter (the "set" methods).     |
| [**IDvdGraphBuilder**](/windows/win32/Strmif/nn-strmif-idvdgraphbuilder?branch=master) | Creates the DVD filter graph.                                                                    |
| [**IDvdInfo2**](/windows/win32/Strmif/nn-strmif-idvdinfo2?branch=master)               | Queries the DVD Navigator for state information and information on the disc (the "get" methods). |
| [**IDvdState**](/windows/win32/Strmif/nn-strmif-idvdstate?branch=master)               | Saves information, such as bookmarks, to disc.                                                   |
| [**IVideoFrameStep**](/windows/win32/Strmif/nn-strmif-ivideoframestep?branch=master)   | Controls "frame stepping" if the decoder supports it.                                            |



 

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



