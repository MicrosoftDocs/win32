---
description: The photo metadata policy for the System.GPS.AreaInformation property.
ms.assetid: d9ecb00b-1f97-4f53-909f-30231104d398
title: System.GPS.AreaInformation Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.AreaInformation Photo Metadata Policy

The photo metadata policy for the [System.GPS.AreaInformation](../properties/props-system-gps-areainformation.md) property.

### PKEY

PKEY\_GPS\_AreaInformation

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_LPWSTR

### Input Type

String.

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policies

### Read Paths



| Order | Path                         | Disk Format |
|-------|------------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=28}    |             |
| 2     | /xmp/exif:GPSAreaInformation | unicode     |



 

### Write Paths



| Order | Path                         | Disk Format |
|-------|------------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=28}    |             |
| 2     | /xmp/exif:GPSAreaInformation | unicode     |



 

### Remove Paths



| Order | Path                         |
|-------|------------------------------|
| 1     | /app1/ifd/gps/{ushort=28}    |
| 2     | /xmp/exif:GPSAreaInformation |



 

### TIFF Policies

### Read Paths



| Order | Path                             | Disk Format |
|-------|----------------------------------|-------------|
| 1     | /ifd/gps/{ushort=28}             |             |
| 2     | /ifd/xmp/exif:GPSAreaInformation | unicode     |



 

### Write Paths



| Order | Path                             | Disk Format |
|-------|----------------------------------|-------------|
| 1     | /ifd/gps/{ushort=28}             |             |
| 2     | /ifd/xmp/exif:GPSAreaInformation | unicode     |



 

### Remove Paths



| Order | Path                             |
|-------|----------------------------------|
| 1     | /ifd/gps/{ushort=28}             |
| 2     | /ifd/xmp/exif:GPSAreaInformation |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.AreaInformation](../properties/props-system-gps-areainformation.md)
</dt> </dl>

 

 
