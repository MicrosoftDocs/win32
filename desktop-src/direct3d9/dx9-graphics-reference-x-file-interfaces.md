---
description: This section contains reference information for the COM interfaces used to read to and write from DirectX .x files. Deprecated.
ms.assetid: 66e3476a-4ee8-48ac-aab8-6653793e0ef3
title: X File Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# X File Interfaces

This section contains reference information for the COM interfaces used to read to and write from DirectX .x files. Deprecated.

-   [**IDirectXFile**](idirectxfile.md)
-   [**IDirectXFileBinary**](idirectxfilebinary.md)
-   [**IDirectXFileData**](idirectxfiledata.md)
-   [**IDirectXFileDataReference**](idirectxfiledatareference.md)
-   [**IDirectXFileEnumObject**](idirectxfileenumobject.md)
-   [**IDirectXFileObject**](idirectxfileobject.md)
-   [**IDirectXFileSaveObject**](idirectxfilesaveobject.md)

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

[X File Reference (Legacy)](dx9-graphics-reference-x-file.md)
</dt> </dl>

 

 



