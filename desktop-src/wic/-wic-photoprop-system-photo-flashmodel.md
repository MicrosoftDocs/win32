---
description: The photo metadata policy for the System.Photo.FlashModel property.
ms.assetid: ef322823-1b87-40ea-a5e3-e7551f14e44d
title: System.Photo.FlashModel Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.FlashModel Photo Metadata Policy

The photo metadata policy for the [System.Photo.FlashModel](../properties/props-system-photo-flashmodel.md) property.

### PKEY

PKEY\_Photo\_FlashModel

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



| Order | Path                           | Disk Format | Data Format | Required |
|-------|--------------------------------|-------------|-------------|----------|
| 1     | /xmp/MicrosoftPhoto:FlashModel | Unicode     |             | Yes      |



 

### Precedence of Paths (TIFF)

If the file is in TIFF format, the handler will use the following order of precedence when reading or writing the data.



| Order | Path                               | Disk Format | Data Format | Required |
|-------|------------------------------------|-------------|-------------|----------|
| 1     | /ifd/xmp/MicrosoftPhoto:FlashModel | Unicode     |             | Yes      |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.FlashModel](../properties/props-system-photo-flashmodel.md)
</dt> </dl>

 

 
