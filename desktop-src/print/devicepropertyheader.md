---
Description: The DEVICEPROPERTYHEADER structure is used as an input parameter to a printer interface DLL's DrvDevicePropertySheets function.
ms.assetid: f1b9cd2f-fa5b-4f34-a237-06d00badf1d1
title: DEVICEPROPERTYHEADER structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DEVICEPROPERTYHEADER structure

The DEVICEPROPERTYHEADER structure is used as an input parameter to a printer interface DLL's [**DrvDevicePropertySheets**](drvdevicepropertysheets.md) function.

## Syntax


```C++
typedef struct _DEVICEPROPERTYHEADER {
  WORD   cbSize;
  WORD   Flags;
  HANDLE hPrinter;
  LPTSTR pszPrinterName;
} DEVICEPROPERTYHEADER, *PDEVICEPROPERTYHEADER;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size, in bytes, of the DEVICEPROPERTYHEADER structure.

</dd> <dt>

**Flags**
</dt> <dd>

Is a set of flags that can be set to the following value:



| Value                        | Meaning                                                                 |
|------------------------------|-------------------------------------------------------------------------|
| DPS\_NOPERMISSION<br/> | If set, the user is not permitted to update device settings.<br/> |



 

</dd> <dt>

**hPrinter**
</dt> <dd>

Printer handle.

</dd> <dt>

**pszPrinterName**
</dt> <dd>

Pointer to a NULL-terminated string representing a printer name.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DEVICEPROPERTYHEADER%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




