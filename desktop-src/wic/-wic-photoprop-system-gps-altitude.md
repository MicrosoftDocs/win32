---
description: The photo metadata policy for the System.GPS.Altitude property.
ms.assetid: 63d59aa3-52a6-4b6f-b6ec-a1c4abcee83f
title: System.GPS.Altitude Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.Altitude Photo Metadata Policy

The photo metadata policy for the [System.GPS.Altitude](../properties/props-system-gps-altitude.md) property.

### PKEY

PKEY\_GPS\_Altitude

### Description

The altitude is indicated as an absolute value referenced in meters.

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Input PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value can be written by writing to System.GPS.Altitude.Numerator and System.GPS.Altitude.Denominator. It cannot be written directly. The write paths in the following tables indicate where the value may be saved when it is generated, not when it is written directly. When the value is read, values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=6} |             |
| 2     | /xmp/exif:GPSAltitude    |             |



 

### Write Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=6} |             |
| 2     | /xmp/exif:GPSAltitude    |             |



 

### Remove Paths



| Order | Path                     |
|-------|--------------------------|
| 1     | /app1/ifd/gps/{ushort=6} |
| 2     | /xmp/exif:gpsaltitude    |



 

### TIFF Policies

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/gps/{ushort=6}       |             |
| 2     | /ifd/xmp/exif:GPSAltitude |             |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/gps/{ushort=6}       |             |
| 2     | /ifd/xmp/exif:GPSAltitude |             |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /ifd/gps/{ushort=6}       |
| 2     | /ifd/xmp/exif:gpsaltitude |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.Altitude](../properties/props-system-gps-altitude.md)
</dt> </dl>

 

 
