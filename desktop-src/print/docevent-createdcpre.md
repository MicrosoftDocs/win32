---
Description: The DOCEVENT\_CREATEDCPRE structure contains a set of values used in certain calls to DrvDocumentEvent and IPrintOemUI2::DocumentEvent.
ms.assetid: ad95d11e-c170-4c21-a498-45e38f41cbbb
title: DOCEVENT\_CREATEDCPRE structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DOCEVENT\_CREATEDCPRE structure

The DOCEVENT\_CREATEDCPRE structure contains a set of values used in certain calls to [**DrvDocumentEvent**](drvdocumentevent.md) and [**IPrintOemUI2::DocumentEvent**](iprintoemui2-documentevent.md).

## Syntax


```C++
typedef struct _DOCEVENT_CREATEDCPRE {
  PWSTR     pszDriver;
  PWSTR     pszDevice;
  PDEVMODEW pdm;
  BOOL      bIC;
} DOCEVENT_CREATEDCPRE, *PDCEVENT_CREATEDCPRE;
```



## Members

<dl> <dt>

**pszDriver**
</dt> <dd>

Reserved for system use. Set to zero.

</dd> <dt>

**pszDevice**
</dt> <dd>

Pointer to the first byte of a Unicode string that contains either the device name or the port name, depending on whether print spooling is enabled or disabled. If the print job is being sent directly to the printer (spooling is disabled), this member contains the printer name. If a print job is being spooled, this member contains the port name.

</dd> <dt>

**pdm**
</dt> <dd>

Pointer to a [**DEVMODEW**](https://www.bing.com/search?q=**DEVMODEW**) structure passed to either CreateIC or CreateDC (both described in the Microsoft Windows SDK documentation). This member can be **NULL**.

</dd> <dt>

**bIC**
</dt> <dd>

Specifies whether the DEVMODEW structure pointed to by the **pdm** member is being passed to CreateIC or CreateDC. If **TRUE**, CreateIC is being called. If **FALSE**, CreateDC is being called.

</dd> </dl>

## Remarks

The DOCEVENT\_CREATEDCPRE structure is defined for Windows XP and later.

This structure is used in conjunction with a call to [**DrvDocumentEvent**](drvdocumentevent.md) or [**IPrintOemUI2::DocumentEvent**](iprintoemui2-documentevent.md), in which the *iEsc* parameter is set to DOCUMENTEVENT\_CREATEDCPRE. Before calling either of these functions, the caller must fill in the members of this structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



## See also

<dl> <dt>

[**DrvDocumentEvent**](drvdocumentevent.md)
</dt> <dt>

[**IPrintOemUI2::DocumentEvent**](iprintoemui2-documentevent.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DOCEVENT_CREATEDCPRE%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





