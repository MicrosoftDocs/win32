---
description: The photo metadata policy for the System.Photo.FocalLengthInFilm property.
ms.assetid: 3ad63a7a-5ced-4e7f-a4a0-e1463f3d3fa3
title: System.Photo.FocalLengthInFilm Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.FocalLengthInFilm Photo Metadata Policy

The photo metadata policy for the [System.Photo.FocalLengthInFilm](../properties/props-system-photo-focallengthinfilm.md) property.

### PKEY

PKEY\_FocalLengthInFilm

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



| Order | Path                            | Disk Format |
|-------|---------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=41989}   | ushort      |
| 2     | /xmp/exif:FocalLengthIn35mmFilm | unicode     |



 

### Write Paths



| Order | Path                            | Disk Format |
|-------|---------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=41989}   | ushort      |
| 2     | /xmp/exif:FocalLengthIn35mmFilm | unicode     |



 

### Remove Paths



| Order | Path                            |
|-------|---------------------------------|
| 1     | /app1/ifd/exif/{ushort=41989}   |
| 2     | /xmp/exif:focallengthin35mmfilm |



 

### TIFF Policies

### Read Paths



| Order | Path                                | Disk Format |
|-------|-------------------------------------|-------------|
| 1     | /ifd/exif/{ushort=41989}            | ushort      |
| 2     | /ifd/xmp/exif:FocalLengthIn35mmFilm | unicode     |



 

### Write Paths



| Order | Path                                | Disk Format |
|-------|-------------------------------------|-------------|
| 1     | /ifd/exif/{ushort=41989}            | ushort      |
| 2     | /ifd/xmp/exif:FocalLengthIn35mmFilm | unicode     |



 

### Remove Paths



| Order | Path                                |
|-------|-------------------------------------|
| 1     | /ifd/exif/{ushort=41989}            |
| 2     | /ifd/xmp/exif:focallengthin35mmfilm |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.FocalLengthInFilm](../properties/props-system-photo-focallengthinfilm.md)
</dt> </dl>

 

 
