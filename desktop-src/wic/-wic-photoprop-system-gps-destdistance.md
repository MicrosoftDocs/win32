---
description: The photo metadata policy for the System.GPS.DestDistance property.
ms.assetid: 1bd72acb-f462-454d-aec2-72d5b4517de3
title: System.GPS.DestDistance Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.DestDistance Photo Metadata Policy

The photo metadata policy for the [System.GPS.DestDistance](../properties/props-system-gps-destdistance.md) property.

### PKEY

PKEY\_GPS\_DestDistance

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value is generated from System.GPS.DestDistanceNumerator and System.GPS.DestDistanceDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=26} |             |
| 2     | /xmp/exif:GPSDestDistance |             |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=26} |             |
| 2     | /xmp/exif:GPSDestDistance |             |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /app1/ifd/gps/{ushort=26} |
| 2     | /xmp/exif:gpsdestdistance |



 

### TIFF Policies

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/gps/{ushort=26}          |             |
| 2     | /ifd/xmp/exif:GPSDestDistance |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/gps/{ushort=26}          |             |
| 2     | /ifd/xmp/exif:GPSDestDistance |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /ifd/gps/{ushort=26}          |
| 2     | /ifd/xmp/exif:gpsdestdistance |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.DestDistance](../properties/props-system-gps-destdistance.md)
</dt> </dl>

 

 
