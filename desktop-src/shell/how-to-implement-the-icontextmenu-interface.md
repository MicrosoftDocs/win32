---
Description: 'IContextMenu is the most powerful but also the most complicated interface to implement.'
ms.assetid: 'F0C1D60E-7A5A-4609-9136-F4E535E9F6F1'
title: How to Implement the IContextMenu Interface
---

# How to Implement the IContextMenu Interface

[**IContextMenu**](icontextmenu.md) is the most powerful but also the most complicated interface to implement. We strongly recommend that you implement a verb by using one of the static verb methods. For more information, see [Choosing a Static or Dynamic Shortcut Menu Method](shortcut-choose-method.md). [**IContextMenu**](icontextmenu.md) has three methods, [**GetCommandString**](icontextmenu-getcommandstring.md), [**InvokeCommand**](icontextmenu-invokecommand.md), and [**QueryContextMenu**](icontextmenu-querycontextmenu.md), which are discussed here in detail.

## What you need to know

### Technologies

-   C++

### Prerequisites

-   Static Verb
-   Shortcut Menu

## Instructions

### IContextMenu::GetCommandString Method

The handler's [**IContextMenu::GetCommandString**](icontextmenu-getcommandstring.md) method is used to return the canonical name for a verb. This method is optional. In Windows XP and earlier versions of Windows, when Windows Explorer has a Status bar, this method is used to retrieve the help text that is displayed in the Status bar for a menu item.

The *idCmd* parameter holds the identifier offset of the command that was defined when [**IContextMenu::QueryContextMenu**](icontextmenu-querycontextmenu.md) was called. If a help string is requested, *uFlags* will be set to **GCS\_HELPTEXTW**. Copy the help string to the *pszName* buffer, casting it to a **PWSTR**. The verb string is requested by setting *uFlags* to **GCS\_VERBW**. Copy the appropriate string to *pszName*, just as with the help string. The **GCS\_VALIDATEA** and **GCS\_VALIDATEW** flags are not used by shortcut menu handlers.

