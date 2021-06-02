---
description: X file format, load, and save options.
ms.assetid: 813a2b4b-6577-4cdf-a2e6-e06870638354
title: D3DXF
ms.topic: article
ms.date: 05/31/2018
---

# D3DXF

X file format, load, and save options.

## File Formats

The following table specifies the type of file data:



| \#defines for File Format     | Value | Description                                                                                    |
|-------------------------------|-------|------------------------------------------------------------------------------------------------|
| D3DXF\_FILEFORMAT\_BINARY     | 0     | Legacy-format binary file. See [X File Reference (Legacy)](dx9-graphics-reference-x-file.md). |
| D3DXF\_FILEFORMAT\_TEXT       | 1     | Text file.                                                                                     |
| D3DXF\_FILEFORMAT\_COMPRESSED | 2     | Compressed file. With this flag, you must also specify the binary format or the text format.   |



 

## File Load Options

The following table specifies file load options with .x files:



| \#define                      | Value | Description                |
|-------------------------------|-------|----------------------------|
| D3DXF\_FILELOAD\_FromFile     | 0     | Load data from a file.     |
| D3DXF\_FILELOAD\_FROMWFILE    | 1     | Load data from a file.     |
| D3DXF\_FILELOAD\_FROMRESOURCE | 2     | Load data from a resource. |
| D3DXF\_FILELOAD\_FROMMEMORY   | 3     | Load data from memory.     |



 

## File Save Options

The following table specifies file save and load options with .x files:



| \#define                 | Value | Description                    |
|--------------------------|-------|--------------------------------|
| D3DXF\_FILESAVE\_TOFILE  | 0     | Save to a file.                |
| D3DXF\_FILESAVE\_TOWFILE | 1     | Save to a wide-character file. |



 

## Constant Information



| Requirement                         | Value           |
|--------------------------|------------|
| Header                   | d3dx9xof.h |
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[D3DX X File Constants](dx9-graphics-reference-d3dx-x-file-constants.md)
</dt> <dt>

[**D3DXSaveMeshToX**](d3dxsavemeshtox.md)
</dt> </dl>

 

 



