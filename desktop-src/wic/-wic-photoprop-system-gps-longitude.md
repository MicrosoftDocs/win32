---
description: The photo metadata policy for the System.GPS.Longitude property.
ms.assetid: 36539e20-d00c-4bbb-b9ee-1cf5e4b8df4b
title: System.GPS.Longitude Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.Longitude Photo Metadata Policy

The photo metadata policy for the [System.GPS.Longitude](../properties/props-system-gps-longitude.md) property.

### PKEY

PKEY\_GPS\_Longitude

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_VECTOR \| VT\_R8

### Conflict Resolution Policy

This value can be written by writing to System.GPS.LongitudeNumerator and System.GPS.LongitudeDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=4} |             |
| 2     | /xmp/exif:GPSLongitude   |             |



 

### Write Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=4} |             |
| 2     | /xmp/exif:GPSLongitude   |             |



 

### Remove Paths



| Order | Path                     |
|-------|--------------------------|
| 1     | /app1/ifd/gps/{ushort=4} |
| 2     | /xmp/exif:gpslongitude   |



 

### TIFF Policies

### Read Paths



| Order | Path                       | Disk Format |
|-------|----------------------------|-------------|
| 1     | /ifd/gps/{ushort=4}        |             |
| 2     | /ifd/xmp/exif:GPSLongitude |             |



 

### Write Paths



| Order | Path                       | Disk Format |
|-------|----------------------------|-------------|
| 1     | /ifd/gps/{ushort=4}        |             |
| 2     | /ifd/xmp/exif:GPSLongitude |             |



 

### Remove Paths



| Order | Path                       |
|-------|----------------------------|
| 1     | /ifd/gps/{ushort=4}        |
| 2     | /ifd/xmp/exif:gpslongitude |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.Longitude](../properties/props-system-gps-longitude.md)
</dt> </dl>

 

 
