---
description: The photo metadata policy for the System.Photo.ExposureBias property.
ms.assetid: 00ebe037-0116-4d75-868b-d75b3e58a84d
title: System.Photo.ExposureBias Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.ExposureBias Photo Metadata Policy

The photo metadata policy for the [System.Photo.ExposureBias](../properties/props-system-photo-exposurebias.md) property.

### PKEY

PKEY\_Photo\_ExposureBias

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value is generated from System.Photo.ExposureBiasNumerator and System.Photo.ExposureBiasDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37380} |             |
| 2     | /xmp/exif:ExposureBiasValue   |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37380} |             |
| 2     | /xmp/exif:ExposureBiasValue   |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=37380} |
| 2     | /xmp/exif:exposurebiasvalue   |



 

### TIFF Policies

### Read Paths



| Order | Path                            | Disk Format |
|-------|---------------------------------|-------------|
| 1     | /ifd/exif/{ushort=37380}        |             |
| 2     | /ifd/xmp/exif:ExposureBiasValue |             |



 

### Write Paths



| Order | Path                            | Disk Format |
|-------|---------------------------------|-------------|
| 1     | /ifd/exif/{ushort=37380}        |             |
| 2     | /ifd/xmp/exif:ExposureBiasValue |             |



 

### Remove Paths



| Order | Path                            |
|-------|---------------------------------|
| 1     | /ifd/exif/{ushort=37380}        |
| 2     | /ifd/xmp/exif:exposurebiasvalue |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.ExposureBias](../properties/props-system-photo-exposurebias.md)
</dt> </dl>

 

 
