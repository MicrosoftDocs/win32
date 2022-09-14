---
description: Shortcuts to C++ DVD Reference Pages
ms.assetid: b37337b7-b3be-4f49-b350-df5e3c88e3cf
title: Shortcuts to C++ DVD Reference Pages
ms.topic: article
ms.date: 05/31/2018
---

# Shortcuts to C++ DVD Reference Pages

The following interfaces are those typically used when writing a DVD application in C++.



| Interface                                    | Purpose                                                                                          |
|----------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**IAMLine21Decoder**](/previous-versions/windows/desktop/api/il21dec/nn-il21dec-iamline21decoder) | Controls closed captioning display.                                                              |
| [**IDvdCmd**](/windows/desktop/api/Strmif/nn-strmif-idvdcmd)                   | Used in advanced command synchronization techniques to control a command object.                 |
| [**IDvdControl2**](/windows/desktop/api/Strmif/nn-strmif-idvdcontrol2)         | Issues commands to the [DVD Navigator](dvd-navigator-filter.md) filter (the "set" methods).     |
| [**IDvdGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-idvdgraphbuilder) | Creates the DVD filter graph.                                                                    |
| [**IDvdInfo2**](/windows/desktop/api/Strmif/nn-strmif-idvdinfo2)               | Queries the DVD Navigator for state information and information on the disc (the "get" methods). |
| [**IDvdState**](/windows/desktop/api/Strmif/nn-strmif-idvdstate)               | Saves information, such as bookmarks, to disc.                                                   |
| [**IVideoFrameStep**](/windows/desktop/api/Strmif/nn-strmif-ivideoframestep)   | Controls "frame stepping" if the decoder supports it.                                            |



 

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



