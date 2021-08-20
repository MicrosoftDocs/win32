---
description: Request for returning the list of events in a frame.
MS-HAID: vspixengine.IFrameEventsRequest
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IFrameEventsRequest interface
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: E171A94C-012F-4296-B1EC-2E814F977565
api_name: 
 - IFrameEventsRequest
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.iframeeventsrequest"></span>IFrameEventsRequest interface

Request for returning the list of events in a frame.

## Members

The **IFrameEventsRequest** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IFrameEventsRequest** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IFrameEventsRequest** interface has these methods.

<table><colgroup><col  /><col  /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;"><a href="/windows/desktop/direct3dtools/iframeeventsrequest-requestasync-dword-dword-dword-arr-iframeeventscallback-ptr-dword-dword"><strong>RequestAsync</strong></a></td><td style="text-align: left;"><p>An asynchronous request to get specified information about a single specified frame.</p></td></tr><tr class="even"><td style="text-align: left;"><a href="/windows/desktop/direct3dtools/iframeeventsrequest-requestsupportedcolumnsasync-iframeeventscallback-ptr-dword"><strong>RequestSupportedColumnsAsync</strong></a></td><td style="text-align: left;"><p>An asynchronous request to get information about what columns (fields) this frame events request type supports.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 
