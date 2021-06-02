---
description: The photo metadata policy for the System.GPS.Latitude property.
ms.assetid: 0f8cea07-da96-4d2a-8444-6073b51e1236
title: System.GPS.Latitude Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.Latitude Photo Metadata Policy

The photo metadata policy for the [System.GPS.Latitude](../properties/props-system-gps-latitude.md) property.

### PKEY

PKEY\_GPS\_Latitude

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_VECTOR \| VT\_R8

### Conflict Resolution Policy

This value can be written by writing to System.GPS.LatitudeNumerator and System.GPS.LatitudeDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=2} |             |
| 2     | /xmp/exif:GPSLatitude    |             |



 

### Write Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=2} |             |
| 2     | /xmp/exif:GPSLatitude    |             |



 

### Remove Paths



| Order | Path                     |
|-------|--------------------------|
| 1     | /app1/ifd/gps/{ushort=2} |
| 2     | /xmp/exif:gpslatitude    |



 

### TIFF Policies

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/gps/{ushort=2}       |             |
| 2     | /ifd/xmp/exif:GPSLatitude |             |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/gps/{ushort=2}       |             |
| 2     | /ifd/xmp/exif:GPSLatitude |             |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /ifd/gps/{ushort=2}       |
| 2     | /ifd/xmp/exif:gpslatitude |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.Latitude](../properties/props-system-gps-latitude.md)
</dt> </dl>

 

 
