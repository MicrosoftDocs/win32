---
description: The photo metadata policy for the System.Photo.Brightness property.
ms.assetid: 3fd73845-f1d9-468c-abf8-081109880974
title: System.Photo.Brightness Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.Brightness Photo Metadata Policy

The photo metadata policy for the [System.Photo.Brightness](../properties/props-system-photo-aperture.md) property.

### PKEY

PKEY\_Photo\_Brightness

### Containers

JPEG, TIFF

### Read-Only

Yes

### Input Type

Double

### Conflict Resolution Policy

This value is generated from System.Photo.ApertureNumerator and System.Photo.ApertureDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37379} |             |
| 2     | /xmp/exif:BrightnessValue     |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37379} |             |
| 2     | /xmp/exif:BrightnessValue     |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=37379} |
| 2     | /xmp/exif:brightnessvalue     |



 

### TIFF Policies

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/exif/{ushort=37379}      |             |
| 2     | /ifd/xmp/exif:BrightnessValue |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/exif/{ushort=37379}      |             |
| 2     | /ifd/xmp/exif:BrightnessValue |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /ifd/exif/{ushort=37379}      |
| 2     | /ifd/xmp/exif:brightnessvalue |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.Brightness](../properties/props-system-photo-aperture.md)
</dt> </dl>

 

 
