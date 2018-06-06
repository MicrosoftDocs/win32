---
Description: The OEMCUIPPARAM structure is used as an input parameter to a user interface plug-in's IPrintOemUI::CommonUIProp method.
ms.assetid: 178b635c-0916-44f5-87a3-a2766601dcab
title: OEMCUIPPARAM structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# OEMCUIPPARAM structure

The OEMCUIPPARAM structure is used as an input parameter to a user interface plug-in's [**IPrintOemUI::CommonUIProp**](iprintoemui-commonuiprop.md) method.

## Syntax


```C++
typedef struct _OEMCUIPPARAM {
  DWORD           cbSize;
  POEMUIOBJ       poemuiobj;
  HANDLE          hPrinter;
  PWSTR           pPrinterName;
  HANDLE          hModule;
  HANDLE          hOEMHeap;
  PDEVMODE        pPublicDM;
  PVOID           pOEMDM;
  DWORD           dwFlags;
  POPTITEM        pDrvOptItems;
  DWORD           cDrvOptItems;
  POPTITEM        pOEMOptItems;
  DWORD           cOEMOptItems;
  PVOID           pOEMUserData;
  OEMCUIPCALLBACK OEMCUIPCallback;
} OEMCUIPPARAM;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size of the OEMCUIPPARAM structure. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**poemuiobj**
</dt> <dd>

Pointer to an [**OEMUIOBJ**](oemuiobj.md) structure.

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

Handle to a heap from which space can be allocated by calling the **HeapAlloc** function (described in the Microsoft Windows SDK documentation). Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**pPublicDM**
</dt> <dd>

Pointer to the printer's public DEVMODEW structure. Valid only if the [**IPrintOemUI::CommonUIProp**](iprintoemui-commonuiprop.md) method's *dwMode* argument is OEMCUIP\_DOCPROP. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**pOEMDM**
</dt> <dd>

Pointer to the user interface plug-in's private DEVMODEW members. Valid only if the **IPrintOemUI::CommonUIProp** method's *dwMode* argument is OEMCUIP\_DOCPROP. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**dwFlags**
</dt> <dd>

<dl> <dt>

<span id="For_calls_to_IPrintOemUI__CommonUIProp_with_its_dwMode_parameter_set_to_OEMCUIP_DOCPROP_"></span><span id="for_calls_to_iprintoemui__commonuiprop_with_its_dwmode_parameter_set_to_oemcuip_docprop_"></span><span id="FOR_CALLS_TO_IPRINTOEMUI__COMMONUIPROP_WITH_ITS_DWMODE_PARAMETER_SET_TO_OEMCUIP_DOCPROP_"></span>For calls to **IPrintOemUI::CommonUIProp** with its *dwMode* parameter set to OEMCUIP\_DOCPROP:
</dt> <dd>

Contains the contents of the **fMode** member of the [**DOCUMENTPROPERTYHEADER**](documentpropertyheader.md) structure received by the printer driver's [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function.

</dd> <dt>

<span id="For_calls_to_IPrintOemUI__CommonUIProp_with_its_dwMode_parameter_set_to_OEMCUIP_PRNPROP_"></span><span id="for_calls_to_iprintoemui__commonuiprop_with_its_dwmode_parameter_set_to_oemcuip_prnprop_"></span><span id="FOR_CALLS_TO_IPRINTOEMUI__COMMONUIPROP_WITH_ITS_DWMODE_PARAMETER_SET_TO_OEMCUIP_PRNPROP_"></span>For calls to **IPrintOemUI::CommonUIProp** with its *dwMode* parameter set to OEMCUIP\_PRNPROP:
</dt> <dd>

Contains the contents of the **Flags** member of the DEVICEPROPERTYHEADER structure received by the printer driver's [**DrvDevicePropertySheets**](drvdevicepropertysheets.md) function.

</dd> </dl> </dd> <dt>

**pDrvOptItems**
</dt> <dd>

Pointer to the printer driver's [**OPTITEM**](optitem.md) array. Not valid the first time **IPrintOemUI::CommonUIProp** is called. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**cDrvOptItems**
</dt> <dd>

Count of OPTITEM structures in the array pointed to by **pDrvOptItems**. Supplied by the Unidrv or Pscript5 driver.

</dd> <dt>

**pOEMOptItems**
</dt> <dd>

Pointer to an array of OPTITEM structures. Supplied by **IPrintOemUI::CommonUIProp** caller. The second time the **IPrintOemUI::CommonUIProp** method is called, it must place OPTITEM structures defined by the user interface plug-in in this array, and it must place the structure count in **cOEMOptItems**. For each OPTITEM structure placed in the array, you must do the following:

-   Set the OPTITEM structure's **DMPubID** member either to one of the predefined values or to a value greater than DMPUB\_USER. If you use any predefined values, you must search through the entire OPTITEM array for structures already containing those values, and you must set their OPTIF\_HIDE flags.

-   Allocate space for OPTTYPES and OPTPARAMS structures by calling the Windows SDK **HeapAlloc** function, using the handle contained in the OEMCUIPPARAM structure's **hOEMHeap** member. The printer driver deallocates this space when it is no longer needed.

Not valid the first time **IPrintOemUI::CommonUIProp** is called.

</dd> <dt>

**cOEMOptItems**
</dt> <dd>

Count of OPTITEM structures contained in the array pointed by **pOEMOptItems**. Supplied by the Unidrv or Pscript5 driver.

The first time the **IPrintOemUI::CommonUIProp** method is called, the caller-supplied value for **cOEMOptItems** is zero. The **IPrintOemUI::CommonUIProp** method must change this value to indicate the number of OPTITEM structures that the method supplies. The second time it is called, **IPrintOemUI::CommonUIProp** must supply the number of OPTITEM structures actually added to the array pointed to by **pOEMOptItems**.

</dd> <dt>

**pOEMUserData**
</dt> <dd>

Used by the **IPrintOemUI::CommonUIProp** method, the second time it is called, to provide the **OEMCUIPCallback** function with optional extra input information.

</dd> <dt>

**OEMCUIPCallback**
</dt> <dd>

Used by the **IPrintOemUI::CommonUIProp** method, the second time it is called, to return the address of a callback function of type [**OEMCUIPCALLBACK**](oemcuipcallback.md).

</dd> </dl>

## Remarks

A user interface plug-in receives this structure's address as an input argument to both its [**IPrintOemUI::CommonUIProp**](iprintoemui-commonuiprop.md) method and its [**OEMCUIPCALLBACK**](oemcuipcallback.md)-typed callback function.

For additional information about the use of this structure and associated functions, see [User Interface Plug-Ins](https://www.bing.com/search?q=User+Interface+Plug-Ins).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMCUIPPARAM%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




