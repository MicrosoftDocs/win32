---
title: Persisting Ribbon State
description: The Windows Ribon framework (Ribbon) provides the ability to preserve the state of a variety of user settings and preferences across application sessions.
ms.assetid: f59e36be-8e3d-454a-b93c-9fc5fc5ecb47
ms.topic: article
ms.date: 05/31/2018
---

# Persisting Ribbon State

The Windows Ribon framework (Ribbon) provides the ability to preserve the state of a variety of user settings and preferences across application sessions.

-   [Introduction](#introduction)
-   [A Predictable Experience](#a-predictable-experience)
-   [Save Ribbon Settings](#save-ribbon-settings)
-   [Load Ribbon Settings](#load-ribbon-settings)
-   [Related topics](#related-topics)

## Introduction

Various aspects of a ribbon, including configuration and interaction preferences, can be customized by a user at run time to improve usability and productivity. The Ribbon framework provides the functionality to preserve these settings across application sessions through two methods defined in the implementation of the [**IUIRibbon**](/windows/desktop/api/uiribbon/nn-uiribbon-iuiribbon) interface: [**IUIRibbon::LoadSettingsFromStream**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiribbon-loadsettingsfromstream) and [**IUIRibbon::SaveSettingsToStream**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiribbon-savesettingstostream).

## A Predictable Experience

The [Ribbon User Experience Guidelines](https://msdn.microsoft.com/library/cc872782.aspx) advise that, to provide the most predictable user experience possible, Ribbon applications should preserve the state of the ribbon (aside from the last selected tab) as the application is closed. In this way, when the same application is launched, the settings and customizations from the previous session can be restored and the user can expect to continue interacting with the application in the same way as they left it.

Ribbon settings that can be modified at run time and preserved across application sessions are listed in the Command context menu. They include:

-   Commands added to the [Quick Access Toolbar](windowsribbon-controls-quickaccesstoolbar.md) Command list by the user. Specified by an [**IUICollection**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicollection) object through the [UI\_PKEY\_ItemsSource](windowsribbon-reference-properties-uipkey-itemssource.md) property key.

    The following screen shot shows the **Add to Quick Access Toolbar** context menu Command.

    ![screen shot of the command context menu in the microsoft paint ribbon.](images/controls/qat-contextmenu-add.png)

-   The preferred [Quick Access Toolbar](windowsribbon-controls-quickaccesstoolbar.md) docking state. Specified by the [**UI\_CONTROLDOCK**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_controldock) value of the [UI\_PKEY\_QuickAccessToolbarDock](windowsribbon-reference-properties-uipkey-quickaccesstoolbardock.md) property key.

    This screen shot shows the [Quick Access Toolbar](windowsribbon-controls-quickaccesstoolbar.md) in its default application title bar location and the **Show Quick Access Toolbar below the Ribbon** context menu Command.

    ![screen shot of the command context menu in the microsoft paint ribbon.](images/controls/qat-contextmenu-add.png)

    This screen shot shows the [Quick Access Toolbar](windowsribbon-controls-quickaccesstoolbar.md) below the ribbon.

    ![screen shot of the quick access toolbar docked below the ribbon.](images/controls/qat-dockbottom.png)

-   The ribbon minimized state as specified by the boolean value of the [UI\_PKEY\_Minimized](windowsribbon-reference-properties-uipkey-minimized.md) property key.

    > [!Note]  
    > The ribbon minimized state is not equivalent to the ribbon collapsed state. When in collapsed state, the ribbon is completely hidden and cannot be interacted with. The framework invokes this state automatically if the application window is reduced in size, either horizontally or vertically, to the point that the ribbon obscures the application workspace. The framework restores the ribbon when the size of the application window is increased.

     

    This screen shot shows the **Minimize the Ribbon** context menu Command.

    ![screen shot of the command context menu in the microsoft paint ribbon.](images/controls/qat-contextmenu-add.png)

    This screen shot shows a minimized ribbon.

    ![screen shot of the minimized microsoft paint ribbon.](images/properties/ui-pkey-minimized.png)

## Save Ribbon Settings

The [**IUIRibbon::SaveSettingsToStream**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiribbon-savesettingstostream) method writes a binary representation of the persistent ribbon state (outlined in the previous section) to an [IStream](/windows/win32/api/objidl/nn-objidl-istream) object. The application then saves the content of the IStream object to a file or the Windows registry.

The following example demonstrates the basic code required to write the ribbon state to an [IStream](/windows/win32/api/objidl/nn-objidl-istream) object using the [**IUIRibbon::SaveSettingsToStream**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiribbon-savesettingstostream) method.


```C++
// pRibbon        - Pointer to the IUIRibbon interface
// ppStatusStream - Pointer to the location of a newly created IStream object
HRESULT CApplication::SaveRibbonStatusToStream(
                        __in IUIRibbon *pRibbon, 
                        __out IStream **ppStatusStream)
{
  HRESULT hr = E_FAIL; 

  *ppStatusStream = NULL;
  IStream* pStream;
  if (SUCCEEDED(hr = CreateStreamOnHGlobal(
                       NULL,  // Internally allocate a new shared memory.
                       FALSE, // Free hGlobal after IStream object released.
                       &pStream)))
  {
    if (SUCCEEDED(hr = pRibbon->SaveSettingsToStream(*ppStatusStream)))
    {                  
      pStream->AddRef();
      *ppStatusStream = pStream;
    }
    pStream->Release();
  }
  return hr;
}
```



## Load Ribbon Settings

The [**IUIRibbon::LoadSettingsFromStream**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiribbon-loadsettingsfromstream) method is used to retrieve the persistent ribbon state information stored as an [IStream](/windows/win32/api/objidl/nn-objidl-istream) object by the [**IUIRibbon::SaveSettingsToStream**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiribbon-savesettingstostream) method. The information in the IStream object is applied to the ribbon UI when the application initializes.

The following example demonstrates the basic code required to load the ribbon state from an [IStream](/windows/win32/api/objidl/nn-objidl-istream) object with the [**IUIRibbon::LoadSettingsFromStream**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiribbon-loadsettingsfromstream) method.


```C++
// pRibbon       - Pointer to the IUIRibbon interface
// pStatusStream - Pointer to the IStream object that contains the Ribbon state information
HRESULT CApplication::LoadRibbonStatusFromStream(
                        __in IUIRibbon *pRibbon, 
                        __in IStream *pStatusStream)
{     
  HRESULT hr = E_FAIL;
  if (pStatusStream)
  {
    // Set the stream position to the beginning first.
    LARGE_INTEGER liStart = {0, 0};
    ULARGE_INTEGER ulActual;
    pStatusStream->Seek(liStart, STREAM_SEEK_SET, &ulActual);
    hr = pRibbon->LoadSettingsFromStream(pStatusStream);
  }
  return hr;
}
```



For optimal performance, the [**IUIRibbon::LoadSettingsFromStream**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiribbon-loadsettingsfromstream) method should be called from the [**IUIApplication::OnViewChanged**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiapplication-onviewchanged) callback function during the framework initialization phase, as shown in the following example.


```C++
IFACEMETHODIMP CMyRibbonApplication::OnViewChanged(
                                       UINT nViewID, 
                                       __in UI_VIEWTYPE typeID, 
                                       __in IUnknown* pView, 
                                       UI_VIEWVERB verb, 
                                       INT iReasonCode)
{
  HRESULT hr = E_NOTIMPL;
  if (UI_VIEWVERB_CREATE == verb)
  {
    IUIRibbon* pRibbon = NULL;
    hr = pView->QueryInterface(IID_PPV_ARGS(&pRibbon));

    if (SUCCEEDED(hr))
    {
      hr = _LoadRibbonSettings(pRibbon);
      pRibbon->Release();
    }
  }
  return hr;
}

HRESULT CMyRibbonApplication::_LoadRibbonSettings(IUIRibbon* pRibbon)
{
  ...
  pRibbon->LoadSettingsFromStream(pStream);
  ...
}
```



Multiple instances of the same Ribbon framework application can manage each ribbon state independently as separate [IStream](/windows/win32/api/objidl/nn-objidl-istream) objects or as a group through a single IStream object.

When synchronizing ribbon state across a group of application instances, each top-level window must listen for a [WM\_ACTIVATE](../inputdev/wm-activate.md) notification. The top-level window being deactivated saves its ribbon state using the [**IUIRibbon::SaveSettingsToStream**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiribbon-savesettingstostream) method, and the top-level window being activated loads its ribbon state using the [**IUIRibbon::LoadSettingsFromStream**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiribbon-loadsettingsfromstream) method.

## Related topics

<dl> <dt>

[Quick Access Toolbar](windowsribbon-controls-quickaccesstoolbar.md)
</dt> </dl>

 

 