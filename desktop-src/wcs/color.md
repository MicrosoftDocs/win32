---
title: COLOR union
description: Description of the COLOR union.
ms.assetid: af0b0522-b519-4fe8-8dab-3d9f40643902
keywords:
- COLOR union Windows Color System
ms.localizationpriority: high
s.topic: structure
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# COLOR union

Description of the COLOR union.

## Syntax


```C++
typedef union tagCOLOR {
  struct GRAYCOLOR  gray;
  struct RGBCOLOR  rbg;
  struct CMYKCOLOR  cmyk;
  struct XYZCOLOR  XYZ;
  struct YxyCOLOR  Yxy;
  struct LabCOLOR  Lab;
  struct GENERIC3CHANNEL  gen3ch;
  struct NAMEDCOLOR  named;
  struct HiFiCOLOR  hifi;
  struct {
    DWORD reserved1;
    VOID  *reserved2;
  };
} COLOR;
```



## Members

<dl> <dt>

**gray**
</dt> <dd>

TBD

</dd> <dt>

**rbg**
</dt> <dd>

TBD

</dd> <dt>

**cmyk**
</dt> <dd>

TBD

</dd> <dt>

**XYZ**
</dt> <dd>

TBD

</dd> <dt>

**Yxy**
</dt> <dd>

TBD

</dd> <dt>

**Lab**
</dt> <dd>

TBD

</dd> <dt>

**gen3ch**
</dt> <dd>

TBD

</dd> <dt>

**named**
</dt> <dd>

TBD

</dd> <dt>

**hifi**
</dt> <dd>

TBD

</dd> <dt>

**reserved1**
</dt> <dd>

TBD

</dd> <dt>

**reserved2**
</dt> <dd>

TBD

</dd> </dl>

## Remarks

A variable of type COLOR may be accessed as any of the supported color space colors by accessing the appropriate member of the union. For instance, given the following variable declaration:

`COLOR aColor;`

the red, green and blue values could be set in the following manner:

`aColor.rgb.red=100;`

`aColor.rgb.green=50;`

`aColor.rgb.blue=2;`

## Requirements



|                   |                                                                                  |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Icm.h</dt> </dl> |



 

 





