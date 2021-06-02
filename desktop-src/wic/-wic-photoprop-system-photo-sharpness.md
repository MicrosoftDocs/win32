---
description: The photo metadata policy for the System.Photo.Sharpness property.
ms.assetid: 0fda4832-940b-4b5a-bd20-7e48c7800925
title: System.Photo.Sharpness Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.Sharpness Photo Metadata Policy

The photo metadata policy for the [System.Photo.Sharpness](../properties/props-system-photo-sharpness.md) property.

### PKEY

PKEY\_Photo\_Sharpness

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_UI4

### Input Type

UShort

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=41994} | ushort      |
| 2     | /xmp/exif:Sharpness           | unicode     |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=41994} | ushort      |
| 2     | /xmp/exif:Sharpness           | unicode     |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=41994} |
| 2     | /xmp/exif:sharpness           |



 

### TIFF Policies

### Read Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /ifd/exif/{ushort=41994} | ushort      |
| 2     | /ifd/xmp/exif:Sharpness  | unicode     |



 

### Write Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /ifd/exif/{ushort=41994} | ushort      |
| 2     | /ifd/xmp/exif:Sharpness  | unicode     |



 

### Remove Paths



| Order | Path                     |
|-------|--------------------------|
| 1     | /ifd/exif/{ushort=41994} |
| 2     | /ifd/xmp/exif:sharpness  |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.Sharpness](../properties/props-system-photo-sharpness.md)
</dt> </dl>

 

 
