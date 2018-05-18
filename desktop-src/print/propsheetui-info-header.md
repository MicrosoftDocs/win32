---
Description: 'The PROPSHEETUI\_INFO\_HEADER structure is used as an input parameter to an application''s PFNPROPSHEETUI-typed function, when the function is called with a reason value of PROPSHEETUI\_REASON\_GET\_INFO\_HEADER.'
ms.assetid: '148c463c-a18b-4f24-b3dc-af74c3de97b7'
title: 'PROPSHEETUI\_INFO\_HEADER structure'
---

# PROPSHEETUI\_INFO\_HEADER structure

The PROPSHEETUI\_INFO\_HEADER structure is used as an input parameter to an application's [**PFNPROPSHEETUI**](pfnpropsheetui.md)-typed function, when the function is called with a reason value of PROPSHEETUI\_REASON\_GET\_INFO\_HEADER.

## Syntax


```C++
typedef struct _PROPSHEETUI_INFO_HEADER {
  WORD      cbSize;
  WORD      Flags;
  LPTSTR    pTitle;
  HWND      hWndParent;
  HINSTANCE hInst;
  union {
    HICON     hIcon;
    ULONG_PTR IconID;
  };
} PROPSHEETUI_INFO_HEADER, *PPROPSHEETUI_INFO_HEADER;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

CPSUI-supplied size, in bytes, of the PROPSHEETUI\_INFO\_HEADER structure.

</dd> <dt>

**Flags**
</dt> <dd>

Optional, application-specified bit flags that modify the property sheet page's appearance. The flags listed in the following table can be used in any combination.



| Flag                               | Description                                                                                                                                                                          |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSUIHDRF\_DEFTITLE<br/>      | If set, CPSUI should include "Default" in the title bar string. CPSUI adds "Default" after the **pTitle** string and, if PSUIHDRF\_PROPTITLE is set, before "Properties".<br/> |
| PSUIHDRF\_EXACT\_PTITLE<br/> | If set, CPSUI uses the text specified by **pTitle** without modification. This flag overrides PSUIHDRF\_DEFTITLE and PSUIHDRF\_PROPTITLE.<br/>                                 |
| PSUIHDRF\_NOAPPLYNOW<br/>    | If set, CPSUI should not include an **Apply Now** button.<br/>                                                                                                                 |
| PSUIHDRF\_PROPTITLE<br/>     | If set, CPSUI should append "Properties" to the title bar string. (By default, CPSUI sets this flag before calling the application.)<br/>                                      |
| PSUIHDRF\_USEHICON<br/>      | If set, the **hIcon**/**IconID** union contains an icon handle. If not set, the union contains an icon resource identifier.<br/>                                               |



 

</dd> <dt>

**pTitle**
</dt> <dd>

String identifier, representing text to be displayed in the property sheet's title bar. This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier with HIWORD set to zero. For printer interface DLLs, the string typically contains the printer's name.

</dd> <dt>

**hWndParent**
</dt> <dd>

Handle to the window to be used as the parent of the property sheet. By default, CPSUI supplies the window handle that it received for the *hWndOwner* parameter to [**CommonPropertySheetUI**](commonpropertysheetui.md), but the application can overwrite that handle with another.

</dd> <dt>

**hInst**
</dt> <dd>

Application-supplied instance handle, which CPSUI uses when loading application resources.

</dd> <dt>

**hIcon**
</dt> <dd></dd> <dt>

**IconID**
</dt> <dd>

This union identifies the icon to be displayed in the property sheet's title bar. The union member is selected by PSUIHDRF\_USEICON in **Flags**.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PROPSHEETUI_INFO_HEADER%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




