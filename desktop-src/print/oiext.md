---
Description: The OIEXT structure supplies additional, optional information about a property sheet page option that is described by an OPTITEM structure.
ms.assetid: 932e5520-0ebf-4cfa-893a-a7eb969cb697
title: OIEXT structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OIEXT structure

The OIEXT structure supplies additional, optional information about a property sheet page option that is described by an [**OPTITEM**](optitem.md) structure.

## Syntax


```C++
typedef struct _OIEXT {
  WORD      cbSize;
  WORD      Flags;
  HINSTANCE hInstCaller;
  LPTSTR    pHelpFile;
  ULONG_PTR dwReserved[4];
} OIEXT, *POIEXT;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size, in bytes, of the OIEXT structure.

</dd> <dt>

**Flags**
</dt> <dd>

Can contain the following bit flag:



| Flag                            | Description                                                                                                                                                                                                     |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OIEXTF\_ANSI\_STRING<br/> | If set, **pHelpFile** points to an ANSI string.<br/> If not set, **pHelpFile** points to a Unicode string.<br/> CPSUI does not check this flag if **pHelpFile** specifies a resource ID.<br/> |



 

</dd> <dt>

**hInstCaller**
</dt> <dd>

Instance handle to a DLL containing string and icon resources belonging to the [**OPTITEM**](optitem.md), [**OPTTYPE**](opttype.md), and [**OPTPARAM**](optparam.md) structures associated with the OIEXT structure. If **NULL**, CPSUI obtains resources from the DLL identified by the **hInstCaller** member of a [**COMPROPSHEETUI**](compropsheetui.md) structure.

</dd> <dt>

**pHelpFile**
</dt> <dd>

Pointer to a NULL-terminated string representing a path to a help file containing help information for the option. This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier with HIWORD set to zero. If **NULL**, CPSUI uses the help file identified by the **pHelpFile** member of a [**COMPROPSHEETUI**](compropsheetui.md) structure.

</dd> <dt>

**dwReserved**
</dt> <dd>

Reserved, must be initialized to zero.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OIEXT%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




