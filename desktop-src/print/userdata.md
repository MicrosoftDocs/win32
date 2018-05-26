---
Description: The USERDATA structure is used by Unidrv and Pscript to specify additional information about printer features. A USERDATA structure pointer is supplied as the UserData member for each OPTITEM structure.
ms.assetid: 2a0a74cd-2dcf-4485-8941-7f205dcecede
title: USERDATA structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# USERDATA structure

The USERDATA structure is used by [*Unidrv*](wdkgloss.u#wdkgloss-unidrv) and [*Pscript*](wdkgloss.p#wdkgloss-pscript) to specify additional information about printer features. A USERDATA structure pointer is supplied as the **UserData** member for each [**OPTITEM**](optitem.md) structure.

## Syntax


```C++
typedef struct _USERDATA {
  DWORD     dwSize;
  ULONG_PTR dwItemID;
  PSTR      pKeyWordName;
  DWORD     dwReserved[8];
} USERDATA, *PUSERDATA;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Size, in bytes, of the USERDATA structure.

</dd> <dt>

**dwItemID**
</dt> <dd>

Printer feature identifier.

</dd> <dt>

**pKeyWordName**
</dt> <dd>

Pointer to a nonlocalized text string identifying a printer feature.

</dd> <dt>

**dwReserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20USERDATA%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




