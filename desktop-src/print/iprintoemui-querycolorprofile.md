---
Description: The IPrintOemUI::QueryColorProfile method allows a user interface plug-in to specify an ICC profile to use for color management.
ms.assetid: ce1131f9-4b9c-4f20-afc9-514ccbc7ecf7
title: IPrintOemUI::QueryColorProfile method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUI::QueryColorProfile method

The `IPrintOemUI::QueryColorProfile` method allows a user interface plug-in to specify an ICC profile to use for color management.

## Syntax


```C++
HRESULT QueryColorProfile(
   HANDLE    hPrinter,
   POEMUIOBJ poemuiobj,
   PDEVMODE  pPublicDM,
   PVOID     pOEMDM,
   ULONG     ulQueryMode,
   VOID      *pvProfileData,
   ULONG     *pcbProfileData,
   FLONG     *pflProfileData
);
```



## Parameters

<dl> <dt>

*hPrinter* 
</dt> <dd>

Caller-supplied printer handle.

</dd> <dt>

*poemuiobj* 
</dt> <dd>

Caller-supplied pointer to an [**OEMUIOBJ**](oemuiobj.md) structure.

</dd> <dt>

*pPublicDM* 
</dt> <dd>

Caller-supplied pointer to a validated [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure.

</dd> <dt>

*pOEMDM* 
</dt> <dd>

Caller-supplied pointer to the user interface plug-in's private DEVMODEW structure members.

</dd> <dt>

*ulQueryMode* 
</dt> <dd>

One of the following caller-supplied bit flags, indicating the type of profile to be specified.



| Flag                          | Definition                                            |
|-------------------------------|-------------------------------------------------------|
| QCP\_DEVICEPROFILE<br/> | The caller is requesting a device profile.<br/> |
| QCP\_SOURCEPROFILE<br/> | The caller is requesting a source profile.<br/> |



 

</dd> <dt>

*pvProfileData* 
</dt> <dd>

Caller-supplied pointer to a buffer to receive profile information.

</dd> <dt>

*pcbProfileData* 
</dt> <dd>

Caller-supplied pointer to a value representing the size, in bytes, of the buffer pointed to by *pvProfileData*.

</dd> <dt>

*pflProfileData* 
</dt> <dd>

One of the following method-supplied bit flags, indicating the type of information the method is returning.



| Flag                          | Definition                                                                                                      |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------|
| QCP\_PROFILEDISK<br/>   | The method is returning the file name of an ICC profile in the buffer pointed to by *pvProfileData*.<br/> |
| QCP\_PROFILEMEMORY<br/> | The method is returning profile data in the buffer pointed to by *pvProfileData*.<br/>                    |



 

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

A user interface plug-in's `IPrintOemUI::QueryColorProfile` method performs the same types of operations as the **DrvQueryColorProfile** function that is exported by user-mode printer interface DLLs. For information about printer events and how they should be processed, see the description of the [**DrvQueryColorProfile**](drvquerycolorprofile.md) function.

If you provide a user interface plug-in, the printer driver's **DrvQueryColorProfile** function calls the `IPrintOemUI::QueryColorProfile` method. The **DrvQueryColorProfile** function performs its own processing for the specified event, and then calls the `IPrintOemUI::QueryColorProfile` method to handle additional processing of the event.

If `IPrintOemUI::QueryColorProfile` methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.

For more information about creating and installing user interface plug-ins, see [Customizing Microsoft's Printer Drivers](https://www.bing.com/search?q=Customizing+Microsoft's+Printer+Drivers).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI::QueryColorProfile%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




