---
description: The photo metadata policy for the System.Photo.FocalLength property.
ms.assetid: a282c31f-00dd-4df5-9b93-300bb9bc8f2d
title: System.Photo.FocalLength Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.FocalLength Photo Metadata Policy

The photo metadata policy for the [System.Photo.FocalLength](../properties/props-system-photo-focallength.md) property.

### PKEY

PKEY\_Photo\_FocalLength

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value is generated from System.Photo.FocalLengthNumerator and System.Photo.FocalLengthDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37386} |             |
| 2     | /xmp/exif:FocalLength         |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37386} |             |
| 2     | /xmp/exif:FocalLength         |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=37386} |
| 2     | /xmp/exif:focallength         |



 

### TIFF Policies

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/exif/{ushort=37386}  |             |
| 2     | /ifd/xmp/exif:FocalLength |             |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/exif/{ushort=37386}  |             |
| 2     | /ifd/xmp/exif:FocalLength |             |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /ifd/exif/{ushort=37386}  |
| 2     | /ifd/xmp/exif:focallength |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.FocalLength](../properties/props-system-photo-focallength.md)
</dt> </dl>

 

 
