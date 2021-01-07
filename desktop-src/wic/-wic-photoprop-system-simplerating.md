---
description: The photo metadata policy for the System.SimpleRating property.
ms.assetid: d932a251-f238-4582-a1c4-cf4855f26fb3
title: System.SimpleRating Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.SimpleRating Photo Metadata Policy

The photo metadata policy for the [System.SimpleRating](../properties/props-system-simplerating.md) property.

### PKEY

PKEY\_SimpleRating

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_UI4

### Input PROPVARIANT Type

May be VT\_UI1, VT\_UI2, or VT\_UI4. The integer value may range from 0 to 5.

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /app1/ifd/{ushort=18246} | ushort      |
| 2     | /xmp/xmp:Rating          | unicode     |



 

### Write Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /app1/ifd/{ushort=18246} | ushort      |
| 2     | /xmp/xmp:Rating          | unicode     |



 

### Remove Paths



| Order | Path                     |
|-------|--------------------------|
| 1     | /app1/ifd/{ushort=18246} |
| 2     | /xmp/xmp:rating          |



 

### TIFF Policies

### Read Paths



| Order | Path                | Disk Format |
|-------|---------------------|-------------|
| 1     | /ifd/{ushort=18246} | ushort      |
| 2     | /ifd/xmp/xmp:Rating | unicode     |



 

### Write Paths



| Order | Path                | Disk Format |
|-------|---------------------|-------------|
| 1     | /ifd/{ushort=18246} | ushort      |
| 2     | /ifd/xmp/xmp:Rating | unicode     |



 

### Remove Paths



| Order | Path                |
|-------|---------------------|
| 1     | /ifd/{ushort=18246} |
| 2     | /ifd/xmp/xmp:rating |



 

## Remarks

## Related topics

<dl> <dt>

[System.SimpleRating](../properties/props-system-simplerating.md)
</dt> </dl>

 

 
