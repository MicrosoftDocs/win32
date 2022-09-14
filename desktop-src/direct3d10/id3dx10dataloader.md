---
description: Data loading object used by ID3DX10ThreadPump Interface for loading data asynchronously.
ms.assetid: bda2414c-bbab-47ac-b23a-f58fb86e732d
title: ID3DX10DataLoader interface (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10DataLoader
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10DataLoader interface

Data loading object used by [**ID3DX10ThreadPump Interface**](id3dx10threadpump.md) for loading data asynchronously.

## Members

The **ID3DX10DataLoader** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DX10DataLoader** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX10DataLoader** interface has these methods.



| Method                                             | Description                                                                                                                                                                                                                        |
|:---------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Decompress**](id3dx10dataloader-decompress.md) | Used to decompress encoded data. Typically this would be used to load resources from file systems, such as ZIP files. When loading from an uncompressed resource, the decompression stage does not have to do any work.<br/> |
| [**Destroy**](id3dx10dataloader-destroy.md)       | Used by a [**ID3DX10ThreadPump Interface**](id3dx10threadpump.md) to destroy the loader after a work item completes.<br/>                                                                                                   |
| [**Load**](id3dx10dataloader-load.md)             | Used by a [**ID3DX10ThreadPump Interface**](id3dx10threadpump.md) to load data from a disk.<br/>                                                                                                                            |



 

## Remarks

This object can be inherited and its members redefined. Doing so would enable you to customize the API for loading and decompressing your own custom file formats.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
