---
title: Supporting Visual Styles in MFC Snap-ins
description: To support visual themes in a snap-in built on the Microsoft Foundation Classes (MFC) framework, the snap-in must create and reference a manifest (as described in Supporting Visual Styles in Snap-ins), as well as provide code to theme property sheets and other UI elements. This section describes example code changes. For brevity, error-checking is minimized in the example code.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3af193d1-4cc8-4980-8dc5-0c84a1c63c6b
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Supporting Visual Styles in MFC Snap-ins

To support visual themes in a snap-in built on the Microsoft Foundation Classes (MFC) framework, the snap-in must create and reference a manifest (as described in [Supporting Visual Styles in Snap-ins](supporting-visual-styles-in-snap-ins.md)), as well as provide code to theme property sheets and other UI elements. This section describes example code changes. For brevity, error-checking is minimized in the example code.

The following sections provide details.

-   [Supporting visual styles in property sheets](#supporting-visual-styles-in-property-sheets)
-   [Supporting visual styles in other UI elements](#supporting-visual-styles-in-other-ui-elements)

## Supporting visual styles in property sheets

During the creation of your property sheets, you will need to change your code to use the PROPSHEETPAGE\_LATEST structure. For example, your snap-in's property pages may be created by code similar to the following.


```C++
HRESULT CExtendPropertySheet::CreatePropertyPages(
    LPPROPERTYSHEETCALLBACK pCallback,
    LONG_PTR handle,
    LPDATAOBJECT lpIDataObject )
{

    // m_MyPage derives from the MFC CPropertyPage class.
    HPROPSHEETPAGE hPage = ::CreatePropertySheetPage(&amp;m_MyPage.m_psp);
    pCallback->AddPage(hPage);
    return S_OK;
}
```



The code should be modified to use the latest property sheet structure. For example, the following code example shows the use of a helper function, MyCreatePropertySheetPage, which is called from the modified implementation of **CExtendPropertySheet::CreatePropertyPages**.


```C++
HRESULT CExtendPropertySheet::CreatePropertyPages(
    LPPROPERTYSHEETCALLBACK pCallback,
    LONG_PTR handle,
    LPDATAOBJECT lpIDataObject )
{
    // m_MyPage derives from the MFC CPropertyPage class.
    HPROPSHEETPAGE hPage = MyCreatePropertySheetPage(&amp;m_MyPage.m_psp);
    pCallback->AddPage(hPage);
    return S_OK;
}

#ifndef PROPSHEETPAGE_LATEST
    #ifdef UNICODE
        #define PROPSHEETPAGE_LATEST PROPSHEETPAGEW_LATEST
    #else
        #define PROPSHEETPAGE_LATEST PROPSHEETPAGEA_LATEST
    #endif
#endif
 
HPROPSHEETPAGE MyCreatePropertySheetPage(AFX_OLDPROPSHEETPAGE* ppsp)
{
    PROPSHEETPAGE_LATEST pspLatest = {0};
    CopyMemory (&amp;pspLatest, ppsp, ppsp->dwSize);
    pspLatest.dwSize = sizeof(pspLatest);
 
    return (::CreatePropertySheetPage (&amp;pspLatest));
}
```



## Supporting visual styles in other UI elements

Before that displays other snap-in UI elements through calls to functions such as **CreateWindow** or **DialogBox**, set an activation context so that the UI element will support the active visual theme. A helper class can assist you in setting the activation context, and an instance of the helper class can be created when your **CApp** object is created. The following is an example of the implementation for the **CAppFusionInit** helper class (the class can be named to whatever you like). The helper class relies on [**CreateActCtx**](https://msdn.microsoft.com/library/windows/desktop/aa375125) and [**ReleaseActCtx**](https://msdn.microsoft.com/library/windows/desktop/aa375713), which are activation context functions provided by Windows.


```C++
class CAppFusionInit{
   HANDLE  m_hActCtx;
   HMODULE m_hModule;
   int     m_resourceID;
public:
    CAppFusionInit(HMODULE hMod, int id) : m_hActCtx(INVALID_HANDLE_VALUE), m_hModule(hMod), m_resourceID(id)
       {InitializeFromModuleID(hMod,id);}
    ~CAppFusionInit()
       {FusionUninitialize();}

private:
    // The following is deliberately not implemented.
    CAppFusionInit(const CAppFusionInit&amp;); 
    // The following is deliberately not implemented.
    void operator=(const CAppFusionInit&amp;);
private:
    void InitializeFromModuleID(HMODULE hMod, int id)
    {
      TCHAR szPath[MAX_PATH];
      if (0 == GetModuleFileName(hMod, szPath, countof(szPath)))
          return;
      ACTCTX act = {0};
      act.dwFlags = ACTCTX_FLAG_RESOURCE_NAME_VALID;
      act.lpResourceName = MAKEINTRESOURCE(id);
      if (INVALID_HANDLE_VALUE == m_hActCtx)
      {
         act.cbSize = sizeof(act);
         act.lpSource = szPath;

#ifdef UNICODE
         m_hActCtx = CreateActCtxW(&amp;act);
#else
         m_hActCtx = CreateActCtxA(&amp;act);
#endif // !UNICODE
      }
    }
    void FusionUninitialize()
    {
      if (INVALID_HANDLE_VALUE != m_hActCtx)
      {
         ReleaseActCtx(m_hActCtx);
         m_hActCtx = INVALID_HANDLE_VALUE;
      }
    }
public:
     HANDLE GetThemeContextHandle()
    {
        return m_hActCtx;
    }
};
```



Implement a function in your CApp class to get the activation context handle.


```C++
HANDLE CMyApp::GetFusionInitHandle()
{
    if (m_pfusionInit)
       return m_pfusionInit->GetThemeContextHandle();
    return NULL;
}
```



Provide code to create an instance of the CAppFusionInit class in your implementation of CApp::InitInstance. The constant SXS\_MANIFEST\_RESOURCE\_ID is the snap-in's identifier for the snap-in provided manifest.


```C++
m_pfusionInit = new CAppFusionInit(NULL,
  static_cast<int>(
    reinterpret_cast<ULONG_PTR>(SXS_MANIFEST_RESOURCE_ID)));
```



Provide code to delete the instance of the CAppFusionInit class in your implementation of CApp::ExitInstance.


```C++
if (m_pfusionInit)
    delete m_pfusionInit;
```



Create a helper class to manage the activation context. The helper class relies on [**ActivateActCtx**](https://msdn.microsoft.com/library/windows/desktop/aa374151) and [**DeactivateActCtx**](https://msdn.microsoft.com/library/windows/desktop/aa375140), which are activation context functions provided by Windows.


```C++
class CThemeContextActivator {
public:
    CThemeContextActivator(HANDLE hActCtx) : m_ulActivationCookie(0)
        { ActivateActCtx(hActCtx, &amp;m_ulActivationCookie); }

    ~CThemeContextActivator()
     { 
       if (m_ulActivationCookie != 0)
          DeactivateActCtx(0, m_ulActivationCookie);
     }
private:
     ULONG_PTR m_ulActivationCookie;
};
```



Create an instance of the **CThemeContextActivator** class before calling any UI-creating functions, such as **CreateWindow** or **DialogBox**.


```C++
CThemeContextActivator activator(GetMyApp()->GetFusionInitHandle());
// Make the call to CreateWindow, DialogBox, and so on.
// ...
```



 

 