The following example shows a simple implementation of [**GetCommandString**](icontextmenu-getcommandstring.md) that corresponds to the [**QueryContextMenu**](icontextmenu-querycontextmenu.md) example given in the [IContextMenu::QueryContextMenu Method](shortcut-menu-using-dynamic-verbs.md#icontextmenuquerycontextmenu-method) section of this topic. Because the handler adds only one menu item, there is only one set of strings that can be returned. The method tests whether *idCmd* is valid and, if it is, returns the requested string.

The [**StringCchCopy**](menurc.stringcchcopy) function is used to copy the requested string to *pszName* to ensure that the copied string does not exceed the size of the buffer specified by *cchName*. This example implements support only for the Unicode values of *uFlags*, because only those have been used in Windows Explorer since Windows 2000.


```
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
                // to discover the canonical name for the verb that is passed in
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

This method is called when a user clicks a menu item to tell the handler to run the associated command. The *pici* parameter points to a structure that contains the information required to run the command.

Although *pici* is declared in Shlobj.h as a [**CMINVOKECOMMANDINFO**](cminvokecommandinfo.md) structure, in practice it often points to a [**CMINVOKECOMMANDINFOEX**](cminvokecommandinfoex.md) structure. This structure is an extended version of **CMINVOKECOMMANDINFO** and has several additional members that make it possible to pass Unicode strings.

Check the **cbSize** member of *pici* to determine which structure was passed in. If it is a [**CMINVOKECOMMANDINFOEX**](cminvokecommandinfoex.md) structure and the **fMask** member has the **CMIC\_MASK\_UNICODE** flag set, cast *pici* to **CMINVOKECOMMANDINFOEX**. This enables your application to use the Unicode information that is contained in the last five members of the structure.

The structure's **lpVerb** or **lpVerbW** member is used to identify the command to be executed. Commands are identified in one of the following two ways:

-   By the command's verb string
-   By the command's identifier offset

To distinguish between these two cases, check the high-order word of **lpVerb** for the ANSI case or **lpVerbW** for the Unicode case. If the high-order word is nonzero, **lpVerb** or **lpVerbW** holds a verb string. If the high-order word is zero, the command offset is in the low-order word of **lpVerb**.

The following example shows a simple implementation of [**IContextMenu::InvokeCommand**](icontextmenu-invokecommand.md) that corresponds to the [**IContextMenu::QueryContextMenu**](icontextmenu-querycontextmenu.md) and [**IContextMenu::GetCommandString**](icontextmenu-getcommandstring.md) examples given before and after this section. The method first determines which structure is being passed in. It then determines whether the command is identified by its offset or its verb. If **lpVerb** or **lpVerbW** holds a valid verb or offset, the method displays a message box.


```
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

    if( !fUnicode &amp;&amp; HIWORD(lpcmi->lpVerb))
    {
        if(StrCmpIA(lpcmi->lpVerb, m_pszVerb))
        {
            return E_FAIL;
        }
    }

    else if( fUnicode &amp;&amp; HIWORD(((CMINVOKECOMMANDINFOEX *) lpcmi)->lpVerbW))
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

The Shell calls [**IContextMenu::QueryContextMenu**](icontextmenu-querycontextmenu.md) to enable the shortcut menu handler to add its menu items to the menu. It passes in the **HMENU** handle in the *hmenu* parameter. The *indexMenu* parameter is set to the index to be used for the first menu item that is to be added.

Any menu items that are added by the handler must have identifiers that fall between the values in the *idCmdFirst* and *idCmdLast* parameters. Typically, the first command identifier is set to *idCmdFirst*, which is incremented by one (1) for each additional command. This practice helps you to avoid exceeding *idCmdLast* and maximizes the number of available identifiers in case the Shell calls more than one handler.

An item identifier's *command offset* is the difference between the identifier and the value in *idCmdFirst*. Store the offset of each item that your handler adds to the shortcut menu, because the Shell might use the offset to identify the item if it subsequently calls [**IContextMenu::GetCommandString**](icontextmenu-getcommandstring.md) or [**IContextMenu::InvokeCommand**](icontextmenu-invokecommand.md).

You should also assign a [verb](launch.md) to each command that you add. A verb is a string that can be used instead of the offset to identify the command when [**InvokeCommand**](icontextmenu-invokecommand.md) is called. It is also used by functions such as [**ShellExecuteEx**](shellexecuteex.md) to execute shortcut menu commands.

There are three flags that can be passed in through the *uFlags* parameter that are relevant to shortcut menu handlers. They are described in the following table.



| Flag             | Description                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CMF\_DEFAULTONLY | The user has selected the default command, usually by double-clicking the object. [**IContextMenu::QueryContextMenu**](icontextmenu-querycontextmenu.md) should return control to the Shell without modifying the menu. |
| CMF\_NODEFAULT   | No item in the menu should be the default item. The method should add its commands to the menu.                                                                                                                          |
| CMF\_NORMAL      | The shortcut menu will be displayed normally. The method should add its commands to the menu.                                                                                                                            |



 

Use either [**InsertMenu**](menurc.insertmenu) or [**InsertMenuItem**](menurc.insertmenuitem) to add menu items to the list. Then return an **HRESULT** value with the severity set to SEVERITY\_SUCCESS. Set the code value to the offset of the largest command identifier that was assigned, plus one (1). For example, assume that *idCmdFirst* is set to 5 and you add three items to the menu with command identifiers of 5, 7, and 8. The return value should be MAKE\_HRESULT(SEVERITY\_SUCCESS, 0, 8 + 1).

The following example shows a simple implementation of [**QueryContextMenu**](icontextmenu-querycontextmenu.md) that inserts a single command. The identifier offset for the command is IDM\_DISPLAY, which is set to zero. The **m\_pszVerb** and **m\_pwszVerb** variables are private variables that are used to store the associated language-independent verb string in both ANSI and Unicode formats.


```
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
                   "&amp;Display File Name");

    
        
        hr = StringCbCopyA(m_pszVerb, sizeof(m_pszVerb), "display");
        hr = StringCbCopyW(m_pwszVerb, sizeof(m_pwszVerb), L"display");

        return MAKE_HRESULT(SEVERITY_SUCCESS, 0, USHORT(IDM_DISPLAY + 1));
    }

    return MAKE_HRESULT(SEVERITY_SUCCESS, 0, USHORT(0));}
```



## Remarks

For other verb implementation tasks, see [Creating Shortcut Menu Handlers](context-menu-handlers.md).

 

 



