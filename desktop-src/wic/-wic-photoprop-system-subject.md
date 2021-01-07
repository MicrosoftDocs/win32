---
description: The photo metadata policy for the System.Subject property.
ms.assetid: 5ab7c74b-8a5e-4329-8a49-291470d406cc
title: System.Subject Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Subject Photo Metadata Policy

The photo metadata policy for the [System.Subject](../properties/props-system-subject.md) property.

### PKEY

PKEY\_Subject

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_LPWSTR

### Input PROPVARIANT Type

Either VT\_LPWSTR or VT\_LPWSTR

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                     | Disk Format    |
|-------|--------------------------|----------------|
| 1     | /app1/ifd/{ushort=40095} | unicode\_bytes |
| 2     | /app1/ifd/{ushort=270}   | ascii          |



 

### Write Paths



| Order | Path                     | Disk Format    |
|-------|--------------------------|----------------|
| 1     | /app1/ifd/{ushort=40095} | unicode\_bytes |



 

### Remove Paths



| Order | Path                     |
|-------|--------------------------|
| 1     | /app1/ifd/{ushort=40095} |
| 2     | /app1/ifd/{ushort=270}   |



 

### TIFF Policy

### Read Paths



| Order | Path                | Disk Format    |
|-------|---------------------|----------------|
| 1     | /ifd/{ushort=40095} | unicode\_bytes |
| 2     | /ifd/{ushort=270}   | ascii          |



 

### Write Paths



| Order | Path                | Disk Format    |
|-------|---------------------|----------------|
| 1     | /ifd/{ushort=40095} | unicode\_bytes |



 

### Remove Paths



| Order | Path                |
|-------|---------------------|
| 1     | /ifd/{ushort=40095} |
| 2     | /ifd/{ushort=270}   |



 

## Remarks

## Related topics

<dl> <dt>

[System.Subject](../properties/props-system-subject.md)
</dt> </dl>

 

 
