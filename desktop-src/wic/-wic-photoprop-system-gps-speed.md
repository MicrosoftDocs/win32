---
Description: The photo metadata policy for the System.GPS.Speed property.
ms.assetid: 278826c2-3057-4da2-8c86-0e44471ad7b0
title: System.GPS.Speed Photo Metadata Policy
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.Speed Photo Metadata Policy

The photo metadata policy for the [System.GPS.Speed](http://msdn.microsoft.com/en-us/library/bb760582(VS.85).aspx) property.

### PKEY

PKEY\_GPS\_Speed

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value is generated from System.GPS.SpeedNumerator and System.GPS.SpeedDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=13} |             |
| 2     | /xmp/exif:GPSSpeed        |             |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=13} |             |
| 2     | /xmp/exif:GPSSpeed        |             |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /app1/ifd/gps/{ushort=13} |
| 2     | /xmp/exif:gpsspeed        |



 

### TIFF Policies

### Read Paths



| Order | Path                   | Disk Format |
|-------|------------------------|-------------|
| 1     | /ifd/gps/{ushort=13}   |             |
| 2     | /ifd/xmp/exif:GPSSpeed |             |



 

### Write Paths



| Order | Path                   | Disk Format |
|-------|------------------------|-------------|
| 1     | /ifd/gps/{ushort=13}   |             |
| 2     | /ifd/xmp/exif:GPSSpeed |             |



 

### Remove Paths



| Order | Path                   |
|-------|------------------------|
| 1     | /ifd/gps/{ushort=13}   |
| 2     | /ifd/xmp/exif:gpsspeed |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.Speed](http://msdn.microsoft.com/en-us/library/bb760582(VS.85).aspx)
</dt> </dl>

 

 



