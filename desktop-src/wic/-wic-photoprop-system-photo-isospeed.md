---
description: The photo metadata policy for the System.Photo.ISOSpeed property.
ms.assetid: 22b5552c-41b1-4090-a827-b920dcbba5e9
title: System.Photo.ISOSpeed Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.ISOSpeed Photo Metadata Policy

The photo metadata policy for the [System.Photo.ISOSpeed](../properties/props-system-photo-focallengthinfilm.md) property.

### PKEY

PKEY\_Photo\_ISOSpeed

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



| Order | Path                                    | Disk Format |
|-------|-----------------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=34855}           | ushort      |
| 2     | /xmp/<xmpseq>exif:ISOSpeedRatings | unicode     |
| 3     | /xmp/exif:ISOSpeed                      | unicode     |



 

### Write Paths



| Order | Path                                    | Disk Format |
|-------|-----------------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=34855}           | ushort      |
| 2     | /xmp/<xmpseq>exif:ISOSpeedRatings | unicode     |
| 3     | /xmp/exif:ISOSpeed                      | unicode     |



 

### Remove Paths



| Order | Path                                    |
|-------|-----------------------------------------|
| 1     | /app1/ifd/exif/{ushort=34855}           |
| 2     | /xmp/<xmpseq>exif:isospeedratings |
| 3     | /xmp/exif:isospeed                      |



 

### TIFF Policies

### Read Paths



| Order | Path                                        | Disk Format |
|-------|---------------------------------------------|-------------|
| 1     | /ifd/exif/{ushort=34855}                    | ushort      |
| 2     | /ifd/xmp/<xmpseq>exif:ISOSpeedRatings | unicode     |
| 3     | /ifd/xmp/exif:ISOSpeed                      | unicode     |



 

### Write Paths



| Order | Path                                        | Disk Format |
|-------|---------------------------------------------|-------------|
| 1     | /ifd/exif/{ushort=34855}                    | ushort      |
| 2     | /ifd/xmp/<xmpseq>exif:ISOSpeedRatings | unicode     |
| 3     | /ifd/xmp/exif:ISOSpeed                      | unicode     |



 

### Remove Paths



| Order | Path                                        |
|-------|---------------------------------------------|
| 1     | /ifd/exif/{ushort=34855}                    |
| 2     | /ifd/xmp/<xmpseq>exif:isospeedratings |
| 3     | /ifd/xmp/exif:isospeed                      |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.ISOSpeed](../properties/props-system-photo-focallengthinfilm.md)
</dt> </dl>

 

 
