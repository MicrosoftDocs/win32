---
description: Used to execute tasks asynchronously, and created with D3DX10CreateThreadPump.
ms.assetid: 8d03c94a-9b64-464c-b0f4-4e5f5a00503f
title: ID3DX10ThreadPump interface (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10ThreadPump
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10ThreadPump interface

Used to execute tasks asynchronously, and created with [**D3DX10CreateThreadPump**](d3dx10createthreadpump.md). There are several D3DX10 APIs that can optionally take a thread pump as a parameter, such as [**D3DX10CreateTextureFromFile**](d3dx10createtexturefromfile.md) and [**D3DX10CompileFromFile**](d3dx10compilefromfile.md) (see remarks for complete list). If the thread pump is passed into these APIs, they will execute asynchronously on a separate thread pump thread. The advantage to doing this is that it can make loading and processing large amounts of data happen without seeing a noticable slow down in performance on screen.

## Members

The **ID3DX10ThreadPump** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DX10ThreadPump** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX10ThreadPump** interface has these methods.



| Method                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:---------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddWorkItem**](id3dx10threadpump-addworkitem.md)                       | Add a work item to the thread pump.<br/>                                                                                                                                                                                                                                                                                                                                                                                   |
| [**GetQueueStatus**](id3dx10threadpump-getqueuestatus.md)                 | Get the number of items in each of the three queues inside the thread pump.<br/>                                                                                                                                                                                                                                                                                                                                           |
| [**GetWorkItemCount**](id3dx10threadpump-getworkitemcount.md)             | Get the number of work items currently in the thread pump.<br/>                                                                                                                                                                                                                                                                                                                                                            |
| [**ProcessDeviceWorkItems**](id3dx10threadpump-processdeviceworkitems.md) | Set work items to the device after they have finished loading and processing. When the thread pump has finished loading and processing a resource or shader, it will hold it in a queue until this API is called, at which point the processed items will be set to the device. This is useful for controlling the amount of processing that is spent on binding resources to the device for each frame. See remarks.<br/> |
| [**PurgeAllItems**](id3dx10threadpump-purgeallitems.md)                   | Clear all work items from the thread pump.<br/>                                                                                                                                                                                                                                                                                                                                                                            |
| [**WaitForAllItems**](id3dx10threadpump-waitforallitems.md)               | Wait for all work items in the thread pump to finish.<br/>                                                                                                                                                                                                                                                                                                                                                                 |



 

## Remarks

The thread pump loads and processes data in a 3 step process. It goes:

1.  Load and decompress the data with a Data Loader. The data loader object has three methods that the thread pump will call internally as it is loading and decompressing the data: [**ID3DX10DataLoader::Load**](id3dx10dataloader-load.md), [**ID3DX10DataLoader::Decompress**](id3dx10dataloader-decompress.md), and [**ID3DX10DataLoader::Destroy**](id3dx10dataloader-destroy.md). The specific functionality of these three APIs differs depending on the type of data being loaded and decompressed. The data loader interface can also be inherited and its APIs can be changed if one is loading a data file defined in one's own custom format.
2.  Process the data with a Data Processor. The data processor object has three methods that the thread pump will call internally as it is processing the data: [**ID3DX10DataProcessor::Process**](id3dx10dataprocessor-process.md), [**ID3DX10DataProcessor::CreateDeviceObject**](id3dx10dataprocessor-createdeviceobject.md), and [**ID3DX10DataProcessor::Destroy**](id3dx10dataprocessor-destroy.md). The way it processes the data will be different depending on the type of data. For example, if the data is a texture stored as a JPEG, then **ID3DX10DataProcessor::Process** will do JPEG decompression to get the image's raw image bits. If the data is a shader, then **ID3DX10DataProcessor::Process** will compile the HLSL into bytecode. After the data has been processed a device object will be created for that data (with **ID3DX10DataProcessor::CreateDeviceObject**) and the object will be added to a queue of device objects. The data processor interface can also be inherited and its APIs can be changed if one is processing a data file defined in one's own custom format.
3.  Bind the device object to the device. This is done when one's application calls [**ID3DX10ThreadPump::ProcessDeviceWorkItems**](id3dx10threadpump-processdeviceworkitems.md), which will bind a specified number of objects in the queue of device objects to the device.

The thread pump can be used to load data in one of two ways: by calling an API that takes a thread pump as a parameter, such as [**D3DX10CreateTextureFromFile**](d3dx10createtexturefromfile.md) and [**D3DX10CompileFromFile**](d3dx10compilefromfile.md), or by calling [**ID3DX10ThreadPump::AddWorkItem**](id3dx10threadpump-addworkitem.md). In the case of the APIs that take a thread pump, the data loader and data processor are created internally. In the case of **AddWorkItem**, the data loader and data processor must be created beforehand and are then passed into AddWorkItem. D3DX10 provides a set of APIs for creating data loaders and data processors that have functionality for loading and processing common data formats (see remarks for complete list of APIs). For custom data formats, the data loader and data processor interfaces must be inherited and their methods must be redefined.

The thread pump object takes up a substantial amount of resources, so generally only one should be created per application.

Built-in D3DX10 data loaders



