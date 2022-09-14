---
description: Windows Explorer is a powerful resource-browsing and management application.
ms.assetid: 879CE652-EDC0-4a14-925E-C83763133BE5
title: Developing with Windows Explorer
ms.topic: article
ms.date: 05/31/2018
---

# Developing with Windows Explorer

Windows Explorer is a powerful resource-browsing and management application. Windows Explorer can be accessed as an integrated whole through Explorer.exe or the [**IExplorerBrowser**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorerbrowser) interface. Windows Explorer (Explorer.exe) can be spawned as a separate process using [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) or a similar function.

Open explorer windows can be discovered and programmed by using [**IShellWindows**](/windows/desktop/api/Exdisp/nn-exdisp-ishellwindows) (CLSID\_ShellWindows), and new instances of Windows Explorer can be created by using [**IWebBrowser2**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa752127(v=vs.85)) (CLSID\_ShellBrowserWindow).

The following code sample demonstrates how the Windows Explorer automation model can be used to create and discover explorer windows that are running.


```
#define _WIN32_WINNT 0x0600
#define _WIN32_IE 0x0700
#define _UNICODE

#include <windows.h>
#include <shobjidl.h>
#include <shlobj.h>
#include <shlwapi.h>
#include <strsafe.h>
#include <propvarutil.h>
 
#pragma comment(lib, "shlwapi.lib")
#pragma comment(lib, "ole32.lib")
#pragma comment(lib, "shell32.lib")
#pragma comment(lib, "propsys.lib")
 
// Use the Shell Windows object to find all of the explorer and IExplorer 
// windows and close them.
 
void CloseExplorerWindows()
{
    IShellWindows* psw;
    
    if (SUCCEEDED(CoCreateInstance(CLSID_ShellWindows, 
                                   NULL,  
                                   CLSCTX_LOCAL_SERVER, 
                                   IID_PPV_ARGS(&psw))))
    {
        VARIANT v = { VT_I4 };
        if (SUCCEEDED(psw->get_Count(&v.lVal)))
        {
            // Walk backward to make sure that the windows that close
            // do not cause the array to be reordered.
            while (--v.lVal >= 0)
            {
                IDispatch *pdisp;
                
                if (S_OK == psw->Item(v, &pdisp))
                {
                    IWebBrowser2 *pwb;
                    if (SUCCEEDED(pdisp->QueryInterface(IID_PPV_ARGS(&pwb))))
                    {
                        pwb->Quit();
                        pwb->Release();
                    }
                    pdisp->Release();
                }
            }
        }
        psw->Release();
    }
}
 
// Convert an IShellItem or IDataObject into a VARIANT that holds an IDList
// suitable for use with IWebBrowser2::Navigate2.
 
HRESULT InitVariantFromObject(IUnknown *punk, VARIANT *pvar)
{
    VariantInit(pvar);
 
    PIDLIST_ABSOLUTE pidl;
    HRESULT hr = SHGetIDListFromObject(punk, &pidl);
    if (SUCCEEDED(hr))
    {
        hr = InitVariantFromBuffer(pidl, ILGetSize(pidl), pvar);
        CoTaskMemFree(pidl);
    }
    return hr;
}
 
HRESULT ParseItemAsVariant(PCWSTR pszItem, IBindCtx *pbc, VARIANT *pvar)
{
    VariantInit(pvar);
 
    IShellItem *psi;
    HRESULT hr = SHCreateItemFromParsingName(pszItem, NULL, IID_PPV_ARGS(&psi));
    if (SUCCEEDED(hr))
    {
        hr = InitVariantFromObject(psi, pvar);
        psi->Release();
    }
    return hr;
}

HRESULT GetKnownFolderAsVariant(REFKNOWNFOLDERID kfid, VARIANT *pvar)
{
    VariantInit(pvar);
 
    PIDLIST_ABSOLUTE pidl;
    HRESULT hr = SHGetKnownFolderIDList(kfid, 0, NULL, &pidl);
    if (SUCCEEDED(hr))
    {
        hr = InitVariantFromBuffer(pidl, ILGetSize(pidl), pvar);
        CoTaskMemFree(pidl);
    }
    return hr;
}

HRESULT GetShellItemFromCommandLine(REFIID riid, void **ppv)
{
    *ppv = NULL;
    HRESULT hr = E_FAIL;

    int cArgs;
    PWSTR *ppszCmd = CommandLineToArgvW(GetCommandLineW(), &cArgs);
    if (ppszCmd && cArgs > 1)
    {
        WCHAR szSpec[MAX_PATH];
        StringCchCopyW(szSpec, ARRAYSIZE(szSpec), ppszCmd[1]);
        PathUnquoteSpacesW(szSpec);

        hr = szSpec[0] ? S_OK : E_FAIL;   // Protect against empty data
        if (SUCCEEDED(hr))
        {
            hr = SHCreateItemFromParsingName(szSpec, NULL, riid, ppv);
            if (FAILED(hr))
            {
                WCHAR szFolder[MAX_PATH];
                GetCurrentDirectoryW(ARRAYSIZE(szFolder), szFolder);

                hr = PathAppendW(szFolder, szSpec) ? S_OK : E_FAIL;
                if (SUCCEEDED(hr))
                {
                    hr = SHCreateItemFromParsingName(szFolder, NULL, riid, ppv);
                }
            }
        }
    }
    return hr;
}

HRESULT GetShellItemFromCommandLineAsVariant(VARIANT *pvar)
{
    VariantInit(pvar);

    IShellItem *psi;
    HRESULT hr = GetShellItemFromCommandLine(IID_PPV_ARGS(&psi));
    if (SUCCEEDED(hr))
    {
        hr = InitVariantFromObject(psi, pvar);
        psi->Release();
    }
    return hr;
}

void OpenWindow()
{
    IWebBrowser2 *pwb;
    HRESULT hr = CoCreateInstance(CLSID_ShellBrowserWindow, 
                                  NULL,
                                  CLSCTX_LOCAL_SERVER, 
                                  IID_PPV_ARGS(&pwb));
    if (SUCCEEDED(hr))
    {
        CoAllowSetForegroundWindow(pwb, 0);

        pwb->put_Left(100);
        pwb->put_Top(100);
        pwb->put_Height(600);
        pwb->put_Width(800);
 
        VARIANT varTarget = {0};
        hr = GetShellItemFromCommandLineAsVariant(&varTarget);
        if (FAILED(hr))
        {
            hr = GetKnownFolderAsVariant(FOLDERID_UsersFiles, &varTarget);
        }

        if (SUCCEEDED(hr))
        {
            VARIANT vEmpty = {0};
            hr = pwb->Navigate2(&varTarget, &vEmpty, &vEmpty, &vEmpty, &vEmpty);
            if (SUCCEEDED(hr))
            {
                pwb->put_Visible(VARIANT_TRUE);
            }
            VariantClear(&varTarget);
        }
        pwb->Release();
    }
}

int WINAPI WinMain(HINSTANCE, HINSTANCE, LPSTR, int)
{
    HRESULT hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED |  COINIT_DISABLE_OLE1DDE);
    if (SUCCEEDED(hr))
    {
        CloseExplorerWindows();

        OpenWindow();

        CoUninitialize();
    }
    return 0;
}
```



