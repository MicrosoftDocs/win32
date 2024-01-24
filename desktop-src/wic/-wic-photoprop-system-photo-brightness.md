---
description: The photo metadata policy for the System.Photo.Brightness property.
ms.assetid: 3fd73845-f1d9-468c-abf8-081109880974
title: System.Photo.Brightness Photo Metadata Policy
ms.topic: article
ms.date: 10/19/2021
---

# System.Photo.Brightness photo metadata policy

The photo metadata policy for the [System.Photo.Brightness](/windows/win32/properties/props-system-photo-brightness) property.

### PKEY

PKEY\_Photo\_Brightness

### Containers

JPEG, TIFF

### Read-only

Yes

### Input type

Double

### Conflict-resolution policy

This value is generated from [System.Photo.BrightnessNumerator](/windows/win32/properties/props-system-photo-brightnessnumerator) and [System.Photo.BrightnessDenominator](/windows/win32/properties/props-system-photo-brightnessdenominator). It can't be written directly. Values from different schemas are reconciled.

### JPEG policy

### Read paths

| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37379} |             |
| 2     | /xmp/exif:BrightnessValue     |             |

### Write paths

| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37379} |             |
| 2     | /xmp/exif:BrightnessValue     |             |

### Remove paths

| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=37379} |
| 2     | /xmp/exif:brightnessvalue     |

### TIFF policies

### Read paths

| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/exif/{ushort=37379}      |             |
| 2     | /ifd/xmp/exif:BrightnessValue |             |

### Write paths

| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/exif/{ushort=37379}      |             |
| 2     | /ifd/xmp/exif:BrightnessValue |             |

### Remove paths

| Order | Path                          |
|-------|-------------------------------|
| 1     | /ifd/exif/{ushort=37379}      |
| 2     | /ifd/xmp/exif:brightnessvalue |

## Remarks

## Related topics

* [System.Photo.Brightness](../properties/props-system-photo-aperture.md)

