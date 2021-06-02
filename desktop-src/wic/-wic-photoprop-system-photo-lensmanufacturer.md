---
description: The photo metadata policy for the System.Photo.LensManufacturer property.
ms.assetid: ee25da96-982f-475e-8957-e24ef7721b78
title: System.Photo.LensManufacturer Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.LensManufacturer Photo Metadata Policy

The photo metadata policy for the [System.Photo.LensManufacturer](../properties/props-system-photo-lensmanufacturer.md) property.

### PKEY

PKEY\_Photo\_LensManufacturer

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_LPWSTR

### Input Type

String.

### Conflict Resolution Policy

Values from different schemas are reconciled.

### Precedence of Paths (JPEG)

If the file is in JPEG format, the handler will use the following path when reading or writing the data.



| Order | Path                                 | Disk Format | Required |
|-------|--------------------------------------|-------------|----------|
| 1     | /xmp/MicrosoftPhoto:LensManufacturer | Unicode     | Yes      |



 

### Precedence of Paths (TIFF)

If the file is in TIFF format, the handler will use the following order of precedence when reading or writing the data.



| Order | Path                                     | Disk Format | Required |
|-------|------------------------------------------|-------------|----------|
| 1     | /ifd/xmp/MicrosoftPhoto:LensManufacturer | Unicode     | Yes      |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.LensManufacturer](../properties/props-system-photo-lensmanufacturer.md)
</dt> </dl>

 

 
