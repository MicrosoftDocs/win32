---
title: OLE/COM Object Viewer
description: The OLE-COM object viewer, Oleview.exe, is an application supplied with Visual C++ that displays the COM objects installed on your computer and the interfaces they support. You can use this object viewer to view type libraries.
ms.assetid: 896a78a7-f023-4f32-b5bb-afee4a40a7fc
ms.topic: article
ms.date: 05/31/2018
---

# OLE/COM Object Viewer

The OLE/COM Object Viewer, oleview.exe, is an application supplied in the Windows SDK that displays the COM objects installed on your computer and the interfaces they support. You can use this object viewer to view type libraries and interfaces. 

The OLE/COM Object Viewer app is found in the Windows SDK in \\Program Files (x86)\\Windows Kits\\10\\[version]\\[architecture]\\oleview.exe. The first time you use oleview.exe, run it from an elevated command prompt. The interface viewer requires administrator rights to register its DLL.

## To view a COM object's type library

1.  On the object viewer **File** menu, choose **View TypeLib**. An **Open** dialog box appears.

1.  Specify the type library file you want to open, and choose **OK**.

The object viewer displays the object's interfaces.

## To view a registered object's interfaces

1. In the **Object Classes** > **Grouped by Component** category in the viewer, open the **Automation Objects** folder to view the registered Automation objects.

1. Select one of the controls. Several tabs appear in the right pane; the interfaces that are implemented by the control are displayed on the **Registry** tab.

   - If you open the shortcut menu for a control in the left pane and then choose **View Type Information**, the ITypeInfo Viewer displays a reconstructed .idl or .odl file.

   - If you expand the control node in the left pane, a list of the interfaces in the object is displayed. If you select an interface, its registry entry is displayed in the right pane.

   - If you open the shortcut menu for an interface and then choose View, the OLE/COM Object Viewer displays a dialog box that shows the GUID for the interface and an option to view type library information, if it is available. Selecting **View Type Info** displays a portion of a reconstructed .idl file that is specific to the interface in the ITypeInfo Viewer.

   - In the ITypeInfo Viewer, you can select an interface member in the tree view to display the accessor method signatures in the right pane.

## Related topics

<dl> <dt>

[Translating to C++](translating-to-c--.md)
</dt> </dl>

 

 
