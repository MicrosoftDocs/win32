---
description: The photo metadata policy for the System.GPS.DOP property.
ms.assetid: 62efd1cc-a2ae-4e53-a0f2-4822b8c91c42
title: System.GPS.DOP Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.DOP Photo Metadata Policy

The photo metadata policy for the [System.GPS.DOP](../properties/props-system-gps-dop.md) property.

### PKEY

PKEY\_GPS\_DOP

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value can be written by writing to System.GPS.DOPNumerator and System.GPS.DOPDenominator. It cannot be written directly. Values from different schemas are reconciled.

### Precedence of Paths (JPEG)

If the file is in JPEG format, the handler will read, write, and remove the data in the following order:



| Order | Path                          | Disk Format   | Required |
|-------|-------------------------------|---------------|----------|
| 1     | /xmp/exif:GPSDOP              | XMP rational  | Yes      |
| 2     | /app1/ifd/gps/\\{ushort=11\\} | EXIF rational | No       |



 

### Precedence of Paths (TIFF)

If the file is in TIFF format, the handler will read, write, and remove the data in the following order:



| Order | Path                     | Disk Format   | Required |
|-------|--------------------------|---------------|----------|
| 1     | /ifd/xmp/exif:GPSDop     | XMP rational  | Yes      |
| 2     | /ifd/gps/\\{ushort=11\\} | EXIF rational | No       |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.DOP](../properties/props-system-gps-dop.md)
</dt> </dl>

 

 
