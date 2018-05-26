---
Description: The PSPINFO structure is used as an input parameter to a property sheet pages dialog box procedure, when the Windows message is WM\_INITDIALOG. The dialog box procedures address is specified in a DLGPAGE structure.
ms.assetid: 80a15ee4-e160-49fc-9c61-a14b14d19751
title: PSPINFO structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PSPINFO structure

The PSPINFO structure is used as an input parameter to a property sheet page's dialog box procedure, when the Windows message is WM\_INITDIALOG. The dialog box procedure's address is specified in a [**DLGPAGE**](dlgpage.md) structure.

## Syntax


```C++
typedef struct _PSPINFO {
  WORD            cbSize;
  WORD            wReserved;
  HANDLE          hComPropSheet;
  HANDLE          hCPSUIPage;
  PFNCOMPROPSHEET pfnComPropSheet;
} PSPINFO, *PPSPINFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

CPSUI-supplied size, in bytes, of the PSPINFO structure.

</dd> <dt>

**wReserved**
</dt> <dd>

Reserved.

</dd> <dt>

**hComPropSheet**
</dt> <dd>

CPSUI-supplied handle to the parent of the page whose handle is contained in **hCPSUIPage**.

</dd> <dt>

**hCPSUIPage**
</dt> <dd>

CPSUI-supplied handle to the property sheet page.

</dd> <dt>

**pfnComPropSheet**
</dt> <dd>

CPSUI-supplied pointer to its [**ComPropSheet**](compropsheet.md) function.

</dd> </dl>

## Remarks

Before CPSUI calls **CreatePropertySheetPage** to create a property sheet page, it expands the size of the standard PROPSHEETPAGE structure in order to append a PSPINFO structure. When the operating system calls a dialog box procedure (pointed to by a [**DLGPAGE**](dlgpage.md) structure) and specifies a WM\_INITDIALOG message, the function's **lParam** member points to the expanded PROPSHEETPAGE structure containing the PSPINFO structure.

(The **CreatePropertySheetPage** function, PROPSHEETPAGE structure, WM\_INITDIALOG message, and dialog box procedures are all described in the Microsoft Windows SDK documentation.)

To obtain the PSPINFO structure's address, use the PPSPINFO\_FROM\_WM\_INITDIALOG\_LPARAM macro (defined in compstui.h) as follows:


```
PPSPINFO pPspInfo;
if (Msg == WM_INITDIALOG) {
    pPspInfo = PPSPINFO_FROM_WM_INITDIALOG_LPARAM(lParam);
}
```



The PSPINFO structure pointer can be saved for later use, but the structure's contents must not be modified.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PSPINFO%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




