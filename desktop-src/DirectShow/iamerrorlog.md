---
description: The IAMErrorLog interface provides a callback method for error logging in DirectShow Editing Services (DES).DES does not implement this interface.
ms.assetid: d5366072-2de7-437c-b198-cbc4d8623c45
title: IAMErrorLog interface (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMErrorLog
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMErrorLog interface

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IAMErrorLog` interface provides a callback method for error logging in [DirectShow Editing Services](directshow-editing-services.md) (DES).

DES does not implement this interface. To perform error logging, implement this interface in your application and call [**IAMSetErrorLog::put\_ErrorLog**](iamseterrorlog-put-errorlog.md) on the timeline. If an error occurs when you render the project, DES will call the [**IAMErrorLog::LogError**](iamerrorlog-logerror.md) method implemented by your application.

DES logs errors only when you render a project using the [**IRenderEngine**](irenderengine.md) interface. For example, if you save a project as a DirectShow filter graph (.grf format) and play the graph file, there is no error logging. For more information on using this interface, see [Logging Errors](logging-errors.md).

## Members

The **IAMErrorLog** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IAMErrorLog** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMErrorLog** interface has these methods.



| Method                                   | Description               |
|:-----------------------------------------|:--------------------------|
| [**LogError**](iamerrorlog-logerror.md) | Logs an error.<br/> |



 

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



 

 
