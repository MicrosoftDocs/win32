---
Description: 'The DRIVER\_UPGRADE\_INFO\_1 structure is used as an input to a printer interface DLL''s DrvUpgradePrinter function.'
ms.assetid: 'fef7c63b-ca9e-47f4-96cb-4dafa080ddcf'
title: 'DRIVER\_UPGRADE\_INFO\_1 structure'
---

# DRIVER\_UPGRADE\_INFO\_1 structure

The DRIVER\_UPGRADE\_INFO\_1 structure is used as an input to a printer interface DLL's [**DrvUpgradePrinter**](drvupgradeprinter.md) function.

## Syntax


```C++
typedef struct _DRIVER_UPGRADE_INFO_1 {
  LPTSTR pPrinterName;
  LPTSTR pOldDriverDirectory;
} DRIVER_UPGRADE_INFO_1, *PDRIVER_UPGRADE_INFO_1;
```



## Members

<dl> <dt>

**pPrinterName**
</dt> <dd>

Pointer to a NULL-terminated string that specifies the name of the printer.

</dd> <dt>

**pOldDriverDirectory**
</dt> <dd>

Pointer to a NULL-terminated string that specifies the local directory in which the old printer driver files can be found.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



## See also

<dl> <dt>

[**DrvUpgradePrinter**](drvupgradeprinter.md)
</dt> <dt>

[**DRIVER\_UPGRADE\_INFO\_2**](driver-upgrade-info-2.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DRIVER_UPGRADE_INFO_1%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





