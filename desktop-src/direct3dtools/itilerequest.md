---
description: Request for a tiled texture to be written as a DDS file.
MS-HAID: vspixengine.ITileRequest
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: ITileRequest interface
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: DBA493E7-EBB6-490D-BDC6-946265A474D6
api_name: 
 - ITileRequest
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.itilerequest"></span>ITileRequest interface

Request for a tiled texture to be written as a DDS file.

## Members

The **ITileRequest** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITileRequest** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **ITileRequest** interface has these methods.

<table><colgroup><col  /><col  /></colgroup><thead><tr class="header"><th >Method</th><th >Description</th></tr></thead><tbody><tr class="odd"><td ><a href="/windows/desktop/direct3dtools/itilerequest-requestbuffertileasync-eventid-dword-bstr-uint-ibufferobjectdatacallback-ptr-dword-dword"><strong>RequestBufferTileAsync</strong></a></td><td ><p>Requests to get the raw contents of a tile.</p></td></tr><tr class="even"><td ><a href="/windows/desktop/direct3dtools/itilerequest-requesttexturetileasync-eventid-dword-uint-uint-uint-uint-bstr-itexturecallback-ptr-dword-dword"><strong>RequestTextureTileAsync</strong></a></td><td ><p>Requests to get the contents of a tiled texture as a .DDS (DirectDraw Surface) file.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 
