---
title: Working with Menu Buttons Implementation Details
description: Working with Menu Buttons Implementation Details
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 144357de-3e42-4808-828f-0780ecef08c5
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- toolbars and menu buttons MMC , implementation details (menu buttons)
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Working with Menu Buttons: Implementation Details

## To add menu buttons using IExtendControlBar

1.  Implement the [**IExtendControlbar**](/windows/desktop/api/Mmc/nn-mmc-iextendcontrolbar) interface and its two methods, [**SetControlBar**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-setcontrolbar) and [**ControlbarNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify).

    The snap-in's [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) implementation should implement and expose the [**IExtendControlbar**](/windows/desktop/api/Mmc/nn-mmc-iextendcontrolbar) interface.

2.  In the snap-in's implementation of [**SetControlBar**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-setcontrolbar):

    -   Cache the [**IControlBar**](/windows/desktop/api/Mmc/nn-mmc-icontrolbar) interface pointer that is passed into [**SetControlBar**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-setcontrolbar). Use this interface pointer to call the **IControlBar** methods.
    -   Call [**IControlBar::Create**](/windows/desktop/api/Mmc/nf-mmc-icontrolbar-create) with the *nType* parameter set to **MENUBUTTON** to create a new menu button. The *pExtendControlbar* parameter specifies the snap-in's [**IExtendControlbar**](/windows/desktop/api/Mmc/nn-mmc-iextendcontrolbar) interface associated with the control. The *ppUnknown* parameter will hold a pointer to the address of the [**IUnknown**](https://www.bing.com/search?q=**IUnknown**) interface of the menu button control. Use this pointer to call the methods of the [**IMenuButton**](/windows/desktop/api/Mmc/nn-mmc-imenubutton) interface associated with the new control.
    -   Add the menu button by calling [**IMenuButton::AddButton**](/windows/desktop/api/Mmc/nf-mmc-imenubutton-addbutton). The *idCommand* parameter specifies a snap-in-defined value that uniquely identifies the menu button to be added. The *lpButtonText* and *lpTooltipText* parameters point to the values of the button text and tooltip text, respectively.

3.  In the snap-in's implementation of [**ControlbarNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify), handle the menu button-specific notification messages that MMC sends during calls to the **ControlbarNotify** method. There are three such notifications: [**MMCN\_MENU\_BTNCLICK**](mmcn-menu-btnclick.md), [**MMCN\_SELECT**](mmcn-select.md), and [**MMCN\_DESELECT\_ALL**](mmcn-deselect-all.md).

    -   The [**MMCN\_SELECT**](mmcn-select.md) notification message is sent to the snap-in's [**ControlbarNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify) method when an item is selected or deselected in either the scope pane or result pane. The snap-in can respond to this notification by attaching its menu button to the control (using [**IControlbar::Attach**](/windows/desktop/api/Mmc/nf-mmc-icontrolbar-attach)) and enabling the menu button (using **IControlbar::SetButtonState**) during selection of an item. During deselection of the item, the snap-in can again call **IControlbar::SetButtonState**, this time to disable the menu button and make it hidden.
    -   The [**MMCN\_MENU\_BTNCLICK**](mmcn-menu-btnclick.md) notification message is sent to the snap-in's [**ControlbarNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify) implementation when a user clicks one of the snap-in's menu buttons. MMC sends this notification with a [**MENUBUTTONDATA**](/windows/desktop/api/Mmc/ns-mmc-_menubuttondata) structure that holds the same command identifier (*idCommand*) that the snap-in specified for the button when it added the button using [**IMenuButton::AddButton**](/windows/desktop/api/Mmc/nf-mmc-imenubutton-addbutton). The snap-in can process the command and then return **S\_OK**.

4.  Implement a mechanism for setting the attributes of the menu buttons using the [**IMenuButton::SetButtonState**](/windows/desktop/api/Mmc/nf-mmc-imenubutton-setbuttonstate) method.

## Sample Code

The following code examples show implementations of the [**IExtendControlBar::SetControlBar**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-setcontrolbar) and [**IExtendControlBar::ControlbarNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify) methods. All samples are taken from the MenuBtn sample snap-in that accompanies the MMC SDK. The MenuBtn sample demonstrates how to add a menu button to a snap-in.

Be aware that all sample code assumes Unicode compilation.

## IExtendControlBar::SetControlBar Implementation


