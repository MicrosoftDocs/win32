---
description: The photo metadata policy for the System.Photo.FNumber property.
ms.assetid: 434d52cb-c98d-4860-87f7-4aedab7f8188
title: System.Photo.FNumber Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.FNumber Photo Metadata Policy

The photo metadata policy for the [System.Photo.FNumber](../properties/props-system-photo-fnumber.md) property.

### PKEY

PKEY\_Photo\_FNumber

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value is generated from System.Photo.FNumberNumerator and System.Photo.FNumberDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=33437} |             |
| 2     | /xmp/exif:FNumber             |             |



 

### Write Paths



|       |                               |             |     |
|-------|-------------------------------|-------------|-----|
| Order | Path                          | Disk Format |     |
| 1     | /app1/ifd/exif/{ushort=33437} |             |     |
| 2     | /xmp/exif:FNumber             |             |     |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=33437} |
| 2     | /xmp/exif:fnumber             |



 

### TIFF Policies

### Read Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /ifd/exif/{ushort=33437} |             |
| 2     | /ifd/xmp/exif:FNumber    |             |



 

### Write Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /ifd/exif/{ushort=33437} |             |
| 2     | /ifd/xmp/exif:FNumber    |             |



 

### Remove Paths



| Order | Path                     |
|-------|--------------------------|
| 1     | /ifd/exif/{ushort=33437} |
| 2     | /ifd/xmp/exif:fnumber    |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.FNumber](../properties/props-system-photo-fnumber.md)
</dt> </dl>

 

 
