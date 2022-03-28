---
description: Shortcut menu handlers are also known as context menu handlers or verb handlers. A shortcut menu handler is a type of file type handler.
ms.assetid: 7FC65C6F-3798-404c-B359-2BC75D3F54E7
title: Customizing a Shortcut Menu Using Dynamic Verbs
ms.topic: article
ms.date: 05/31/2018
---

# Customizing a Shortcut Menu Using Dynamic Verbs

Shortcut menu handlers are also known as context menu handlers or verb handlers. A shortcut menu handler is a type of file type handler.

This topic is organized as follows:

- [About Static and Dynamic Verbs](#about-static-and-dynamic-verbs)
- [How Shortcut Menu Handlers Work with Dynamic Verbs](#how-shortcut-menu-handlers-work-with-dynamic-verbs)
- [Avoiding Collisions Due to Unqualified Verb Names](#avoiding-collisions-due-to-unqualified-verb-names)
- [Registering a Shortcut Menu Handler with a Dynamic Verb](#registering-a-shortcut-menu-handler-with-a-dynamic-verb)
- [Implementing the IContextMenu Interface](#implementing-the-icontextmenu-interface)
    - [IContextMenu::GetCommandString Method](#icontextmenugetcommandstring-method)
    - [IContextMenu::InvokeCommand Method](#icontextmenuinvokecommand-method)
    - [IContextMenu::QueryContextMenu Method](#icontextmenuquerycontextmenu-method)
- [Related topics](#related-topics)

## About Static and Dynamic Verbs

We strongly encourage you to implement a shortcut menu using one of the static verb methods. We recommend that you follow the instructions provided in the "Customizing a Shortcut Menu using Static Verbs" section of [Creating Context Menu Handlers](context-menu-handlers.md). To get dynamic behavior for static verbs in Windows 7 and later, see "Getting Dynamic Behavior for Static Verbs" in [Creating Context Menu Handlers](context-menu-handlers.md). For details on static verb implementation, and which dynamic verbs to avoid, see [Choosing a Static or Dynamic Verb for your Shortcut Menu](shortcut-choose-method.md).

If you must extend the shortcut menu for a file type by registering a dynamic verb for the file type, then follow the instructions provided later in this topic.

> [!Note]  
> There are special considerations for 64-bit Windows when registering handlers that work in the context of 32-bit applications: when Shell verbs are invoked in the context of a 32-bit application, the WOW64 subsystem redirects file system access to some paths. If your .exe handler is stored in one of those paths, it is not accessible in this context. Therefore, as a work around, either store your .exe in a path that does not get redirected, or store a stub version of your .exe that launches the real version.

 

## How Shortcut Menu Handlers Work with Dynamic Verbs

In addition to [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown), shortcut menu handlers export the following additional interfaces to handle the messaging needed to implement owner-drawn menu items:

- [**IShellExtInit**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellextinit) (mandatory)
- [**IContextMenu**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) (mandatory)
- [**IContextMenu2**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icontextmenu2) (optional)
- [**IContextMenu3**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icontextmenu3) (optional)

For more information on owner-drawn menu items, see the *Creating Owner-Drawn Menu Items* section in [Using Menus](../menurc/using-menus.md).

Shell uses the [**IShellExtInit**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellextinit) interface to initialize the handler. When the Shell calls [**IShellExtInit::Initialize**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellextinit-initialize), it passes in a data object with the object's name and a pointer to an item identifier list (PIDL) of the folder that contains the file. The *hkeyProgID* parameter is the registry location under which the shortcut menu handle is registered. The **IShellExtInit::Initialize** method must extract the file name from the data object and store the name and the folder's pointer to an item identifier list (PIDL) for later use. For more information on handler initialization, see [Implementing IShellExtInit](handlers.md).

When verbs are presented in a shortcut menu, they are first discovered, then presented to the user, and finally invoked. The following list describes these three steps in more detail:

1.  The Shell calls [**IContextMenu::QueryContextMenu**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-querycontextmenu), which returns a set of verbs that can be based on the state of the items or the system.
2.  The system passes in an **HMENU** handle that the method can use to add items to the shortcut menu.
3.  If the user clicks one of the handler's items, the Shell calls [**IContextMenu::InvokeCommand**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-invokecommand). The handler can then execute the appropriate command.

## Avoiding Collisions Due to Unqualified Verb Names

Because verbs are registered per type, the same verb name can be used for verbs on different items. Doing so enables applications to refer to common verbs independent of the item type. While this functionality is useful, the use of unqualified names can result in collisions with multiple independent software vendors (ISVs) that choose the same verb name. To avoid this, always prefix verbs with the ISV name as follows:

`ISV_Name.verb`

Always use an application specific ProgID. Adopting the convention of mapping the file name extension to an ISV provided ProgID avoids potential collisions. However, because some item types do not use this mapping, there is a need for vendor-unique names. When adding a verb to an existing ProgID that might already have that verb registered, you must first remove the registry key for the old verb before adding your own verb. You must do so to avoid merging the verb information from the two verbs. Failure to do so results in unpredictable behavior.

## Registering a Shortcut Menu Handler with a Dynamic Verb

Shortcut menu handlers are associated with either a file type or a folder. For file types, the handler is registered under the following subkey.

```
HKEY_CLASSES_ROOT
   Program ID
      shellex
         ContextMenuHandlers
```

To associate a shortcut menu handler with either a file type or a folder, first create a subkey under the **ContextMenuHandlers** subkey. Name the subkey for the handler, and set the subkey's default value to the string form of the handler's class identifier (CLSID) GUID.

Then to associate a shortcut menu handler with different kinds of folders, register the handler the same way you would for a file type, but under the *FolderType* subkey as shown in the following example.

```
HKEY_CLASSES_ROOT
   FolderType
      shellex
         ContextMenuHandlers
```

For more information about about which folder types you can register handlers for, see [Registering Shell Extension Handlers](handlers.md).

If a file type has a shortcut menu associated with it, then double-clicking an object normally launches the default command, and the handler's [**IContextMenu::QueryContextMenu**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-querycontextmenu) method is not called. To specify that the handler's **IContextMenu::QueryContextMenu** method should be called when an object is double-clicked, create a subkey under the handler's **CLSID** subkey as shown here.

```
HKEY_CLASSES_ROOT
   CLSID
      {00000000-1111-2222-3333-444444444444}
         shellex
            MayChangeDefaultMenu
```

When an object associated with the handler is double-clicked, [**IContextMenu::QueryContextMenu**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-querycontextmenu) is called with the **CMF\_DEFAULTONLY** flag set in the *uFlags* parameter.

Shortcut menu handlers should set the **MayChangeDefaultMenu** subkey only if they might need to change the shortcut menu's default verb. Setting this subkey forces the system to load the handler's DLL when an associated item is double-clicked. If your handler does not change the default verb, you should not set this subkey because doing so causes the system to load your DLL unnecessarily.

The following example illustrates registry entries that enable a shortcut menu handler for an .myp file type. The handler's **CLSID** subkey includes a **MayChangeDefaultMenu** subkey to guarantee that the handler is called when the user double-clicks a related object.

```
HKEY_CLASSES_ROOT
   .myp
      (Default) = MyProgram.1
   CLSID
      {00000000-1111-2222-3333-444444444444}
         InProcServer32
            (Default) = C:\MyDir\MyCommand.dll
            ThreadingModel = Apartment
         shellex
            MayChangeDefaultMenu
   MyProgram.1
      (Default) = MyProgram Application
      shellex
         ContextMenuHandler
            MyCommand = {00000000-1111-2222-3333-444444444444}
```

## Implementing the IContextMenu Interface

[**IContextMenu**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) is the most powerful but also the most complicated method to implement. We strongly recommend that you implement a verb by using one of the static verb methods. For more information, see [Choosing a Static or Dynamic Verb for your Shortcut Menu](shortcut-choose-method.md). [**IContextMenu**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) has three methods, **GetCommandString**, **InvokeCommand**, and **QueryContextMenu**, which are discussed here in detail.

### IContextMenu::GetCommandString Method

The handler's [**IContextMenu::GetCommandString**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-getcommandstring) method is used to return the canonical name for a verb. This method is optional. In Windows XP and earlier versions of Windows, when Windows Explorer has a Status bar, this method is used to retrieve the help text that is displayed in the Status bar for a menu item.

The *idCmd* parameter holds the identifier offset of the command that was defined when [**IContextMenu::QueryContextMenu**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-querycontextmenu) was called. If a help string is requested, *uFlags* will be set to **GCS\_HELPTEXTW**. Copy the help string to the *pszName* buffer, casting it to a **PWSTR**. The verb string is requested by setting *uFlags* to **GCS\_VERBW**. Copy the appropriate string to *pszName*, just as with the help string. The **GCS\_VALIDATEA** and **GCS\_VALIDATEW** flags are not used by shortcut menu handlers.

The following example shows a simple implementation of [**IContextMenu::GetCommandString**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-getcommandstring) that corresponds to the [**IContextMenu::QueryContextMenu**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-querycontextmenu) example given in the [IContextMenu::QueryContextMenu Method](#icontextmenuquerycontextmenu-method) section of this topic. Because the handler adds only one menu item, there is only one set of strings that can be returned. The method tests whether *idCmd* is valid and, if it is, returns the requested string.

The [**StringCchCopy**](/windows/win32/api/strsafe/nf-strsafe-stringcchcopya) function is used to copy the requested string to *pszName* to ensure that the copied string does not exceed the size of the buffer specified by *cchName*. This example only implements support for the Unicode values of *uFlags*, because only those have been used in Windows Explorer since Windows 2000.


```C++
IFACEMETHODIMP CMenuExtension::GetCommandString(UINT idCommand, 
                                                UINT uFlags, 
                                                UINT *pReserved, 
                                                PSTR pszName, 
                                                UINT cchName)
{
    HRESULT hr = E_INVALIDARG;

    if (idCommand == IDM_DISPLAY)
    {
        switch (uFlags)
        {
            case GCS_HELPTEXTW:
                // Only useful for pre-Vista versions of Windows that 
                // have a Status bar.
                hr = StringCchCopyW(reinterpret_cast<PWSTR>(pszName), 
                                    cchName, 
                                    L"Display File Name");
                break; 

            case GCS_VERBW:
                // GCS_VERBW is an optional feature that enables a caller
                // to discover the canonical name for the verb passed in
                // through idCommand.
                hr = StringCchCopyW(reinterpret_cast<PWSTR>(pszName), 
                                    cchName, 
                                    L"DisplayFileName");
                break; 
        }
    }
    return hr;
}
```



### IContextMenu::InvokeCommand Method

This method is called when a user clicks a menu item to tell the handler to run the associated command. The *pici* parameter points to a structure that contains the information required.

Although *pici* is declared in Shlobj.h as a [**CMINVOKECOMMANDINFO**](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-cminvokecommandinfo) structure, in practice it often points to a [**CMINVOKECOMMANDINFOEX**](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-cminvokecommandinfoex) structure. This structure is an extended version of **CMINVOKECOMMANDINFO** and has several additional members that make it possible to pass Unicode strings.

Check the **cbSize** member of *pici* to determine which structure was passed in. If it is a [**CMINVOKECOMMANDINFOEX**](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-cminvokecommandinfoex) structure and the **fMask** member has the **CMIC\_MASK\_UNICODE** flag set, cast *pici* to **CMINVOKECOMMANDINFOEX**. This enables your application to use the Unicode information contained in the last five members of the structure.

The structure's **lpVerb** or **lpVerbW** member is used to identify the command to be executed. Commands are identified in one of the following two ways:

-   By the command's verb string
-   By the command's identifier offset

To distinguish between these two cases, check the high-order word of **lpVerb** for the ANSI case or **lpVerbW** for the Unicode case. If the high-order word is nonzero, **lpVerb** or **lpVerbW** holds a verb string. If the high-order word is zero, the command offset is in the low-order word of **lpVerb**.

The following example shows a simple implementation of [**IContextMenu::InvokeCommand**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-invokecommand) that corresponds to the [**IContextMenu::QueryContextMenu**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-querycontextmenu) and [**IContextMenu::GetCommandString**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-getcommandstring) examples given before and after this section. The method first determines which structure is being passed in. It then determines whether the command is identified by its offset or its verb. If **lpVerb** or **lpVerbW** holds a valid verb or offset, the method displays a message box.


```C++
STDMETHODIMP CShellExtension::InvokeCommand(LPCMINVOKECOMMANDINFO lpcmi)
{
    BOOL fEx = FALSE;
    BOOL fUnicode = FALSE;

    if(lpcmi->cbSize == sizeof(CMINVOKECOMMANDINFOEX))
    {
        fEx = TRUE;
        if((lpcmi->fMask & CMIC_MASK_UNICODE))
        {
            fUnicode = TRUE;
        }
    }

    if( !fUnicode && HIWORD(lpcmi->lpVerb))
    {
        if(StrCmpIA(lpcmi->lpVerb, m_pszVerb))
        {
            return E_FAIL;
        }
    }

    else if( fUnicode && HIWORD(((CMINVOKECOMMANDINFOEX *) lpcmi)->lpVerbW))
    {
        if(StrCmpIW(((CMINVOKECOMMANDINFOEX *)lpcmi)->lpVerbW, m_pwszVerb))
        {
            return E_FAIL;
        }
    }

    else if(LOWORD(lpcmi->lpVerb) != IDM_DISPLAY)
    {
        return E_FAIL;
    }

    else
    {
        MessageBox(lpcmi->hwnd,
                   "The File Name",
                   "File Name",
                   MB_OK|MB_ICONINFORMATION);
    }

    return S_OK;
}
```



### IContextMenu::QueryContextMenu Method

The Shell calls [**IContextMenu::QueryContextMenu**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-querycontextmenu) to enable the shortcut menu handler to add its menu items to the menu. It passes in the **HMENU** handle in the *hmenu* parameter. The *indexMenu* parameter is set to the index to be used for the first menu item that is to be added.

Any menu items that are added by the handler must have identifiers that fall between the values in the *idCmdFirst* and *idCmdLast* parameters. Typically, the first command identifier is set to *idCmdFirst*, which is incremented by one (1) for each additional command. This practice helps you avoid exceeding *idCmdLast* and maximizes the number of available identifiers in case the Shell calls more than one handler.

An item identifier's *command offset* is the difference between the identifier and the value in *idCmdFirst*. Store the offset of each item that your handler adds to the shortcut menu because the Shell might use it to identify the item if it subsequently calls [**IContextMenu::GetCommandString**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-getcommandstring) or [**IContextMenu::InvokeCommand**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-invokecommand).

You should also assign a [verb](launch.md) to each command you add. A verb is a string that can be used instead of the offset to identify the command when [**IContextMenu::InvokeCommand**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-invokecommand) is called. It is also used by functions such as [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) to execute shortcut menu commands.

There are three flags that can be passed in through the *uFlags* parameter that are relevant to shortcut menu handlers. They are described in the following table.



| Flag             | Description                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CMF\_DEFAULTONLY | The user has selected the default command, usually by double-clicking the object. [**IContextMenu::QueryContextMenu**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-querycontextmenu) should return control to the Shell without modifying the menu. |
| CMF\_NODEFAULT   | No item in the menu should be the default item. The method should add its commands to the menu.                                                                                                                          |
| CMF\_NORMAL      | The shortcut menu will be displayed normally. The method should add its commands to the menu.                                                                                                                            |



 

Use either [**InsertMenu**](/windows/win32/api/winuser/nf-winuser-insertmenua) or [**InsertMenuItem**](/windows/win32/api/winuser/nf-winuser-insertmenuitema) to add menu items to the list. Then return an **HRESULT** value with the severity set to **SEVERITY\_SUCCESS**. Set the code value to the offset of the largest command identifier that was assigned, plus one (1). For example, assume that *idCmdFirst* is set to 5 and you add three items to the menu with command identifiers of 5, 7, and 8. The return value should be `MAKE_HRESULT(SEVERITY_SUCCESS, 0, 8 - 5 + 1)`.

The following example shows a simple implementation of [**IContextMenu::QueryContextMenu**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-querycontextmenu) that inserts a single command. The identifier offset for the command is IDM\_DISPLAY, which is set to zero. The **m\_pszVerb** and **m\_pwszVerb** variables are private variables used to store the associated language-independent verb string in both ANSI and Unicode formats.


```C++
#define IDM_DISPLAY 0

STDMETHODIMP CMenuExtension::QueryContextMenu(HMENU hMenu,
                                              UINT indexMenu,
                                              UINT idCmdFirst,
                                              UINT idCmdLast,
                                              UINT uFlags)
{
    HRESULT hr;
    
    if(!(CMF_DEFAULTONLY & uFlags))
    {
        InsertMenu(hMenu, 
                   indexMenu, 
                   MF_STRING | MF_BYPOSITION, 
                   idCmdFirst + IDM_DISPLAY, 
                   "&Display File Name");

    
        
        hr = StringCbCopyA(m_pszVerb, sizeof(m_pszVerb), "display");
        hr = StringCbCopyW(m_pwszVerb, sizeof(m_pwszVerb), L"display");

        return MAKE_HRESULT(SEVERITY_SUCCESS, 0, USHORT(IDM_DISPLAY + 1));
    }

    return MAKE_HRESULT(SEVERITY_SUCCESS, 0, USHORT(0));
}
```



For other verb implementation tasks, see [Creating Context Menu Handlers](context-menu-handlers.md).

## Related topics

<dl> <dt>

[Shortcut (Context) Menus and Shortcut Menu Handlers](context-menu.md)
</dt> <dt>

[Verbs and File Associations](fa-verbs.md)
</dt> <dt>

[Choosing a Static or Dynamic Verb for your Shortcut Menu](shortcut-choose-method.md)
</dt> <dt>

[Best Practices for Shortcut Menu Handlers and Multiple Selection Verbs](verbs-best-practices.md)
</dt> <dt>

[Creating Shortcut Menu Handlers](context-menu-handlers.md)
</dt> <dt>

[Shortcut Menu Reference](context-menu-reference.md)
</dt> </dl>

 

 
