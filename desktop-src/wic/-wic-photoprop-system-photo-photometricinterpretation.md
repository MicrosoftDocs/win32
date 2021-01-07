---
description: The photo metadata policy for the System.Photo.PhotometricInterpretation property.
ms.assetid: ff36b2c3-8763-4640-a049-b5880fd26929
title: System.Photo.PhotometricInterpretation Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.PhotometricInterpretation Photo Metadata Policy

The photo metadata policy for the [System.Photo.PhotometricInterpretation](../properties/props-system-photo-photometricinterpretation.md) property.

### PKEY

PKEY\_Photo\_PhotometricInterpretation

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_UI2

### Input Type

UShort

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                                | Disk Format |
|-------|-------------------------------------|-------------|
| 1     | /app1/ifd/{ushort=262}              | ushort      |
| 2     | /xmp/tiff:PhotometricInterpretation | unicode     |



 

### Write Paths



| Order | Path                                | Disk Format |
|-------|-------------------------------------|-------------|
| 1     | /app1/ifd/{ushort=262}              | ushort      |
| 2     | /xmp/tiff:PhotometricInterpretation | unicode     |



 

### Remove Paths



| Order | Path                                |
|-------|-------------------------------------|
| 1     | /app1/ifd/{ushort=262}              |
| 2     | /xmp/tiff:photometricinterpretation |



 

### TIFF Policies

### Read Paths



| Order | Path                                    | Disk Format |
|-------|-----------------------------------------|-------------|
| 1     | /ifd/{ushort=262}                       | ushort      |
| 2     | /ifd/xmp/tiff:PhotometricInterpretation | unicode     |



 

### Write Paths



| Order | Path                                    | Disk Format |
|-------|-----------------------------------------|-------------|
| 1     | /ifd/{ushort=262}                       | ushort      |
| 2     | /ifd/xmp/tiff:PhotometricInterpretation | unicode     |



 

### Remove Paths



| Order | Path                                    |
|-------|-----------------------------------------|
| 1     | /ifd/{ushort=262}                       |
| 2     | /ifd/xmp/tiff:photometricinterpretation |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.PhotometricInterpretation](../properties/props-system-photo-photometricinterpretation.md)
</dt> </dl>

 

 
