---
title: Standard Properties
description: Standard Properties
ms.assetid: 08b7c388-a362-4d71-ac24-93675984881f
ms.topic: article
ms.date: 05/31/2018
---

# Standard Properties

OLE defines a set of standard DISPIDs for all three kinds of properties: control, ambient, and extended. The following tables list these standards for control properties, ambient properties, and extended properties.



| Control property                                                                               | Type                             | Description                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BackColor, ForeColor, FillColor, BorderColor<br/>                                        | **OLE\_COLOR**<br/>        | The control's color scheme<br/>                                                                                                                                                                                                    |
| BackStyle, FillStyle, BorderStyle, BorderWidth, BorderVisible, DrawStyle, DrawWidth<br/> | **short** or **long**<br/> | Bits that define a control's visual behavior, such as being solid or transparent, having thick or thin borders, line styles, and so forth.<br/>                                                                                    |
| Font<br/>                                                                                | **IDispatch \***<br/>      | The font used in the control, which is an **IDispatch** pointer to a standard font object. See [Standard Font Object](standard-font-object.md) for more information.<br/>                                                         |
| Caption, Text<br/>                                                                       | **BSTR**<br/>              | Strings containing the control's label (the caption) or its textual contents (the text). Note that the caption does not necessarily name the control in the container. See the extended Name property in the following table.<br/> |
| Enabled<br/>                                                                             | **BOOL**<br/>              | Determines whether the control is enabled or disabled. If disabled, the control is probably grayed.<br/>                                                                                                                           |
| Window<br/>                                                                              | **HWND**<br/>              | The window handle of the control, if it has one.<br/>                                                                                                                                                                              |
| TabStop<br/>                                                                             | **BOOL**<br/>              | Determines whether this control is a tab stop.<br/>                                                                                                                                                                                |



 



| Ambient property                         | Type                        | Description                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BackColor, ForeColor<br/>          | **OLE\_COLOR**<br/>   | Provides controls with the default background and foreground colors. Use by a control is optional.<br/>                                                                                                                                                                                                                                                                                          |
| Font<br/>                          | **IDispatch \***<br/> | A pointer to a standard font object that defines the default font for the form. Use by a control is optional. See [Standard Font Object](standard-font-object.md) for more information.<br/>                                                                                                                                                                                                    |
| LocaleID<br/>                      | **LCID**<br/>         | The language used in the container. Use by a control is recommended.<br/>                                                                                                                                                                                                                                                                                                                        |
| UserMode<br/>                      | **BOOL**<br/>         | Describes whether the container is in a design mode (**FALSE**) or run-mode (**TRUE**), which a control should use to change its available functionality as necessary.<br/>                                                                                                                                                                                                                      |
| UIDead<br/>                        | **BOOL**<br/>         | Describes whether the container is in a mode where controls should ignore user input. This applies irrespective of UserMode. A container might always set UIDead to **TRUE** in design mode, and may set it to **TRUE** when it has hit a breakpoint or such during run mode. A control must pay attention to this property.<br/>                                                                |
| MessageReflect<br/>                | **BOOL**<br/>         | Specifies whether the container would like to receive Windows messages such as WM\_CTLCOLOR, WM\_DRAWITEM, WM\_PARENTNOTIFY, and so on as events.<br/>                                                                                                                                                                                                                                           |
| SupportsMnemonics<br/>             | **BOOL**<br/>         | Describes whether the container processes mnemonics or not. A control can do whatever it wants with this information, such as not underline characters it would normally use as a mnemonic.<br/>                                                                                                                                                                                                 |
| ShowGrabHandles, ShowHatching<br/> | **BOOL**<br/>         | Describes whether a control should show a hatch border or grab handles (in the hatch border) when in-place active. Controls must obey these properties, giving the container ultimate control over who actually draws these bits of user interface. A control container may want to draw its own instead of relying on each control, in which case these ambients will always be **FALSE**.<br/> |
| DisplayAsDefault<br/>              | **BOOL**<br/>         | The container will expose a **TRUE** for this property through whatever site contains what is marked as the default button when the button control should draw itself with a thicker default frame.<br/>                                                                                                                                                                                         |



 



| Extended property          | Type                        | Description                                                           |
|----------------------------|-----------------------------|-----------------------------------------------------------------------|
| Name<br/>            | **BSTR**<br/>         | The container's name for the control.<br/>                      |
| Visible<br/>         | **BOOL**<br/>         | The control's visibility.<br/>                                  |
| Parent<br/>          | **IDispatch \***<br/> | The dispinterface of the form containing the control.<br/>      |
| Default, Cancel<br/> | **BOOL**<br/>         | Indicates if this control is the default or cancel button.<br/> |



 

All of these standard properties have negative DISPID values, indicating their standard status.

Note that to avoid conflicts in the programmatic symbols for these DISPIDs, all ambient properties are given symbols in the form DISPID\_AMBIENT\_*property* as in DISPID\_AMBIENT\_FORECOLOR. All other symbols use DISPID\_*property* as usual.

Some ambient properties, as well as control properties, involve colors. The **OLE\_COLOR** type mentioned in the previous tables can refer to a standard **COLORREF** type, an index to a palette, a palette-relative index, or a system color index used with the [**GetSysColor**](/windows/desktop/api/winuser/nf-winuser-getsyscolor) function. The [**OleTranslateColor**](/windows/desktop/api/OleCtl/nf-olectl-oletranslatecolor) function converts an **OLE\_COLOR** type to a **COLORREF** type given a palette.

## Related topics

<dl> <dt>

[Control Properties](control-properties.md)
</dt> </dl>

 