The Windows Explorer client area can be hosted by using the [IExplorerBrowser](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorerbrowser) interface. The Windows Explorer client and the namespace tree controls are standard components of Windows Vista and later. Developers can reuse the interfaces as building components. One common use of these controls is to create customized explorers appropriate to the problem domain.

The controls in Windows Explorer are classified into the following functional categories:

-   [Navigation Controls](#navigation-controls)
-   [Command Controls](#command-controls)
-   [Property and Preview Controls](#property-and-preview-controls)
-   [Filtering and View Controls](#filtering-and-view-controls)
-   [Listview Control](#listview-control)

## Navigation Controls

Navigation controls assist users in determining context and navigating the associated logical domain space, called the pagespace. For example, the pagespace for Windows Explorer is the Shell namespace. Pagespaces are composed of zero or more pages.

The following table lists and describes the navigation controls available in Windows Explorer in the Windows Vista and later operating systems.



| Navigation control               | Description                                                                                                                                                                                |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Address Bar (Breadcrumb control) | Displays the address of the current page in the pagespace. Breadcrumb buttons can be clicked to navigate to any ancestor in the pagespace. Users can also type URLs and paths to navigate. |
| Folder Tree                      | Provides a new version of a tree control, optimized for large pagespaces.                                                                                                                  |
| Travel                           | Enables relative navigation through web-style buttons such as **Back** and **Forward**.                                                                                                    |
| Title                            | Displays the current explorer name and context.                                                                                                                                            |
| Pagespace                        | Displays the current branch of the pagespace. Pages can be ordered by different criteria. Users can click a page to navigate to it.                                                        |



 

## Command Controls

Command controls advertise the features and functionality of the Windows Explorer to users. These controls perform either general actions or actions specific to one selected item or items.



| Command control | Description                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Toolbar         | Displays buttons for commonly used commands (a new version of a command toolbar). Customization options include drop-down buttons, split buttons, optional descriptive text, and an overflow area. |
| Hero            | Appears as a single, optional, custom control in the center of the toolbar. It represents the primary command for the current context.                                                             |
| Menu Bar        | Presents commands through menus.                                                                                                                                                                   |
| Context Menu    | Lists a contextually relevant subset of available commands that are displayed as a result of right-clicking an item.                                                                               |



 

## Property and Preview Controls

Property and preview controls are used to preview items, and to view and edit item properties.



| Control    | Description                                                                                                                                                                                                                                        |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Preview    | Displays a preview of the selected item, such as a thumbnail or a Live Icon.                                                                                                                                                                       |
| Properties | Displays properties of the selected item. For multiple selections, it displays a summary of properties for the selected group of items. For a null selection, it displays a summary of properties for the current page (contents of the listview). |



 

## Filtering and View Controls

Filtering and view controls are used to manipulate the set of items in the listview and to change the presentation of items in the listview.



| Control   | Description                                                                                                                 |
|-----------|-----------------------------------------------------------------------------------------------------------------------------|
| Filter    | Filters or arranges items in a listview based on properties listed as columns. Clicking on a column sorts by that property. |
| Wordwheel | Dynamically and incrementally filters the displayed items in a listview based on an input text string.                      |
| View      | Enables the user to change the view mode of a listview control. A slider can be used to determine icon size.                |



 

## Listview Control

The listview control is used to view a set of items in one of four view modes: details, tiles, icons, or panorama. The listview control also enables the user to select and activate one or more items.

> [!Caution]  
> Although some of these controls have names and/or functionality that is similar to standard Windows Presentation Foundation (WPF) controls found in the System.Windows.Controls namespace, they are distinct classes.

 

These separate controls work together largely through events generated either by user interaction or by the controls themselves. The following table shows the three primary event categories.



| Event category | Example                                                       |
|----------------|---------------------------------------------------------------|
| Navigation     | Going from one page to another.                               |
| Selection      | Changing the current selection in the listview.               |
| View Change    | Changing the presentation order or view mode in the listview. |



 

 

 
