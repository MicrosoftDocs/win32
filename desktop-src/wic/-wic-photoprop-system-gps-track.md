---
description: The photo metadata policy for the System.GPS.Track property.
ms.assetid: ac9e14a0-55f1-437e-9d27-df0fa09671c1
title: System.GPS.Track Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.Track Photo Metadata Policy

The photo metadata policy for the [System.GPS.Track](../properties/props-system-gps-track.md) property.

### PKEY

PKEY\_GPS\_Track

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value is generated from System.GPS.TrackNumerator and System.GPS.TrackDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=15} |             |
| 2     | /xmp/exif:GPSTrack        |             |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=15} |             |
| 2     | /xmp/exif:GPSTrack        |             |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /app1/ifd/gps/{ushort=15} |
| 2     | /xmp/exif:gpstrack        |



 

### TIFF Policies

### Read Paths



| Order | Path                   | Disk Format |
|-------|------------------------|-------------|
| 1     | /ifd/gps/{ushort=15}   |             |
| 2     | /ifd/xmp/exif:GPSTrack |             |



 

### Write Paths



| Order | Path                   | Disk Format |
|-------|------------------------|-------------|
| 1     | /ifd/gps/{ushort=15}   |             |
| 2     | /ifd/xmp/exif:GPSTrack |             |



 

### Remove Paths



| Order | Path                   |
|-------|------------------------|
| 1     | /ifd/gps/{ushort=15}   |
| 2     | /ifd/xmp/exif:gpstrack |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.Track](../properties/props-system-gps-track.md)
</dt> </dl>

 

 
