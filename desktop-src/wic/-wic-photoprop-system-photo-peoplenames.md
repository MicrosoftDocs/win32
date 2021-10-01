---
description: The photo metadata policy for the System.Photo.PeopleNames property.
ms.assetid: 567d5542-fc7b-4d19-bc3c-b9d6e26e3387
title: System.Photo.PeopleNames Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.PeopleNames Photo Metadata Policy

The photo metadata policy for the [System.Photo.PeopleNames](../properties/props-system-photo-peoplenames.md) property.

### PKEY

PKEY\_Photo\_PeopleNames

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_VECTOR \| VT\_LPWSTR

### Input Type

StringMulti

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                                                           | Disk Format |
|-------|----------------------------------------------------------------|-------------|
| 1     | /xmp/&lt;xmpstruct&gt;MP:RegionInfo/&lt;xmpbag&gt;MPRI:Regions | ushort      |



 

### Write Paths

This property cannot be written using the metadata policy.

### Remove Paths



| Order | Path                                |
|-------|-------------------------------------|
| 1     | /xmp/&lt;xmpstruct&gt;MP:RegionInfo |



 

### TIFF Policies

### Read Paths



| Order | Path                                                               | Disk Format |
|-------|--------------------------------------------------------------------|-------------|
| 1     | /ifd/xmp/&lt;xmpstruct&gt;MP:RegionInfo/&lt;xmpbag&gt;MPRI:Regions | ushort      |



 

### Write Paths

This property cannot be written using the metadata policy.

### Remove Paths



| Order | Path                                    |
|-------|-----------------------------------------|
| 1     | /ifd/xmp/&lt;xmpstruct&gt;MP:RegionInfo |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.ProgramMode](../properties/props-system-photo-programmode.md)
</dt> </dl>

 

 
