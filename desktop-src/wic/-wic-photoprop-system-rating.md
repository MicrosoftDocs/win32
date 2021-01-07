---
description: The photo metadata policy for the System.Rating property.
ms.assetid: e4d2c12e-617a-431e-9062-62acf6ef21c8
title: System.Rating Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Rating Photo Metadata Policy

The photo metadata policy for the [System.Rating](../properties/props-system-rating.md) property.

### PKEY

PKEY\_Rating

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_UI4

### Input PROPVARIANT Type

May be VT\_UI1, VT\_UI2, or VT\_UI4. The value may range from 0 to 99.

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                       | Disk Format |
|-------|----------------------------|-------------|
| 1     | /app1/ifd/{ushort=18249}   | ushort      |
| 2     | /xmp/MicrosoftPhoto:Rating | unicode     |



 

### Write Paths



| Order | Path                       | Disk Format |
|-------|----------------------------|-------------|
| 1     | /app1/ifd/{ushort=18249}   | ushort      |
| 2     | /xmp/MicrosoftPhoto:Rating | unicode     |



 

### Remove Paths



| Order | Path                       |
|-------|----------------------------|
| 1     | /app1/ifd/{ushort=18249}   |
| 2     | /xmp/microsoftphoto:rating |



 

### TIFF Policies

### Read Paths



| Order | Path                           | Disk Format |
|-------|--------------------------------|-------------|
| 1     | /ifd/{ushort=18249}            | ushort      |
| 2     | /ifd/xmp/MicrosoftPhoto:Rating | unicode     |



 

### Write Paths



| Order | Path                           | Disk Format |
|-------|--------------------------------|-------------|
| 1     | /ifd/{ushort=18249}            | ushort      |
| 2     | /ifd/xmp/MicrosoftPhoto:Rating | unicode     |



 

### Remove Paths



| Order | Path                           |
|-------|--------------------------------|
| 1     | /ifd/{ushort=18249}            |
| 2     | /ifd/xmp/microsoftphoto:rating |



 

## Remarks

## Related topics

<dl> <dt>

[System.Rating](../properties/props-system-rating.md)
</dt> </dl>

 

 
