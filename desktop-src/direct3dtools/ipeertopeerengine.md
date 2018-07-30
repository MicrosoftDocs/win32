---
Description: Interface for remote communicating data about a vsglog.
MS-HAID: vspixengine.IPeerToPeerEngine
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPeerToPeerEngine interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.ipeertopeerengine"></span>IPeerToPeerEngine interface

Interface for remote communicating data about a vsglog.

## Members

The **IPeerToPeerEngine** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IPeerToPeerEngine** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPeerToPeerEngine** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;">[<strong>CancelSetPlaybackEndpoint</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432713)</td><td style="text-align: left;"><p>Cancels a previous request to set up a remote connection.</p></td></tr><tr class="even"><td style="text-align: left;">[<strong>GetPlaybackEndpoint</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432714)</td><td style="text-align: left;"><p>Gets the endpoint address of a remote engine.</p></td></tr><tr class="odd"><td style="text-align: left;">[<strong>SetPlaybackEndpoint</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432715)</td><td style="text-align: left;"><p>Sets the endpoint address used to connect to a remote engine.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



