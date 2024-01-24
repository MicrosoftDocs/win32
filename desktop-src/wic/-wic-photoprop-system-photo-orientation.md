---
description: The photo metadata policy for the System.Photo.Orientation property.
ms.assetid: 27e6d4f5-39d5-4cb4-88bc-b0d61ccaa2f3
title: System.Photo.Orientation Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.Orientation Photo Metadata Policy

The photo metadata policy for the [System.Photo.Orientation](../properties/props-system-photo-meteringmode.md) property.

### PKEY

PKEY\_Photo\_Orientation

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_UI2

### Input Type

UShort

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                   | Disk Format |
|-------|------------------------|-------------|
| 1     | /app1/ifd/{ushort=274} | ushort      |
| 2     | /xmp/tiff:Orientation  | unicode     |



 

### Write Paths



| Order | Path                   | Disk Format |
|-------|------------------------|-------------|
| 1     | /app1/ifd/{ushort=274} | ushort      |
| 2     | /xmp/tiff:Orientation  | unicode     |



 

### Remove Paths



| Order | Path                   |
|-------|------------------------|
| 1     | /app1/ifd/{ushort=274} |
| 2     | /xmp/tiff:orientation  |



 

### TIFF Policies

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/{ushort=274}         | ushort      |
| 2     | /ifd/xmp/tiff:Orientation | unicode     |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/{ushort=274}         | ushort      |
| 2     | /ifd/xmp/tiff:Orientation | unicode     |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /ifd/{ushort=274}         |
| 2     | /ifd/xmp/tiff:orientation |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.Orientation](../properties/props-system-photo-meteringmode.md)
</dt> </dl>

 

 