```C++
HRESULT CComponent::SetControlbar(
                   /* [in] */ LPCONTROLBAR pControlbar)
{
    HRESULT hr = S_OK;
 
    //
    //  Clean up
    //
 
    // if there is a cached control bar, release it
    if (m_ipControlBar) {
        m_ipControlBar->Release();
        m_ipControlBar = NULL;
    }
 
    // if there is a cached menubutton, release it
    if (m_ipMenuButton) {
        m_ipMenuButton->Release();
        m_ipMenuButton = NULL;
    }
 
    //
    // Install new pieces if necessary
    //
 
    // if a new one came in, cache and AddRef
    if (pControlbar) {
        m_ipControlBar = pControlbar;
        m_ipControlBar->AddRef();
 
        // add menu button
        hr = m_ipControlBar->Create(MENUBUTTON,  // type of control
            dynamic_cast<IExtendControlbar *>(this),
            reinterpret_cast<IUnknown **>(&amp;m_ipMenuButton));
 
        _ASSERT(SUCCEEDED(hr));
 
        // The IControlbar::Create AddRefs the menu button object it
        // created so no need to do any addref on the interface.
 
        hr = m_ipMenuButton->AddButton(IDR_STATE_MENU, L"Vehicle 
                             Status", L"Change vehicle state");
        _ASSERT(SUCCEEDED(hr));
    }
 
    return hr;
}
```



In the sample, `CComponent` is an instance of the [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) interface. IDR\_STATE\_MENU is a snap-in resource that defines the menu button layout.

## IExtendControlBar::ControlbarNotify Implementation


```C++
{
    HRESULT hr = S_OK;
 
    if (event == MMCN_SELECT) 
    { 
        CDelegationBase *base = 
            GetOurDataObject(reinterpret_cast<IDataObject *>(param))->
            GetBaseNodeObject();
 
        hr = base->SetMenuState(m_ipControlBar, m_ipMenuButton, 
                                (BOOL) LOWORD(arg), (BOOL) 
                                HIWORD(arg));
    } 
    else if (event == MMCN_MENU_BTNCLICK)
    {
        CDelegationBase *base = 
            GetOurDataObject(reinterpret_cast<IDataObject *>(arg))->
            GetBaseNodeObject();
 
        hr = base->OnSetMenuButton(m_ipConsole, 
                                   (MENUBUTTONDATA *)param);
    }
 
    return hr;
}
```



This sample implementation of the [**ControlbarNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify) method handles the [**MMCN\_SELECT**](mmcn-select.md) and [**MMCN\_MENU\_BTNCLICK**](mmcn-menu-btnclick.md) notifications. The `CComponent::ControlbarNotify` method delegates the handling of the notification messages to the actual snap-in object that represents the selected scope or result item.

For example, when the user selects the "Future Vehicles" scope item in the scope pane and then a "Vehicle" result item in its result pane, the snap-in attaches its menu button to the toolbar control and then sets the button's state to visible and enabled. This is done in the `CRocket::SetMenuState` method, where `CRocket` is the snap-in object that represents the selected "Vehicle" result item.


```C++
HRESULT CRocket::SetMenuState(IControlbar *pControlbar, 
                              IMenuButton *pMenuButton, 
                              BOOL bScope, 
                              BOOL bSelect)
{
    HRESULT hr = S_OK;
    
    if (bSelect)
    {
        // Always make sure the menuButton is attached
        hr = pControlbar->Attach(MENUBUTTON, pMenuButton);
        
        hr = pMenuButton->SetButtonState(IDR_STATE_MENU, HIDDEN, 
                                         FALSE);
        hr = pMenuButton->SetButtonState(IDR_STATE_MENU, ENABLED, 
                                         TRUE);
    }
    else if (!bSelect) 
    {
        hr = pMenuButton->SetButtonState(IDR_STATE_MENU, ENABLED, 
                                         FALSE);
        hr = pMenuButton->SetButtonState(IDR_STATE_MENU, HIDDEN, 
                                         TRUE);
    }
    
    return hr;
}
```



The same method on the same object is called when the selected "Vehicle" result item is deselected.

The `CComponent::ControlbarNotify` method also delegates the handling of the [**MMCN\_MENU\_BTNCLICK**](mmcn-menu-btnclick.md) notification message to the snap-in object that represents the selected scope or result item. For example, MMC sends this message when the user selects a "Vehicle" result item (a `CRocket` object) and then clicks the menu button.


