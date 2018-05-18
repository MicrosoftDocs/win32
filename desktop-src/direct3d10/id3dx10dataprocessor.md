---
Description: 'Data processing object used by ID3DX10ThreadPump Interface for processing loaded data asynchronously.'
ms.assetid: 'c932f558-10da-45fc-a833-8ed86fa065ab'
title: ID3DX10DataProcessor interface
---

# ID3DX10DataProcessor interface

Data processing object used by [**ID3DX10ThreadPump Interface**](id3dx10threadpump.md) for processing loaded data asynchronously.

## Members

The **ID3DX10DataProcessor** interface inherits from the [**IUnknown**](com.iunknown) interface. **ID3DX10DataProcessor** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX10DataProcessor** interface has these methods.



| Method                                                                | Description                                                                                                                         |
|:----------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateDeviceObject**](id3dx10dataprocessor-createdeviceobject.md) | Create a device object.<br/>                                                                                                  |
| [**Destroy**](id3dx10dataprocessor-destroy.md)                       | Used by a [**ID3DX10ThreadPump Interface**](id3dx10threadpump.md) to destroy the processor after a work item completes.<br/> |
| [**Process**](id3dx10dataprocessor-process.md)                       | Process some data.<br/>                                                                                                       |



 

## Remarks

This object can be inherited and its members redefined. Doing so would enable you to customize the API for processing your own custom file formats.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




