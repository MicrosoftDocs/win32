---
description: The photo metadata policy for the System.Image.ImageID property.
ms.assetid: 2a092d16-e7b9-4ffe-9bdb-01ed328ca26f
title: System.Image.ImageID Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Image.ImageID Photo Metadata Policy

The photo metadata policy for the [System.Image.ImageID](../properties/props-system-image-imageid.md) property.

### PKEY

PKEY\_Image\_ImageID

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_LPWSTR

### Input Type

String.

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=42016} | ascii       |
| 2     | /xmp/exif:ImageUniqueID       | unicode     |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=42016} | ascii       |
| 2     | /xmp/exif:ImageUniqueID       | unicode     |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=42016} |
| 2     | /xmp/exif:ImageUniqueID       |



 

### TIFF Policy

### Read Paths



| Order | Path                        | Disk Format |
|-------|-----------------------------|-------------|
|       | /ifd/exif/{ushort=42016}    | ascii       |
|       | /ifd/xmp/exif:ImageUniqueID | unicode     |



 

### Write Paths



| Order | Path                        | Disk Format |
|-------|-----------------------------|-------------|
|       | /ifd/exif/{ushort=42016}    | ascii       |
|       | /ifd/xmp/exif:ImageUniqueID | unicode     |



 

### Remove Paths



| Order | Path                        |
|-------|-----------------------------|
|       | /ifd/exif/{ushort=42016}    |
|       | /ifd/xmp/exif:ImageUniqueID |



 

## Remarks

## Related topics

<dl> <dt>

[System.Image.ImageID](../properties/props-system-image-imageid.md)
</dt> </dl>

 

 
