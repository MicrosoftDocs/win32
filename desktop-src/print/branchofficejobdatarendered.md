---
Description: Contains the necessary data for logging a branch office job Pipeline Rendering Event on a remote server. This is based on job-related data available to the spooler.
ms.assetid: 67A296B3-5D59-475E-9026-EDAB90C8E3DD
title: BranchOfficeJobDataRendered structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BranchOfficeJobDataRendered structure

Contains the necessary data for logging a branch office job Pipeline Rendering Event on a remote server. This is based on job-related data available to the spooler.

## Syntax


```C++
typedef struct {
  LONGLONG Size;
  DWORD    ICMMethod;
  short    Color;
  short    PrintQuality;
  short    YResolution;
  short    Copies;
  short    TTOption;
} BranchOfficeJobDataRendered, *PBranchOfficeJobDataRendered;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Specifies the 64-bit size of the job.

</dd> <dt>

**ICMMethod**
</dt> <dd>

Describes the **DWORD** type member **ICMMethod**.

</dd> <dt>

**Color**
</dt> <dd>

Describes the **short** type member **Color**.

</dd> <dt>

**PrintQuality**
</dt> <dd>

Describes the **short** type member **PrintQuality**.

</dd> <dt>

**YResolution**
</dt> <dd>

Describes the **short** type member **YResolution**.

</dd> <dt>

**Copies**
</dt> <dd>

Describes the **short** type member **Copies**.

</dd> <dt>

**TTOption**
</dt> <dd>

Describes the **short** type member **TTOption**.

</dd> </dl>

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20BranchOfficeJobDataRendered%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




