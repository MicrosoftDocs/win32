---
Description: The OEMFONTINSTPARAM structure is used as an input parameter to a user interface plug-in's IPrintOemUI::FontInstallerDlgProc method.
ms.assetid: cdd3ed28-a077-4b89-9222-ba282b9c7205
title: OEMFONTINSTPARAM structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# OEMFONTINSTPARAM structure

The OEMFONTINSTPARAM structure is used as an input parameter to a user interface plug-in's [**IPrintOemUI::FontInstallerDlgProc**](iprintoemui-fontinstallerdlgproc.md) method.

## Syntax


```C++
typedef struct _OEMFONTINSTPARAM {
  DWORD  cbSize;
  HANDLE hPrinter;
  HANDLE hModule;
  HANDLE hHeap;
  DWORD  dwFlags;
  PWSTR  pFontInstallerName;
} OEMFONTINSTPARAM, *POEMFONTINSTPARAM;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size, in bytes, of the OEMFONTINSTPARAM structure.

</dd> <dt>

**hPrinter**
</dt> <dd>

Unidrv-supplied printer handle.

</dd> <dt>

**hModule**
</dt> <dd>

Unidrv-supplied handle to the user interface plug-in.

</dd> <dt>

**hHeap**
</dt> <dd>

Unidrv-supplied handle to a heap from which space can be allocated by calling the **HeapAlloc** function (described in the Microsoft Windows SDK documentation).

</dd> <dt>

**dwFlags**
</dt> <dd>

Unidrv-supplied flags. The only defined flag is FG\_CANCHANGE which, if set, indicates the user interface should allow the user to change the installed fonts. Otherwise the user interface should be displayed in read-only mode.

</dd> <dt>

**pFontInstallerName**
</dt> <dd>

Pointer to a string representing the font installer's name. The [**IPrintOemUI::FontInstallerDlgProc**](iprintoemui-fontinstallerdlgproc.md) method must supply this string if the received message is WM\_USER+WM\_FI\_NAME. The string must be placed in memory allocated using **hHeap**.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMFONTINSTPARAM%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




