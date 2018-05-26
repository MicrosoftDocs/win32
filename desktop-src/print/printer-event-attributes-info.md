---
Description: The PRINTER\_EVENT\_ATTRIBUTES\_INFO structure contains the former attributes and the new attributes for a printer.
ms.assetid: 3c39a515-f4f4-4309-8d4e-461b8835295b
title: PRINTER\_EVENT\_ATTRIBUTES\_INFO structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PRINTER\_EVENT\_ATTRIBUTES\_INFO structure

The PRINTER\_EVENT\_ATTRIBUTES\_INFO structure contains the former attributes and the new attributes for a printer.

## Syntax


```C++
typedef struct _PRINTER_EVENT_ATTRIBUTES_INFO {
  DWORD cbSize;
  DWORD dwOldAttributes;
  DWORD dwNewAttributes;
} PRINTER_EVENT_ATTRIBUTES_INFO, *PPRINTER_EVENT_ATTRIBUTES_INFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Specifies the size of this structure.

</dd> <dt>

**dwOldAttributes**
</dt> <dd>

A set of bits describing the current printer attributes.

</dd> <dt>

**dwNewAttributes**
</dt> <dd>

A set of bits describing the new printer attributes to be applied to the printer.

</dd> </dl>

## Remarks

The bits in the **dwOldAttributes** and **dwNewAttributes** members of this structure are set in accordance with the **Attributes** member of the PRINTER\_INFO\_2 structure (defined in the Microsoft Windows SDK documentation).

Because this structure might become larger in future operating system versions, anyone using this structure is advised to check that the value in the **cbSize** member of this structure is at least as large as the offset of the member to be accessed.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



## See also

<dl> <dt>

[**DrvPrinterEvent**](drvprinterevent.md)
</dt> <dt>

[**IPrintOemUI::PrinterEvent**](iprintoemui-printerevent.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PRINTER_EVENT_ATTRIBUTES_INFO%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





