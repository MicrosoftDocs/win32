---
Description: The photo metadata policy for the System.Photo.FlashEnergy property.
ms.assetid: d10a4de9-16fe-4920-aa7f-b2f95fb23045
title: System.Photo.FlashEnergy Photo Metadata Policy
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Photo.FlashEnergy Photo Metadata Policy

The photo metadata policy for the [System.Photo.FlashEnergy](http://msdn.microsoft.com/en-us/library/bb760447(VS.85).aspx) property.

### PKEY

PKEY\_Photo\_FlashEnergy

### Containers

JPEG, TIFF

### Read-Only

Yes

### Input Type

Double

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=41483} |             |
| 2     | /xmp/exif:FlashEnergy         |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=41483} |             |
| 2     | /xmp/exif:FlashEnergy         |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=41483} |
| 2     | /xmp/exif:flashenergy         |



 

### TIFF Policies

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/exif/{ushort=41483}  |             |
| 2     | /ifd/xmp/exif:FlashEnergy |             |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/exif/{ushort=41483}  |             |
| 2     | /ifd/xmp/exif:FlashEnergy |             |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /ifd/exif/{ushort=41483}  |
| 2     | /ifd/xmp/exif:flashenergy |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.FlashEnergy](http://msdn.microsoft.com/en-us/library/bb760447(VS.85).aspx)
</dt> </dl>

 

 



