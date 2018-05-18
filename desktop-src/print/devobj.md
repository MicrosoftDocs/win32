---
Description: 'The DEVOBJ structure is used as an input argument to several of a rendering plug-in''s COM interface methods.'
ms.assetid: 'cdcd0437-e4fc-4041-827f-caa3c435325c'
title: DEVOBJ structure
---

# DEVOBJ structure

The DEVOBJ structure is used as an input argument to several of a rendering plug-in's COM interface methods.

## Syntax


```C++
typedef struct _DEVOBJ {
  DWORD     dwSize;
  PDEVOEM   pdevOEM;
  HANDLE    hEngine;
  HANDLE    hPrinter;
  HANDLE    hOEM;
  PDEVMODE  pPublicDM;
  PVOID     pOEMDM;
  PDRVPROCS pDrvProcs;
} DEVOBJ;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Specifies the size, in bytes, of the DEVOBJ structure. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**pdevOEM**
</dt> <dd>

Pointer to the rendering plug-in's private PDEV structure, as returned by [**IPrintOemUni::EnablePDEV**](iprintoemuni-enablepdev.md) or [**IPrintOemPS::EnablePDEV**](iprintoemps-enablepdev.md). Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**hEngine**
</dt> <dd>

GDI handle to the physical device. This handle is received by the printer driver's [**DrvCompletePDEV**](display.drvcompletepdev) function, as the function's *hdev* argument.

</dd> <dt>

**hPrinter**
</dt> <dd>

Spooler's handle to the printer. This handle is received by the printer driver's [**DrvEnablePDEV**](display.drvenablepdev) function, as the function's *hDriver* argument.

</dd> <dt>

**hOEM**
</dt> <dd>

Plug-in instance handle. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**pPublicDM**
</dt> <dd>

Pointer to the printer's [**DEVMODEW**](display.devmodew) structure. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**pOEMDM**
</dt> <dd>

Pointer to the rendering plug-in's private DEVMODEW structure members. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**pDrvProcs**
</dt> <dd>

Not used. In a previous version of the interface, this was a pointer to a [**DRVPROCS**](drvprocs.md) structure.

</dd> </dl>

## Remarks

The DEVOBJ structure is accessible to graphics DDI hooking functions through the [**SURFOBJ**](display.surfobj) structure's **dhpdev** member. For more information, see [**IPrintOemUni::EnablePDEV**](iprintoemuni-enablepdev.md) or [**IPrintOemPS::EnablePDEV**](iprintoemps-enablepdev.md).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUni::EnablePDEV**](iprintoemuni-enablepdev.md)
</dt> <dt>

[**IPrintOemPS::EnablePDEV**](iprintoemps-enablepdev.md)
</dt> <dt>

[**DrvCompletePDEV**](display.drvcompletepdev)
</dt> <dt>

[**DrvEnablePDEV**](display.drvenablepdev)
</dt> <dt>

[**DEVMODEW**](display.devmodew)
</dt> <dt>

[**SURFOBJ**](display.surfobj)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DEVOBJ%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





