---
Description: A user interface plug-in's IPrintOemUI::FontInstallerDlgProc method replaces the Unidrv font installer's user interface.
ms.assetid: 6f63d48d-7c2f-4531-b6db-fd4fdcfbce27
title: IPrintOemUI::FontInstallerDlgProc method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUI::FontInstallerDlgProc method

A user interface plug-in's `IPrintOemUI::FontInstallerDlgProc` method replaces the Unidrv font installer's user interface.

## Syntax


```C++
HRESULT FontInstallerDlgProc(
   HWND   hWnd,
   UINT   usMsg,
   WPARAM wParam,
   LPARAM lParam
);
```



## Parameters

<dl> <dt>

*hWnd* 
</dt> <dd>

Window handle.

</dd> <dt>

*usMsg* 
</dt> <dd>

Message identifier.

</dd> <dt>

*wParam* 
</dt> <dd>

First message parameter.

</dd> <dt>

*lParam* 
</dt> <dd>

Second message parameter.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

A user interface plug-in can implement the `IPrintOemUI::FontInstallerDlgProc` method as a means of replacing Unidrv's font installer. For more information, see [Customized Font Installers for Unidrv](https://www.bing.com/search?q=Customized Font Installers for Unidrv).

The `IPrintOemUI::FontInstallerDlgProc` method is used by Unidrv as a dialog box procedure, and its address is passed to **DialogBoxParam** (described in the Microsoft Windows SDK documentation) when a user invokes the font installer from Unidrv's user interface.

If the message received for *usMsg* is WM\_INIT or WM\_USER+WM\_FI\_NAME, *lParam* points to an [**OEMFONTINSTPARAM**](oemfontinstparam.md) structure.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUI**](iprintoemui-interface.md)
</dt> <dt>

[**IPrintOemUI::UpdateExternalFonts**](iprintoemui-updateexternalfonts.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI::FontInstallerDlgProc%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





