---
description: Understand best practices for shortcut menu handlers and multiple verbs when you implement a custom file format in the Windows Shell.
title: Best Practices for Shortcut Menu Handlers and Multiple Verbs
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 4D352ECB-6214-4f6e-A3E5-F79E154D090A
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Best Practices for Shortcut Menu Handlers and Multiple Verbs

This topic is organized as follows:

-   [Best Practices](#best-practices-for-shortcut-menu-handlers-and-multiple-verbs)
    -   [Best Practices for Verb Implementations](#best-practices-for-verb-implementations)
-   [Best Practices for Multiple Selection Verbs](#best-practices-for-multiple-selection-verbs)
    -   [Heterogenous Selections](#heterogenous-selections)
-   [Related topics](#related-topics)

## Best Practices

Static verb are simplest verbs to implement, and provide rich functionality. We strongly encourage you to implement a verb using one of the static verb methods.

### Best Practices for Verb Implementations

The following list represents best practices for verb implementations:

-   Always chose the simplest verb method that meets your needs.
-   Use a static verb method, if possible.
-   Do not perform resource-intensive operations or I/O on the UI thread. Both [**IShellExtInit::Initialize**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellextinit-initialize) and [**IContextMenu::QueryContextMenu**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-querycontextmenu) need to be very conservative in the work they perform. [**IContextMenu::InvokeCommand**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-invokecommand) must be performed in another process, or you must create a new thread to avoid blocking the caller.
-   Prefix verbs with the independent software vendor (ISV) name as follows, `ISVName.verb`. Using unqualified names can result in collisions with multiple ISVs that chose the same verb name.
-   Always use an application-specific ProgID. Because some item types do not use this mapping, there is a need for vendor-unique names.
-   Position the UI relative to the invoking method, but do not run on an invoker thread.
-   Do not accept the return value **S\_OK** for canonical verbs passed to the [**IContextMenu::InvokeCommand**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-invokecommand) method. Doing so causes a failure for the real verb implementation to be invoked, and returns a failure code for canonical verbs. If you do not support canonical verbs, then return failure when a nonzero HIWORD(lpVerb) value is encountered.
-   Avoid the use of **rundll32.exe** as the host for your verb.
-   When implementing [**IContextMenu::QueryContextMenu**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-querycontextmenu) be sure to return the number of verbs that have been added to the menu through the **HRESULT** value using the ResultFromShort macro.
-   If you register on one of the following registry key entries, then exercise caution and be sure to register your handler on the most specific type to reduce the possibly unintended consequences:
    -   **HKEY\_CLASSES\_ROOT\\\***
    -   **HKEY\_CLASSES\_ROOT\\AllFileSystemObjects**
    -   **HKEY\_CLASSES\_ROOT\\Folder**
    -   **HKEY\_CLASSES\_ROOT\\Directory**
-   Set the **MayChangeDefaultMenu** key only if you anticipate that you might need to change the default verb in the shortcut menu. If your handler does not change the default verb, then you should not set this key because doing so causes the system to load your DLL unnecessarily.
-   Minimize the work you perform in [**IShellExtInit::Initialize**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellextinit-initialize). For shortcut menu handlers, capture the data object passed to **IShellExtInit::Initialize**, and then process it in [**IContextMenu::QueryContextMenu**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-querycontextmenu), or [**IContextMenu::InvokeCommand**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-invokecommand).

## Best Practices for Multiple Selection Verbs

Because the number of items in a multi-selection verb scenario can be large, it is important that you consider the performance implications of your verb implementations. For example, when a user searches for "\*" over a scope that includes large numbers of items, and then clicks **Select All** and right-clicks, the verb is presented with a selection that can have thousands of items in it. As a result, verbs should only consider the first item in the selection, and the overall item count. The first item is defined as either the item at the top of the view, or the item that the user first right-clicked.

In Windows 7 and later, the number of items passed to a verb is limited to 16 when a shortcut menu is queried. The verb is then re-created and re-initialized with the full selection when that verb is invoked.

It is appropriate in some cases to consider a small number of fixed items. For example, it is appropriate for a "diff" verb to consider only the first two items. Generally, you need not test every item in the selection to see if it is a certain type, or query every item in the selection for its properties. Look rather at the first item and decide if it is appropriate to add your verb.

### Heterogenous Selections

Optimistic verbs are automatically added in the multi-selection case, assuming that uninspected items can be handled by the verb. In contrast, pessimistic verbs are not added when the selection contains uninspected items, and are only added in cases where the number of items is small.

Player style verbs should be optimistic, and silently skip the items that are not handled. If a failure to act on items can cause data loss or confusion, then the verb should warn users about items that cannot be processed. For example a "backup" verb should indicate that some items could not be backed up.

## Related topics

<dl> <dt>

[Choosing a Static or Dynamic Verb for your Shortcut Menu](shortcut-choose-method.md)
</dt> <dt>

[Creating Shortcut Menu Handlers](context-menu-handlers.md)
</dt> <dt>

[Customizing a Shortcut Menu Using Dynamic Verbs](shortcut-menu-using-dynamic-verbs.md)
</dt> <dt>

[Shortcut (Context) Menus and Shortcut Menu Handlers](context-menu.md)
</dt> <dt>

[Verbs and File Associations](fa-verbs.md)
</dt> <dt>

[Shortcut Menu Reference](context-menu-reference.md)
</dt> </dl>

 

 



