---
title: PROPSHEETHEADER structure (Prsht.h)
description: Defines the frame and pages of a property sheet.
keywords:
- PROPSHEETHEADER structure Windows Controls
topic_type:
- apiref
api_name:
- PROPSHEETHEADER
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 02/23/2021
---

# PROPSHEETHEADER  structure

Defines the frame and pages of a property sheet.

## Syntax

```cpp
typedef struct {
    DWORD      dwSize;
    DWORD      dwFlags;
    HWND       hwndParent;
    HINSTANCE  hInstance;
    union {
        HICON   hIcon;
        LPCTSTR pszIcon;
    };
    LPCTSTR  pszCaption;
    UINT     nPages;
    union {
        UINT    nStartPage;
        LPCTSTR pStartPage;
    };
    union {
        LPCPROPSHEETPAGE ppsp;
        HPROPSHEETPAGE   *phpage;
    };
    PFNPROPSHEETCALLBACK pfnCallback;
    union {
        HBITMAP hbmWatermark;
        LPCTSTR pszbmWatermark;
    };
    HPALETTE  hplWatermark;
    union {
        HBITMAP hbmHeader;
        LPCSTR  pszbmHeader;
    };
} PROPSHEETHEADER, *LPPROPSHEETHEADER;
```

## Members

*dwSize* 

Type: [DWORD](../winprog/windows-data-types.md)

Size, in bytes, of this structure. The property sheet manager uses this member to determine which version of the **PROPSHEETHEADER** structure you are using. For more information, see the Remarks.

*dwFlags* 

Type: [DWORD](../winprog/windows-data-types.md)

Flags that indicate which options to use when creating the property sheet page. This member can be a combination of the following values.

