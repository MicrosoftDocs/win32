---
title: ISoftKbd interface (Softkbdc.h)
description: The ISoftKbd interface is used by applications and text services to implement a soft keyboard.
ms.assetid: 804634bd-646e-459f-9fbb-cd6929b11fab
keywords:
- ISoftKbd interface Text Services Framework
- ISoftKbd interface Text Services Framework , described
topic_type:
- apiref
api_name:
- ISoftKbd
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd interface

The **ISoftKbd** interface is used by applications and text services to implement a soft keyboard.

## Members

The **ISoftKbd** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ISoftKbd** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISoftKbd** interface has these methods.



| Method                                                                                        | Description                                                                                                   |
|:----------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| [**AdviseSoftKeyboardEventSink**](isoftkbd-advisesoftkeyboardeventsink.md)                   | Installs a soft keyboard event sink to handle OnKeySelection notifications from the soft keyboard.<br/> |
| [**CreateSoftKeyboardLayoutFromResource**](isoftkbd-createsoftkeyboardlayoutfromresource.md) | Creates a soft keyboard layout from the specified resource.<br/>                                        |
| [**CreateSoftKeyboardLayoutFromXMLFile**](isoftkbd-createsoftkeyboardlayoutfromxmlfile.md)   | Creates a soft keyboard layout from the specified XML file.<br/>                                        |
| [**CreateSoftKeyboardWindow**](isoftkbd-createsoftkeyboardwindow.md)                         | Creates a soft keyboard window.<br/>                                                                    |
| [**DestroySoftKeyboardWindow**](isoftkbd-destroysoftkeyboardwindow.md)                       | Destroys a soft keyboard window.<br/>                                                                   |
| [**EnumSoftKeyboard**](isoftkbd-enumsoftkeyboard.md)                                         | Enumerates the possible soft keyboards that support the specified language.<br/>                        |
| [**GetSoftKeyboardColors**](isoftkbd-getsoftkeyboardcolors.md)                               | Retrieves the soft keyboard color corresponding to the supplied color type.<br/>                        |
| [**GetSoftKeyboardPosSize**](isoftkbd-getsoftkeyboardpossize.md)                             | Retrieves the starting position and size of a soft keyboard.<br/>                                       |
| [**GetSoftKeyboardTextFont**](isoftkbd-getsoftkeyboardtextfont.md)                           | Retrieves the text font used by a soft keyboard.<br/>                                                   |
| [**GetSoftKeyboardTypeMode**](isoftkbd-getsoftkeyboardtypemode.md)                           | Retrieves the type mode for a soft keyboard.<br/>                                                       |
| [**Initialize**](isoftkbd-initialize.md)                                                     | Initializes all necessary fields for a soft keyboard and generates standard soft keyboard layouts.<br/> |
| [**SelectSoftKeyboard**](isoftkbd-selectsoftkeyboard.md)                                     | Selects the specified soft keyboard.<br/>                                                               |
| [**SetKeyboardLabelText**](isoftkbd-setkeyboardlabeltext.md)                                 | Sets the label text from the layout for a soft keyboard.<br/>                                           |
| [**SetKeyboardLabelTextCombination**](isoftkbd-setkeyboardlabeltextcombination.md)           | Sets a combination of label and text used to describe a soft keyboard.<br/>                             |
| [**SetSoftKeyboardColors**](isoftkbd-setsoftkeyboardcolors.md)                               | Sets the soft keyboard color corresponding to the supplied color type.<br/>                             |
| [**SetSoftKeyboardPosSize**](isoftkbd-setsoftkeyboardpossize.md)                             | Sets the starting position and size of a soft keyboard.<br/>                                            |
| [**SetSoftKeyboardTextFont**](isoftkbd-setsoftkeyboardtextfont.md)                           | Sets the text font used by a soft keyboard.<br/>                                                        |
| [**SetSoftKeyboardTypeMode**](isoftkbd-setsoftkeyboardtypemode.md)                           | Sets the type mode for a soft keyboard.<br/>                                                            |
| [**ShowKeysForKeyScanMode**](isoftkbd-showkeysforkeyscanmode.md)                             | Displays the keys used for the key scan mode for a soft keyboard.<br/>                                  |
| [**ShowSoftKeyboard**](isoftkbd-showsoftkeyboard.md)                                         | Displays a soft keyboard.<br/>                                                                          |
| [**UnadviseSoftKeyboardEventSink**](isoftkbd-unadvisesoftkeyboardeventsink.md)               | Removes a soft keyboard event sink.<br/>                                                                |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                        |
| Header<br/>                   | <dl> <dt>Softkbdc.h</dt> </dl>  |
| IDL<br/>                      | <dl> <dt>Softkbd.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Softkbd.dll</dt> </dl> |



 

