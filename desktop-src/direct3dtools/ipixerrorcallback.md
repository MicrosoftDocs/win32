---
Description: Callback from engine to handle errors.
MS-HAID: vspixengine.IPixErrorCallback
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixErrorCallback interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.ipixerrorcallback"></span>IPixErrorCallback interface

Callback from engine to handle errors.

## Members

The **IPixErrorCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IPixErrorCallback** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPixErrorCallback** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432785"><strong>ErrorListCallback</strong></a></td><td style="text-align: left;"><p>A callback that notifies the host of errors returned by the associated request.</p></td></tr><tr class="even"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432786"><strong>MessagesCallback</strong></a></td><td style="text-align: left;"><p>A callback that notifies the host of messages returned by the associated request.</p></td></tr><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432787"><strong>WarningListCallback</strong></a></td><td style="text-align: left;"><p>A callback that notifies the host of warnings returned by the associated request.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



