---
description: The photo metadata policy for the System.Photo.CameraModel property.
ms.assetid: ff85e6ee-dc75-45bc-a406-2290b012c22d
title: System.Photo.CameraModel Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.CameraModel Photo Metadata Policy

The photo metadata policy for the [System.Photo.CameraModel](../properties/props-system-photo-cameramodel.md) property.

### PKEY

PKEY\_Photo\_CameraModel

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

### JPEG Policy

### Read Paths



| Order | Path                   | Disk Format |
|-------|------------------------|-------------|
| 1     | /app1/ifd/{ushort=272} | ascii       |
| 2     | /xmp/tiff:Model        | unicode     |
| 3     | /xmp/tiff:model        | unicode     |



 

### Write Paths



| Order | Path                   | Disk Format |
|-------|------------------------|-------------|
| 1     | /app1/ifd/{ushort=272} | ascii       |
| 2     | /xmp/tiff:Model        | unicode     |
| 3     | /xmp/tiff:model        | unicode     |



 

### Remove Paths



| Order | Path                   |
|-------|------------------------|
| 1     | /app1/ifd/{ushort=272} |
| 2     | /xmp/tiff:Model        |
| 3     | /xmp/tiff:model        |



 

### TIFF Policy

### Read Paths



| Order | Path                | Disk Format |
|-------|---------------------|-------------|
| 1     | /ifd/{ushort=272}   | ascii       |
| 2     | /ifd/xmp/tiff:Model | unicode     |
| 3     | /ifd/xmp/tiff:model | unicode     |



 

### Write Paths



| Order | Path                | Disk Format |
|-------|---------------------|-------------|
| 1     | /ifd/{ushort=272}   | ascii       |
| 2     | /ifd/xmp/tiff:Model | unicode     |
| 3     | /ifd/xmp/tiff:model | unicode     |



 

### Remove Paths



| Order | Path                |
|-------|---------------------|
| 1     | /ifd/{ushort=272}   |
| 2     | /ifd/xmp/tiff:Model |
| 3     | /ifd/xmp/tiff:model |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.CameraModel](../properties/props-system-photo-cameramodel.md)
</dt> </dl>

 

 
