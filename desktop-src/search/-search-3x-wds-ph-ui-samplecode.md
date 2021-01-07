---
description: The following sample code shows how to create Shell extensions for a custom protocol handler.
ms.assetid: 4b65ced8-8dc9-43f6-bfe1-3703aea3459f
title: 'Code Sample: Shell Extensions for Protocol Handlers'
ms.topic: article
ms.date: 05/31/2018
---

# Code Sample: Shell Extensions for Protocol Handlers

The following sample code shows how to create Shell extensions for a custom protocol handler.

## Sample code

> [!Note]
>
> **THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.**
>
> Copyright (c)Microsoft Corporation. All rights reserved.

 


```
// ********************** IDL structure **********************

#include <pshpack1.h>

typedef struct
{
    WORD    cbSize;
    WORD    cchUrl;      // Store the length of the URL.
    WCHAR   pwszUrl[1];  // Store the URL.
} URLIDL;


#include <poppack.h>

class ATL_NO_VTABLE CSampleShellFolder :
    public CComTearOffObjectBase<CSampleSearchProtocol>,
    public IPersistFolder,
    public IShellFolder
{
public:
    DECLARE_PROTECT_FINAL_CONSTRUCT()

    BEGIN_COM_MAP(CSampleShellFolder)
        COM_INTERFACE_ENTRY(IPersistFolder)
        COM_INTERFACE_ENTRY(IShellFolder)
    END_COM_MAP()

    CSampleShellFolder();
    virtual ~CSampleShellFolder();
    HRESULT FinalConstruct() {return S_OK;};
    void FinalRelease() {};

    // IPersist
    STDMETHOD(GetClassID)(CLSID* pCLSID);

    // IPersistFolder
    STDMETHOD(Initialize)(const ITEMIDLIST* pidl);

    // IShellFolder
    STDMETHOD(ParseDisplayName)
 (HWND hwnd, IBindCtx* pbc, OLECHAR* pszName, 
ULONG* pchEaten, ITEMIDLIST** ppidl, ULONG* pdwAttributes);
    STDMETHOD(EnumObjects)
 (HWND hwnd, DWORD grfFlags, IEnumIDList** ppenmIDList);
    STDMETHOD(BindToObject)
(const ITEMIDLIST* pidl, IBindCtx* pbc, REFIID riid, void** ppvObj);
    STDMETHOD(BindToStorage)
(const ITEMIDLIST* pidl, IBindCtx* pbc, REFIID riid, void** ppvObj);
    STDMETHOD(CompareIDs)
(LPARAM lParam, const ITEMIDLIST* pidl1, const ITEMIDLIST* pidl2);
    STDMETHOD(CreateViewObject)
(HWND hwndOwner, REFIID riid, void** ppvObj) ;
    STDMETHOD(GetAttributesOf)
(UINT cidl, const ITEMIDLIST** ppidl, SFGAOF* prgfInOut);
    STDMETHOD(GetUIObjectOf)
(HWND hwndOwner, UINT cidl, const ITEMIDLIST** ppidl,
 REFIID riid, UINT* prgfInOut, void** ppvObj);
    STDMETHOD(GetDisplayNameOf)
(const ITEMIDLIST* pidl, DWORD dwFlags, STRRET* pstrName);
    STDMETHOD(SetNameOf)
(HWND hwnd, const ITEMIDLIST* pidl, const OLECHAR* pszName,
 DWORD dwFlags, ITEMIDLIST** ppidlOut);

// IDL Helper Routines
private:
    static HRESULT CreateIDL(CString & strUrl, ITEMIDLIST** ppidl);
    static SampleIDL *IsURLIDL(const ITEMIDLIST* pidl);
    static HRESULT GetUrlFromIDL (const ITEMIDLIST *pidl, CString & strUrl); 
};

// ******************* IDL Helper routines *******************

//------------------------------------------------------------
//  GetUrlFromIDL()
//
// Return the URL for the specified PIDL.
//------------------------------------------------------------

HRESULT CSampleShellFolder::GetUrlFromIDL(
      const ITEMIDL * pidl,
      CString &strUrl)
{
    if (IsURLIDL(pidl) == NULL)
        return E_FAIL;

    URLIDL *pURLIDL=(URLIDL *)pidl;
    strUrl.SetString(pURLIDL->pwszUrl,pURLIDL->cchUrl);
    return S_OK;
}

//------------------------------------------------------------
//  CreateIDL()
//
// Create a PIDL for the specified URL.
//------------------------------------------------------------

HRESULT CSampleShellFolder::CreateIDL(
      CString &strUrl, 
      ITEMIDL** ppidl)
{
    HRESULT hr = S_OK;

    // Check assertions.
    _ASSERTE(ppidl);

    // Initialize the return value.
    *ppidl = NULL;

    // Get the size of the URL
    WORD cb;
    WORD cbUrl = strUrl.GetLength() * sizeof(WCHAR);
    cb = (WORD)sizeof(URLIDL) + cbUrl;

    // Allocate an additional WORD, which is the "next"
    // PIDL (one of cb==0).
    URLIDL* pURLIDL = (URLIDL*)LocalAlloc(LPTR, cb + sizeof(WORD));
    hr = (pURLIDL ? S_OK : E_FAIL);
    if (SUCCEEDED(hr))
    {
        pURLIDL->cbSize = cb;
        // Store the number of characters in the URL.
        pURLIDL->cchUrl = (WORD)strUrl.GetLength(); 

        // NOTE: CopyChars copies the exact number of characters
        // *including* the terminating null character.

        CString::CopyChars(
                  pURLIDL->pwszUrl, 
                  (LPCTSTR)strUrl, 
                  strUrl.GetLength() + 1);

        // Terminate the IDL.
        ITEMIDL *pidlNext = (ITEMIDL *)
                  (((LPBYTE)pURLIDL) + pURLIDL->cbSize);
        *((WORD *)pidlNext) = 0;

        // Return a clone of the IDL.
        *ppidl = ILClone((ITEMIDL*)pURLIDL);
        hr = (*ppidl ? S_OK : E_OUTOFMEMORY);

        // Free the IDL.
        LocalFree((HLOCAL)pURLIDL);
    }

    return hr;
}

//------------------------------------------------------------
//  IsURLIDL()
//
// Check the validity of a PIDL, returning a pointer to the
// URLIDL portion of the PIDL.
//------------------------------------------------------------

URLIDL *CSampleShellFolder::IsURLIDL(const ITEMIDL* pidl)
{
    URLIDL * pURLIDL = NULL;
    CString strSample = L"sample:";
    
    // Check for the presence and length of a PIDL.
    // If the PIDL is present and of sufficient length,
    // compare it to the start URL.
    if (pidl && 
        (ILGetSize(pidl) > strSample.GetLength()*sizeof(WCHAR)) )
    {
        pURLIDL = (URLIDL *)pidl;
        CString strUrl;
        strUrl.SetString(pURLIDL->pwszUrl, 7);
        if (strUrl.CompareNoCase(strSample) == 0)
        {
            return pURLIDL;
        }
    }

    return NULL;
}

// ************************ IPersist *************************
//------------------------------------------------------------
// IPersist::GetClassID
//
// Retrieve the class identifier (CLSID) of an object. The
// CLSID is a unique value that identifies the code that can
// manipulate the persistent data.
//------------------------------------------------------------
STDMETHODIMP CSampleShellFolder::GetClassID(CLSID* pCLSID)
{
    if (pCLSID == NULL)
        return E_POINTER;

    *pCLSID = CLSID_SampleProtocol;
    return S_OK;
}

// ********************* IPersistFolder **********************

//------------------------------------------------------------
// IPersistFolder::Initialize
//
// Instruct a ShellFolder object to initialize itself based
// on the information provided. 
//------------------------------------------------------------

STDMETHODIMP CSampleShellFolder::Initialize(const ITEMIDL* pidl)
{
    // Since we have only one folder in this sample, there
    // is nothing to store.
    return S_OK;
}

// ******************** IShellFolder *************************

//------------------------------------------------------------
// IShellFolder::ParseDisplayName
//
// Translate a file object's display name or a folder's
// display name into an item identifier list.
//------------------------------------------------------------

STDMETHODIMP CSampleShellFolder::ParseDisplayName(
      HWND hwnd, IBindCtx* pbc,
      OLECHAR* pszName,
      ULONG* pchEaten,
      ITEMIDL** ppidl,
      ULONG* pdwAttributes)
{
    HRESULT hr = E_FAIL;

    if ((pszName == NULL) || (ppidl == NULL))
        return E_POINTER;

    *ppidl = NULL;

    CString strName = L"";
    
    // Get the first seven bytes of the name.
    strName.SetString(pszName, 7);
    
    // Determine whether the name starts with "outlook",
    // the first seven characters of outlookexpress.
    if (strName.CompareNoCase(L"sample:") == 0)
    {

        // If TRUE, we can assume this is an outlookexpress URL.
        CString strUrl = pszName;

        // Create the PIDL.
        hr = CSampleShellFolder::CreateURLIDL(strUrl, ppidl);

        if (SUCCEEDED(hr))
        {
            if (pchEaten != NULL)
                *pchEaten = strUrl.GetLength();

            if (pdwAttributes != NULL)
                *pdwAttributes = 0;
        }
    }
    return hr;
}

//------------------------------------------------------------
// IShellFolder::EnumObjects
//
// Enable a client to determine the contents of a folder by
// creating an item identifier enumeration object and returning
// its IEnumIDL interface. The methods supported by that
// interface can then be used to enumerate the folder's contents.
//------------------------------------------------------------

STDMETHODIMP CSampleShellFolder::EnumObjects(
      HWND hwnd,
      DWORD grfFlags,
      IEnumIDL** ppenmIDL)
{
    return E_NOTIMPL;
}

//------------------------------------------------------------
// IShellFolder::BindToObject
//
// Retrieve an IShellFolder object for a subfolder.
//------------------------------------------------------------

STDMETHODIMP CSampleShellFolder::BindToObject(
      const ITEMIDL* pidl,
      IBindCtx* pbc,
      REFIID riid, void** ppvObj)
{
    return E_NOTIMPL;
}

//------------------------------------------------------------
// IShellFolder::BindToStorage
//
// Request a pointer to an object's storage interface.
//------------------------------------------------------------

STDMETHODIMP CSampleShellFolder::BindToStorage(
      const ITEMIDL* pidl,
      IBindCtx* pbc,
      REFIID riid, void** ppvObj)
{
    // NOTE: Although this code is not implemented in the sample, 
    // it is possible to bind to IUrlAccessor->BindToStream()
    // to bind to the storage.
    return E_NOTIMPL;
}

//------------------------------------------------------------
// IShellFolder::CompareIDs
//
// Determine the relative order of two file objects or folders,
// given their item identifier lists.
//------------------------------------------------------------

STDMETHODIMP CSampleShellFolder::CompareIDs(
      LPARAM lParam,
      const ITEMIDL* pidl1,
      const ITEMIDL* pidl2)
{
    if ((pidl1 == NULL) || (pidl2 == NULL))
        return E_POINTER;

    // Ensure that these are our PIDLs
    URLIDL * pURLIDL1 = IsURLIDL(pidl1);
    URLIDL * pURLIDL2 = IsURLIDL(pidl2);
    if (!pURLIDL1 || !pURLIDL2)
    {
        return S_FALSE;
    }

    // Check the query for equality
    CString strUrl1;
    CString strUrl2;
    strUrl1.SetString(pURLIDL1->pwszUrl, pURLIDL1->cchUrl);
    strUrl2.SetString(pURLIDL2->pwszUrl, pURLIDL2->cchUrl);
    return (strUrl1.CompareNoCase(strUrl2));
}

//------------------------------------------------------------
// IShellFolder::CreateViewObject
//
// Request an object that can be used to obtain information
// from or interact with a folder object.
//------------------------------------------------------------

STDMETHODIMP CSampleShellFolder::CreateViewObject(
      HWND hwndOwner,
      REFIID riid,
      void** ppvObj)
{
    return E_NOTIMPL;
}

//------------------------------------------------------------
// IShellFolder::GetAttributesOf
//
// Retrieve the attributes of one or more file objects or
// subfolders.
//------------------------------------------------------------

STDMETHODIMP CSampleShellFolder::GetAttributesOf(
      UINT cidl,
      const ITEMIDL** ppidl,
      SFGAOF* prgfInOut)
{
    for ( UINT i = 0; i < cidl; i++)
    {
        DWORD dwAttrs = 0;
            
        // SFGAO_FOLDER | SFGAO_CANLINK;
        dwAttrs |= SFGAO_NONENUMERATED|SFGAO_READONLY; 

        *prgfInOut &= dwAttrs;
    }
    return S_OK;
}

//------------------------------------------------------------
// IShellFolder::GetUIObjectOf
//
// Retrieve an OLE interface that can be used to carry out
// actions on the specified file objects or folders.
//------------------------------------------------------------

STDMETHODIMP CSampleShellFolder::GetUIObjectOf(
      HWND hwndOwner, 
      UINT cidl, 
      const ITEMIDL** ppidl, 
      REFIID riid, 
      UINT* prgfInOut, 
      void** ppvObj)
{
    if ((ppidl == NULL) || (ppvObj == NULL))
        return E_POINTER;

    *ppvObj = NULL;

    // Create the appropriate object.
    HRESULT hr=S_OK;

    // By design, we handle only one object at a time.
    if (cidl > 1)
        return E_INVALIDARG;

    CString strUrl;
    hr = GetUrlFromIDL(*ppidl, strUrl);

    if (SUCCEEDED(hr))
    {
         if (riid == __uuidof(IContextMenu))
         {
                // Return the IContextMenu for this URL
          }
         else
         if (riid == __uuidof(IExtractIcon))
         {
                // Return the IExtractIcon for this URL
         }
         else
             Hr = E_NOINTERFACE;        
    }
    return hr;
}

//------------------------------------------------------------
// IShellFolder::GetDisplayNameOf
//
// Retrieve the display name for the specified file object
// or subfolder.
//------------------------------------------------------------

STDMETHODIMP CSampleShellFolder::GetDisplayNameOf(
      const ITEMIDL* pidl,
      DWORD dwFlags, 
      STRRET* pstrName)
{
    HRESULT hr = S_OK;
    URLIDL * pURLIDL = IsURLIDL(pidl);

    if (pURLIDL)
    {
        pstrName->uType = STRRET_OFFSET;
        pstrName->uOffset = sizeof(WORD) + sizeof(WORD);
    }
    return hr;
}

//------------------------------------------------------------
// IShellFolder::SetNameOf
//
// Set the display name of a file object or subfolder,
// changing the item identifier in the process.
//------------------------------------------------------------

STDMETHODIMP CSampleShellFolder::SetNameOf(
      HWND hwnd,
      const ITEMIDL* pidl,
      const OLECHAR* pszName, 
      DWORD dwFlags, 
      ITEMIDL** ppidlOut)
{
    return E_NOTIMPL;
}
        
```



## Additional Resources

-   For Search code samples, see [Windows Search SDK Samples](https://www.microsoft.com/downloads/details.aspx?FamilyID=645300AE-5E7A-4CE7-95F0-49793F8F76E8).
-   For Shell code samples, see [Shell SDK Samples](/previous-versions/windows/desktop/legacy/dd940376(v=vs.85)).

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

[Adding Icons and Context Menus](-search-3x-wds-ph-ui-extensions.md)
</dt> <dt>

[Installing and Registering Protocol Handlers](-search-3x-wds-ph-install-registration.md)
</dt> <dt>

[Creating a Search Connector for a Protocol Handler](-search-3x-wds-ph-search-connector.md)
</dt> <dt>

[Debugging Protocol Handlers](-search-ws-protocolhandlertesting.md)
</dt> </dl>

 

 
