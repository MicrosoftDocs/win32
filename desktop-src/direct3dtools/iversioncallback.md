---
description: Callback to return the versions of all the interfaces supported. This allows the consumer to be out of sync with the capture engine.
MS-HAID: vspixengine.IVersionCallback
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IVersionCallback interface
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 7135E175-C537-4B0C-8F0A-CB77E3F2D945
api_name: 
 - IVersionCallback
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.iversioncallback"></span>IVersionCallback interface

Callback to return the versions of all the interfaces supported. This allows the consumer to be out of sync with the capture engine.

## Members

The **IVersionCallback** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IVersionCallback** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IVersionCallback** interface has these methods.

<table><colgroup><col  /><col  /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;"><a href="/windows/desktop/direct3dtools/iversioncallback-versiontableready-guid-arr-uint"><strong>VersionTableReady</strong></a></td><td style="text-align: left;"><p>A callback function used to notify the host of which interfaces are supported.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 
