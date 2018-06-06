---
Description: The OEMQueryAdvanceWidths function returns character advance widths for a specified set of glyphs.
ms.assetid: 058ced7e-50bc-4847-b082-57608ac5ddd2
title: OEMQueryAdvanceWidths function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OEMQueryAdvanceWidths function

The `OEMQueryAdvanceWidths` function returns character advance widths for a specified set of glyphs.

## Syntax


```C++
BOOL APIENTRY OEMQueryAdvanceWidths(
        DHPDEV                                       dhpdev,
        FONTOBJ                                      *pfo,
        ULONG                                        iMode,
  _In_  _reads_(cGlyphs) HGLYPH                      *phg,
  _Out_ _writes_bytes_(cGlyphs*sizeof(USHORT)) PVOID pvWidths,
        ULONG                                        cGlyphs
);
```



## Parameters

<dl> <dt>

*dhpdev* 
</dt> <dd></dd> <dt>

*pfo* 
</dt> <dd></dd> <dt>

*iMode* 
</dt> <dd></dd> <dt>

*phg* \[in\]
</dt> <dd></dd> <dt>

*pvWidths* \[out\]
</dt> <dd></dd> <dt>

*cGlyphs* 
</dt> <dd></dd> </dl>

## 

### Comments

See [**DrvQueryAdvanceWidths**](https://msdn.microsoft.com/b97114b5-6cc7-4af6-badb-d6aa5fc581ef).

Do not directly hook out this drawing function. Instead, implement [**OEMEnableDriver**](oemenabledriver.md) so that it fills in a [**DRVENABLEDATA**](https://msdn.microsoft.com/dbeaecf8-dea1-4412-babb-6e40bf5dc7b0) structure listing all of the drawing DDIs to be hooked out.

If you call into the core driver, cast the call using the **PFN\_DrvQueryAdvanceWidths** function pointer.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMQueryAdvanceWidths%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




