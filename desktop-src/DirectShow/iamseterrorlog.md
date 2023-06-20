---
description: The IAMSetErrorLog interface sets or retrieves an error log in DirectShow Editing Services (DES).
ms.assetid: ce658533-eacf-4b5d-9910-dca918de09e7
title: IAMSetErrorLog interface (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMSetErrorLog
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMSetErrorLog interface

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IAMSetErrorLog` interface sets or retrieves an error log in [DirectShow Editing Services](directshow-editing-services.md) (DES). The timeline object implements this interface. Applications can use this interface to log rendering errors at run time. Implement the [**IAMErrorLog**](iamerrorlog.md) interface in your application, and then call the [**IAMSetErrorLog::put\_ErrorLog**](iamseterrorlog-put-errorlog.md) method on the timeline.

For more information on using this interface, see [Logging Errors](logging-errors.md).

## Members

The **IAMSetErrorLog** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IAMSetErrorLog** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMSetErrorLog** interface has these methods.



| Method                                               | Description                                                 |
|:-----------------------------------------------------|:------------------------------------------------------------|
| [**get\_ErrorLog**](iamseterrorlog-get-errorlog.md) | Retrieves the current error log for this object.<br/> |
| [**put\_ErrorLog**](iamseterrorlog-put-errorlog.md) | Specifies an error log for the object.<br/>           |



 

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



 

 
