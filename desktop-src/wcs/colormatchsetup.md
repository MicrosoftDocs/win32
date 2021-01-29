---
title: COLORMATCHSETUP structure
description: The COLORMATCHSETUP structure contains information that the SetupColorMatching function uses to initialize the ColorManagement dialog box.
ms.assetid: 920c9ac2-bb77-4805-9345-15611db1aade
keywords:
- COLORMATCHSETUP structure Windows Color System
topic_type:
- apiref
api_name:
- COLORMATCHSETUP
api_location:
- Icm.h
api_type:
- HeaderDef
ms.localizationpriority: high


ms.topic: structure
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# COLORMATCHSETUP structure

The **COLORMATCHSETUP** structure contains information that the [**SetupColorMatching**](setupcolormatching.md) function uses to initialize the **ColorManagement** dialog box. After the user closes the dialog box, **SetupColorMatching** returns information about the user's selection in this structure.

## Syntax


```C++
typedef struct _tagCOLORMATCHSETUP {
  DWORD         dwSize;
  DWORD         dwVersion;
  DWORD         dwFlags;
  HWND          hwndOwner;
  PCTSTR        pSourceName;
  PCTSTR        pDisplayName;
  PCTSTR        pPrinterName;
  DWORD         dwRenderIntent;
  DWORD         dwProofingIntent;
  PTSTR         pMonitorProfile;
  DWORD         ccMonitorProfile;
  PTSTR         pPrinterProfile;
  DWORD         ccPrinterProfile;
  PTSTR         pTargetProfile;
  DWORD         ccTargetProfile;
  DLGPROC       lpfnHook;
  LPARAM        lParam;
  PCMSCALLBACKA lpfnApplyCallback;
  LPARAM        lParamApplyCallback;
} COLORMATCHSETUP;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Size of the structure. Should be set to **sizeof** ( **COLORMATCHSETUP** ).

</dd> <dt>

**dwVersion**
</dt> <dd>

Version of the **COLORMATCHSETUP** structure. This should be set to COLOR\_MATCH\_VERSION.

</dd> <dt>

**dwFlags**
</dt> <dd>

A set of bit flags used to initialize the dialog box. If set to 0 on entry, all controls assume their default states.

When the dialog box returns, these flags are set to indicate the user's input.

This member can be set using a combination of the following flags.



| Flag                   | Meaning                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CMS\_DISABLEICM        | If set on entry, this flag indicates that the "Enable Color Management" check box is cleared, disabling all other controls. If set on exit, it means that the user does not wish color management performed.                                                                                                                                                                              |
| CMS\_ENABLEPROOFING    | If set on entry, this flag indicates that the Proofing controls are to be enabled, and the Proofing check box is checked. If set on exit, it means that the user wishes to perform color management for a different target device than the selected printer.                                                                                                                              |
| CMS\_SETRENDERINTENT   | If set on entry, this flag indicates that the **dwRenderIntent** member contains the value to use to initialize the Rendering Intent control. Otherwise, the control defaults to Picture rendering. This flag is set on exit if WCS is enabled.                                                                                                                                           |
| CMS\_SETPROOFINTENT    | Ignored unless CMS\_ENABLEPROOFING is also set. If set on entry, and CMS\_ENABLEPROOFING is also set, this flag indicates that the **dwProofingIntent** member is to be used to initialize the Target Rendering Intent control. Otherwise, the control defaults to Picture rendering. This flag is set on exit if proofing is enabled.                                                    |
| CMS\_SETMONITORPROFILE | If set on entry, this flag indicates that the color management profile named in the **pMonitorProfile** member is to be the initial selection in the monitor profile control. If the specified profile is not associated with the monitor, this flag is ignored, and the default profile for the monitor is used.                                                                         |
| CMS\_SETPRINTERPROFILE | If set on entry, this flag indicates that the color management profile named in the **pPrinterProfile** member is to be the initial selection in the printer profile control. If the specified profile is not associated with the printer, this flag is ignored, and the default profile for the printer is used.                                                                         |
| CMS\_SETTARGETPROFILE  | If set on entry, this flag indicates that the color profile named in the **pTargetProfile** member is to be the initial selection in the target profile control. If the specified profile is not installed, this flag is ignored, and the default profile for the printer is used. If the printer has no default profile, then the first profile in alphabetical order will be displayed. |
| CMS\_USEHOOK           | This flag specifies that the **lpfnHook** member contains the address of a hook procedure, and the **lParam** member contains a value to be passed to the hook procedure when the WM\_INITDIALOG message is sent.                                                                                                                                                                         |
| CMS\_MONITOROVERFLOW   | This flag is set on exit if color management is to be enabled and the buffer size given in **ccMonitorProfile** is insufficient for the selected profile name. **GetLastError** returns ERROR\_INSUFFICIENT\_BUFFER in such a case.                                                                                                                                                       |
| CMS\_PRINTERROVERFLOW  | This flag is set on exit if color management is to be enabled and the buffer size given in **ccPrinterProfile** is insufficient for the selected profile name. **GetLastError** returns ERROR\_INSUFFICIENT\_BUFFER in such a case.                                                                                                                                                       |
| CMS\_TARGETOVERFLOW    | This flag is set on exit if proofing is to be enabled and the buffer size given in **ccTargetProfile** is insufficient for the selected profile name. **GetLastError** returns ERROR\_INSUFFICIENT\_BUFFER in such a case.                                                                                                                                                                |
| CMS\_USEAPPLYCALLBACK  | If set on entry, this flag indicates that the **SetupColorMatching** function should call the function [**PCMSCALLBACKW**](/windows/win32/api/icm/nc-icm-pcmscallbackw). The address of the callback function is contained in *lpfnApplyCallback*.                                                                                                                                                                    |
| CMS\_USEDESCRIPTION    | If set on entry, this flag instructs the **SetupColorMatching** function to retrieve the profile description contained in the profile description tags (See ICC Profile Format Specification v3.4). It will insert them into the **Monitor Profile**, **Printer Profile**, **Emulated Device Profile** edit boxes in the **Color Management** common dialog box.                          |



 

</dd> <dt>

**hwndOwner**
</dt> <dd>

The window handle to the owner of the dialog box, or **NULL** if the dialog box has no owner.

</dd> <dt>

**pSourceName**
</dt> <dd>

Pointer to an application-specified string which describes the source profile of the item for which color management is to be performed. If this is **NULL**, the Image Source control displays the name of the Windows default color profile.

</dd> <dt>

**pDisplayName**
</dt> <dd>

Points to a string naming the monitor to be used for color management. If this is not the name of a valid monitor, the first enumerated monitor is used.

</dd> <dt>

**pPrinterName**
</dt> <dd>

Points to a string naming the printer on which the image is to be rendered. If this is not a valid printer name, the default printer is used and named in the dialog.

</dd> <dt>

**dwRenderIntent**
</dt> <dd>

The type of color management desired. Valid values are:

INTENT\_PERCEPTUAL

 

INTENT\_SATURATION

 

INTENT\_RELATIVE\_COLORIMETRIC

 

INTENT\_ABSOLUTE\_COLORIMETRIC

For more information, see [Rendering Intents](rendering-intents.md).

</dd> <dt>

**dwProofingIntent**
</dt> <dd>

The type of color management desired for the proofed image. Valid values are:

INTENT\_PERCEPTUAL

 

INTENT\_SATURATION

 

INTENT\_RELATIVE\_COLORIMETRIC

 

INTENT\_ABSOLUTE\_COLORIMETRIC

For more information, see [Rendering Intents](rendering-intents.md).

</dd> <dt>

**pMonitorProfile**
</dt> <dd>

Pointer to a buffer in which to place the name of the user-selected monitor profile. If the CMS\_SETMONITORPROFILE flag is used, this flag can also be used to select a profile other than the monitor default when the dialog is first displayed.

</dd> <dt>

**ccMonitorProfile**
</dt> <dd>

The size of the buffer pointed to by the **pMonitorProfile** member, in characters. If the buffer is not large enough to hold the selected name, the name is truncated to this size, and ERROR\_INSUFFICIENT\_BUFFER is returned. A buffer of MAX\_PATH size always works.

</dd> <dt>

**pPrinterProfile**
</dt> <dd>

Points to a buffer in which to place the name of the user-selected printer profile. If the CMS\_SETPRINTERPROFILE flag is used, this flag can also be used to select a profile other than the printer default when the dialog is first displayed.

</dd> <dt>

**ccPrinterProfile**
</dt> <dd>

The size of the buffer pointed to by the **pPrinterProfile** member, in characters. If the buffer is not large enough to hold the selected name, the name is truncated to this size, and ERROR\_INSUFFICIENT\_BUFFER is returned. A buffer of MAX\_PATH size always works.

</dd> <dt>

**pTargetProfile**
</dt> <dd>

Points to a buffer in which to place the name of the user-selected target profile for proofing. If the CMS\_SETTARGETPROFILE flag is used, this flag can also be used to select a profile other than the printer default when the dialog is first displayed.

</dd> <dt>

**ccTargetProfile**
</dt> <dd>

The size of the buffer pointed to by the **pTargetProfile** member, in characters. If the buffer is not large enough to hold the selected name, the name is truncated to this size, and ERROR\_INSUFFICIENT\_BUFFER is returned. A buffer of MAX\_PATH size always works.

</dd> <dt>

**lpfnHook**
</dt> <dd>

If the CMS\_USEHOOK flag is set, this member is the address of a dialog procedure (see [DialogProc](https://msdn.microsoft.com/windows/desktop/37c1b0b2-cf81-45d9-9a4e-9e5f7fa58dfd) ) that can filter or handle messages for the dialog. The hook procedure receives no messages issued before WM\_INITDIALOG. It is called on the WM\_INITDIALOG message after the system-provided dialog procedure has processed the message. On all other messages, the hook procedure receives the message before the system-provided procedure. If the hook procedure returns **TRUE** to these messages, the system-provided procedure is not called.

The hook procedure may call the [EndDialog](https://msdn.microsoft.com/windows/desktop/925e8aa8-9d8d-4bec-a19e-ba24e78b2d10) function.

</dd> <dt>

**lParam**
</dt> <dd>

If the CMS\_USEHOOK flag is set, this member is passed to the application-provided hook procedure as the *lParam* parameter when the WM\_INITDIALOG message is processed.

</dd> <dt>

**lpfnApplyCallback**
</dt> <dd>

Contains a pointer to a callback function that is invoked when the **Apply** button of the Color Management dialog box is selected. If no callback function is provided, this member should be set to **NULL**. See [**PCMSCALLBACKW**](/windows/win32/api/icm/nc-icm-pcmscallbackw).

</dd> <dt>

**lParamApplyCallback**
</dt> <dd>

Contains a value that will be passed to the function **ApplyCallbackFunction** through its *lParam* parameter. The meaning and content of the value is specified by the application.

</dd> </dl>

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl> |



## See also

<dl> <dt>

[A Common Dialog for Color Management](what-s-new-in-version-1-0-of-wcs.md)
</dt> <dt>

[DialogProc](https://msdn.microsoft.com/windows/desktop/37c1b0b2-cf81-45d9-9a4e-9e5f7fa58dfd)
</dt> <dt>

[EndDialog](https://msdn.microsoft.com/windows/desktop/925e8aa8-9d8d-4bec-a19e-ba24e78b2d10)
</dt> </dl>

 

 