| Value | Meaning |
|-------|---------|
| PSH_DEFAULT (0x00000000) | Uses the default meaning for all structure members, and creates a normal property sheet. This flag has a value of zero and is not combined with other flags. |
| PSH_AEROWIZARD (0x00004000) | [Version 6.00](common-control-versions.md) and later. Creates a wizard property sheet that uses the Aero style. The PSH_WIZARD flag must also be set. The single-threaded apartment (STA) model must be used. |
| PSH_HASHELP (0x00000200) | Permits property sheet pages to display a **Help** button. You must also set the PSP_HASHELP flag in the page's [PROPSHEETPAGE](pss-propsheetpage.md) structure when the page is created. If any of the initial property sheet pages enable a **Help** button, PSH_HASHELP will be set automatically. If none of the initial pages enable a **Help** button, you must explicitly set PSH_HASHELP if you want to have Help buttons on any pages that might be added later. This flag is not supported in conjunction with PSH_AEROWIZARD.|
| PSH_HEADER (0x00080000) | [Version 5.80](common-control-versions.md) and later. Indicates that a header bitmap will be used with a Wizard97 wizard. You must also set the PSH_WIZARD97 flag. If the PSH_USEHBMHEADER flag is set, then the header bitmap is obtained from the *hbmHeader* member. Otherwise, the header bitmap is obtained from the *pszbmHeader* member. This flag is not supported in conjunction with PSH_AEROWIZARD. |
| PSH_HEADERBITMAP (0x08000000) | [Version 6.00](common-control-versions.md) and later. The *pszbmHeader* member specifies a bitmap that is displayed in the header area. Must be used in combination with PSH_AEROWIZARD. |
| PSH_MODELESS (0x00000400) | Causes the [PropertySheet](/windows/win32/api/prsht/nf-prsht-propertysheeta) function to create the property sheet as a modeless dialog box instead of as a modal dialog box. When this flag is set, [PropertySheet](/windows/win32/api/prsht/nf-prsht-propertysheeta) returns immediately after the dialog box is created, and the return value from [PropertySheet](/windows/win32/api/prsht/nf-prsht-propertysheeta) is the window handle to the property sheet dialog box. This flag is not supported in conjunction with PSH_AEROWIZARD. |
| PSH_NOAPPLYNOW (0x00000080) | Removes the **Apply** button. This flag is not supported in conjunction with PSH_AEROWIZARD. |
| PSH_NOCONTEXTHELP (0x02000000) | [Version 5.80](common-control-versions.md) and later. Removes the context-sensitive Help button ("?"), which is usually present on the caption bar of property sheets. This flag is not valid for wizards. See [About Property Sheets](property-sheets.md) for a discussion of how to remove the caption bar **Help** button for earlier versions of the common controls. This flag is not supported in conjunction with PSH_AEROWIZARD. |
| PSH_NOMARGIN (0x10000000) | [Version 6.00](common-control-versions.md) or later. Specifies that no margin is inserted between the page and the frame. Must be used in combination with PSH_AEROWIZARD. |
| PSH_PROPSHEETPAGE (0x00000008) | Uses the *ppsp* member and ignores the *phpage* member when creating the pages for the property sheet. |
| PSH_PROPTITLE (0x00000001) | Displays a title in the title bar of the property sheet. The title takes the appropriate form for the Windows version. In recent versions of Windows, the title is the string specified by the *pszCaption* member followed by the string **Properties**. This flag is not supported for wizards.  |
| PSH_RESIZABLE (0x04000000) | Allows the wizard to be resized by the user. Maximize and minimize buttons appear in the wizard's frame and the frame is sizable. To use this flag, you must also set PSH_AEROWIZARD. |
| PSH_RTLREADING (0x00000800) | Displays the title of the property sheet (*pszCaption*) using right-to-left (RTL) reading order for Hebrew or Arabic languages. If this flag is not specified, the title is displayed in left-to-right (LTR) reading order. |
| PSH_STRETCHWATERMARK (0x00040000) | Stretches the watermark in Wizard97-style wizards. This flag is not supported in conjunction with PSH_AEROWIZARD. This style flag is only included to provide backward compatibility for certain applications. Its use is not recommended, and it is only supported by common controls versions 4.0 and 4.01. With common controls version 5.80 and later, this flag is ignored. |
| PSH_USECALLBACK (0x00000100) | Calls the function specified by the *pfnCallback* member when initializing the property sheet defined by this structure. |
| PSH_USEHBMHEADER (0x00100000) | [Version 5.80](common-control-versions.md). Obtains the header bitmap from the *hbmHeader* member instead of the *pszbmHeader* member. You must also set either the PSH_AEROWIZARD flag or the PSH_WIZARD97 flag together with the PSH_HEADER flag. |
| PSH_USEHBMWATERMARK (0x00010000) | [Version 5.80](common-control-versions.md). Obtains the watermark bitmap from the *hbmWatermark* member instead of the *pszbmWatermark* member. You must also set PSH_WIZARD97 and PSH_WATERMARK. This flag is not supported in conjunction with PSH_AEROWIZARD. |
| PSH_USEHICON (0x00000002) | Uses *hIcon* as the small icon in the title bar of the property sheet dialog box. |
| PSH_USEHPLWATERMARK (0x00020000) | [Version 5.80](common-control-versions.md). Uses the **HPALETTE** structure pointed to by the *hplWatermark* member instead of the default palette to draw the watermark bitmap and/or header bitmap for a Wizard97 wizard. You must also set PSH_WIZARD97, and PSH_WATERMARK or PSH_HEADER. This flag is not supported in conjunction with PSH_AEROWIZARD.  |
| PSH_USEICONID (0x00000004) | Uses *pszIcon* as the name of the icon resource to load and use as the small icon in the title bar of the property sheet dialog box. |
| PSH_USEPAGELANG (0x00200000) | [Version 5.80](common-control-versions.md). Specifies that the language for the property sheet will be taken from the first page's resource. That page must be specified by resource identifier. |
| PSH_USEPSTARTPAGE (0x00000040) | Uses the *pStartPage* member instead of the *nStartPage* member when displaying the initial page of the property sheet. |
| PSH_WATERMARK (0x00008000) | [Version 5.80](common-control-versions.md). Specifies that a watermark bitmap will be used with a Wizard97 wizard on pages that have the PSP_HIDEHEADER style. You must also set the PSH_WIZARD97 flag. The watermark bitmap is obtained from the *pszbmWatermark* member, unless PSH_USEHBMWATERMARK is set. In that case, the header bitmap is obtained from the *hbmWatermark* member. This flag is not supported in conjunction with PSH_AEROWIZARD.  |
| PSH_WIZARD (0x00000020) | Creates a wizard property sheet. When using PSH_AEROWIZARD, you must also set this flag. |
| PSH_WIZARD97 (0x01000000) | [Version 5.80](common-control-versions.md). Creates a Wizard97-style property sheet, which supports bitmaps in the header of interior pages and on the left side of exterior pages. This flag is not supported in conjunction with PSH_AEROWIZARD. |
| PSH_WIZARDCONTEXTHELP (0x00001000) | Adds a context-sensitive **Help** button ("?"), which is usually absent from the caption bar of a wizard. This flag is not valid for regular property sheets. This flag is not supported in conjunction with PSH_AEROWIZARD. |
| PSH_WIZARDHASFINISH (0x00000010)  | Always displays the **Finish** button on the wizard. You must also set either PSH_WIZARD, PSH_WIZARD97, or PSH_AEROWIZARD. |
| PSH_WIZARD_LITE (0x00400000) | [Version 5.80](common-control-versions.md). Uses the Wizard-lite style. This style is similar in appearance to PSH_WIZARD97, but it is implemented much like PSH_WIZARD. There are few restrictions on how the pages are formatted. For instance, there are no enforced borders, and the PSH_WIZARD_LITE style does not paint the watermark and header bitmaps for you the way Wizard97 does. This flag is not supported in conjunction with PSH_AEROWIZARD. |

