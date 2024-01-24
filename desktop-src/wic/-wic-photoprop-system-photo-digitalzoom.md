---
description: The photo metadata policy for the System.Photo.DigitalZoom property.
ms.assetid: 22a69d3e-4ec3-4652-b4bb-dfcfffc2322b
title: System.Photo.DigitalZoom Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.DigitalZoom Photo Metadata Policy

The photo metadata policy for the [System.Photo.DigitalZoom](../properties/props-system-photo-digitalzoom.md) property.

### PKEY

PKEY\_Photo\_DigitalZoom

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value is generated from System.Photo.DigitalZoomNumerator and System.Photo.DigitalZoomDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=41988} |             |
| 2     | /xmp/exif:DigitalZoomRatio    |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=41988} |             |
| 2     | /xmp/exif:DigitalZoomRatio    |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=41988} |
| 2     | /xmp/exif:digitalzoomratio    |



 

### TIFF Policies

### Read Paths



| Order | Path                           | Disk Format |
|-------|--------------------------------|-------------|
| 1     | /ifd/exif/{ushort=41988}       |             |
| 2     | /ifd/xmp/exif:DigitalZoomRatio |             |



 

### Write Paths



| Order | Path                           | Disk Format |
|-------|--------------------------------|-------------|
| 1     | /ifd/exif/{ushort=41988}       |             |
| 2     | /ifd/xmp/exif:DigitalZoomRatio |             |



 

### Remove Paths



| Order | Path                           |
|-------|--------------------------------|
| 1     | /ifd/exif/{ushort=41988}       |
| 2     | /ifd/xmp/exif:digitalzoomratio |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.DigitalZoom](../properties/props-system-photo-digitalzoom.md)
</dt> </dl>

 

 
