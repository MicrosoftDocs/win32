---
title: Localization Support for Common Controls
description: This topic describes the support for national languages that is built into the common controls.
ms.assetid: c5720198-9071-4213-8dad-50b4c015c5f0
ms.topic: article
ms.date: 05/31/2018
---

# Localization Support for Common Controls

This topic describes the support for national languages that is built into the common controls. The built-in national language support simplifies the implementation of localized applications.

This topic contains the following sections:

-   [Specifying a Language for the Common Controls](#specifying-a-language-for-the-common-controls)
-   [Specifying a Language for Controls in a Dialog Box](#specifying-a-language-for-controls-in-a-dialog-box)
-   [Related topics](#related-topics)

## Specifying a Language for the Common Controls

If you want to specify a language for the common controls that is different than the system language, call [**InitMUILanguage**](/windows/desktop/api/Commctrl/nf-commctrl-initmuilanguage). The language specified by this function applies only to the process from which the function is called.

To determine the language currently being used by the common controls, call [**GetMUILanguage**](/windows/desktop/api/Commctrl/nf-commctrl-getmuilanguage). It returns the value that was set by a previous call to [**InitMUILanguage**](/windows/desktop/api/Commctrl/nf-commctrl-initmuilanguage). The language returned is the one that was specified for the process it is called from. If **InitMUILanguage** has not been called, or was called from another process, **GetMUILanguage** will return a default value.

## Specifying a Language for Controls in a Dialog Box

Unlike common controls, predefined controls such as buttons or edit boxes do not use the current system language by default. The native font control is an invisible control that works in the background to allow a dialog box's predefined controls to display the current system language.

To use the native font control, follow this procedure.

1.  Initialize the native font control by calling [**InitCommonControlsEx**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrolsex). Set the **dwICC** member of the [**INITCOMMONCONTROLSEX**](/windows/desktop/api/Commctrl/ns-commctrl-taginitcommoncontrolsex) structure pointed to by *lpInitCtrls* to ICC\_NATIVEFNTCTL\_CLASS.
2.  Add the control to the resource script for the dialog box. Set one or more of the following style flags to specify which controls will be affected. 

    | Flag              | Applies to                                                                                                                                                                                                                                                       |
    |-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | NFS\_EDIT         | Edit controls                                                                                                                                                                                                                                                    |
    | NFS\_STATIC       | Static controls                                                                                                                                                                                                                                                  |
    | NFS\_LISTCOMBO    | List, ComboBox, List-View, and ComboBoxEx controls                                                                                                                                                                                                               |
    | NFS\_BUTTON       | Button controls                                                                                                                                                                                                                                                  |
    | NFS\_ALL          | All controls                                                                                                                                                                                                                                                     |
    | NFS\_USEFONTASSOC | East Asian platform. The control uses the font association feature instead of switching to the native font. All other platforms ignore it. This is deprecated for Windows Vista, and is not supported in comctl v6. This exists in comctl v5 for legacy reasons. |

    

     

The following example illustrates how to add a native font control to a resource script. It causes the dialog box's edit, list, and combo box controls to display text using the current system language.


```
CONTROL    "",-1,"NativeFontCtl",NFS_EDIT|NFS_LISTCOMBO,0,0,0,0
```



## Related topics

<dl> <dt>

[About Common Controls](common-controls-intro.md)
</dt> </dl>

 

 




