---
description: The SetTimelineObject method sets the timeline for the render engine to use.
ms.assetid: 9b60b148-9768-43ba-a986-a96838c4d2bb
title: IRenderEngine::SetTimelineObject method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRenderEngine.SetTimelineObject
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IRenderEngine::SetTimelineObject method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetTimelineObject` method sets the timeline for the render engine to use.

## Syntax


```C++
HRESULT SetTimelineObject(
   IAMTimeline *pTimeline
);
```



## Parameters

<dl> <dt>

*pTimeline* 
</dt> <dd>

Pointer to the timeline object's [**IAMTimeline**](iamtimeline.md) interface.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                                            | Description                                    |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | Success.<br/>                            |
| <dl> <dt>**E\_MUST\_INIT\_RENDERER**</dt> </dl> | Render engine failed to initialize.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>          | Insufficient memory.<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl>              | Invalid pointer.<br/>                    |



 

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



## See also

<dl> <dt>

[**IRenderEngine Interface**](irenderengine.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




