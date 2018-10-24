---
Description: Extensions to the original IPixEngine interface.
MS-HAID: vspixengine.IPixEngine2
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine2 interface
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.ipixengine2"></span>IPixEngine2 interface

Extensions to the original IPixEngine interface.

## Members

The **IPixEngine2** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IPixEngine2** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPixEngine2** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432747"><strong>EndExperiment</strong></a></td><td style="text-align: left;"><p>Ends the experiement and completes the graphics log.</p></td></tr><tr class="even"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432748"><strong>GetPlaybackMachine</strong></a></td><td style="text-align: left;"><p>Gets information about the current playback machine.</p></td></tr><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432749"><strong>OnNewDataAvailable</strong></a></td><td style="text-align: left;"><p>Requests to indicate that the graphics log has new data inside of it.</p></td></tr><tr class="even"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432750"><strong>SetPlaybackMachine</strong></a></td><td style="text-align: left;"><p>Sets the current playback machine for the specified graphics log.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



