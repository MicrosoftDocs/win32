---
description: The photo metadata policy for the System.Photo.MaxAperture property.
ms.assetid: 9d12d265-0b0a-44d9-bbf6-ca7d748382ee
title: System.Photo.MaxAperture Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.MaxAperture Photo Metadata Policy

The photo metadata policy for the [System.Photo.MaxAperture](../properties/props-system-photo-maxaperture.md) property.

### PKEY

PKEY\_Photo\_MaxAperture

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Input Type

Double

### Conflict Resolution Policy

This value is generated from System.Photo.MaxApertureNumerator and System.Photo.MaxApertureDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37381} |             |
| 2     | /xmp/exif:MaxApertureValue    |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37381} |             |
| 2     | /xmp/exif:MaxApertureValue    |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=37381} |
| 2     | /xmp/exif:maxaperturevalue    |



 

### TIFF Policies

### Read Paths



| Order | Path                           | Disk Format |
|-------|--------------------------------|-------------|
| 1     | /ifd/exif/{ushort=37381}       |             |
| 2     | /ifd/xmp/exif:MaxApertureValue |             |



 

### Write Paths



| Order | Path                           | Disk Format |
|-------|--------------------------------|-------------|
| 1     | /ifd/exif/{ushort=37381}       |             |
| 2     | /ifd/xmp/exif:MaxApertureValue |             |



 

### Remove Paths



| Order | Path                           |
|-------|--------------------------------|
| 1     | /ifd/exif/{ushort=37381}       |
| 2     | /ifd/xmp/exif:maxaperturevalue |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.MaxAperture](../properties/props-system-photo-maxaperture.md)
</dt> </dl>

 

 
