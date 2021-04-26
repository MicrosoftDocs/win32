---
description: The following flags are used to specify which channels in a texture to operate on. Deprecated.
ms.assetid: 6e421a0a-7e82-4640-a96c-7ec648df970d
title: DXFILE Constants
ms.topic: article
ms.date: 05/31/2018
---

# DXFILE Constants

The following flags are used to specify which channels in a texture to operate on. Deprecated.

## DXFILEFORMAT



| \#define                 | Value | Description      |
|--------------------------|-------|------------------|
| DXFILEFORMAT\_BINARY     | 0     | Binary file.     |
| DXFILEFORMAT\_TEXT       | 1     | Text file.       |
| DXFILEFORMAT\_COMPRESSED | 2     | Compressed file. |



 

These \#defines are declared in Dxfile.h.

## DXFILELOADOPTIONS



| \#define                 | Value | Description                  |
|--------------------------|-------|------------------------------|
| DXFILELOAD\_FROMFILE     | 0x00L | Load a file from a file.     |
| DXFILELOAD\_FROMRESOURCE | 0x01L | Load a file from a resource. |
| DXFILELOAD\_FROMMEMORY   | 0x02L | Load a file from memory.     |
| DXFILELOAD\_FROMSTREAM   | 0x04L | Load a file from a stream.   |
| DXFILELOAD\_FROMURL      | 0x08L | Load a file from a URL.      |



 

These \#defines are declared in Dxfile.h.

## Related topics

<dl> <dt>

[X File Reference (Legacy)](dx9-graphics-reference-x-file.md)
</dt> </dl>

 

 



