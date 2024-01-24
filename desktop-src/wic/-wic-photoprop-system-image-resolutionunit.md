---
description: The photo metadata policy for the System.Image.ResolutionUnit property.
ms.assetid: b8b744bd-976b-4648-a04b-33607467d6ac
title: System.Image.ResolutionUnit Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Image.ResolutionUnit Photo Metadata Policy

The photo metadata policy for the [System.Image.ResolutionUnit](../properties/props-system-image-resolutionunit.md) property.

### PKEY

PKEY\_Image\_ResolutionUnit

### Containers

JPEG, TIFF

### Read-Only

Yes.

### Output PROPVARIANT Type

VT\_I2

### Input Type

UShort

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /app1/ifd/{ushort=296}   | ushort      |
| 2     | /xmp/tiff:ResolutionUnit | unicode     |



 

### Write Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /app1/ifd/{ushort=296}   | ushort      |
| 2     | /xmp/tiff:ResolutionUnit | unicode     |



 

### Remove Paths



| Order | Path                     |
|-------|--------------------------|
| 1     | /app1/ifd/{ushort=296}   |
| 2     | /xmp/tiff:resolutionunit |



 

### TIFF Policies

### Read Paths



| Order | Path                         | Disk Format |
|-------|------------------------------|-------------|
| 1     | /ifd/{ushort=296}            | ushort      |
| 2     | /ifd/xmp/tiff:ResolutionUnit | unicode     |



 

### Write Paths



| Order | Path                         | Disk Format |
|-------|------------------------------|-------------|
| 1     | /ifd/{ushort=296}            | ushort      |
| 2     | /ifd/xmp/tiff:ResolutionUnit | unicode     |



 

### Remove Paths



| Order | Path                         |
|-------|------------------------------|
| 1     | /ifd/{ushort=296}            |
| 2     | /ifd/xmp/tiff:resolutionunit |



 

## Remarks

## Related topics

<dl> <dt>

[System.Image.ResolutionUnit](../properties/props-system-image-resolutionunit.md)
</dt> </dl>

 

 
