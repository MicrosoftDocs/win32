---
description: To ensure that your data is indexed and presented correctly to the user during searches, you need to implement Shell data stores (also known as Shell Namespace Extensions), and file type handlers (also known as Shell extensions, extension handlers, or Shell extension handlers).
ms.assetid: 38cebb3c-51bf-439c-8d4e-445344f6cb66
title: Adding Icons, Previews and Shortcut Menus
ms.topic: article
ms.date: 05/31/2018
---

# Adding Icons, Previews and Shortcut Menus

To ensure that your data is indexed and presented correctly to the user during searches, you need to implement Shell data stores (also known as [Shell Namespace Extensions](../shell/nse-works.md)), and file type handlers (also known as Shell extensions, [extension handlers](../shell/handlers.md), or Shell extension handlers).

This topic describes the following interfaces:

-   [Implementing File Type Handlers](#implementing-file-type-handlers)
    -   [IPersist](#ipersist)
    -   [IPersistFolder](#ipersistfolder)
    -   [IShellFolder](#ishellfolder)
    -   [IContextMenu](#icontextmenu)
    -   [IExtractIcon](#iextracticon)
    -   [IPreviewHandler](#ipreviewhandler)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## Implementing File Type Handlers

These Shell extensions or file type handlers provide your users with the following Shell experiences:

-   The results view displays a specific icon for your item type.
-   The results view displays a preview of the item when the user selects the item.
-   Users can double-click items to initiate events such as opening the file.
-   Users can right-click items to access a shortcut (context) menu.
-   Users can drag-and-drop items.

Like all Component Object Model (COM) objects, file type handlers must implement an [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface and a class factory.

In Windows XP or earlier, handlers should also implement:

-   Either [IPersistFile Interface](/windows/win32/api/objidl/nn-objidl-ipersistfile)
-   Or [IShellExtInit Interface](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellextinit)

In Windows Vista, [IPersistFile Interface](/windows/win32/api/objidl/nn-objidl-ipersistfile) and [IShellExtInit Interface](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellextinit) were replaced by the following three interfaces for Shell to initialize the handler:

-   [IInitializeWithStream Interface](/windows/win32/api/propsys/nn-propsys-iinitializewithstream)
-   [IInitializeWithItem Interface](/windows/win32/api/shobjidl_core/nn-shobjidl_core-iinitializewithitem)
-   [IInitializeWithFile Interface](/windows/win32/api/propsys/nn-propsys-iinitializewithfile)

To provide a reasonable user experience you must provide a Shell data store with your protocol handler. That data store then serves as the "factory" for icon handlers, shortcut menu handlers, preview handlers, and so forth. Minimal implementations of [IPersist Interface](/windows/desktop/api/objidl/nn-objidl-ipersist) and [IPersistFolder Interface](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ipersistfolder) are required by [IShellFolder Interface](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder), and a minimal implementation of IShellFolder Interface is required for the [IContextMenu](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) and [IExtractIcon](/windows/win32/api/shlobj_core/nn-shlobj_core-iextracticona).

> [!Note]  
> The same class identifier (CLSID) should be implemented for **IPersist**, **IPersistFolder** and **IShellFolder**.

 

For more information about creating a Shell data store to support a protocol handler, see [Implementing the Basic Folder Object Interfaces](/previous-versions/windows/desktop/legacy/cc144093(v=vs.85)).

### IPersist

The **IPersist** interface defines the single method **GetClassID**, which is designed to supply the CLSID of an object that can be stored persistently in the system.



| Method     | Description                                      |
|------------|--------------------------------------------------|
| GetClassID | Returns the CLSID of the Shell data store object |



 

### IPersistFolder

The **IPersistFolder** interface is used to initialize Shell folder objects. Implementation of this interface, which is derived from **IPersist**, is how the folder is told where it is in the Shell namespace. You do not use this interface directly. It is used by the file system implementation of [IShellFolder::BindToObject Method](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject) when it initializes a Shell folder object.



| Method     | Description                                                                                            |
|------------|--------------------------------------------------------------------------------------------------------|
| Initialize | Instructs a Shell folder object to initialize itself based on the information passed and returns S\_OK |



 

### IShellFolder

The [IShellFolder Interface](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) interface is used to manage folders, and a partial implementation is required so that the icon and context interfaces implemented for a protocol handler will behave correctly in the Windows Search results user interface. Most of the functionality required is exposed through the **GetUIObjectOf** method. This method enables an add-in to query for the **IExtractIcon** and **IContextMenu** interfaces.

The [IShellFolder Interface](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) interface uses PIDLs instead of URLs. In contrast to the requirements of a complete Shell data store, add-ins can use a simple IDL structure that contains only the URL.

The following methods of [IShellFolder Interface](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) must be implemented. Five of these methods require minimal implementation.



| Method           | Description                                                                                                                                                                                                                                                                   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BindToObject     | Returns E\_NOTIMPL                                                                                                                                                                                                                                                            |
| BindToStorage    | Returns E\_NOTIMPL                                                                                                                                                                                                                                                            |
| CreateViewObject | Returns E\_NOTIMPL                                                                                                                                                                                                                                                            |
| SetNameOf        | Returns E\_NOTIMPL                                                                                                                                                                                                                                                            |
| ParseDisplayName | Converts a URL to the PIDL structure                                                                                                                                                                                                                                          |
| CompareIDs       | Compares two PIDL values                                                                                                                                                                                                                                                      |
| GetDisplayNameOf | Returns the URL for a PIDL                                                                                                                                                                                                                                                    |
| GetUIObjectOf    | This method is similar to the [IUnknown::QueryInterface Method](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)). If an icon is requested, the caller requests the IID\_IExtractIcon; if a shortcut menu is requested, the caller requests the IID\_IContextMenu |



 

**IShellFolder** is not used to enumerate folders. This means that the display name of a folder will be the physical URL. This may change in the future.

### IContextMenu

When Windows Search displays results to the user, the user can right-click an item and see a shortcut menu defined by your **IContextMenu** interface. Shortcut menus are also known as context menus.

The default action on the context menu is the same action taken when the item is double-clicked. Without the corresponding **IShellFolder** or **IContextMenu** interfaces for the item, the default behavior for a double-click event is to pass the URL as an argument to the [ShellExecute Function](/windows/win32/api/shellapi/nf-shellapi-shellexecutea) function.

Refer to [Creating Context Menu Handlers](../shell/context-menu-handlers.md) for more information on creating shortcut menu handlers, and [Sample: Shell Extensions for Protocol Handlers](-search-3x-wds-ph-ui-samplecode.md) for sample code.

### IExtractIcon

**IExtractIcon** retrieves an icon for the Windows Search user interface based on the URL in the PIDL provided by your protocol handler.

Refer to [Creating Icon Handlers](../shell/how-to-create-icon-handlers.md) for more information on creating icon handlers and [Sample: Shell Extensions for Protocol Handlers](-search-3x-wds-ph-ui-samplecode.md) for sample code.

### IPreviewHandler

The [IPreviewHandler](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ipreviewhandler) renders a rich preview of a selected item in Windows Explorer. Previews are available in Windows Search 4.0, or in Windows Vista with Windows Desktop Search 3.x.

To create a custom preview handler:

1.  Implement an [IPreviewHandler](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ipreviewhandler) that takes an [IStream](/windows/win32/api/objidl/nn-objidl-istream), following the guidelines provided in [Preview Handlers](../shell/preview-handlers.md).
2.  Register your preview handler:

    ```
    HKEY_CLASSES_ROOT\<Your_Object_Type>
    ```

    ```
    HKEY_CLASSES_ROOT\<Your_Object_Type>\ShellEx
    ```

    ```
    HKEY_CLASSES_ROOT\<Your_Object_Type>\ShellEx\{8895b1c6-b41f-4c1c-a562-0d564250836f}
       @ = {<Your_PreviewHandler_GUID>}
    ```

3.  Complete the following two steps to implement a Shell folder for your URL:
    1.  In [IShellFolder::GetUIObjectOf Method](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getuiobjectof), handle [IQueryAssociations](/windows/win32/api/shlwapi/nn-shlwapi-iqueryassociations) and return your association for your Shell items, as shown in the following code sample.

        ```
        CComPtr<IQueryAssociations> spqa;
        AssocCreate(CLSID_QueryAssociations, __uuidof(IQueryAssociations), &spqa);
        spqa->Init(0, L"Your_Object_Type", NULL, NULL);
        spqa->QueryInterface(riid, ppvReturn);
        ```

        

    2.  After the Shell queries your Shell folder for the data stream to initialize the preview handler, go to your [IShellFolder::BindToObject Method](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject) method, handle IID\_IStream and return an [IStream](/windows/win32/api/objidl/nn-objidl-istream) to your URL.

To reuse an existing preview handler for your file type, follow these two steps:

1.  Register that preview handler for your file type using the CLSID of the existing preview handler in place of <Your\_PreviewHandler\_GUID>.
2.  Implement a Shell folder.

For more information on creating preview handlers, see [IPreviewHandler](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ipreviewhandler) and [Preview Handlers](../shell/preview-handlers.md).

## Additional Resources

-   For an overview of the indexing process, see [The Indexing Process](-search-indexing-process-overview.md).
-   For information about creating handlers, see [Registering Shell Extensions](../shell/reg-shell-exts.md), [Creating Shell Extension Handlers](../shell/handlers.md), [Context Menu](/previous-versions/windows/desktop/legacy/cc144169(v=vs.85)), [Shell Namespace Extensions](../shell/nse-works.md) and [Preview Handlers](../shell/preview-handlers.md).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Developing Protocol Handlers](-search-3x-wds-phaddins.md)
</dt> <dt>

[Understanding Protocol Handlers](-search-3x-wds-extidx-prot-implementing.md)
</dt> <dt>

[Notifying the Index of Changes](-search-3x-wds-notifyingofchanges.md)
</dt> <dt>

[Code Sample: Shell Extensions for Protocol Handlers](-search-3x-wds-ph-ui-samplecode.md)
</dt> <dt>

[Installing and Registering Protocol Handlers](-search-3x-wds-ph-install-registration.md)
</dt> <dt>

[Creating a Search Connector for a Protocol Handler](-search-3x-wds-ph-search-connector.md)
</dt> <dt>

[Debugging Protocol Handlers](-search-ws-protocolhandlertesting.md)
</dt> </dl>

 

 
