---
Description: The OEMQueryFont function is used by GDI to get the IFIMETRICS structure for a given font.
ms.assetid: cee6b2dd-e79b-4372-8371-c57fe950de88
title: OEMQueryFont function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OEMQueryFont function

The `OEMQueryFont` function is used by GDI to get the [**IFIMETRICS**](https://msdn.microsoft.com/fd2606ed-ec61-430a-aaad-38a4c3a207b6) structure for a given font.

## Syntax


```C++
PIFIMETRICS APIENTRY OEMQueryFont(
   DHPDEV    dhpdev,
   ULONG_PTR iFile,
   ULONG     iFace,
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

*pid* 
</dt> <dd></dd> </dl>

## 

### Comments

See [**DrvQueryFont**](https://msdn.microsoft.com/2ba6c8e3-9707-48dd-98d9-072f3eee8cd0).

Do not directly hook out this function. Instead, implement [**OEMEnableDriver**](oemenabledriver.md) so that it fills in a [**DRVENABLEDATA**](https://msdn.microsoft.com/dbeaecf8-dea1-4412-babb-6e40bf5dc7b0) structure listing all of the DDIs to be hooked out.

If you call into the core driver, cast the call using the **PFN\_DrvQueryFont** function pointer.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMQueryFont%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




