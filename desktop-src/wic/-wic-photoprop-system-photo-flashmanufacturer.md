---
description: The photo metadata policy for the System.Photo.FlashManufacturer property.
ms.assetid: f62e85ec-2dc6-456b-a43b-7b76d162b608
title: System.Photo.FlashManufacturer Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.FlashManufacturer Photo Metadata Policy

The photo metadata policy for the [System.Photo.FlashManufacturer](../properties/props-system-photo-flashmanufacturer.md) property.

### PKEY

PKEY\_Photo\_FlashManufacturer

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



| Order | Path                                  | Disk Format | Data Format | Required |
|-------|---------------------------------------|-------------|-------------|----------|
| 1     | /xmp/MicrosoftPhoto:FlashManufacturer | Unicode     |             | Yes      |



 

### Precedence of Paths (TIFF)

If the file is in TIFF format, the handler will use the following order of precedence when reading or writing the data.



| Order | Path                                      | Disk Format | Data Format | Required |
|-------|-------------------------------------------|-------------|-------------|----------|
| 1     | /ifd/xmp/MicrosoftPhoto:FlashManufacturer | Unicode     |             | Yes      |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.FlashManufacturer](../properties/props-system-photo-flashmanufacturer.md)
</dt> </dl>

 

 
