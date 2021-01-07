---
description: The photo metadata policy for the System.Photo.Contrast property.
ms.assetid: c5e2589d-507c-4b92-9ada-7d64e7c45dd8
title: System.Photo.Contrast Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.Contrast Photo Metadata Policy

The photo metadata policy for the [System.Photo.Contrast](../properties/props-system-photo-contrast.md) property.

### PKEY

PKEY\_Photo\_Contrast

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
| 1     | /app1/ifd/exif/{ushort=41992} | ushort      |
| 2     | /xmp/exif:Contrast            | unicode     |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=41992} | ushort      |
| 2     | /xmp/exif:Contrast            | unicode     |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=41992} |
| 2     | /xmp/exif:contrast            |



 

### TIFF Policies

### Read Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /ifd/exif/{ushort=41992} | ushort      |
| 2     | /ifd/xmp/exif:Contrast   | unicode     |



 

### Write Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /ifd/exif/{ushort=41992} | ushort      |
| 2     | /ifd/xmp/exif:Contrast   | unicode     |



 

### Remove Paths



| Order | Path                     |
|-------|--------------------------|
| 1     | /ifd/exif/{ushort=41992} |
| 2     | /ifd/xmp/exif:contrast   |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.Contrast](../properties/props-system-photo-contrast.md)
</dt> </dl>

 

 
