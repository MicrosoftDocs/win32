---
Description: The photo metadata policy for the System.Photo.PeopleNames property.
ms.assetid: 567d5542-fc7b-4d19-bc3c-b9d6e26e3387
title: System.Photo.PeopleNames Photo Metadata Policy
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Photo.PeopleNames Photo Metadata Policy

The photo metadata policy for the [System.Photo.PeopleNames](http://msdn.microsoft.com/en-us/library/dd391582(VS.85).aspx) property.

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

[System.Photo.ProgramMode](http://msdn.microsoft.com/en-us/library/bb760520(VS.85).aspx)
</dt> </dl>

 

 



