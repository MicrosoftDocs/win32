---
description: The photo metadata policy for the System.Photo.ProgramMode property.
ms.assetid: f1954dc7-d4df-4675-ab3b-a65f2354e57a
title: System.Photo.ProgramMode Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.ProgramMode Photo Metadata Policy

The photo metadata policy for the [System.Photo.ProgramMode](../properties/props-system-photo-programmode.md) property.

### PKEY

PKEY\_Photo\_ProgramMode

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
| 1     | /app1/ifd/exif/{ushort=34850} | ushort      |
| 2     | /xmp/exif:ExposureProgram     | unicode     |
| 3     | /xmp/exif:ProgramMode         | unicode     |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=34850} | ushort      |
| 2     | /xmp/exif:ExposureProgram     | unicode     |
| 3     | /xmp/exif:ProgramMode         | unicode     |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=34850} |
| 2     | /xmp/exif:exposureprogram     |
| 3     | /xmp/exif:programmode         |



 

### TIFF Policies

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/exif/{ushort=34850}      | ushort      |
| 2     | /ifd/xmp/exif:ExposureProgram | unicode     |
| 3     | /ifd/xmp/exif:ProgramMode     | unicode     |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/exif/{ushort=34850}      | ushort      |
| 2     | /ifd/xmp/exif:ExposureProgram | unicode     |
| 3     | /ifd/xmp/exif:ProgramMode     | unicode     |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /ifd/exif/{ushort=34850}      |
| 2     | /ifd/xmp/exif:exposureprogram |
| 3     | /ifd/xmp/exif:programmode     |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.ProgramMode](../properties/props-system-photo-programmode.md)
</dt> </dl>

 

 
