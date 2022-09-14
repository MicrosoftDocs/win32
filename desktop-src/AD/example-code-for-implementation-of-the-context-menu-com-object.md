---
title: Example Code for Implementation of the Context Menu COM Object
description: The following code example can be used to implement an Active Directory context menu extension. The single context menu item will display a message box that contains the ADsPath of each item selected.
ms.assetid: dc8f2c31-6031-4c7d-a173-5cedcedbfb26
ms.tgt_platform: multiple
keywords:
- Active Directory AD , example code C/C++ , implementation of the context menu COM object
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Implementation of the Context Menu COM Object

The following code example can be used to implement an Active Directory context menu extension. The single context menu item will display a message box that contains the ADsPath of each item selected.

## IShellExtInit Implementation

The following code example can be used to implement the [**IShellExtInit**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellextinit) methods.


```C++
///////////////////////////////////////////////////////////////////////////
//
// IShellExtInit Implementation
//

/**************************************************************************

   CContMenuExt::Initialize()

**************************************************************************/

STDMETHODIMP CContMenuExt::Initialize(  LPCITEMIDLIST pidlFolder,
                                        LPDATAOBJECT pDataObj,
                                        HKEY  hKeyProgId)
{
    STGMEDIUM   stm;
    FORMATETC   fe;
    HRESULT     hr;

    if(NULL == pDataObj)
    {
        return E_INVALIDARG;
    }

    fe.cfFormat = RegisterClipboardFormat(CFSTR_DSOBJECTNAMES);
    fe.ptd = NULL;
    fe.dwAspect = DVASPECT_CONTENT;
    fe.lindex = -1;
    fe.tymed = TYMED_HGLOBAL;
    hr = pDataObj->GetData(&fe, &stm);
    if(SUCCEEDED(hr))
    {
        LPDSOBJECTNAMES pdson = (LPDSOBJECTNAMES)GlobalLock(stm.hGlobal);

        if(pdson)
        {
            DWORD   dwBytes = GlobalSize(stm.hGlobal);

            m_pObjectNames = (DSOBJECTNAMES*)GlobalAlloc(GPTR, dwBytes);
            if(m_pObjectNames)
            {
                CopyMemory(m_pObjectNames, pdson, dwBytes);
            }
            
            GlobalUnlock(stm.hGlobal);
        }
        
        ReleaseStgMedium(&stm);
    }

    fe.cfFormat = RegisterClipboardFormat(CFSTR_DS_DISPLAY_SPEC_OPTIONS);
    fe.ptd = NULL;
    fe.dwAspect = DVASPECT_CONTENT;
    fe.lindex = -1;
    fe.tymed = TYMED_HGLOBAL;
    hr = pDataObj->GetData(&fe, &stm);
    if(SUCCEEDED(hr))
    {
        PDSDISPLAYSPECOPTIONS   pdso;
        
        pdso = (PDSDISPLAYSPECOPTIONS)GlobalLock(stm.hGlobal);
        if(pdso)
        {
            DWORD   dwBytes = GlobalSize(stm.hGlobal);

            m_pDispSpecOpts = (PDSDISPLAYSPECOPTIONS)GlobalAlloc(GPTR, dwBytes);
            if(m_pDispSpecOpts)
            {
                CopyMemory(m_pDispSpecOpts, pdso, dwBytes);
            }
            
            GlobalUnlock(stm.hGlobal);
        }

        ReleaseStgMedium(&stm);
    }

    return hr;
}

```



## IContextMenu Implementation

The following code example can be used to implement the [**IContextMenu**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) methods.


