---
title: DirectComposition error codes
description: This section describes the error codes that are specific to DirectComposition.
ms.assetid: 8DFBFC34-DBD0-4731-8305-B33E90C96C54
topic_type:
- apiref
api_name:
- DCOMPOSITION_ERROR_ACCESS_DENIED
- DCOMPOSITION_ERROR_SURFACE_BEING_RENDERED
- DCOMPOSITION_ERROR_SURFACE_NOT_BEING_RENDERED
- DCOMPOSITION_ERROR_WINDOW_ALREADY_COMPOSED
api_location:
- Dcomp.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DirectComposition error codes

If an error occurs, Microsoft DirectComposition returns a code as an **HRESULT** value. This section describes the error codes that are specific to DirectComposition. For a list of general Component Object Model (COM) error codes, see [COM Error Codes](https://msdn.microsoft.com/library/windows/desktop/dd542642).

<dl> <dt>

<span id="DCOMPOSITION_ERROR_ACCESS_DENIED"></span><span id="dcomposition_error_access_denied"></span>**DCOMPOSITION\_ERROR\_ACCESS\_DENIED**
</dt> <dd> <dl> <dt>


</dt> <dt>



The window handle that was specified in a call to the [**IDCompositionDevice::CreateTargetForHwnd**](/windows/desktop/api/Dcomp/) method belongs to a different process from the one that created the device object.


</dt> </dl> </dd> <dt>

<span id="DCOMPOSITION_ERROR_SURFACE_BEING_RENDERED"></span><span id="dcomposition_error_surface_being_rendered"></span>**DCOMPOSITION\_ERROR\_SURFACE\_BEING\_RENDERED**
</dt> <dd> <dl> <dt>


</dt> <dt>



The surface was already being rendered when the application called the [**IDCompositionSurface::BeginDraw**](/windows/desktop/api/Dcomp/), [**IDCompositionSurface::SuspendDraw**](/windows/desktop/api/Dcomp/), or [**IDCompositionSurface::ResumeDraw**](/windows/desktop/api/Dcomp/) method. For more information, see Remarks.


</dt> </dl> </dd> <dt>

<span id="DCOMPOSITION_ERROR_SURFACE_NOT_BEING_RENDERED"></span><span id="dcomposition_error_surface_not_being_rendered"></span>**DCOMPOSITION\_ERROR\_SURFACE\_NOT\_BEING\_RENDERED**
</dt> <dd> <dl> <dt>


</dt> <dt>



The application called the [**IDCompositionSurface::SuspendDraw**](/windows/desktop/api/Dcomp/), [**IDCompositionSurface::ResumeDraw**](/windows/desktop/api/Dcomp/), or [**IDCompositionSurface::EndDraw**](/windows/desktop/api/Dcomp/) method for a surface that is not being rendered. For more information, see Remarks.


</dt> </dl> </dd> <dt>

<span id="DCOMPOSITION_ERROR_WINDOW_ALREADY_COMPOSED"></span><span id="dcomposition_error_window_already_composed"></span>**DCOMPOSITION\_ERROR\_WINDOW\_ALREADY\_COMPOSED**
</dt> <dd> <dl> <dt>


</dt> <dt>



The [**IDCompositionDevice::CreateTargetForHwnd**](/windows/desktop/api/Dcomp/) method was called with *hwnd* and *topmost* parameters for which a visual tree already exists.


</dt> </dl> </dd> </dl>

## Remarks

If a call to the [**IDCompositionSurface::BeginDraw**](/windows/desktop/api/Dcomp/) was the most recent action:



| Calling this method:                                    | Returns this value:                               |
|---------------------------------------------------------|---------------------------------------------------|
| [**BeginDraw**](/windows/desktop/api/Dcomp/)     | **DCOMPOSITION\_ERROR\_SURFACE\_BEING\_RENDERED** |
| [**EndDraw**](/windows/desktop/api/Dcomp/)         | S\_OK                                             |
| [**SuspendDraw**](/windows/desktop/api/Dcomp/) | S\_OK                                             |
| [**ResumeDraw**](/windows/desktop/api/Dcomp/)   | **DCOMPOSITION\_ERROR\_SURFACE\_BEING\_RENDERED** |



 

If a call to the [**IDCompositionSurface::SuspendDraw**](/windows/desktop/api/Dcomp/) was the most recent action:



| Calling this method:                                    | Returns this value:                               |
|---------------------------------------------------------|---------------------------------------------------|
| [**BeginDraw**](/windows/desktop/api/Dcomp/)     | **DCOMPOSITION\_ERROR\_SURFACE\_BEING\_RENDERED** |
| [**EndDraw**](/windows/desktop/api/Dcomp/)         | S\_OK                                             |
| [**SuspendDraw**](/windows/desktop/api/Dcomp/) | **DCOMPOSITION\_ERROR\_SURFACE\_BEING\_RENDERED** |
| [**ResumeDraw**](/windows/desktop/api/Dcomp/)   | S\_OK                                             |



 

If a call to the [**IDCompositionSurface::ResumeDraw**](/windows/desktop/api/Dcomp/) was the most recent action:



| Calling this method:                                    | Returns this value:                                |
|---------------------------------------------------------|----------------------------------------------------|
| [**BeginDraw**](/windows/desktop/api/Dcomp/)     | **DCOMPOSITION\_ERROR\_SURFACE\_BEING\_RENDERED**  |
| [**EndDraw**](/windows/desktop/api/Dcomp/)         | S\_OK                                              |
| [**SuspendDraw**](/windows/desktop/api/Dcomp/) | S\_OK                                              |
| [**ResumeDraw**](/windows/desktop/api/Dcomp/)   | **DCOMPOSITION\_ERROR\_SURFACE\_BEING\_RENDERED.** |



 

If a call to the [**IDCompositionSurface::EndDraw**](/windows/desktop/api/Dcomp/) was the most recent action:



| Calling this method:                                    | Returns this value:                                     |
|---------------------------------------------------------|---------------------------------------------------------|
| [**BeginDraw**](/windows/desktop/api/Dcomp/)     | S\_OK                                                   |
| [**EndDraw**](/windows/desktop/api/Dcomp/)         | **DCOMPOSITION\_ERROR\_SURFACE\_NOT\_BEING\_RENDERED.** |
| [**SuspendDraw**](/windows/desktop/api/Dcomp/) | **DCOMPOSITION\_ERROR\_SURFACE\_NOT\_BEING\_RENDERED.** |
| [**ResumeDraw**](/windows/desktop/api/Dcomp/)   | **DCOMPOSITION\_ERROR\_SURFACE\_NOT\_BEING\_RENDERED.** |



 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Dcomp.h</dt> </dl> |



## See also

<dl> <dt>

[DirectComposition Reference](reference.md)
</dt> </dl>

 

 





