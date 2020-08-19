---
title: Example Code for Implementation of the Property Sheet COM Object
description: The following code example can be used to implement an Active Directory property sheet extension.
ms.assetid: aeee870e-1a0e-437f-a724-0bbac30f5e34
ms.tgt_platform: multiple
keywords:
- Example Code for Implementation of the Property Sheet COM Object AD
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Implementation of the Property Sheet COM Object

The following code example can be used to implement an Active Directory property sheet extension.

## IShellExtInit Implementation

The following C++ code example can be used to implement the [**IShellExtInit**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellextinit) methods.


```C++
/**************************************************************************

    CPropSheetExt::Initialize()

**************************************************************************/

STDMETHODIMP CPropSheetExt::Initialize( LPCITEMIDLIST pidlFolder,
                                        IDataObject *pDataObj,
                                        HKEY hKeyProgId)
{
    STGMEDIUM   stm;
    FORMATETC   fe;
    HRESULT     hr = S_OK;

    if(NULL == pDataObj)
    {
        return E_INVALIDARG;
    }

    hr = pDataObj->QueryInterface(IID_IDataObject, (LPVOID*)&m_pdo);
    if(FAILED(hr))
    {
        return hr;
    }

    fe.cfFormat = RegisterClipboardFormat(CFSTR_DSOBJECTNAMES);
    fe.ptd = NULL;
    fe.dwAspect = DVASPECT_CONTENT;
    fe.lindex = -1;
    fe.tymed = TYMED_HGLOBAL;
    hr = m_pdo->GetData(&fe, &stm);
    if(SUCCEEDED(hr))
    {
        LPDSOBJECTNAMES pdson = (LPDSOBJECTNAMES)GlobalLock(stm.hGlobal);

        if(pdson)
        {
            LPWSTR  pwszName = (LPWSTR)((LPBYTE)pdson + pdson->aObjects[0].offsetName);
            
            m_pwszADsPath = (LPWSTR)GlobalAlloc(GPTR, (lstrlenW(pwszName) + 1) * sizeof(WCHAR));
            if(m_pwszADsPath)
            {
                wcscpy_s(m_pwszADsPath, pwszName);
            }
            
            LPWSTR  pwszClass = (LPWSTR)((LPBYTE)pdson + pdson->aObjects[0].offsetClass);
            pwszClass = NULL;

            GlobalUnlock(stm.hGlobal);
        }
        
        ReleaseStgMedium(&stm);
    }

    m_hwndNotifyObj = CreateADsNotificationObject(pDataObj);

    if(m_hwndNotifyObj)
    {
        ADSPROPINITPARAMS   InitParams;
        
        hr = GetADsPageInfo(m_hwndNotifyObj, &InitParams);
        if(SUCCEEDED(hr))
        {
            if(InitParams.pDsObj)
            {
                hr = InitParams.pDsObj->QueryInterface( IID_IDirectoryObject, 
                                                        (LPVOID*) & m_pDirObj);
            }
        }
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



## IShellPropSheetExt Implementation

The following C++ code example can be used to implement the [**IShellPropSheetExt**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellpropsheetext) methods.


```C++
/**************************************************************************

    CPropSheetExt::AddPages()

**************************************************************************/

STDMETHODIMP CPropSheetExt::AddPages(   LPFNADDPROPSHEETPAGE pfnAddPage, 
                                        LPARAM lParam)
{
    PROPSHEETPAGE  psp;
    HPROPSHEETPAGE hPage;

    psp.dwSize        = sizeof(psp);
    psp.dwFlags       = PSP_USETITLE | PSP_USECALLBACK;
    psp.hInstance     = g_hInst;
    psp.pszTemplate   = MAKEINTRESOURCE(IDD_PAGEDLG);
    psp.hIcon         = 0;
    psp.pszTitle      = g_szPageTitle;
    psp.pfnDlgProc    = (DLGPROC)PageDlgProc;
    psp.pcRefParent   = NULL;
    psp.pfnCallback   = PageCallbackProc;
    //pass the object pointer to the dialog box
    psp.lParam        = (LPARAM)this;

    hPage = CreatePropertySheetPage(&psp);
                
    if(hPage) 
    {
        if(pfnAddPage(hPage, lParam))
        {
            /*
            Maintain this object until the page is released in 
            PageCallbackProc.
            */
            this->AddRef();
            return S_OK;
        }
        else
        {
            DestroyPropertySheetPage(hPage);
        }
    }
    else
    {
        return E_OUTOFMEMORY;
    }

    return E_FAIL;
}

/**************************************************************************

    CPropSheetExt::ReplacePage()

**************************************************************************/

STDMETHODIMP CPropSheetExt::ReplacePage(    UINT uPageID, 
                                            LPFNADDPROPSHEETPAGE lpfnAddPage, 
                                            LPARAM lParam)
{
    return E_NOTIMPL;
}

