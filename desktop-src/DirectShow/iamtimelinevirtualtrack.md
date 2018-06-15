---
Description: The IAMTimelineVirtualTrack interface provides methods for working with virtual tracks in DirectShow Editing Services (DES). Compositions and tracks support this interface.
ms.assetid: 69d1d2ea-d33f-406d-a9ca-ddfb890bed34
title: IAMTimelineVirtualTrack interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IAMTimelineVirtualTrack interface

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IAMTimelineVirtualTrack` interface provides methods for working with virtual tracks in [DirectShow Editing Services](directshow-editing-services.md) (DES). Compositions and tracks support this interface.

## Members

The **IAMTimelineVirtualTrack** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) interface. **IAMTimelineVirtualTrack** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMTimelineVirtualTrack** interface has these methods.



| Method                                                               | Description                                       |
|:---------------------------------------------------------------------|:--------------------------------------------------|
| [**SetTrackDirty**](iamtimelinevirtualtrack-settrackdirty.md)       | Not supported.<br/>                         |
| [**TrackGetPriority**](iamtimelinevirtualtrack-trackgetpriority.md) | Retrieves the object's priority level.<br/> |



 

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](http://go.microsoft.com/fwlink/p/?linkid=129787). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



 

 




