---
description: This section contains reference information for the COM interfaces used to read to and write from .x files.
ms.assetid: 54d8a02b-5376-49ac-a0d5-fc3cd8ab82e6
title: D3DX X File Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# D3DX X File Interfaces

This section contains reference information for the COM interfaces used to read to and write from .x files.

-   [**ID3DXFile**](id3dxfile.md)
-   [**ID3DXFileData**](id3dxfiledata.md)
-   [**ID3DXFileEnumObject**](id3dxfileenumobject.md)
-   [**ID3DXFileSaveData**](id3dxfilesavedata.md)
-   [**ID3DXFileSaveObject**](id3dxfilesaveobject.md)

The following tables illustrate the relationship between the .x file interfaces.



| Interface             | Derives from           | Derives from |
|-----------------------|------------------------|--------------|
|                       | IDirectXFile           | IUnknown     |
| IDirectXFileBinary    | IDirectXFileObject     | IUnknown     |
| IDirectXFileData      | IDirectXFileObject     | IUnknown     |
| IDirectXFileReference | IDirectXFileObject     | IUnknown     |
|                       | IDirectXFileSaveObject | IUnknown     |



 

## Related topics

<dl> <dt>

[X File Reference](dx9-graphics-reference-d3dx-x-file.md)
</dt> </dl>

 

 