```



## Miscellaneous Implementation

The following C++ code example can be used to implement the utility methods and functions used in the previous code example.


```C++
HWND CreateADsNotificationObject(IDataObject *pDataObject)
{
    STGMEDIUM   stm;
    FORMATETC   fe;
    HRESULT     hr;
    HWND        hwndNotifyObject = NULL;

    /*
    The "DsAdminMultiSelectClipFormat" clipboard format is supported by the 
    data object if the Active Directory Users and Computers snap-in supports 
    multi-selection property sheets.
    */
    fe.cfFormat = RegisterClipboardFormat(TEXT("DsAdminMultiSelectClipFormat"));
    fe.ptd = NULL;
    fe.dwAspect = DVASPECT_CONTENT;
    fe.lindex = -1;
    fe.tymed = TYMED_HGLOBAL;
    hr = pDataObject->GetData(&fe, &stm);
    if (SUCCEEDED(hr))
    {
        PWSTR pwzUniqueID = (LPWSTR)GlobalLock(stm.hGlobal);

        if (pwzUniqueID)
        {
            hr = ADsPropCreateNotifyObj(pDataObject, pwzUniqueID, &hwndNotifyObject);

            GlobalUnlock(stm.hGlobal);
        }
            
        ReleaseStgMedium(&stm);
    }
    else
    {
        fe.cfFormat = RegisterClipboardFormat(CFSTR_DSOBJECTNAMES);
        fe.ptd = NULL;
        fe.dwAspect = DVASPECT_CONTENT;
        fe.lindex = -1;
        fe.tymed = TYMED_HGLOBAL;
        hr = pDataObject->GetData(&fe, &stm);
        if(SUCCEEDED(hr))
        {
            LPDSOBJECTNAMES pdson = (LPDSOBJECTNAMES)GlobalLock(stm.hGlobal);

            if(pdson)
            {
                LPWSTR  pwszName = (LPWSTR)((LPBYTE)pdson + pdson->aObjects[0].offsetName);
                
                hr = ADsPropCreateNotifyObj(pDataObject, pwszName, &hwndNotifyObject);

                GlobalUnlock(stm.hGlobal);
            }
            
            ReleaseStgMedium(&stm);
        }
    }

    return hwndNotifyObject;
}

/**************************************************************************

    GetADsPageInfo()
   
**************************************************************************/

HRESULT GetADsPageInfo(HWND hwndNotifyObject, ADSPROPINITPARAMS *pip)
{
    if(!IsWindow(hwndNotifyObject))
    {
        return E_INVALIDARG;
    }

    ADSPROPINITPARAMS   InitParams;
    
    InitParams.dwSize = sizeof(ADSPROPINITPARAMS);
    if(ADsPropGetInitInfo(hwndNotifyObject, &InitParams))
    {
        *pip = InitParams;
    
        return InitParams.hr;
    }
    
    return E_FAIL;
}

/**************************************************************************

    CPropSheetExt::PageDlgProc

**************************************************************************/

#define THIS_POINTER_PROP  TEXT("ThisPointerProperty")

BOOL CALLBACK CPropSheetExt::PageDlgProc(   HWND hWnd, 
                                            UINT uMsg, 
                                            WPARAM wParam, 
                                            LPARAM lParam)
{
    // Get the object pointer.
    CPropSheetExt *pExt = (CPropSheetExt*)GetProp(hWnd, THIS_POINTER_PROP);
    
    switch(uMsg)
    {
    case WM_INITDIALOG:
        {
            /*
            Get the pointer to the object. This is contained in the LPARAM of 
            the PROPSHEETPAGE structure.
            */
            LPPROPSHEETPAGE pPage = (LPPROPSHEETPAGE)lParam;

            if(pPage)
            {
                pExt = (CPropSheetExt*)pPage->lParam;

                if(pExt)
                {
                    // Set the page window handle in the object.
                    pExt->m_hwndPage = hWnd;
                    
                    // Store the object pointer with this particular page dialog.
                    SetProp(hWnd, THIS_POINTER_PROP, (HANDLE)pExt);

                    ADsPropSetHwnd(pExt->m_hwndNotifyObj, hWnd, g_szPageTitle);

                    // Forward the message to the message handler.
                    return pExt->OnInitDialog(wParam, lParam);
                }
            }
        }
        break;

    case WM_NOTIFY:
        if(pExt)
        {
            // Forward the message to the message handler.
            return pExt->OnNotify(wParam, lParam);
        }
        break;
    
    case WM_COMMAND:
        if(pExt)
        {
            // Forward the message to the message handler.
            return pExt->OnCommand(wParam, lParam);
        }
        return FALSE;
    
    case WM_DESTROY:
        if(pExt)
        {
            // Forward the message to the message handler.
            pExt->OnDestroy();
        }
        
        // Remove the property from the page.
        RemoveProp(hWnd, THIS_POINTER_PROP);
        break; 
    }

    return FALSE;
}


/**************************************************************************

    CPropSheetExt::PageCallbackProc()

    This function is called when the page is created and released. This is 
    even called if the page is never actually displayed. 

**************************************************************************/

UINT CALLBACK CPropSheetExt::PageCallbackProc(  HWND hWnd,
                                                UINT uMsg,
                                                LPPROPSHEETPAGE ppsp)
{
    switch(uMsg)
    {
    case PSPCB_CREATE:
        // Must return TRUE to create the page.
        return TRUE;

    case PSPCB_RELEASE:
        {
            /*
            Release the object. This is called even if the page dialog was 
            never actually created.
            */
            CPropSheetExt *pPropSheetExt = (CPropSheetExt*)ppsp->lParam;

            if(pPropSheetExt)
            {
                if(IsWindow(pPropSheetExt->m_hwndNotifyObj))
                {
                    SendMessage(pPropSheetExt->m_hwndNotifyObj, 
                        WM_ADSPROP_NOTIFY_EXIT, 
                        0, 
                        0);

                    pPropSheetExt->m_hwndNotifyObj = NULL;
                }
                pPropSheetExt->Release();
            }
        }
        break;
    }

    return FALSE;
}


```



 

 