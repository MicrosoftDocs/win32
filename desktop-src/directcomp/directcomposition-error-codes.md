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
ms.topic: article
ms.date: 05/31/2018
---

# DirectComposition error codes

If an error occurs, Microsoft DirectComposition returns a code as an **HRESULT** value. This section describes the error codes that are specific to DirectComposition. For a list of general Component Object Model (COM) error codes, see [COM Error Codes](https://msdn.microsoft.com/library/windows/desktop/dd542642).

<dl> <dt>

<span id="DCOMPOSITION_ERROR_ACCESS_DENIED"></span><span id="dcomposition_error_access_denied"></span>**DCOMPOSITION\_ERROR\_ACCESS\_DENIED**
</dt> <dd> <dl> <dt>


</dt> <dt>



The window handle that was specified in a call to the [**IDCompositionDevice::CreateTargetForHwnd**](https://msdn.microsoft.com/en-us/library/Hh437396(v=VS.85).aspx) method belongs to a different process from the one that created the device object.


</dt> </dl> </dd> <dt>

<span id="DCOMPOSITION_ERROR_SURFACE_BEING_RENDERED"></span><span id="dcomposition_error_surface_being_rendered"></span>**DCOMPOSITION\_ERROR\_SURFACE\_BEING\_RENDERED**
</dt> <dd> <dl> <dt>


</dt> <dt>



The surface was already being rendered when the application called the [**IDCompositionSurface::BeginDraw**](https://msdn.microsoft.com/en-us/library/Hh449100(v=VS.85).aspx), [**IDCompositionSurface::SuspendDraw**](https://msdn.microsoft.com/en-us/library/Hh449106(v=VS.85).aspx), or [**IDCompositionSurface::ResumeDraw**](https://msdn.microsoft.com/en-us/library/Hh449104(v=VS.85).aspx) method. For more information, see Remarks.


</dt> </dl> </dd> <dt>

<span id="DCOMPOSITION_ERROR_SURFACE_NOT_BEING_RENDERED"></span><span id="dcomposition_error_surface_not_being_rendered"></span>**DCOMPOSITION\_ERROR\_SURFACE\_NOT\_BEING\_RENDERED**
</dt> <dd> <dl> <dt>


</dt> <dt>



The application called the [**IDCompositionSurface::SuspendDraw**](https://msdn.microsoft.com/en-us/library/Hh449106(v=VS.85).aspx), [**IDCompositionSurface::ResumeDraw**](https://msdn.microsoft.com/en-us/library/Hh449104(v=VS.85).aspx), or [**IDCompositionSurface::EndDraw**](https://msdn.microsoft.com/en-us/library/Hh449102(v=VS.85).aspx) method for a surface that is not being rendered. For more information, see Remarks.


</dt> </dl> </dd> <dt>

<span id="DCOMPOSITION_ERROR_WINDOW_ALREADY_COMPOSED"></span><span id="dcomposition_error_window_already_composed"></span>**DCOMPOSITION\_ERROR\_WINDOW\_ALREADY\_COMPOSED**
</dt> <dd> <dl> <dt>


</dt> <dt>



The [**IDCompositionDevice::CreateTargetForHwnd**](https://msdn.microsoft.com/en-us/library/Hh437396(v=VS.85).aspx) method was called with *hwnd* and *topmost* parameters for which a visual tree already exists.


</dt> </dl> </dd> </dl>

## Remarks

If a call to the [**IDCompositionSurface::BeginDraw**](https://msdn.microsoft.com/en-us/library/Hh449100(v=VS.85).aspx) was the most recent action:



| Calling this method:                                    | Returns this value:                               |
|---------------------------------------------------------|---------------------------------------------------|
| [**BeginDraw**](https://msdn.microsoft.com/en-us/library/Hh449100(v=VS.85).aspx)     | **DCOMPOSITION\_ERROR\_SURFACE\_BEING\_RENDERED** |
| [**EndDraw**](https://msdn.microsoft.com/en-us/library/Hh449102(v=VS.85).aspx)         | S\_OK                                             |
| [**SuspendDraw**](https://msdn.microsoft.com/en-us/library/Hh449106(v=VS.85).aspx) | S\_OK                                             |
| [**ResumeDraw**](https://msdn.microsoft.com/en-us/library/Hh449104(v=VS.85).aspx)   | **DCOMPOSITION\_ERROR\_SURFACE\_BEING\_RENDERED** |



 

If a call to the [**IDCompositionSurface::SuspendDraw**](https://msdn.microsoft.com/en-us/library/Hh449106(v=VS.85).aspx) was the most recent action:



| Calling this method:                                    | Returns this value:                               |
|---------------------------------------------------------|---------------------------------------------------|
| [**BeginDraw**](https://msdn.microsoft.com/en-us/library/Hh449100(v=VS.85).aspx)     | **DCOMPOSITION\_ERROR\_SURFACE\_BEING\_RENDERED** |
| [**EndDraw**](https://msdn.microsoft.com/en-us/library/Hh449102(v=VS.85).aspx)         | S\_OK                                             |
| [**SuspendDraw**](https://msdn.microsoft.com/en-us/library/Hh449106(v=VS.85).aspx) | **DCOMPOSITION\_ERROR\_SURFACE\_BEING\_RENDERED** |
| [**ResumeDraw**](https://msdn.microsoft.com/en-us/library/Hh449104(v=VS.85).aspx)   | S\_OK                                             |



 

If a call to the [**IDCompositionSurface::ResumeDraw**](https://msdn.microsoft.com/en-us/library/Hh449104(v=VS.85).aspx) was the most recent action:



| Calling this method:                                    | Returns this value:                                |
|---------------------------------------------------------|----------------------------------------------------|
| [**BeginDraw**](https://msdn.microsoft.com/en-us/library/Hh449100(v=VS.85).aspx)     | **DCOMPOSITION\_ERROR\_SURFACE\_BEING\_RENDERED**  |
| [**EndDraw**](https://msdn.microsoft.com/en-us/library/Hh449102(v=VS.85).aspx)         | S\_OK                                              |
| [**SuspendDraw**](https://msdn.microsoft.com/en-us/library/Hh449106(v=VS.85).aspx) | S\_OK                                              |
| [**ResumeDraw**](https://msdn.microsoft.com/en-us/library/Hh449104(v=VS.85).aspx)   | **DCOMPOSITION\_ERROR\_SURFACE\_BEING\_RENDERED.** |



 

If a call to the [**IDCompositionSurface::EndDraw**](https://msdn.microsoft.com/en-us/library/Hh449102(v=VS.85).aspx) was the most recent action:



| Calling this method:                                    | Returns this value:                                     |
|---------------------------------------------------------|---------------------------------------------------------|
| [**BeginDraw**](https://msdn.microsoft.com/en-us/library/Hh449100(v=VS.85).aspx)     | S\_OK                                                   |
| [**EndDraw**](https://msdn.microsoft.com/en-us/library/Hh449102(v=VS.85).aspx)         | **DCOMPOSITION\_ERROR\_SURFACE\_NOT\_BEING\_RENDERED.** |
| [**SuspendDraw**](https://msdn.microsoft.com/en-us/library/Hh449106(v=VS.85).aspx) | **DCOMPOSITION\_ERROR\_SURFACE\_NOT\_BEING\_RENDERED.** |
| [**ResumeDraw**](https://msdn.microsoft.com/en-us/library/Hh449104(v=VS.85).aspx)   | **DCOMPOSITION\_ERROR\_SURFACE\_NOT\_BEING\_RENDERED.** |



 

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

 

 