```C++
HRESULT CRocket::OnSetMenuButton(IConsole *pConsole, MENUBUTTONDATA *pmbd) 
{ 
    HMENU hMenu = GetMenu(pmbd->idCommand);
    HRESULT hr = S_FALSE;
    HWND  hWnd;
    
    if (hMenu)
    {
        hr = pConsole->GetMainWindow(&amp;hWnd);
        
        if (SUCCEEDED(hr)) 
        {
            LONG ret = TrackPopupMenuEx(hMenu, TPM_NONOTIFY | 
                       TPM_RETURNCMD, pmbd->x, 
                       pmbd->y, hWnd, NULL);
            
            if (ret != 0) { // !cancelled
                hr = OnMenuButtonCommand(pConsole, pmbd->idCommand, 
                     ret);
            }
        }
        
        DestroyMenu(hMenu);
    }
    
    return hr;
}
```



The method first calls `GetMenu`, a snap-in-defined function that loads the snap-in's menu resource and calls the Windows API function [**EnableMenuItem**](https://msdn.microsoft.com/library/windows/desktop/ms647636) to specify the attributes of the menu button's items.


```C++
HMENU CRocket::GetMenu(int nMenuId)
{
    HMENU hResMenu = LoadMenu(g_hinst, MAKEINTRESOURCE(nMenuId));
    HMENU hMenu = GetSubMenu(hResMenu,0);
    
    if (IDR_STATE_MENU == nMenuId) {
        switch (iStatus)
        {
        case RUNNING:
            EnableMenuItem(hMenu, ID_COMMAND_START, MF_BYCOMMAND | 
                           MF_GRAYED);
            EnableMenuItem(hMenu, ID_COMMAND_PAUSE, MF_BYCOMMAND | 
                           MF_ENABLED);
            EnableMenuItem(hMenu, ID_COMMAND_STOP, MF_BYCOMMAND | 
                           MF_ENABLED);
            break;
            
        case PAUSED:
            //sample code removed here
            break;
            
        case STOPPED:
            //sample code removed here
            break;
        }
    } else {
        // some other menu, set state accordingly
    }
    
    return hMenu;
}
```



The **ID\_COMMAND\_START**, **ID\_COMMAND\_PAUSE**, and **ID\_COMMAND\_STOP** values specify the resource IDs defined by the snap-in for the menu button's three items.

Returning to the `CRocket::OnSetMenuButton` method, it then calls the MMC interface method [**IConsole2::GetMainWindow**](https://www.bing.com/search?q=**IConsole2::GetMainWindow**) to get a handle to the console's main frame window. It then passes this handle in a call to another Windows API function, [**TrackPopupMenuEx**](https://www.bing.com/search?q=**TrackPopupMenuEx**); this function displays the menu button on the main frame window at the positions indicated by the **x** and **y** members of the [**MENUBUTTONDATA**](/windows/desktop/api/Mmc/ns-mmc-_menubuttondata) structure passed into `CRocket::OnSetMenuButton`. The **TrackPopupMenuEx** function also tracks the selection of items on the menu button and returns the command ID of the user's selection. The `CRocket` object than processes this selection in its `OnMenuButtonCommand` method:


```C++
HRESULT CRocket::OnMenuButtonCommand(IConsole *pConsole, int nMenuId, long lCommandID)
{
    _TCHAR szVehicle[128];
    
    if (IDR_STATE_MENU == nMenuId) {
        switch (lCommandID) {
        case ID_COMMAND_START:
            iStatus = RUNNING;
            break;
            
        case ID_COMMAND_PAUSE:
            iStatus = PAUSED;
            break;
            
        case ID_COMMAND_STOP:
            iStatus = STOPPED;
            break;
        }
        
        wsprintf(szVehicle, _T("Vehicle %s has been %s"), szName, 
                 (long)iStatus == RUNNING ? _T("started") : 
                 (long)iStatus == PAUSED ? _T("paused") :
                 (long)iStatus == STOPPED ? _T("stopped") : 
                 _T("!!!unknown command!!!"));
        
        int ret = 0;
        MAKE_WIDEPTR_FROMTSTR(pszVehicle, szVehicle);
        pConsole->MessageBox(pszVehicle, L"Vehicle command", 
                             MB_OK | MB_ICONINFORMATION, &amp;ret);
    }
    
    return S_OK;
}
```



Each `CRocket` object stores its status (**RUNNING**, **PAUSED**, or **STOPPED**) in its **iStatus** member variable.

## Related topics

<dl> <dt>

[Working with Toolbars and Menu Buttons: Interfaces](working-with-toolbars-and-menu-buttons-interfaces.md)
</dt> <dt>

[Extending a Primary Snap-in's Control Bar](extending-a-primary-snap-ins-control-bar.md)
</dt> </dl>

 

 




