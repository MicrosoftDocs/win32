---
title: ID3DX11DataProcessor interface (D3DX11core.h)
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. Data processing object used by ID3DX11ThreadPump Interface for loading data asynchronously.
ms.assetid: ab893879-416f-4b17-9035-a7f03a62b753
keywords:
- ID3DX11DataProcessor interface Direct3D 11
- ID3DX11DataProcessor interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11DataProcessor
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11DataProcessor interface

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 

Data processing object used by [**ID3DX11ThreadPump Interface**](id3dx11threadpump.md) for loading data asynchronously.

## Members

The **ID3DX11DataProcessor** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ID3DX11DataProcessor** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX11DataProcessor** interface has these methods.




| Method | Description | 
|--------|-------------|
| [**CreateDeviceObject**](id3dx11dataprocessor-createdeviceobject.md) |  **Note:** The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.<br> Creates a device object.<br> | 
| [**Destroy**](id3dx11dataprocessor-destroy.md) |  **Note:** The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.<br> Destroys the processor after a work item completes.<br> | 
| [**Process**](id3dx11dataprocessor-process.md) |  **Note:** The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.<br> Processes data.<br> | 




 

## Remarks

This object can be inherited and its members redefined for processing custom file formats.

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

 

