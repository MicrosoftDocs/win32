---
Description: 'The OEMQueryFontTree function provides GDI with a pointer to a structure that defines one of the following:'
ms.assetid: 'e2e30707-dffd-4990-a552-b67a7d9e2ca4'
title: OEMQueryFontTree function
---

# OEMQueryFontTree function

The `OEMQueryFontTree` function provides GDI with a pointer to a structure that defines one of the following:

-   A mapping from Unicode to glyph handles, including glyph variants

-   A mapping of kerning pairs to kerning handles

## Syntax


```C++
PVOID APIENTRY OEMQueryFontTree(
   DHPDEV    dhpdev,
   ULONG_PTR iFile,
   ULONG     iFace,
   ULONG     iMode,
   ULONG_PTR *pid
);
```



## Parameters

<dl> <dt>

*dhpdev* 
</dt> <dd></dd> <dt>

*iFile* 
</dt> <dd></dd> <dt>

*iFace* 
</dt> <dd></dd> <dt>

*iMode* 
</dt> <dd></dd> <dt>

*pid* 
</dt> <dd></dd> </dl>

## 

### Comments

See [**DrvQueryFontTree**](display.drvqueryfonttree).

Do not directly hook out this function. Instead, implement [**OEMEnableDriver**](oemenabledriver.md) so that it fills in a [**DRVENABLEDATA**](display.drvenabledata) structure listing all of the DDIs to be hooked out.

If you call into the core driver, cast the call using the **PFN\_DrvQueryFontTree** function pointer.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMQueryFontTree%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




