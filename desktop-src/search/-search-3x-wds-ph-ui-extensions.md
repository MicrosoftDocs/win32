---
Description: 'To ensure that your data is indexed and presented correctly to the user during searches, you need to implement Shell data stores (also known as Shell Namespace Extensions), and file type handlers (also known as Shell extensions, extension handlers, or Shell extension handlers).'
ms.assetid: '38cebb3c-51bf-439c-8d4e-445344f6cb66'
title: 'Adding Icons, Previews and Shortcut Menus'
---

# Adding Icons, Previews and Shortcut Menus

To ensure that your data is indexed and presented correctly to the user during searches, you need to implement Shell data stores (also known as [Shell Namespace Extensions](http://msdn.microsoft.com/en-us/library/cc144095(VS.85).aspx)), and file type handlers (also known as Shell extensions, [extension handlers](http://msdn.microsoft.com/en-us/library/Cc144067(VS.85).aspx), or Shell extension handlers).

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

Like all Component Object Model (COM) objects, file type handlers must implement an [IUnknown](http://msdn.microsoft.com/en-us/library/ms680509(VS.85).aspx) interface and a class factory.

In Windows XP or earlier, handlers should also implement:

-   Either [IPersistFile Interface](http://msdn.microsoft.com/en-us/library/ms687223(VS.85).aspx)
-   Or [IShellExtInit Interface](http://msdn.microsoft.com/en-us/library/bb775096(VS.85).aspx)

In Windows Vista, [IPersistFile Interface](http://msdn.microsoft.com/en-us/library/ms687223(VS.85).aspx) and [IShellExtInit Interface](http://msdn.microsoft.com/en-us/library/bb775096(VS.85).aspx) were replaced by the following three interfaces for Shell to initialize the handler:

-   [IInitializeWithStream Interface](http://msdn.microsoft.com/en-us/library/bb761810(VS.85).aspx)
-   [IInitializeWithItem Interface](http://msdn.microsoft.com/en-us/library/bb761814(VS.85).aspx)
-   [IInitializeWithFile Interface](http://msdn.microsoft.com/en-us/library/bb761818(VS.85).aspx)

To provide a reasonable user experience you must provide a Shell data store with your protocol handler. That data store then serves as the "factory" for icon handlers, shortcut menu handlers, preview handlers, and so forth. Minimal implementations of [IPersist Interface](http://msdn.microsoft.com/en-us/library/ms688695.aspx) and [IPersistFolder Interface](http://msdn.microsoft.com/en-us/library/bb775348(VS.85).aspx) are required by [IShellFolder Interface](http://msdn.microsoft.com/en-us/library/bb775075(VS.85).aspx), and a minimal implementation of IShellFolder Interface is required for the [IContextMenu](http://msdn.microsoft.com/en-us/library/bb776095(VS.85).aspx) and [IExtractIcon](http://msdn.microsoft.com/en-us/library/bb761854(VS.85).aspx).

> [!Note]  
> The same class identifier (CLSID) should be implemented for **IPersist**, **IPersistFolder** and **IShellFolder**.

 

For more information about creating a Shell data store to support a protocol handler, see [Implementing the Basic Folder Object Interfaces](http://msdn.microsoft.com/en-us/library/cc144093(VS.85).aspx).

### IPersist

The **IPersist** interface defines the single method **GetClassID**, which is designed to supply the CLSID of an object that can be stored persistently in the system.



| Method     | Description                                      |
|------------|--------------------------------------------------|
| GetClassID | Returns the CLSID of the Shell data store object |



 

### IPersistFolder

The **IPersistFolder** interface is used to initialize Shell folder objects. Implementation of this interface, which is derived from **IPersist**, is how the folder is told where it is in the Shell namespace. You do not use this interface directly. It is used by the file system implementation of [IShellFolder::BindToObject Method](http://msdn.microsoft.com/en-us/library/bb775059(VS.85).aspx) when it initializes a Shell folder object.



| Method     | Description                                                                                            |
|------------|--------------------------------------------------------------------------------------------------------|
| Initialize | Instructs a Shell folder object to initialize itself based on the information passed and returns S\_OK |



 

### IShellFolder

The [IShellFolder Interface](http://msdn.microsoft.com/en-us/library/bb775075(VS.85).aspx) interface is used to manage folders, and a partial implementation is required so that the icon and context interfaces implemented for a protocol handler will behave correctly in the Windows Search results user interface. Most of the functionality required is exposed through the **GetUIObjectOf** method. This method enables an add-in to query for the **IExtractIcon** and **IContextMenu** interfaces.

The [IShellFolder Interface](http://msdn.microsoft.com/en-us/library/bb775075(VS.85).aspx) interface uses PIDLs instead of URLs. In contrast to the requirements of a complete Shell data store, add-ins can use a simple IDL structure that contains only the URL.

The following methods of [IShellFolder Interface](http://msdn.microsoft.com/en-us/library/bb775075(VS.85).aspx) must be implemented. Five of these methods require minimal implementation.



| Method           | Description                                                                                                                                                                                                                                                                   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BindToObject     | Returns E\_NOTIMPL                                                                                                                                                                                                                                                            |
| BindToStorage    | Returns E\_NOTIMPL                                                                                                                                                                                                                                                            |
| CreateViewObject | Returns E\_NOTIMPL                                                                                                                                                                                                                                                            |
| SetNameOf        | Returns E\_NOTIMPL                                                                                                                                                                                                                                                            |
| ParseDisplayName | Converts a URL to the PIDL structure                                                                                                                                                                                                                                          |
| CompareIDs       | Compares two PIDL values                                                                                                                                                                                                                                                      |
| GetDisplayNameOf | Returns the URL for a PIDL                                                                                                                                                                                                                                                    |
| GetUIObjectOf    | This method is similar to the [IUnknown::QueryInterface Method](http://msdn.microsoft.com/en-us/library/ms682521(VS.85).aspx). If an icon is requested, the caller requests the IID\_IExtractIcon; if a shortcut menu is requested, the caller requests the IID\_IContextMenu |



 

**IShellFolder** is not used to enumerate folders. This means that the display name of a folder will be the physical URL. This may change in the future.

### IContextMenu

When Windows Search displays results to the user, the user can right-click an item and see a shortcut menu defined by your **IContextMenu** interface. Shortcut menus are also known as context menus.

The default action on the context menu is the same action taken when the item is double-clicked. Without the corresponding **IShellFolder** or **IContextMenu** interfaces for the item, the default behavior for a double-click event is to pass the URL as an argument to the [ShellExecute Function](http://msdn.microsoft.com/en-us/library/bb762153(VS.85).aspx) function.

Refer to [Creating Context Menu Handlers](http://msdn.microsoft.com/en-us/library/Cc144171(VS.85).aspx) for more information on creating shortcut menu handlers, and [Sample: Shell Extensions for Protocol Handlers](-search-3x-wds-ph-ui-samplecode.md) for sample code.

### IExtractIcon

**IExtractIcon** retrieves an icon for the Windows Search user interface based on the URL in the PIDL provided by your protocol handler.

Refer to [Creating Icon Handlers](http://msdn.microsoft.com/en-us/library/Cc144122(VS.85).aspx) for more information on creating icon handlers and [Sample: Shell Extensions for Protocol Handlers](-search-3x-wds-ph-ui-samplecode.md) for sample code.

### IPreviewHandler

The [IPreviewHandler](http://msdn.microsoft.com/en-us/library/Bb775315(VS.85).aspx) renders a rich preview of a selected item in Windows Explorer. Previews are available in Windows Search 4.0, or in Windows Vista with Windows Desktop Search 3.x.

To create a custom preview handler:

1.  Implement an [IPreviewHandler](http://msdn.microsoft.com/en-us/library/Bb775315(VS.85).aspx) that takes an [IStream](http://msdn.microsoft.com/en-us/library/Aa380034(VS.85).aspx), following the guidelines provided in [Preview Handlers](http://msdn.microsoft.com/en-us/library/Cc144143(VS.85).aspx).
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
    1.  In [IShellFolder::GetUIObjectOf Method](http://msdn.microsoft.com/en-us/library/bb775073(VS.85).aspx), handle [IQueryAssociations](http://msdn.microsoft.com/en-us/library/Bb761400(VS.85).aspx) and return your association for your Shell items, as shown in the following code sample.

        ```
        CComPtr<IQueryAssociations> spqa;
        AssocCreate(CLSID_QueryAssociations, __uuidof(IQueryAssociations), &amp;spqa);
        spqa->Init(0, L"Your_Object_Type", NULL, NULL);
        spqa->QueryInterface(riid, ppvReturn);
        ```

        

    2.  After the Shell queries your Shell folder for the data stream to initialize the preview handler, go to your [IShellFolder::BindToObject Method](http://msdn.microsoft.com/en-us/library/bb775059(VS.85).aspx) method, handle IID\_IStream and return an [IStream](http://msdn.microsoft.com/en-us/library/Aa380034(VS.85).aspx) to your URL.

To reuse an existing preview handler for your file type, follow these two steps:

1.  Register that preview handler for your file type using the CLSID of the existing preview handler in place of &lt;Your\_PreviewHandler\_GUID&gt;.
2.  Implement a Shell folder.

For more information on creating preview handlers, see [IPreviewHandler](http://msdn.microsoft.com/en-us/library/Bb775315(VS.85).aspx) and [Preview Handlers](http://msdn.microsoft.com/en-us/library/Cc144143(VS.85).aspx).

## Additional Resources

-   For an overview of the indexing process, see [The Indexing Process](-search-indexing-process-overview.md).
-   For information about creating handlers, see [Registering Shell Extensions](http://msdn.microsoft.com/en-us/library/cc144110(VS.85).aspx), [Creating Shell Extension Handlers](http://msdn.microsoft.com/en-us/library/Cc144067(VS.85).aspx), [Context Menu](http://msdn.microsoft.com/en-us/library/cc144169(VS.85).aspx), [Shell Namespace Extensions](http://msdn.microsoft.com/en-us/library/cc144095(VS.85).aspx) and [Preview Handlers](http://msdn.microsoft.com/en-us/library/Cc144143(VS.85).aspx).

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

 

 



