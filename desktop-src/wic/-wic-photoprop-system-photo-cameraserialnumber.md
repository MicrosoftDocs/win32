---
description: The photo metadata policy for the System.Photo.CameraSerialNumber property.
ms.assetid: 85f78f45-5e76-4d52-88a2-ac3c9e2b6a1e
title: System.Photo.CameraSerialNumber Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.CameraSerialNumber Photo Metadata Policy

The photo metadata policy for the [System.Photo.CameraSerialNumber](../properties/props-system-photo-cameraserialnumber.md) property.

### PKEY

PKEY\_Photo\_CameraSerialNumber

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

If the file is in JPEG format, the handler will read, write, and remove the data from the following path:



| Order | Path                                   | Disk Format | Required |
|-------|----------------------------------------|-------------|----------|
| 1     | /xmp/MicrosoftPhoto:CameraSerialNumber | Unicode     | Yes      |



 

### Precedence of Paths (TIFF)

If the file is in TIFF format, the handler will read, write, and remove the data from the following path



| Order | Path                                       | Disk Format | Required |
|-------|--------------------------------------------|-------------|----------|
| 1     | /ifd/xmp/MicrosoftPhoto:CameraSerialNumber | Unicode     | Yes      |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.CameraSerialNumber](../properties/props-system-photo-cameraserialnumber.md)
</dt> </dl>

 

 
