---
title: ActiveX Controls Registry Information
description: ActiveX Controls Registry Information
ms.assetid: fda5b1e6-2048-4df7-ba8f-145652e3883c
ms.topic: article
ms.date: 05/31/2018
---

# ActiveX Controls Registry Information

There are a number of registry entries and flags that are used. Additionally, controls can support component categories to classify the features they provide.

Registry keys related to controls are marked with an asterisk in the following tree:

```
HKEY_CLASSES_ROOT
   CLSID
      {control_CLSID}
         ProgID = <identifier>
         InprocServer32 = <filename>.dll
         *DefaultIcon = <filename>.<ext>,resourceID
         *ToolboxBitmap32 = <filename>.<ext>,resourceID
         *Control
         verb
            *n = &Properties...
         *MiscStatus = 0
         TypeLib = {object_typelibID}
         *Version = version_number
```

The **DefaultIcon** entry is used to identify an icon to be displayed when the control is minimized to an icon. The [**ExtractIcon**](/windows/win32/api/shellapi/nf-shellapi-extracticona) function is used to get the icon from the .DLL or .EXE file specified.

The **ToolboxBitmap32** entry identifies the module name and resource identifier for a 16\*15 bitmap to use for the face of a toolbar or toolbox button. The standard Windows icon size is too large to be used for this purpose. This entry specifically supports control containers that have a design mode in which one selects controls and places them on a form being designed. For example, in Visual Basic, the control's icon is displayed in the Visual Basic toolbox during design mode.

The **Control** entry marks an object as a control. This entry is often used by containers to fill in dialog boxes. The container uses this sub-key to determine whether to include an object in a dialog box that displays controls.

The **Insertable** sub-key can also be used with controls, depending on whether the object can act only as an in-place embedded object with no special control features. Objects marked with **Insertable** appear in the Insert Object dialog box of their container. The **Insertable** entry generally means that the control has been tested with non-control containers.

Both the **Insertable** and the **Control** sub-keys are optional. A control can omit the **Insertable** sub-key if it not designed to work with older containers that do not understand controls. A control can omit the **Control** key if it is only designed to work with a specific container and thus does not wish to be inserted in other containers.

Controls should have a Properties verb, OLEIVERB\_PROPERTIES, along with any other verbs they support. The Properties verb, as well as the standard verb OLEIVERB\_PRIMARY, instructs the control to display its property sheet. The Properties verb is displayed as the Properties item on the container's menu when the control is active. This way, the control can display its own property page allowing some useful functionality to the end user, even if the container does not handle controls.

A control defines the **MiscStatus** key to describe itself to potential containers. The bits take on the values from [**OLEMISC**](/windows/win32/api/oleidl/ne-oleidl-olemisc), and controls add several values to this enumeration. See the **OLEMISC** enumeration values for more information. The client can obtain this information by calling [**IOleObject::GetMiscStatus**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-getmiscstatus) without having to instantiate the control first.

Finally, **Version** describes the version of the control which should match the version of the type library associated with this control.

Also in the type information for a control, the attribute control marks a coclass entry as describing a control.

 

 