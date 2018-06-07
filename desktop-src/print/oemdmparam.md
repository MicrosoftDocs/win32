---
Description: The OEMDMPARAM structure is used as an input parameter to the IPrintOemUI::DevMode, IPrintOemUni::DevMode, and IPrintOemPS::DevMode methods.
ms.assetid: 625980d1-47eb-4427-a9e8-967b1873bbd6
title: OEMDMPARAM structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# OEMDMPARAM structure

The OEMDMPARAM structure is used as an input parameter to the [**IPrintOemUI::DevMode**](iprintoemui-devmode.md), [**IPrintOemUni::DevMode**](iprintoemuni-devmode.md), and [**IPrintOemPS::DevMode**](iprintoemps-devmode.md) methods.

## Syntax


```C++
typedef struct _OEMDMPARAM {
  DWORD    cbSize;
  PVOID    pdriverobj;
  HANDLE   hPrinter;
  HANDLE   hModule;
  PDEVMODE pPublicDMIn;
  PDEVMODE pPublicDMOut;
  PVOID    pOEMDMIn;
  PVOID    pOEMDMOut;
  DWORD    cbBufSize;
} OEMDMPARAM, *POEMDMPARAM;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Contains the size of the OEMDMPARAM structure. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**pdriverobj**
</dt> <dd>

<dl> <dt>

<span id="For_IPrintOemUI__DevMode_"></span><span id="for_iprintoemui__devmode_"></span><span id="FOR_IPRINTOEMUI__DEVMODE_"></span>For **IPrintOemUI::DevMode**:
</dt> <dd>

Not used.

</dd> <dt>

<span id="For_IPrintOemUni__DevMode_and_IPrintOemPS__DevMode_"></span><span id="for_iprintoemuni__devmode_and_iprintoemps__devmode_"></span><span id="FOR_IPRINTOEMUNI__DEVMODE_AND_IPRINTOEMPS__DEVMODE_"></span>For **IPrintOemUni::DevMode** and **IPrintOemPS::DevMode**:
</dt> <dd>

Pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> </dl> </dd> <dt>

**hPrinter**
</dt> <dd>

Handle to the printer device. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**hModule**
</dt> <dd>

Handle to the user interface plug-in module. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**pPublicDMIn**
</dt> <dd>

Pointer to the printer device's public DEVMODEW structure. Supplied by the Unidrv or Pscript5 driver. (Valid if the **DevMode** method's *dwMode* value is OEMDM\_DEFAULT, OEMDM\_CONVERT, or OEMDM\_MERGE.)

</dd> <dt>

**pPublicDMOut**
</dt> <dd>

Pointer to a location to receive public DEVMODEW structure contents. Supplied by the Unidrv or Pscript5 driver. (Valid if the **DevMode** method's *dwMode* value is OEMDM\_CONVERT or OEMDM\_MERGE.)

</dd> <dt>

**pOEMDMIn**
</dt> <dd>

Pointer to a set of private DEVMODEW members. Supplied by the Unidrv or Pscript5 driver. (Valid if the **DevMode** method's *dwMode* value is OEMDM\_CONVERT or OEMDM\_MERGE.)

</dd> <dt>

**pOEMDMOut**
</dt> <dd>

Pointer to memory allocated to receive modified private DEVMODEW contents. Supplied by the Unidrv or Pscript5 driver. (Valid if the **DevMode** method's *dwMode* value is OEMDM\_DEFAULT, OEMDM\_CONVERT or OEMDM\_MERGE.)

</dd> <dt>

**cbBufSize**
</dt> <dd>

On input, contains the caller-supplied size of memory space pointed to by **pOEMDMOut**. (Not valid if the **DevMode** method's *dwMode* value is OEMDM\_SIZE.)

On output, contains the method-supplied size of the current version of the private DEVMODEW section. (Only used if the **DevMode** method's *dwMode* value is OEMDM\_SIZE.)

</dd> </dl>

## Remarks

For more information about the use of OEMDMPARAM structure members, see the description of the [**IPrintOemUI::DevMode**](iprintoemui-devmode.md) method.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMDMPARAM%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




