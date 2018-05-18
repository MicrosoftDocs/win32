---
Description: 'The OEMUIOBJ structure is used as an input argument to several of the methods exported by user interface plug-ins.'
ms.assetid: 'ba9252ec-3aef-4e8c-a335-bde33686beae'
title: OEMUIOBJ structure
---

# OEMUIOBJ structure

The OEMUIOBJ structure is used as an input argument to several of the methods exported by user interface plug-ins.

## Syntax


```C++
typedef struct _OEMUIOBJ {
  DWORD       cbSize;
  POEMUIPROCS pOemUIProcs;
} OEMUIOBJ, *POEMUIOBJ;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size of the OEMUIOBJ structure.

</dd> <dt>

**pOemUIProcs**
</dt> <dd>

Pointer to a an [**OEMUIPROCS**](oemuiprocs.md) structure, which is a private, internal structure.

</dd> </dl>

## Remarks

User interface plug-ins do not need to reference an OEMUIOBJ structure's members. Plug-ins receive a pointer to this structure as input to their [**IPrintOemUI::DeviceCapabilities**](iprintoemui-devicecapabilities.md), [**IPrintOemUI::DevQueryPrintEx**](iprintoemui-devqueryprintex.md) and [**IPrintOemUI::QueryColorProfile**](iprintoemui-querycolorprofile.md) methods. Additionally, the OEMCUIPPARAM structure contains an OEMUIOBJ structure pointer. Plug-ins must supply the received pointer when calling [**IPrintOemDriverUI::DrvGetDriverSetting**](iprintoemdriverui-drvgetdriversetting.md) or [**IPrintOemDriverUI::DrvUpdateUISetting**](iprintoemdriverui-drvupdateuisetting.md).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMUIOBJ%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




