---
description: The IResize interface must be supported by any custom video resizer filter for DirectShow Editing Services (DES). To set a custom resizer filter, call the IRenderEngine2::SetResizerGUID method on the render engine.
ms.assetid: 4740dbff-0881-45e8-b382-98ed9d055403
title: IResize interface (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IResize
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IResize interface

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IResize` interface must be supported by any custom video resizer filter for DirectShow Editing Services (DES). To set a custom resizer filter, call the [**IRenderEngine2::SetResizerGUID**](irenderengine2-setresizerguid.md) method on the render engine.

## Members

The **IResize** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IResize** also has these types of members:

-   [Methods](#methods)

### Methods

The **IResize** interface has these methods.



| Method                                          | Description                                                  |
|:------------------------------------------------|:-------------------------------------------------------------|
| [**get\_InputSize**](iresize-get-inputsize.md) | Returns the resizer filter's current input size.<br/>  |
| [**get\_MediaType**](iresize-get-mediatype.md) | Returns the resizer filter's output media type.<br/>   |
| [**get\_Size**](iresize-get-size.md)           | Returns the current output size and stretch mode.<br/> |
| [**put\_MediaType**](iresize-put-mediatype.md) | Sets the output media type.<br/>                       |
| [**put\_Size**](iresize-put-size.md)           | Sets the output size and stretch mode.<br/>            |



 

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | DirectX 9.0 or later<br/>                                                         |
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[Providing a Custom Video Resizer](providing-a-custom-video-resizer.md)
</dt> </dl>

 

 
