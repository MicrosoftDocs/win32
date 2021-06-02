---
description: Note  This API is deprecated. New applications should not use it. The MSPID data type identifies the purpose of a media steam.
ms.assetid: 83a84eb7-a72c-4ca7-b152-8cc81a5bfdaf
title: MSPID (Mmstream.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MSPID

> [!Note]  
> This API is deprecated. New applications should not use it.

 

The **MSPID** data type identifies the purpose of a media steam.


```C++
typedef GUID MSPID;
typedef REFGUID REFMSPID;
```



## Remarks

**MSPID** is simply a typedef for GUID. The following MSPIDs are defined.



| Value               | Description           |
|---------------------|-----------------------|
| MSPID\_PrimaryVideo | Primary video stream. |
| MSPID\_PrimaryAudio | Primary audio stream. |



 

The **REFMSPID** type defines a reference to an **MSPID**.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mmstream.h</dt> </dl> |



## See also

<dl> <dt>

[Multimedia Streaming Data Types](multimedia-streaming-data-types.md)
</dt> </dl>

 

 




