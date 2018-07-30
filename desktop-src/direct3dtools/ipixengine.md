---
Description: Original interface for communicating data about a vsglog .
MS-HAID: vspixengine.IPixEngine
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.ipixengine"></span>IPixEngine interface

Original interface for communicating data about a vsglog .

## Members

The **IPixEngine** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IPixEngine** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPixEngine** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;">[<strong>OpenFile</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432779)</td><td style="text-align: left;"><p>Opens a graphics log.</p></td></tr><tr class="even"><td style="text-align: left;">[<strong>RunExperiment</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432780)</td><td style="text-align: left;"><p>Runs an experiment.</p></td></tr><tr class="odd"><td style="text-align: left;">[<strong>SaveFile</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432781)</td><td style="text-align: left;"><p>Saves the graphics log to the specified location.</p></td></tr><tr class="even"><td style="text-align: left;">[<strong>SetParentProcess</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432782)</td><td style="text-align: left;"><p>Not used.</p></td></tr><tr class="odd"><td style="text-align: left;">[<strong>ShutDown</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432783)</td><td style="text-align: left;"><p>Shuts down the engine.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



