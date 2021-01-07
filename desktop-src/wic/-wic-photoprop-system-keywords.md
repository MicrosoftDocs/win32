---
description: The photo metadata policy for the System.Keywords property.
ms.assetid: bc9de56f-444c-45a2-9822-fba2fe618d38
title: System.Keywords Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Keywords Photo Metadata Policy

The photo metadata policy for the [System.Keywords](../properties/props-system-keywords.md) property.

### PKEY

PKEY\_Keywords

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_VECTOR \| VT\_LPWSTR

### Input PROPVARIANT Type

VT\_VECTOR \| VT\_LPWSTR is preferred. A VT\_LPWSTR containing a semicolon-delimited string is also accepted.

### Conflict Resolution Policy

Values from different schemas are merged.

### JPEG Policy

### Read Paths



| Order | Path                              | Disk Format    |
|-------|-----------------------------------|----------------|
| 1     | /xmp/<xmpbag>dc:subject     | unicode        |
| 2     | /app13/irb/8bimiptc/iptc/keywords |                |
| 3     | /app1/ifd/{ushort=18247}          | unicode\_bytes |
| 4     | /app1/ifd/{ushort=40094}          | unicode\_bytes |



 

### Write Paths



| Order | Path                                              | Disk Format    |
|-------|---------------------------------------------------|----------------|
| 1     | /xmp/<xmpbag>dc:subject                     | unicode        |
| 2     | /app13/irb/8bimiptc/iptc/keywords                 |                |
| 3     | /app1/ifd/{ushort=18247}                          | unicode\_bytes |
| 4     | /app1/ifd/{ushort=40094}                          | unicode\_bytes |
| 5     | /xmp/<xmpbag>MicrosoftPhoto:LastKeywordXMP  | unicode        |
| 6     | /xmp/<xmpbag>MicrosoftPhoto:LastKeywordIPTC | unicode        |



 

### Remove Paths



| Order | Path                                              |
|-------|---------------------------------------------------|
| 1     | /xmp/dc:subject                                   |
| 2     | /app13/irb/8bimiptc/iptc/keywords                 |
| 3     | /app1/ifd/{ushort=18247}                          |
| 4     | /app1/ifd/{ushort=40094}                          |
| 5     | /xmp/<xmpbag>MicrosoftPhoto:LastKeywordXMP  |
| 6     | /xmp/<xmpbag>MicrosoftPhoto:LastKeywordIPTC |



 

### TIFF Policy

### Read Paths



| Order | Path                              | Disk Format    |
|-------|-----------------------------------|----------------|
| 1     | /ifd/xmp/<xmpbag>dc:subject | unicode        |
| 2     | /ifd/iptc/keywords                |                |
| 3     | /ifd/{ushort=18247}               | unicode\_bytes |
| 4     | /ifd/{ushort=40094}               | unicode\_bytes |
| 5     | /ifd/irb/8bimiptc/iptc/keywords   |                |



 

### Write Paths



| Order | Path                                                             | Disk Format    |
|-------|------------------------------------------------------------------|----------------|
| 1     | /ifd/xmp/<xmpbag>dc:subject                                | unicode        |
| 2     | /ifd/iptc/keywords                                               |                |
| 3     | /ifd/irb/8bimiptc/iptc/keywords                                  |                |
| 4     | /ifd/{ushort=18247}                                              | unicode\_bytes |
| 5     | /ifd/{ushort=40094}                                              | unicode\_bytes |
| 6     | /ifd/xmp/<xmpbag>MicrosoftPhoto:LastKeywordXMP             | unicode        |
| 7     | /ifd/xmp/<xmpbag>MicrosoftPhoto:LastKeywordIPTC            | unicode        |
| 8     | /ifd/xmp/<xmpbag>MicrosoftPhoto:LastKeywordIPTC\_TIFF\_IRB | unicode        |



 

### Remove Paths



| Order | Path                                                             |
|-------|------------------------------------------------------------------|
| 1     | /ifd/xmp/dc:subject                                              |
| 2     | /ifd/iptc/keywords                                               |
| 3     | /ifd/irb/8bimiptc/iptc/keywords                                  |
| 4     | /ifd/{ushort=18247}                                              |
| 5     | /ifd/{ushort=40094}                                              |
| 6     | /ifd/xmp/<xmpbag>MicrosoftPhoto:LastKeywordXMP             |
| 7     | /ifd/xmp/<xmpbag>MicrosoftPhoto:LastKeywordIPTC            |
| 8     | /ifd/xmp/<xmpbag>MicrosoftPhoto:LastKeywordIPTC\_TIFF\_IRB |



 

### Remarks

## Related topics

<dl> <dt>

[System.Keywords](../properties/props-system-keywords.md)
</dt> </dl>

 

 
