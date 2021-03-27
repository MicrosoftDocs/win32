---
description: The ISampleGrabberCB interface provides callback methods for the ISampleGrabber::SetCallback method. If your application calls that method, it must implement this interface. For more information, see ISampleGrabber.
ms.assetid: 30166d1b-cc37-43c4-8f64-681d8f2013b9
title: ISampleGrabberCB interface (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISampleGrabberCB
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# ISampleGrabberCB interface

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `ISampleGrabberCB` interface provides callback methods for the [**ISampleGrabber::SetCallback**](isamplegrabber-setcallback.md) method. If your application calls that method, it must implement this interface. For more information, see [**ISampleGrabber**](isamplegrabber.md).

## Members

The **ISampleGrabberCB** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ISampleGrabberCB** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISampleGrabberCB** interface has these methods.



| Method                                        | Description                                                              |
|:----------------------------------------------|:-------------------------------------------------------------------------|
| [**BufferCB**](isamplegrabbercb-buffercb.md) | Callback method that receives a pointer to the sample buffer.<br/> |
| [**SampleCB**](isamplegrabbercb-samplecb.md) | Callback method that receives a pointer to the media sample.<br/>  |



 

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



 

 
