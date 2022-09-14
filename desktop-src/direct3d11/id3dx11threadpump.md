---
title: ID3DX11ThreadPump interface (D3DX11core.h)
description: A thread pump executes tasks asynchronously.
ms.assetid: 1a99f728-149d-4800-a6e4-e3a00cf8cf4f
keywords:
- ID3DX11ThreadPump interface Direct3D 11
- ID3DX11ThreadPump interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11ThreadPump
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11ThreadPump interface

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 

A thread pump executes tasks asynchronously. It is created by calling [**D3DX11CreateThreadPump**](d3dx11createthreadpump.md). There are several APIs that take an optional thread pump as a parameter, such as [**D3DX11CreateTextureFromFile**](d3dx11createtexturefromfile.md) and [**D3DX11CompileFromFile**](d3dx11compilefromfile.md); if you pass a thread pump interface into these APIs, the functions will execute asynchronously on a separate thread. Particularly on multiprocessor machines, a thread pump can load resources and process data without a noticeable decrease in performance.

## Members

The **ID3DX11ThreadPump** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ID3DX11ThreadPump** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX11ThreadPump** interface has these methods.




| Method | Description | 
|--------|-------------|
| <a href="id3dx11threadpump-addworkitem.md"><strong>AddWorkItem</strong></a> | <blockquote>[!Note]<br />The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.</blockquote><br /> Adds a work item to the thread pump.<br /> | 
| <a href="id3dx11threadpump-getqueuestatus.md"><strong>GetQueueStatus</strong></a> | <blockquote>[!Note]<br />The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.</blockquote><br /> Gets the number of items in each of the three queues inside the thread pump.<br /> | 
| <a href="id3dx11threadpump-getworkitemcount.md"><strong>GetWorkItemCount</strong></a> | <blockquote>[!Note]<br />The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.</blockquote><br /> Gets the number of work items in the thread pump.<br /> | 
| <a href="id3dx11threadpump-processdeviceworkitems.md"><strong>ProcessDeviceWorkItems</strong></a> | <blockquote>[!Note]<br />The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.</blockquote><br /> Sets work items to the device after they have finished loading and processing.<br /> | 
| <a href="id3dx11threadpump-purgeallitems.md"><strong>PurgeAllItems</strong></a> | <blockquote>[!Note]<br />The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.</blockquote><br /> Clears all work items from the thread pump.<br /> | 
| <a href="id3dx11threadpump-waitforallitems.md"><strong>WaitForAllItems</strong></a> | <blockquote>[!Note]<br />The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.</blockquote><br /> Waits for all work items in the thread pump to finish.<br /> | 




 

## Remarks

### Using a Thread Pump

The thread pump loads and processes data using the following three-step process:

1.  Load and decompress the data with a [**Data Loader**](id3dx11dataloader.md). The data loader object has three methods that the thread pump will call internally as it is loading and decompressing the data: [**ID3DX11DataLoader::Load**](id3dx11dataloader-load.md), [**ID3DX11DataLoader::Decompress**](id3dx11dataloader-decompress.md), and [**ID3DX11DataLoader::Destroy**](id3dx11dataloader-destroy.md). The specific functionality of these three APIs differs depending on the type of data being loaded and decompressed. The data loader interface can also be inherited and its APIs can be changed if one is loading a data file defined in one's own custom format.
2.  Process the data with a [**Data Processor**](id3dx11dataprocessor.md). The data processor object has three methods that the thread pump will call internally as it is processing the data: [**ID3DX11DataProcessor::Process**](id3dx11dataprocessor-process.md), [**ID3DX11DataProcessor::CreateDeviceObject**](id3dx11dataprocessor-createdeviceobject.md), and [**ID3DX11DataProcessor::Destroy**](id3dx11dataprocessor-destroy.md). The way it processes the data will be different depending on the type of data. For example, if the data is a texture stored as a JPEG, then [**ID3DX11DataProcessor::Process**](id3dx11dataprocessor-process.md) will do JPEG decompression to get the image's raw image bits. If the data is a shader, then [**ID3DX11DataProcessor::Process**](id3dx11dataprocessor-process.md) will compile the HLSL into bytecode. After the data has been processed a device object will be created for that data (with [**ID3DX11DataProcessor::CreateDeviceObject**](id3dx11dataprocessor-createdeviceobject.md)) and the object will be added to a queue of device objects. The data processor interface can also be inherited and its APIs can be changed if one is processing a data file defined in one's own custom format.
3.  Bind the device object to the device. This is done when one's application calls [**ID3DX11ThreadPump::ProcessDeviceWorkItems**](id3dx11threadpump-processdeviceworkitems.md), which will bind a specified number of objects in the queue of device objects to the device.

The thread pump can be used to load data in one of two ways: by calling an API that takes a thread pump as a parameter, such as [**D3DX11CreateTextureFromFile**](d3dx11createtexturefromfile.md) and [**D3DX11CompileFromFile**](d3dx11compilefromfile.md), or by calling [**ID3DX11ThreadPump::AddWorkItem**](id3dx11threadpump-addworkitem.md). In the case of the APIs that take a thread pump, the data loader and data processor are created internally. In the case of AddWorkItem, the data loader and data processor must be created beforehand and are then passed into AddWorkItem. D3DX11 provides a set of APIs for creating data loaders and data processors that have functionality for loading and processing common data formats. For custom data formats, the data loader and data processor interfaces must be inherited and their methods must be redefined.

The thread pump object takes up a substantial amount of resources, so generally only one should be created per application.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>D3DX11core.h</dt> </dl> |
| Library<br/>                  | <dl> <dt>D3DX11.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](d3d11-graphics-reference-d3dx11-interfaces.md)
</dt> </dl>

 