*hwndParent* 

Type: [HWND](../winprog/windows-data-types.md)

Handle to the property sheet's owner window.

*hInstance* 

Type: [HINSTANCE](../winprog/windows-data-types.md)

Handle to the instance from which to load the icon, title string resource, starting page name, header bitmap, or watermark. If the *pszIcon*, *pszCaption*, *pStartPage*, *pszbmHeader*, or *pszbmWatermark* member identifies a resource to load, this member must be specified.

*hIcon* 

Type: [HICON](../winprog/windows-data-types.md)

Handle to the icon to use as the small icon in the title bar of the property sheet dialog box. This member is used if the *dwFlags* member includes PSH_USEHICON. This member is declared as a union with *pszIcon*.

*pszIcon* 

Type: [LPCTSTR](../winprog/windows-data-types.md)

Icon resource to use as the small icon in the title bar of the property sheet dialog box. This member is used if the *dwFlags* member includes PSH_USEICONID. This member can specify either the identifier of the icon resource or the address of the string that specifies the name of the icon resource. In both cases, the icon is loaded from the instance provided by the *hInstance* member. This member is declared as a union with *hIcon*.

*pszCaption* 

Type: [LPCTSTR](../winprog/windows-data-types.md)

Title of the property sheet dialog box. This member can specify either the identifier of a string resource (loaded from the instance specified by the *hInstance* member) or the address of a string that specifies the title. If the *dwFlags* member includes PSH_PROPTITLE, the string **Properties for** is inserted at the beginning of the title. This field is ignored for Wizard97 wizards. For Aero wizards, the string alone is used for the caption, regardless of whether the PSH_PROPTITLE flag is set.

*nPages* 

Type: [UINT](../winprog/windows-data-types.md)

Number of property sheet pages provided in either the *ppsp* or *phpage* array.

*nStartPage* 

Type: [UINT](../winprog/windows-data-types.md)

Zero-based index of the initial page that appears when the property sheet dialog box is created. This member is used if the *dwFlags* member does not include the PSH_USEPSTARTPAGE flag. This member is declared as a union with *pStartPage*.

*pStartPage* 

Type: [LPCTSTR](../winprog/windows-data-types.md)

