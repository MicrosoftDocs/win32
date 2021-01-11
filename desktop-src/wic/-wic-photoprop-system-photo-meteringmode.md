---
description: The photo metadata policy for the System.Photo.MeteringMode property.
ms.assetid: cb0bf0d5-eccf-4345-a242-76769c34e02d
title: System.Photo.MeteringMode Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.MeteringMode Photo Metadata Policy

The photo metadata policy for the [System.Photo.MeteringMode](../properties/props-system-photo-meteringmode.md) property.

### PKEY

PKEY\_Photo\_MeteringMode

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_UI2

### Input Type

UShort

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37383} | ushort      |
| 2     | /xmp/exif:MeteringMode        | unicode     |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37383} | ushort      |
| 2     | /xmp/exif:MeteringMode        | unicode     |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=37383} |
| 2     | /xmp/exif:meteringmode        |



 

### TIFF Policies

### Read Paths



| Order | Path                       | Disk Format |
|-------|----------------------------|-------------|
| 1     | /ifd/exif/{ushort=37383}   | ushort      |
| 2     | /ifd/xmp/exif:MeteringMode | unicode     |



 

### Write Paths



| Order | Path                       | Disk Format |
|-------|----------------------------|-------------|
| 1     | /ifd/exif/{ushort=37383}   | ushort      |
| 2     | /ifd/xmp/exif:MeteringMode | unicode     |



 

### Remove Paths



| Order | Path                       |
|-------|----------------------------|
| 1     | /ifd/exif/{ushort=37383}   |
| 2     | /ifd/xmp/exif:meteringmode |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.MeteringMode](../properties/props-system-photo-meteringmode.md)
</dt> </dl>

 

 
