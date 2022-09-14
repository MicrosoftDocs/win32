---
description: The photo metadata policy for the System.Photo.LightSource property.
ms.assetid: 051a49ad-bb4c-459f-ae52-dc359a03a14a
title: System.Photo.LightSource Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.LightSource Photo Metadata Policy

The photo metadata policy for the [System.Photo.LightSource](../properties/props-system-photo-lightsource.md) property.

### PKEY

PKEY\_Photo\_LightSource

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_UI4

### Input Type

UShort

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37384} | ushort      |
| 2     | /xmp/exif:LightSource         | unicode     |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37384} | ushort      |
| 2     | /xmp/exif:LightSource         | unicode     |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=37384} |
| 2     | /xmp/exif:lightsource         |



 

### TIFF Policies

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/exif/{ushort=37384}  | ushort      |
| 2     | /ifd/xmp/exif:LightSource | unicode     |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/exif/{ushort=37384}  | ushort      |
| 2     | /ifd/xmp/exif:LightSource | unicode     |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /ifd/exif/{ushort=37384}  |
| 2     | /ifd/xmp/exif:lightsource |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.LightSource](../properties/props-system-photo-lightsource.md)
</dt> </dl>

 

 
