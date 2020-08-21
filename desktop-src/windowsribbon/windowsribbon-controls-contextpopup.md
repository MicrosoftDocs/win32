---
title: Context Popup
description: A Context Popup is the principal control in the ContextPopup View of the Windows Ribbon framework.
ms.assetid: c41b888a-15aa-4c47-ad73-5dc30b5fa6f9
ms.topic: article
ms.date: 05/31/2018
---

# Context Popup

A Context Popup is the principal control in the [**ContextPopup View**](windowsribbon-element-contextpopup.md) of the Windows Ribbon framework. It is a rich context menu system that is only exposed by the framework as an extension to a Ribbon implementation—the framework does not expose the Context Popup as an independent control.

-   [Components of the Context Popup](#context-popup)
-   [Implement the Context Popup](#implement-the-context-popup)
    -   [Markup](#markup)
    -   [Code](#code)
-   [Context Popup Properties](#context-popup-properties)
-   [Related topics](#related-topics)

## Components of the Context Popup

The Context Popup is a logical container for the Context Menu and Mini-Toolbar sub-controls that are exposed through the [**ContextMenu**](windowsribbon-element-contextmenu.md) and [**MiniToolbar**](windowsribbon-element-minitoolbar.md) markup elements, respectively:

-   The [**ContextMenu**](windowsribbon-element-contextmenu.md) exposes a menu of Commands and galleries.
-   The [**MiniToolbar**](windowsribbon-element-minitoolbar.md) exposes a floating toolbar of various Commands, galleries, and complex controls such as the [Font Control](windowsribbon-controls-fontcontrol.md) and the [Combo Box](windowsribbon-controls-combobox.md).

Each sub-control can appear at most once in a Context Popup.

The following screen shot illustrates the Context Popup and its constituent sub-controls.

![screen shot with callouts showing the ribbon contextual ui components.](images/controls/contextpopup.png)

The Context Popup is purely conceptual and does not expose any UI functionality itself, such as positioning or sizing.

> [!Note]  
> The Context Popup is typically displayed by right-clicking the mouse (or through the keyboard shortcut SHIFT+F10) on an object of interest. However, the steps required to display the Context Popup are defined by the application.

 

## Implement the Context Popup

In similar fashion to other Windows Ribbon framework controls, the Context Popup is implemented through a markup component that specifies its presentation details and a code component that governs its functionality.

The following table lists the controls that are supported by each Context Popup sub-control.



| Control                                                                  | Mini-Toolbar | Context Menu |
|--------------------------------------------------------------------------|--------------|--------------|
| [Button](windowsribbon-controls-button.md)                              | x            | x            |
| [Check Box](windowsribbon-controls-checkbox.md)                         | x            | x            |
| [Combo Box](windowsribbon-controls-combobox.md)                         | x            |              |
| [Drop-Down Button](windowsribbon-controls-dropdownbutton.md)            | x            | x            |
| [Drop-Down Color Picker](windowsribbon-controls-dropdowncolorpicker.md) | x            | x            |
| [Drop-Down Gallery](windowsribbon-controls-dropdowngallery.md)          | x            | x            |
| [Font Control](windowsribbon-controls-fontcontrol.md)                   | x            |              |
| [Help Button](windowsribbon-controls-helpbutton.md)                     |              |              |
| [In-Ribbon Gallery](windowsribbon-controls-inribbongallery.md)          |              |              |
| [Spinner](windowsribbon-controls-spinner.md)                            |              |              |
| [Split Button](windowsribbon-controls-splitbutton.md)                   | x            | x            |
| [Split Button Gallery](windowsribbon-controls-splitbuttongallery.md)    | x            | x            |
| [Toggle Button](windowsribbon-controls-togglebutton.md)                 | x            | x            |



 

### Markup

Each Context Popup sub-control must be declared individually in markup.

### Mini-Toolbar

When adding controls to a Context Popup Mini-Toolbar, the following two recommendations should be considered:

-   Controls should be highly recognizable and provide obvious functionality. Familiarity is key, as labels and tooltips are not exposed for Mini-Toolbar controls.
-   Each Command exposed by a control should be presented elsewhere in the ribbon UI. The Mini-Toolbar does not support keyboard navigation.

The following example demonstrates the basic markup for a [**MiniToolbar**](windowsribbon-element-minitoolbar.md) element that contains three [Button](windowsribbon-controls-button.md) controls.

> [!Note]  
> One [**MenuGroup**](windowsribbon-element-menugroup.md) element is specified for each row of controls in the Mini-Toolbar.

 


```C++
<MiniToolbar Name="MiniToolbar">
  <MenuGroup>
    <Button CommandName="cmdButton1" />
    <Button CommandName="cmdButton2" />
    <Button CommandName="cmdButton3" />
  </MenuGroup>
</MiniToolbar>
```



### Context Menu

The following example demonstrates the basic markup for a [**ContextMenu**](windowsribbon-element-contextmenu.md) element that contains three [Button](windowsribbon-controls-button.md) controls.

> [!Note]  
> Each set of controls in the [**MenuGroup**](windowsribbon-element-menugroup.md) element is separated by a horizontal bar in the Context Menu.

 


```C++
<ContextMenu Name="ContextMenu">
  <MenuGroup>
    <Button CommandName="cmdCut" />
    <Button CommandName="cmdCopy" />
    <Button CommandName="cmdPaste" />
  </MenuGroup>
</ContextMenu>
```



Although a Context Popup can contain at most one of each sub-control, multiple [**ContextMenu**](windowsribbon-element-contextmenu.md) and [**MiniToolbar**](windowsribbon-element-minitoolbar.md) element declarations in the Ribbon markup are valid. This allows an application to support various combinations of Context Menu and Mini-Toolbar controls, based on criteria defined by the application, such as workspace context.

For more information, see the [**ContextMap**](windowsribbon-element-contextmap.md) element.

The following example demonstrates the basic markup for the [**ContextPopup**](windowsribbon-element-contextpopup.md) element.


```C++
<ContextPopup>
  <ContextPopup.MiniToolbars>
    <MiniToolbar Name="MiniToolbar">
      <MenuGroup>
        <Button CommandName="cmdButton1" />
        <Button CommandName="cmdButton2" />
        <Button CommandName="cmdButton3" />
      </MenuGroup>
    </MiniToolbar>
  </ContextPopup.MiniToolbars>
  <ContextPopup.ContextMenus>
    <ContextMenu Name="ContextMenu">
      <MenuGroup>
        <Button CommandName="cmdCut" />
        <Button CommandName="cmdCopy" />
        <Button CommandName="cmdPaste" />
      </MenuGroup>
    </ContextMenu>
  </ContextPopup.ContextMenus>
  <ContextPopup.ContextMaps>
    <ContextMap CommandName="cmdContextMap" ContextMenu="ContextMenu" MiniToolbar="MiniToolbar"/>
  </ContextPopup.ContextMaps>
</ContextPopup>
```



### Code

To invoke a Context Popup, the [**IUIContextualUI::ShowAtLocation**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicontextualui-showatlocation) method is called when the top-level window of the Ribbon application receives a WM\_CONTEXTMENU notification.

This example demonstrates how to handle the WM\_CONTEXTMENU notification in the WndProc() method of the Ribbon application.


```C++
case WM_CONTEXTMENU:
  POINT pt;
  POINTSTOPOINT(pt, lParam);

  // ShowContextualUI method defined by the application.
  ShowContextualUI (pt, hWnd);
  break;
```



The following example demonstrates how a Ribbon application can show the Context Popup at a specific screen location using the [**IUIContextualUI::ShowAtLocation**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicontextualui-showatlocation) method.

GetCurrentContext() has a value of `cmdContextMap` as defined in the preceding markup example.

g\_pApplication is a reference to the [**IUIFramework**](/windows/desktop/api/uiribbon/nn-uiribbon-iuiframework) interface.


```C++
HRESULT ShowContextualUI(POINT& ptLocation, HWND hWnd)
{
  GetDisplayLocation(ptLocation, hWnd);

  HRESULT hr = E_FAIL;

  IUIContextualUI* pContextualUI = NULL;
 
  if (SUCCEEDED(g_pFramework->GetView(
                                g_pApplication->GetCurrentContext(), 
                                IID_PPV_ARGS(&pContextualUI))))
  {
    hr = pContextualUI->ShowAtLocation(ptLocation.x, ptLocation.y);
    pContextualUI->Release();
  }

  return hr;
}
```



The reference to [**IUIContextualUI**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicontextualui) can be released before the Context Popup is dismissed, as shown in the preceding example. However, the reference must be released at some point to avoid memory leaks.

> [!Caution]  
> The Mini-Toolbar has a built-in fade effect that is based on the proximity of the mouse pointer. For this reason, it is recommended that the Mini-Toolbar be displayed as close to the mouse pointer as possible. Otherwise, due to the conflicting display mechanisms, the Mini-Toolbar may not render as expected.

 

## Context Popup Properties

There are no property keys associated with the Context Popup control.

## Related topics

<dl> <dt>

[Windows Ribbon Framework Control Library](windowsribbon-controls-entry.md)
</dt> <dt>

[ContextPopup Sample](windowsribbon-contextpopupsample.md)
</dt> </dl>

 

 