Name of the initial page that appears when the property sheet dialog box is created. This member is used if the *dwFlags* member includes the PSH_USESTARTPAGE flag. This member can specify either the identifier of a string resource (loaded from the instance specified by the *hInstance* member) or the address of a string that specifies the name. The start page name is matched against the captions of the pages. This member is declared as a union with *nStartPage*.

*ppsp* 

Type: **LPCPROPSHEETPAGE**

Pointer to an array of [PROPSHEETPAGE](pss-propsheetpage.md) structures that define the pages in the property sheet. If the *dwFlags* member does not include PSH_PROPSHEETPAGE, this member is ignored. Note that the **PROPSHEETPAGE** structure is variable in size. Applications that parse the array pointed to by *ppsp* must take the size of each page into account. This member is declared as a union with *phpage*.

*phpage* 

Type: **HPROPSHEETPAGE\***

Pointer to an array of handles to the property sheet pages. This member is used if the *dwFlags* member does not include PSH_PROPSHEETPAGE. Each handle must have been created by a previous call to the [CreatePropertySheetPage](/windows/win32/api/prsht/nf-prsht-createpropertysheetpagea) function. When the [PropertySheet](/windows/win32/api/prsht/nf-prsht-propertysheeta) function returns, any HPROPSHEETPAGE handles in the *phpage* array will have been destroyed. This member is declared as a union with *ppsp*.

*pfnCallback* 

Type: **PFNPROPSHEETCALLBACK**

Pointer to an application-defined callback function that is called when the property sheet is initialized. For more information about the callback function, see the description of the [PFNPROPSHEETCALLBACK callback function](/windows/win32/api/prsht/nc-prsht-pfnpropsheetcallback) function. If the *dwFlags* member does not include PSH_USECALLBACK, this member is ignored.

*hbmWatermark* 

Type: [HBITMAP](../winprog/windows-data-types.md)

[Version 5.80](common-control-versions.md) or later. Handle to the watermark bitmap. If the *dwFlags* member does not include PSH_USEHBMWATERMARK, this member is ignored.

*pszbmWatermark* 

Type: [LPCTSTR](../winprog/windows-data-types.md)

[Version 5.80](common-control-versions.md) or later. Bitmap resource to use as the watermark. This member can specify either the identifier of the bitmap resource or the address of the string that specifies the name of the bitmap resource. If the *dwFlags* member includes PSH_USEHBMWATERMARK, this member is ignored.

*hplWatermark*

Type: [HPALETTE](../winprog/windows-data-types.md)

[Version 5.80](common-control-versions.md) or later. **HPALETTE** structure used for drawing the watermark bitmap and/or header bitmap. If the *dwFlags* member does not include PSH_USEHPLWATERMARK, this member is ignored.

*hbmHeader*

Type: [HBITMAP](../winprog/windows-data-types.md)

[Version 5.80](common-control-versions.md) or later. Handle to the header bitmap. If the *dwFlags* member does not include PSH_USEHBMHEADER, this member is ignored.

*pszbmHeader*

Type: [LPCSTR](../winprog/windows-data-types.md)

[Version 5.80](common-control-versions.md) or later. Bitmap resource to use as the header. This member can specify either the identifier of the bitmap resource or the address of the string that specifies the name of the bitmap resource. If the *dwFlags* member includes PSH_USEHBMHEADER, this member is ignored.

## Remarks

If the user chooses a setting such as Large Fonts, which enlarges the dialog box, the watermark that is painted on the start and finish pages will be enlarged as well. The size and position of the original bitmap will remain the same. The additional area will be filled with the color of the pixel in the upper-left corner of the bitmap.

The PSH_WIZARD, PSH_WIZARD97, and PSH_WIZARD_LITE styles are mutually incompatible. Only one of these style flags should be set. PSH_AEROWIZARD should be combined with PSH_WIZARD.

## Requirements

| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client | Windows Vista \[desktop apps only\]                                    |
| Minimum supported server | Windows Server 2003 \[desktop apps only\]                              |
| Header                   | Prsht.h |
| Unicode and ANSI names                   | **PROPSHEETHEADERW** (Unicode) and **PROPSHEETHEADERA** (ANSI) |
