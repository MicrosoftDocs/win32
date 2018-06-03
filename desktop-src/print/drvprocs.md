---
Description: The DRVPROCS structure is obsolete and is not used with the COM interfaces for Microsoft printer drivers.
ms.assetid: fcdfb7ba-cbb4-454b-b366-82d0c95b4afd
title: DRVPROCS structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DRVPROCS structure

The DRVPROCS structure is obsolete and is not used with the COM interfaces for Microsoft printer drivers.

The structure contains the addresses of helper functions that are provided to rendering plug-ins by Microsoft printer drivers.

All of the functions pointed to by members of this structure are obsolete. For information about each see:

<dl>

[**DrvWriteSpoolBuf**](drvwritespoolbuf.md)  
[**DrvXMoveTo**](drvxmoveto.md)  
[**DrvYMoveTo**](drvymoveto.md)  
[**DrvGetDriverSetting**](drvgetdriversetting.md)  
[**DrvGetStandardVariable**](drvgetstandardvariable.md) (for information about BGetStandardVariable)  
[**DrvUnidriverTextOut**](drvunidrivertextout.md)  
[**DrvWriteAbortBuf**](drvwriteabortbuf.md)  
</dl>

## Syntax


```C++
typedef struct _DRVPROCS {
  PFN_DrvWriteSpoolBuf       DrvWriteSpoolBuf;
  PFN_DrvXMoveTo             DrvXMoveTo;
  PFN_DrvYMoveTo             DrvYMoveTo;
  PFN_DrvGetDriverSetting    DrvGetDriverSetting;
  PFN_DrvGetStandardVariable BGetStandardVariable;
  PFN_DrvUnidriverTextOut    DrvUnidriverTextOut;
  PFN_DrvWriteAbortBuf       DrvWriteAbortBuf;
} DRVPROCS, *PDRVPROCS;
```



## Members

<dl> <dt>

**DrvWriteSpoolBuf**
</dt> <dd></dd> <dt>

**DrvXMoveTo**
</dt> <dd></dd> <dt>

**DrvYMoveTo**
</dt> <dd></dd> <dt>

**DrvGetDriverSetting**
</dt> <dd></dd> <dt>

**BGetStandardVariable**
</dt> <dd></dd> <dt>

**DrvUnidriverTextOut**
</dt> <dd></dd> <dt>

**DrvWriteAbortBuf**
</dt> <dd></dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DRVPROCS%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




