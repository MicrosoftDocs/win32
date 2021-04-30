---
description: The photo metadata policy for the System.GPS.DestLongitude property.
ms.assetid: 885a522d-e1bf-43fb-a996-97e725b6cf0c
title: System.GPS.DestLongitude Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.DestLongitude Photo Metadata Policy

The photo metadata policy for the [System.GPS.DestLongitude](../properties/props-system-gps-destlongitude.md) property.

### PKEY

PKEY\_GPS\_DestLongitude

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_VECTOR \| VT\_R8

### Input PROPVARIANT Type

VT\_VECTOR \| VT\_R8

### Conflict Resolution Policy

This value is generated from System.GPS.DestLongitudeNumerator and System.GPS.DestLongitudeDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                       | Disk Format |
|-------|----------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=22}  |             |
| 2     | /xmp/exif:GPSDestLongitude |             |



 

### Write Paths



| Order | Path                       | Disk Format |
|-------|----------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=22}  |             |
| 2     | /xmp/exif:GPSDestLongitude |             |



 

### Remove Paths



| Order | Path                       |
|-------|----------------------------|
| 1     | /app1/ifd/gps/{ushort=22}  |
| 2     | /xmp/exif:gpsdestlongitude |



 

### TIFF Policies

### Read Paths



| Order | Path                           | Disk Format |
|-------|--------------------------------|-------------|
| 1     | /ifd/gps/{ushort=22}           |             |
| 2     | /ifd/xmp/exif:GPSDestLongitude |             |



 

### Write Paths



| Order | Path                           | Disk Format |
|-------|--------------------------------|-------------|
| 1     | /ifd/gps/{ushort=22}           |             |
| 2     | /ifd/xmp/exif:GPSDestLongitude |             |



 

### Remove Paths



| Order | Path                           |
|-------|--------------------------------|
| 1     | /ifd/gps/{ushort=22}           |
| 2     | /ifd/xmp/exif:gpsdestlongitude |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.DestLongitude](../properties/props-system-gps-destlongitude.md)
</dt> </dl>

 

 
