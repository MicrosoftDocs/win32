---
Description: 'The OEM\_DMEXTRAHEADER structure must be used to define the first members of a set of private DEVMODEW structure members.'
ms.assetid: 'fecefdbc-3036-4991-900c-203ae8be254b'
title: 'OEM\_DMEXTRAHEADER structure'
---

# OEM\_DMEXTRAHEADER structure

The OEM\_DMEXTRAHEADER structure must be used to define the first members of a set of private [**DEVMODEW**](display.devmodew) structure members.

## Syntax


```C++
typedef struct _OEM_DMEXTRAHEADER {
  DWORD dwSize;
  DWORD dwSignature;
  DWORD dwVersion;
} OEM_DMEXTRAHEADER, *POEM_DMEXTRAHEADER;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Total size, in bytes, of the added private DEVMODEW structure members, including the bytes contained in the OEM\_DMEXTRAHEADER structure.

</dd> <dt>

**dwSignature**
</dt> <dd>

Unique signature value that the plug-in also returns when its [**IPrintOemUI::GetInfo**](iprintoemui-getinfo.md) method receives the OEMGI\_GETSIGNATURE flag.

</dd> <dt>

**dwVersion**
</dt> <dd>

Version number of the user interface plug-in that is defining the private DEVMODEW structure members. The version format is developer-defined.

</dd> </dl>

## Remarks

For more information about adding DEVMODEW structure members, see [Providing DEVMODE Structure Additions](print.providing_devmode_structure_additions).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEM_DMEXTRAHEADER%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




