---
title: Working with Extension Snap-ins
description: Extension snap-ins extend the functionality of other snap-ins, but they are not directly added to a console like stand-alone snap-ins.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5ea3829a-2e3c-4daf-9dfb-940a2a1df3a1'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["extension snap-ins MMC"]
---

# Working with Extension Snap-ins

Extension snap-ins extend the functionality of other snap-ins, but they are not directly added to a console like stand-alone snap-ins. Extension snap-ins can add context menu items, property pages, toolbar buttons, taskpad tasks, and items to the namespace of the extended snap-in (also called the primary snap-in).

Primary snap-ins can themselves extend the functionality of other snap-ins. That is, the same snap-in code base can create a primary snap-in instance and an extension snap-in instance.

An extension snap-in is loaded only when the snap-in it extends is loaded and the feature it extends is used. For example, when the user displays a context menu in a stand-alone snap-in, MMC builds the context menu, prompts the stand-alone snap-in to add its items, and then prompts the extension snap-in to add its items. After all snap-ins have added their items, MMC displays the context menu and then forwards the menu click to the snap-in that owns the item.

An extension snap-in can extend only the node types that a stand-alone snap-in indicates as being extendable. The extension snap-in declares itself as a subordinate to the extendable node types, and then for each occurrence of those node types in the console, the console automatically adds the related snap-in extensions below it.

It is important to understand that a node type can represent a scope item, a standard list view result item, or a virtual list view result item added by the primary snap-in. Consult the documentation for the primary snap-in to determine what the node type represents and the format of its exported data.

There are three types of extension snap-ins; the difference between the various types depends on how they are added and removed:

-   Required extensions are extension snap-ins that are automatically added to the primary snap-in when the primary snap-in is loaded. Required extensions are added to all instances of the primary snap-in. Required extensions cannot be removed programmatically or through the [Add/Remove Snap-in dialog box](add-remove-snap-in-dialog-box.md).
-   Dynamic extensions are extension snap-ins that are added to a scope item or result item programmatically at run time. A snap-in can dynamically add any type of extension to its own items. When an extension snap-in dynamically extends an item of a primary snap-in, the extension snap-in extends only the specific instance of the item. Other items of that node type are not affected. Dynamically adding an extension is not the same as adding an extension to a snap-in through the [Add/Remove Snap-in dialog box](add-remove-snap-in-dialog-box.md). By using the Add/Remove Snap-in dialog box to add an extension to a snap-in, the extension is added to all instances of snap-ins of that type. If you want all instances of your snap-in to be extended by one or more snap-ins, the snap-in should implement required extensions. As just suggested, you cannot add or remove dynamic extensions through the Add/Remove Snap-in dialog box.
-   Extension snap-ins that are neither required extensions nor dynamic extensions can be added or removed through the [Add/Remove Snap-in dialog box](add-remove-snap-in-dialog-box.md). A list of available extensions is presented in the Add/Remove Snap-in dialog box of the primary snap-in that is loaded in the current console.

## Flow of Information to Extension Snap-ins

Extension snap-ins receive context information through data objects, which are passed to extensions when the user selects a scope or result item of a node type that they extend. When the user selects the item in the primary snap-in, MMC requests a data object from the primary snap-in. MMC then passes the data object to the extension snap-in as a parameter in the method call that notifies the extension of the user action. The particular method that is called depends on the context. For example, context menu extensions receive data objects in calls to their [**IExtendContextMenu::AddMenuItems**](iextendcontextmenu-addmenuitems.md) and [**IExtendContextMenu::Command**](iextendcontextmenu-command.md) implementations.

When requesting a data object from the primary snap-in, MMC specifies the cookie value of the selected scope or result item in the cookie parameter in the call to the **QueryDataObject** method. Recall that the cookie value of an item is simply a unique identifier for the item that the snap-in-supplies. For the extension snap-in to extract the correct context information from the data object it receives, a primary snap-in's implementation of [**IDataObject**](_ole_idataobject) must store the cookie value of the item for which MMC is requesting a data object. The primary snap-in should then publish and support special clipboard formats that extensions can use for requesting context information. Primary snap-ins can also publish clipboard formats that allow bidirectional information exchange between the primary snap-in and extensions.

MMC places no restrictions on how data exchange using the [**IDataObject**](_ole_idataobject) interface is accomplished. Following are two common methods that primary snap-ins can use:

-   Implementing the [**IDataObject::GetDataHere**](_ole_idataobject_getdatahere) method in data objects requested by MMC and passed on to extensions. Extension snap-ins must allocate and free the storage medium in the method call and define the format, medium, and target device to use when passing the data.
-   Exposing a private interface on the data object. Extensions can then query the data object passed to them from MMC for the private interface and call methods on the interface to exchange information.

## How MMC Loads an Extension Snap-in

When the user selects a scope or result item in the namespace of a primary snap-in, MMC checks to see if the node type of the selected item is extendable. If it is extendable, MMC looks in the registry under the MMC\\NodeTypes\\{nodetypeGUID}\\Extensions\\{extensionType} subkey for the CLSIDs of all extensions that extend the particular node type. The nodetypeGUID key represents the node type GUID of the node type that is extended, and extensionType represents the type of extension.

MMC then loads the extension snap-ins that extend the selected item and queries them for the interface that implements the extension features. For example, context menu extensions must implement the [**IExtendContextMenu**](iextendcontextmenu.md) interface, and MMC queries the extension snap-in for this interface when a node type it extends is selected. MMC uses the returned interface pointers to call methods on the extensions and to notify them of user actions.

Generally, MMC releases interfaces on extension snap-ins when their user interface is dismissed. For example, a context menu extension is released after the context menu is dismissed. The only exceptions to this are namespace extensions and taskpad extensions (that support the [**IComponentData**](icomponentdata.md) interface). MMC retains their interfaces for the duration of the current MMC session.

Dynamic extensions and required extensions work differently. For more information, see [Adding Dynamic Extensions](adding-dynamic-extensions.md) and [Adding Required Extensions](adding-required-extensions.md).

## Related topics

<dl> <dt>

[Requirements for Primary Snap-ins](requirements-for-primary-snap-ins.md)
</dt> <dt>

[Requirements for Extension Snap-ins](requirements-for-extension-snap-ins.md)
</dt> </dl>

 

 