|                                                                            |                                          |
|----------------------------------------------------------------------------|------------------------------------------|
| [**D3DX10CreateAsyncFileLoader**](d3dx10createasyncfileloader.md)         | Create a file loader asynchronously.     |
| [**D3DX10CreateAsyncMemoryLoader**](d3dx10createasyncmemoryloader.md)     | Create a data loader asynchronously.     |
| [**D3DX10CreateAsyncResourceLoader**](d3dx10createasyncresourceloader.md) | Create a resource loader asynchronously. |



 

Built-in D3DX10 data processors



|                                                                                                  |                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**D3DX10CreateAsyncTextureProcessor**](d3dx10createasynctextureprocessor.md)                   | Create a data processor to be used with a thread pump. This API is similar to D3DX10CreateAsyncTextureInfoProcessor but it also loads the texture. |
| [**D3DX10CreateAsyncTextureInfoProcessor**](d3dx10createasynctextureinfoprocessor.md)           | Create a data processor to be used with a thread pump.                                                                                             |
| [**D3DX10CreateAsyncShaderCompilerProcessor**](d3dx10createasyncshadercompilerprocessor.md)     | Compile a shader and create a data processor asynchronously.                                                                                       |
| [**D3DX10CreateAsyncEffectCompilerProcessor**](d3dx10createasynceffectcompilerprocessor.md)     | Create an effect with a data processor asynchronously.                                                                                             |
| [**D3DX10CreateAsyncEffectCreateProcessor**](d3dx10createasynceffectcreateprocessor.md)         | Create an effect pool asynchronously.                                                                                                              |
| [**D3DX10CreateAsyncEffectPoolCreateProcessor**](d3dx10createasynceffectpoolcreateprocessor.md) | Create a data processor asynchronously.                                                                                                            |
| [**D3DX10CreateAsyncShaderPreprocessProcessor**](d3dx10createasyncshaderpreprocessprocessor.md) | Create a data processor for a shader asynchronously.                                                                                               |



 

APIs that take a thread pump as a parameter.



|                                                                                                  |                                                                  |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [**D3DX10CompileFromFile**](d3dx10compilefromfile.md)                                           | Compile a shader from a file.                                    |
| [**D3DX10CompileFromMemory**](d3dx10compilefrommemory.md)                                       | Compile a shader residing in memory.                             |
| [**D3DX10CompileFromResource**](d3dx10compilefromresource.md)                                   | Compile a shader from a resource.                                |
| [**D3DX10CreateEffectFromFile**](d3dx10createeffectfromfile.md)                                 | Create an effect from a file.                                    |
| [**D3DX10CreateEffectFromMemory**](d3dx10createeffectfrommemory.md)                             | Create an effect from memory.                                    |
| [**D3DX10CreateEffectFromResource**](d3dx10createeffectfromresource.md)                         | Create an effect from a resource.                                |
| [**D3DX10CreateEffectPoolFromFile**](d3dx10createeffectpoolfromfile.md)                         | Create an effect pool from a file.                               |
| [**D3DX10CreateEffectPoolFromMemory**](d3dx10createeffectpoolfrommemory.md)                     | Create an effect pool from a file residing in memory.            |
| [**D3DX10CreateEffectPoolFromResource**](d3dx10createeffectpoolfromresource.md)                 | Create an effect pool from a resource.                           |
| [**D3DX10PreprocessShaderFromFile**](d3dx10preprocessshaderfromfile.md)                         | Create a shader from a file without compiling it.                |
| [**D3DX10PreprocessShaderFromMemory**](d3dx10preprocessshaderfrommemory.md)                     | Create a shader from memory without compiling it.                |
| [**D3DX10PreprocessShaderFromResource**](d3dx10preprocessshaderfromresource.md)                 | Create a shader from a resource without compiling it.            |
| [**D3DX10CreateShaderResourceViewFromFile**](d3dx10createshaderresourceviewfromfile.md)         | Create a shader-resource view from a file.                       |
| [**D3DX10CreateShaderResourceViewFromMemory**](d3dx10createshaderresourceviewfrommemory.md)     | Create a shader-resource view from a file in memory.             |
| [**D3DX10CreateShaderResourceViewFromResource**](d3dx10createshaderresourceviewfromresource.md) | Create a shader-resource view from a resource.                   |
| [**D3DX10GetImageInfoFromFile**](d3dx10getimageinfofromfile.md)                                 | Retrieves information about a given image file.                  |
| [**D3DX10GetImageInfoFromMemory**](d3dx10getimageinfofrommemory.md)                             | Get information about an image already loaded into memory.       |
| [**D3DX10GetImageInfoFromResource**](d3dx10getimageinfofromresource.md)                         | Retrieves information about a given image in a resource.         |
| [**D3DX10CreateTextureFromFile**](d3dx10createtexturefromfile.md)                               | Create a texture resource from a file.                           |
| [**D3DX10CreateTextureFromMemory**](d3dx10createtexturefrommemory.md)                           | Create a texture resource from a file residing in system memory. |
| [**D3DX10CreateTextureFromResource**](d3dx10createtexturefromresource.md)                       | Create a texture resource from another resource.                 |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
