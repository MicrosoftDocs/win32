---
title: Adding Icons and Context Menus with Shell Extensions
description: You can improve your users' experience with Microsoft Windows Desktop Search (WDS) and your protocol handler by implementing Shell extensions.
ms.assetid: 899f3fd1-1ae9-45fe-ae6d-26d4f07bf6e4
ms.topic: article
ms.date: 05/31/2018
---

# Adding Icons and Context Menus with Shell Extensions

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use [Windows Search](../search/-search-3x-wds-overview.md) instead.

You can improve your users' experience with Microsoft Windows Desktop Search (WDS) and your protocol handler by implementing Shell extensions. Without further extension, the protocol handler you create will not include the following user experiences:

-   WDS will not display specific icons for your results.
-   When users double-click an item, the user interface will not respond to the event.
-   When users right-click an item, the context menu will not support any operations for the item.

Minimal implementations of **IPersist** and **IPersistFolder** are required by **IShellFolder**, and a minimal implementation of **IShellFolder** is required for **IContextMenu** and **IExtractIcon**, the two interfaces that provide a more seamless user experience.

 

## IPersist

The **IPersist** interface defines the single method **GetClassID**, which is designed to supply the CLSID of an object that can be stored persistently in the system.



| Method       | Description                                 |
|--------------|---------------------------------------------|
| GetClassID() | Returns the ClassID of the protocol handler |



 

> [!Note]
>
> The same CLSID should be implemented for **IPersist**, **IPersistFolder** and **IShellFolder**.

 

 

## IPersistFolder

The **IPersistFolder** interface is used to initialize Shell folder objects. Implementation of this interface, which is derived from **IPersist**, is how the folder is told where it is in the Shell namespace.



| Method       | Description                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------|
| Initialize() | Instructs a Shell folder object to initialize itself based on the information passed and returns S\_OK |



 

> [!Note]
>
> The same CLSID should be implemented for **IPersist**, **IPersistFolder** and **IShellFolder**.

 

You do not use this interface directly. It is used by the file system implementation of the IShellFolder::BindToObject interface when it initializes a Shell folder object.

 

## IShellFolder

The **IShellFolder** interface is used to manage folders, and a partial implementation is required so that the icon and context interfaces implemented for a protocol handler will behave correctly in the Windows Desktop Search results user interface. Most of the functionality required is exposed through the **GetUIObjectOf** method. This method enables an add-in to query for the **IExtractIcon** and **IContextMenu** interfaces.

The **IShellFolder** interface uses PIDLs instead of URLs. In contrast to the requirements of a complete Namespace extension, add-ins can use a simple IDL structure that contains only the URL.

The following methods of **IShellFolder** must be implemented. Note that five of these methods require minimal implementation.



| Method             | Description                                                                                                                                                                                                 |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BindToObject()     | Returns E\_NOTIMPL                                                                                                                                                                                          |
| BindToStorage()    | Returns E\_NOTIMPL                                                                                                                                                                                          |
| CreateViewObject() | Returns E\_NOTIMPL                                                                                                                                                                                          |
| SetNameOf()        | Returns E\_NOTIMPL                                                                                                                                                                                          |
| ParseDisplayName() | Converts a URL to the PIDL structure                                                                                                                                                                        |
| CompareIDs()       | Compares two PIDL values                                                                                                                                                                                    |
| GetDisplayNameOf() | Returns the URL for a PIDL                                                                                                                                                                                  |
| GetUIObjectOf()    | This method is similar to the OLE COM QueryInterface method. If an icon is requested, the caller requests the IID\_IExtractIcon; if a context menu is requested, the caller requests the IID\_IContextMenu. |



 

> [!Note]
>
> The same CLSID should be implemented for **IPersist**, **IPersistFolder** and **IShellFolder**.

 

**IShellFolder** is not used to enumerate folders. This means that the display name of a folder will be the physical URL. This may change in the future.

 

## IContextMenu

When WDS displays results to the user, the user can right-click an item and see a context menu defined by your **IContextMenu** interface.

The default action on the context menu is the same action taken when the item is double-clicked. Without the corresponding **IShellFolder** or **IContextMenu** interfaces for the item, the default behavior for a double-click event is to pass the URL as an argument to the ShellExecute function.

 

## IExtractIcon

**IExtractIcon** retrieves an icon for the WDS user interface based on the URL in the PIDL provided by your protocol handler.

 

## Code Sample

The [Custom Protocol Handler User Interface Sample Code](-search-2x-wds-ph-ui-samplecode.md) demonstrates an implementation of **IShellFolder** and supporting interfaces and includes support for manipulating the PIDLs.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Custom Protocol Handler User Interface Sample Code](-search-2x-wds-ph-ui-samplecode.md)
</dt> <dt>

[Installing and Registering Protocol Handlers](-search-2x-wds-ph-install-registration.md)
</dt> </dl>

 

 




