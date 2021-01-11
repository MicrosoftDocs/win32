---
description: The PenInputPanel object enables you to easily add in-place pen input to your applications.
ms.assetid: 'ad63302e-b386-4b32-95bf-be1129839c33'
title: PenInputPanel class (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PenInputPanel
- PenInputPanel.IPenInputPanel
api_type: 
- COM
api_location: 
- InkObj.dll
- InkObj.dll.dll
---

# PenInputPanel class

\[Deprecated. **PenInputPanel** has been replaced by the [Text Input Panel (TIP)](text-input-panel-reference.md).\]

The **PenInputPanel** object enables you to easily add in-place pen input to your applications.

The **PenInputPanel** object is available as an attachable object that allows you to add Tablet PC Input Panel functionality to existing controls. The user interface is largely mandated by the current input language. You have the option of choosing the default input method for the **PenInputPanel** object, either handwriting or keyboard. The end user can switch between input methods using buttons on the user interface.

**PenInputPanel** has these types of members:

-   [Enumerations](#enumerations)
-   [Events](#events)
-   [Interfaces](#interfaces)
-   [Methods](#methods)
-   [Properties](#properties)

### Enumerations

The **PenInputPanel** class has these enumerations.



| Enumeration                    | Description                                                                               |
|:-------------------------------|:------------------------------------------------------------------------------------------|
| [**PanelType**](/windows/win32/api/peninputpanel/ne-peninputpanel-paneltype) | Defines the type of input currently available in the **PenInputPanel** object.<br/> |



 

### Events

The **PenInputPanel** class has these events.



| Event                                                  | Description                                                                                                                             |
|:-------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| [**InputFailed**](peninputpanel-inputfailed.md)       | Occurs when input focus changes before the **PenInputPanel** object was able to insert user input into the attached control.<br/> |
| [**PanelChanged**](peninputpanel-panelchanged.md)     | Occurs when the **PenInputPanel** object changes between layouts.<br/>                                                            |
| [**PanelMoving**](peninputpanel-panelmoving.md)       | Occurs when the **PenInputPanel** object is moving.<br/>                                                                          |
| [**VisibleChanged**](peninputpanel-visiblechanged.md) | Occurs when the **PenInputPanel** object has shown or hidden itself.<br/>                                                         |



 

### Interfaces

The **PenInputPanel** class defines these interfaces.



| Interface          | Description                                                             |
|:-------------------|:------------------------------------------------------------------------|
| **IPenInputPanel** | This object implements the **IPenInputPanel** COM interface.<br/> |



 

### Methods

The **PenInputPanel** class has these methods.



| Method                                                         | Description                                                                                                                                                                                             |
|:---------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CommitPendingInput**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-commitpendinginput) | Sends collected ink to the recognizer and posts the recognition result.<br/>                                                                                                                      |
| [**EnableTsf**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-enabletsf)                   | When passed **TRUE**, the **PenInputPanel** attempts to send text to the attached control through the Text Services Framework (TSF) and enables the use of the correction user interface.<br/>    |
| [**MoveTo**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-moveto)                         | Sets the position of the **PenInputPanel** object to a static screen position.<br/>                                                                                                               |
| [**Refresh**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-refresh)                       | Updates and restores the **PenInputPanel** properties based on Tablet PC Input Panel settings, automatically positions the pen input panel and sets the user interface to the default panel.<br/> |



 

### Properties

The **PenInputPanel** class has these properties.



| Property                                                                  | Access type           | Description                                                                                                                                                                    |
|:--------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AttachedEditWindow**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_attachededitwindow)<br/> | Read/write<br/> | Gets or sets the window handle of the control that the **PenInputPanel** object is attached to.<br/>                                                                     |
| [**AutoShow**](/windows/win32/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_autoshow)<br/>                     | Read/write<br/> | Gets or sets a Boolean value that specifies whether the **PenInputPanel** object appears when focus is set using the pen.<br/>                                           |
| [**Busy**](/windows/desktop/api/Peninputpanel/nf-peninputpanel-ipeninputpanel-get_busy)<br/>                             | Read-only<br/>  | Gets a Boolean value that specifies whether the **PenInputPanel** object is currently processing ink.<br/>                                                               |
| [**CurrentPanel**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_currentpanel)<br/>             | Read/write<br/> | Gets or sets which panel type is currently being used for input within the **PenInputPanel** object.<br/>                                                                |
| [**DefaultPanel**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_defaultpanel)<br/>             | Read/write<br/> | Gets or sets which panel type is the default panel type used for input within the **PenInputPanel** object.<br/>                                                         |
| [**Factoid**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_factoid)<br/>                       | Read/write<br/> | Gets or sets the string name of the factoid used in recognition.<br/>                                                                                                    |
| [**Height**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_height)<br/>                         | Read-only<br/>  | Gets the height of the **PenInputPanel** object in client coordinates.<br/>                                                                                              |
| [**HorizontalOffset**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_horizontaloffset)<br/>     | Read/write<br/> | Gets or sets the offset between the left edge of the **PenInputPanel** object and the left edge of the control to which it is attached.<br/>                             |
| [**Left**](/windows/win32/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_left)<br/>                             | Read-only<br/>  | Gets the horizontal, or x-axis, location of the left edge of the **PenInputPanel** object, in screen coordinates.<br/>                                                   |
| [**Top**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_top)<br/>                               | Read-only<br/>  | Gets the vertical, or y-axis, location of the top edge of the **PenInputPanel** object, in screen coordinates.<br/>                                                      |
| [**VerticalOffset**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_verticaloffset)<br/>         | Read/write<br/> | Gets or sets the offset between the closest horizontal edge of the **PenInputPanel** object and the closest horizontal edge of the control to which it is attached.<br/> |
| [**Visible**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_visible)<br/>                       | Read/write<br/> | Gets or sets a value that indicates whether the **PenInputPanel** object is visible.<br/>                                                                                |
| [**Width**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_width)<br/>                           | Read-only<br/>  | Gets the width of the **PenInputPanel** object in client coordinates.<br/>                                                                                               |



 

## Remarks

This object can be instantiated by calling the [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) method in C++.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[Programming the Input Panel Using the PenInputPanel Class](programming-the-input-panel-using-the-peninputpanel-class.md)
</dt> </dl>

 

 
