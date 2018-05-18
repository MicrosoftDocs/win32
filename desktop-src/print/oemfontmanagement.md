---
Description: 'The OEMFontManagement function is an optional entry point provided for PostScript devices.'
ms.assetid: 'fd4e712a-8bde-4c80-b288-3fa7b69a2681'
title: OEMFontManagement function
---

# OEMFontManagement function

The `OEMFontManagement` function is an optional entry point provided for PostScript devices.

## Syntax


```C++
ULONG APIENTRY OEMFontManagement(
        SURFOBJ                     *pso,
        FONTOBJ                     *pfo,
        ULONG                       iMode,
        ULONG                       cjIn,
  _In_  _reads_bytes_(cjIn) PVOID   pvIn,
        ULONG                       cjOut,
  _Out_ _writes_bytes_(cjOut) PVOID pvOut
);
```



## Parameters

<dl> <dt>

*pso* 
</dt> <dd></dd> <dt>

*pfo* 
</dt> <dd></dd> <dt>

*iMode* 
</dt> <dd></dd> <dt>

*cjIn* 
</dt> <dd></dd> <dt>

*pvIn* \[in\]
</dt> <dd></dd> <dt>

*cjOut* 
</dt> <dd></dd> <dt>

*pvOut* \[out\]
</dt> <dd></dd> </dl>

## 

### Comments

See [**DrvFontManagement**](display.drvfontmanagement).

If this function is hooked by the device driver, then GDI passes calls that an application makes to **ExtEscape** for escape numbers 0x100 through 0x3FE, or for the QUERYESCSUPPORT escape when the first DWORD pointed to by *pvIn* is in the range 0x100 through 0x3FE.

Do not directly hook out this drawing function. Instead, implement [**OEMEnableDriver**](oemenabledriver.md) so that it fills in a [**DRVENABLEDATA**](display.drvenabledata) structure listing all of the drawing DDIs to be hooked out.

If you call into the core driver, cast the call using the **PFN\_DrvFontManagement** function pointer.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMFontManagement%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




