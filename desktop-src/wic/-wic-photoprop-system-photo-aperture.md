---
description: The photo metadata policy for the System.Photo.Aperture property.
ms.assetid: 3048eb9d-4ed4-4b5b-960e-9d0fd6704041
title: System.Photo.Aperture Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.Aperture Photo Metadata Policy

The photo metadata policy for the [System.Photo.Aperture](../properties/props-system-photo-aperture.md) property.

### PKEY

PKEY\_Photo\_Aperture

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value is generated from System.Photo.ApertureNumerator and System.Photo.ApertureDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37378} |             |
| 2     | /xmp/exif:ApertureValue       |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37378} |             |
| 2     | /xmp/exif:ApertureValue       |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=37378} |
| 2     | /xmp/exif:aperturevalue       |



 

### TIFF Policies

### Read Paths



| Order | Path                        | Disk Format |
|-------|-----------------------------|-------------|
| 1     | /ifd/exif/{ushort=37378}    |             |
| 2     | /ifd/xmp/exif:ApertureValue |             |



 

### Write Paths



| Order | Path                        | Disk Format |
|-------|-----------------------------|-------------|
| 1     | /ifd/exif/{ushort=37378}    |             |
| 2     | /ifd/xmp/exif:ApertureValue |             |



 

### Remove Paths



| Order | Path                        |
|-------|-----------------------------|
| 1     | /ifd/exif/{ushort=37378}    |
| 2     | /ifd/xmp/exif:aperturevalue |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.Aperture](../properties/props-system-photo-aperture.md)
</dt> </dl>

 

 
