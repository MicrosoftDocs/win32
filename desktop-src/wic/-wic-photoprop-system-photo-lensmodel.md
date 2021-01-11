---
description: The photo metadata policy for the System.Photo.LensModel property.
ms.assetid: 39aeff17-e8d3-4ceb-86a1-1749d2ca98d6
title: System.Photo.LensModel Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.LensModel Photo Metadata Policy

The photo metadata policy for the [System.Photo.LensModel](../properties/props-system-photo-lensmodel.md) property.

### PKEY

PKEY\_Photo\_LensModel

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



| Order | Path                          | Disk Format | Required |
|-------|-------------------------------|-------------|----------|
| 1     | /xmp/MicrosoftPhoto:LensModel | Unicode     | Yes      |



 

### Precedence of Paths (TIFF)

If the file is in TIFF format, the handler will use the following order of precedence when reading or writing the data.



| Order | Path                              | Disk Format | Required |
|-------|-----------------------------------|-------------|----------|
| 1     | /ifd/xmp/MicrosoftPhoto:LensModel | Unicode     | Yes      |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.LensModel](../properties/props-system-photo-lensmodel.md)
</dt> </dl>

 

 