```C++
///////////////////////////////////////////////////////////////////////////
//
// IContextMenu Implementation
//

/**************************************************************************

   CContMenuExt::QueryContextMenu()

**************************************************************************/

STDMETHODIMP CContMenuExt::QueryContextMenu(    HMENU hMenu,
                                                UINT indexMenu,
                                                UINT idCmdFirst,
                                                UINT idCmdLast,
                                                UINT uFlags)
{
    if(m_pObjectNames && !(CMF_DEFAULTONLY & uFlags))
    {
        InsertMenu( hMenu, 
                    indexMenu, 
                    MF_STRING | MF_BYPOSITION, 
                    idCmdFirst + IDM_CONTMENU, 
                    TEXT("AD Sample Context Menu"));

        return MAKE_HRESULT(SEVERITY_SUCCESS, 0, USHORT(IDM_CONTMENU + 1));
    }

    return MAKE_HRESULT(SEVERITY_SUCCESS, 0, USHORT(0));
}

/**************************************************************************

   CContMenuExt::InvokeCommand()

**************************************************************************/

STDMETHODIMP CContMenuExt::InvokeCommand(LPCMINVOKECOMMANDINFO lpcmi)
{
    if(LOWORD(lpcmi->lpVerb) > IDM_CONTMENU)
    {
        return E_INVALIDARG;
    }

    switch (LOWORD(lpcmi->lpVerb))
    {
    case IDM_CONTMENU:
        {
            LPWSTR  pwszName;
            DWORD   dwBytes;
            UINT    i;

            for(i = 0, dwBytes = 0; i < m_pObjectNames->cItems; i++)
            {
                pwszName = (LPWSTR)((LPBYTE)m_pObjectNames + m_pObjectNames->aObjects[i].offsetName);
                dwBytes += (lstrlenW(pwszName) + 2) * sizeof(WCHAR);
            }

            LPWSTR  pwszText = (LPWSTR)GlobalAlloc(GPTR, dwBytes);

            if(pwszText)
            {
                pwszText[0] = 0;
                for(i = 0; i < m_pObjectNames->cItems; i++)
                {
                    pwszName = (LPWSTR)((LPBYTE)m_pObjectNames + m_pObjectNames->aObjects[i].offsetName);
                    wcscat_s(pwszText, pwszName);
                    wcscat_s(pwszText, L"\n");
                }
                
                MessageBoxW(lpcmi->hwnd, 
                            pwszText, 
                            L"Sample Command", 
                            MB_OK | MB_ICONINFORMATION);

                GlobalFree(pwszText);
            }
        }
        break;
    }

    return NOERROR;
}

/**************************************************************************

   CContMenuExt::GetCommandString()

**************************************************************************/

STDMETHODIMP CContMenuExt::GetCommandString(    UINT idCommand,
                                                UINT uFlags,
                                                LPUINT lpReserved,
                                                LPSTR lpszName,
                                                UINT uMaxNameLen)
{
    HRESULT hr = E_INVALIDARG;
    TCHAR   szHelp[] = TEXT("Sample Context Menu Command");
    TCHAR   szVerb[] = TEXT("adcontmenu");

    switch(uFlags)
    {
    case GCS_HELPTEXTA:
        switch(idCommand)
        {
        case IDM_CONTMENU:
            LocalToAnsi((LPSTR)lpszName, szHelp, uMaxNameLen);
            hr = S_OK;
            break;
         }
        break;
   
    case GCS_HELPTEXTW:
        switch(idCommand)
        {
        case IDM_CONTMENU:
            LocalToWideChar((LPWSTR)lpszName, szHelp, uMaxNameLen);
            hr = S_OK;
            break;
         }
        break;
   
    case GCS_VERBA:
        switch(idCommand)
        {
        case IDM_CONTMENU:
            LocalToAnsi((LPSTR)lpszName, szVerb, uMaxNameLen);
            hr = S_OK;
            break;
        }
        break;
   
    case GCS_VERBW:
        switch(idCommand)
        {
        case IDM_CONTMENU:
            LocalToWideChar((LPWSTR)lpszName, szVerb, uMaxNameLen);
            hr = S_OK;
            break;
        }
        break;
   
    case GCS_VALIDATE:
        hr = S_OK;
        break;
    }

    return hr;
}

```



 

 