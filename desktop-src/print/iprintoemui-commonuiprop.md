---
Description: The IPrintOemUI::CommonUIProp method allows a user interface plug-in to modify an existing printer property sheet page.
ms.assetid: 6218913c-d11c-4646-a292-5f8740097d58
title: IPrintOemUI::CommonUIProp method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUI::CommonUIProp method

The `IPrintOemUI::CommonUIProp` method allows a user interface plug-in to modify an existing printer property sheet page.

## Syntax


```C++
HRESULT CommonUIProp(
   DWORD         dwMode,
   POEMCUIPPARAM pOemCUIPParam
);
```



## Parameters

<dl> <dt>

*dwMode* 
</dt> <dd>

Caller-supplied integer constant indicating which property sheet page should be modified. The following constants are valid.



| Value                       | Definition                                                                                                                  |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| OEMCUIP\_DOCPROP<br/> | The method is being called to modify the Layout, Paper/Quality, or Advanced page of the document property sheet.<br/> |
| OEMCUIP\_PRNPROP<br/> | The method is being called to modify the Device Settings page of the printer property sheet.<br/>                     |



 

</dd> <dt>

*pOemCUIPParam* 
</dt> <dd>

Caller-supplied pointer to an [**OEMCUIPPARAM**](oemcuipparam.md) structure.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

When a user interface plug-in's `IPrintOemUI::CommonUIProp` method is called, it should return customized property sheet option items in order to modify an existing printer property sheet page.

The `IPrintOemUI::CommonUIProp` method is called by the printer driver's [printer interface DLL](https://www.bing.com/search?q=printer interface DLL). The method should supply an array of [**OPTITEM**](optitem.md) structures describing property sheet items, along with a callback function for processing user modifications to option values.

You should expect the method to be called twice for each property sheet. The method's *dwMode* parameter value indicates whether it is being called to make changes to the printer property sheet or the document property sheet.

The first time it is called, the method should just return the number of [**OPTITEM**](optitem.md) structures to be added. This number should be placed in the [**OEMCUIPPARAM**](oemcuipparam.md) structure's **cOEMOptItems** member. The printer interface DLL then allocates enough memory to store the specified number of OPTITEMs, and calls `IPrintOemUI::CommonUIProp` again.

The second time it is called, the `IPrintOemUI::CommonUIProp` method should do the following:

-   Fill the driver-supplied array of OPTITEM structures with option descriptions. This array is pointed to by the OEMCUIPPARAM structure's **pOEMOptItems** member, and the number of allocated array elements is contained in the structure's **cOEMOptItems** member. (For information about specifying OPTITEM member values, see the description of the OEMCUIPPARAM structure's **pOEMOptItems** member).

-   Return the number of structures added to the OPTITEM array by placing the number in the OEMCUIPPARAM structure's **cOEMOptItems** member.

-   Return the address of a callback function in the OEMCUIPPARAM structure's **OEMCUIPCallback** member. This callback function is called when a user modifies the property sheet page. The callback function must be of type [**OEMCUIPCALLBACK**](oemcuipcallback.md).

-   Optionally, return the address of a private data structure by placing it in the OEMCUIPPARAM structure's **pOEMUserData** member. The callback function specified by the structure's **OEMCUIPCallback** member receives the OEMCUIPPARAM structure's address as an input parameter and can therefore obtain the private data's address.

    Space for the private data structure should be allocated by calling the Microsoft Windows SDK **HeapAlloc** function, using the handle contained in the OEMCUIPPARAM structure's **hOEMHeap** member.

If `IPrintOemUI::CommonUIProp` methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.

For more information, see [Modifying a Driver-Supplied Property Sheet Page](https://www.bing.com/search?q=Modifying a Driver-Supplied Property Sheet Page).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI::CommonUIProp%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




