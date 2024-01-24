---
description: The photo metadata policy for the System.GPS.DestLatitude property.
ms.assetid: 05284291-977d-49b8-ad92-365f68384960
title: System.GPS.DestLatitude Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.DestLatitude Photo Metadata Policy

The photo metadata policy for the [System.GPS.DestLatitude](../properties/props-system-gps-destlatitude.md) property.

### PKEY

PKEY\_GPS\_DestLatitude

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_VECTOR \| VT\_R8

### Input PROPVARIANT Type

VT\_VECTOR \| VT\_R8

### Conflict Resolution Policy

This value is generated from System.GPS.DestLatitudeNumerator and System.GPS.DestLatitudeDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=20} |             |
| 2     | /xmp/exif:GPSDestLatitude |             |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=20} |             |
| 2     | /xmp/exif:GPSDestLatitude |             |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /app1/ifd/gps/{ushort=20} |
| 2     | /xmp/exif:gpsdestlatitude |



 

### TIFF Policies

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/gps/{ushort=20}          |             |
| 2     | /ifd/xmp/exif:GPSDestLatitude |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/gps/{ushort=20}          |             |
| 2     | /ifd/xmp/exif:GPSDestLatitude |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /ifd/gps/{ushort=20}          |
| 2     | /ifd/xmp/exif:gpsdestlatitude |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.DestLatitude](../properties/props-system-gps-destlatitude.md)
</dt> </dl>

 

 
