---
Description: The SetRenderRange method sets the range of time on the timeline to be rendered. Objects that lie outside the specified range are not rendered, and resources are not allocated for them.
ms.assetid: 2dcdca6b-2bae-4a27-bfbc-19a9b2ea633a
title: IRenderEngineSetRenderRange method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IRenderEngine::SetRenderRange method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetRenderRange` method sets the range of time on the timeline to be rendered. Objects that lie outside the specified range are not rendered, and resources are not allocated for them.

## Syntax


```C++
HRESULT SetRenderRange(
   REFERENCE_TIME Start,
   REFERENCE_TIME Stop
);
```



## Parameters

<dl> <dt>

*Start* 
</dt> <dd>

Start time, in 100-nanosecond units.

</dd> <dt>

*Stop* 
</dt> <dd>

Stop time, in 100-nanosecond units.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                                            | Description                                    |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | Success.<br/>                            |
| <dl> <dt>**E\_MUST\_INIT\_RENDERER**</dt> </dl> | Render engine failed to initialize.<br/> |



 

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



## See also

<dl> <dt>

[**IRenderEngine Interface**](irenderengine.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




