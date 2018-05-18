---
Description: 'The OEMUIPSPARAM structure is passed to a user interface plug-in''s IPrintOemUI::DevicePropertySheets and IPrintOemUI::DocumentPropertySheets methods.'
ms.assetid: 'e7708b33-b032-41b9-84f9-6c5b38044f9c'
title: OEMUIPSPARAM structure
---

# OEMUIPSPARAM structure

The OEMUIPSPARAM structure is passed to a user interface plug-in's [**IPrintOemUI::DevicePropertySheets**](iprintoemui-devicepropertysheets.md) and [**IPrintOemUI::DocumentPropertySheets**](iprintoemui-documentpropertysheets.md) methods.

## Syntax


```C++
typedef struct _OEMUIPSPARAM {
  DWORD     cbSize;
  POEMUIOBJ poemuiobj;
  HANDLE    hPrinter;
  PWSTR     pPrinterName;
  HANDLE    hModule;
  HANDLE    hOEMHeap;
  PDEVMODE  pPublicDM;
  PVOID     pOEMDM;
  PVOID     pOEMUserData;
  DWORD     dwFlags;
  PVOID     pOemEntry;
} OEMUIPSPARAM, *POEMUIPSPARAM;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size of the OEMUIPSPARAM structure. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**poemuiobj**
</dt> <dd>

Not used.

</dd> <dt>

**hPrinter**
</dt> <dd>

Handle to the printer. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**pPrinterName**
</dt> <dd>

String containing the printer name. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**hModule**
</dt> <dd>

Handle to the user interface plug-in. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**hOEMHeap**
</dt> <dd>

Handle to a heap from which space can be allocated by calling the Microsoft Windows SDK **HeapAlloc** function. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**pPublicDM**
</dt> <dd>

<dl> <dt>

<span id="For_calls_to_IPrintOemUI__DocumentPropertySheets_"></span><span id="for_calls_to_iprintoemui__documentpropertysheets_"></span><span id="FOR_CALLS_TO_IPRINTOEMUI__DOCUMENTPROPERTYSHEETS_"></span>For calls to **IPrintOemUI::DocumentPropertySheets**:
</dt> <dd>

Caller-supplied pointer to the printer's public DEVMODEW structure.

</dd> <dt>

<span id="For_calls_to_IPrintOemUI__DevicePropertySheets_"></span><span id="for_calls_to_iprintoemui__devicepropertysheets_"></span><span id="FOR_CALLS_TO_IPRINTOEMUI__DEVICEPROPERTYSHEETS_"></span>For calls to **IPrintOemUI::DevicePropertySheets**:
</dt> <dd>

Not used.

</dd> </dl> </dd> <dt>

**pOEMDM**
</dt> <dd>

<dl> <dt>

<span id="For_calls_to_IPrintOemUI__DocumentPropertySheets_"></span><span id="for_calls_to_iprintoemui__documentpropertysheets_"></span><span id="FOR_CALLS_TO_IPRINTOEMUI__DOCUMENTPROPERTYSHEETS_"></span>For calls to **IPrintOemUI::DocumentPropertySheets**:
</dt> <dd>

Caller-supplied pointer to the user interface plug-in's private DEVMODEW members.

</dd> <dt>

<span id="For_calls_to_IPrintOemUI__DevicePropertySheets_"></span><span id="for_calls_to_iprintoemui__devicepropertysheets_"></span><span id="FOR_CALLS_TO_IPRINTOEMUI__DEVICEPROPERTYSHEETS_"></span>For calls to **IPrintOemUI::DevicePropertySheets**:
</dt> <dd>

Not used.

</dd> </dl> </dd> <dt>

**pOEMUserData**
</dt> <dd>

Pointer, supplied by user interface plug-in, to a location containing private information. This pointer is returned to the plug-in's [**\_CPSUICALLBACK**](-cpsuicallback.md)-typed callback function when a property sheet item has changed.

</dd> <dt>

**dwFlags**
</dt> <dd>

<dl> <dt>

<span id="For_calls_to_IPrintOemUI__DocumentPropertySheets_"></span><span id="for_calls_to_iprintoemui__documentpropertysheets_"></span><span id="FOR_CALLS_TO_IPRINTOEMUI__DOCUMENTPROPERTYSHEETS_"></span>For calls to **IPrintOemUI::DocumentPropertySheets**:
</dt> <dd>

Contains the contents of the **fMode** member of the DOCUMENTPROPERTYHEADER structure received by the printer driver's [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function.

</dd> <dt>

<span id="For_calls_to_IPrintOemUI__DevicePropertySheets_"></span><span id="for_calls_to_iprintoemui__devicepropertysheets_"></span><span id="FOR_CALLS_TO_IPRINTOEMUI__DEVICEPROPERTYSHEETS_"></span>For calls to **IPrintOemUI::DevicePropertySheets**:
</dt> <dd>

Contains the contents of the **Flags** member of the DEVICEPROPERTYHEADER structure received by the printer driver's [**DrvDevicePropertySheets**](drvdevicepropertysheets.md) function.

</dd> </dl> </dd> <dt>

**pOemEntry**
</dt> <dd>

Reserved for system use.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUI::DevicePropertySheets**](iprintoemui-devicepropertysheets.md)
</dt> <dt>

[**IPrintOemUI::DocumentPropertySheets**](iprintoemui-documentpropertysheets.md)
</dt> <dt>

[**\_CPSUICALLBACK**](-cpsuicallback.md)
</dt> <dt>

[**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md)
</dt> <dt>

[**DrvDevicePropertySheets**](drvdevicepropertysheets.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMUIPSPARAM%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





