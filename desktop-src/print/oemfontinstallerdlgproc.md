---
Description: OEMFontInstallerDlgProc function
ms.assetid: '6007723b-c7db-42da-bc50-328e19f80448'
title: OEMFontInstallerDlgProc function
---

# OEMFontInstallerDlgProc function

## Syntax


```C++
INT_PTR APIENTRY OEMFontInstallerDlgProc(
   HWND   hWnd,
   UINT   usMsg,
   WPARAM wParam,
   LPARAM lParam
);
```



## Parameters

<dl> <dt>

*hWnd* 
</dt> <dd></dd> <dt>

*usMsg* 
</dt> <dd></dd> <dt>

*wParam* 
</dt> <dd></dd> <dt>

*lParam* 
</dt> <dd></dd> </dl>

## 

This function is obsolete for Windows XP and later. It is supported only for earlier plug-ins. Use [**IPrintOemUI::FontInstallerDlgProc**](iprintoemui-fontinstallerdlgproc.md).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMFontInstallerDlgProc%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




