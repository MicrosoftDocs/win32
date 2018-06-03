---
title: IMediaTransform Process method
description: The Process method enables your transform to process a block of data.
ms.assetid: 87e62098-2f21-4b1b-91b7-16ed03ea8807
keywords:
- Process method Windows Movie Maker and DVD Maker
- Process method Windows Movie Maker and DVD Maker , IMediaTransform interface
- IMediaTransform interface Windows Movie Maker and DVD Maker , Process method
topic_type:
- apiref
api_name:
- IMediaTransform.Process
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMediaTransform::Process method

The **Process** method enables your transform to process a block of data.

## Syntax


```C++
HRESULT Process(
  [in] IBufferManager *pManager,
  [in] TIME_INFO      *pTimeInfo,
  [in] PIPELINE_TIME  duration,
  [in] IBuffer        **ppInputs,
  [in] DWORD          dwInputCount,
  [in] IBuffer        *pOutput
);
```



## Parameters

<dl> <dt>

*pManager* \[in\]
</dt> <dd>

Pointer to an [**IBufferManager**](ibuffermanager.md) manager object that can be used to allocate buffers or surfaces or acquire the Direct3D device.

</dd> <dt>

*pTimeInfo* \[in\]
</dt> <dd>

Pointer to a [TIME\_INFO](time-info.md) structure that describes the submitted sample.

</dd> <dt>

*duration* \[in\]
</dt> <dd>

A [PIPELINE\_TIME](pipeline-time.md) value that describes the duration of the effect or transition.

</dd> <dt>

*ppInputs* \[in\]
</dt> <dd>

An array of [**IBuffer**](ibuffer.md) interface pointers that contain sample data. Each element of the array points to a buffer containing a sample from one input source. An effect transform will have only one input; a transition will have two.

</dd> <dt>

*dwInputCount* \[in\]
</dt> <dd>

**DWORD** that specifies the number of buffers in *ppInputs*.

</dd> <dt>

*pOutput* \[in\]
</dt> <dd>

Pointer to an **IBuffer** that holds the output sample. Windows Movie Maker allocates this buffer for the transform.

</dd> </dl>

## Return value

The transform can return S\_OK to indicate success, or an error code to indicate failure. If the transform returns an error code, Windows Movie Maker will no longer call the **Process** method of this transform for the current playback. If the user stops and restarts the clip, Windows Movie Maker will begin calling **Process** again.

## Remarks

Nodes should not cache temporary surface buffers but should create them each time **Process** is called. Caching temporary buffers is not recommended because the application could lose access to the device or could lose system resources between calls. If your transform loads parameters from an XML initialization file, you must navigate to the required parameter and either retrieve the value (by calling [**ITransformPropertyPoint::get\_Value**](itransformpropertypoint-get-value.md)) or ask Windows Movie Maker to calculate the current value for you by calling [**ITransformProperty::CalcValueAtTime**](itransformproperty-calcvalueattime.md). For more information about property interfaces, see [Property Management Interfaces](property-management-interfaces.md).

The following steps show how to handle the **Process** call:

1.  Call [**GetSurface**](getsurface.md) on output/inputs to get surfaces to read from and write to.
2.  Call [**GetTexture**](gettexture.md) on inputs/outputs to get textures to read from/write to.
3.  Query the [**IBufferManager**](ibuffermanager.md) interface passed in for [**ISurfaceManager**](isurfacemanager.md) to get an **IDirect3DDevice9** interface for the device.
4.  Call **IDirect3DDevice9::BeginScene** to begin rendering.
5.  Call **IDirect3DDevice9::SetRenderTarget** and pass in *pOutput*.
6.  Manipulate the data as needed. If this is a transition, you will need to calculate the position of the current frame within the total transition. This is done by calculating pTimeInfo.segmentTime / duration. Get new or existing surfaces and textures, as described later in this topic.
7.  Call **IDirect3DDevice9::EndScene** to queue the scene for rendering.
8.  Free any temporary caches you created, increment any persistent values that need to be modified, and return.

To create a new texture, call **IDirect3DDevice9::CreateTexture**.

To retrieve an existing surface or texture, call **GetSurface** or **GetTexture**, passing in the **IBuffer** interface that holds the existing surface or texture you want to use.

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**IMediaTransform Interface**](imediatransform.md)
</dt> </dl>

 

 





