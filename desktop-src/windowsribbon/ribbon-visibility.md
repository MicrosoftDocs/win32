---
title: Displaying the Ribbon
description: The Windows Ribbon framework exposes a set of properties that allow an application to specify how the Ribbon UI is displayed at run time.
ms.assetid: c6716183-ef32-4fb2-812a-2d8f27448db5
keywords:
- Windows Ribbon,customizing colors
- Ribbon,customizing colors
- customizing Windows Ribbon colors
ms.topic: article
ms.date: 05/31/2018
---

# Displaying the Ribbon

The Windows Ribbon framework exposes a set of properties that allow an application to specify how the Ribbon UI is displayed at run time.

-   [Introduction](#introduction)
-   [Minimize the Ribbon](#minimize-the-ribbon)
-   [Hide the Ribbon](#hide-the-ribbon)
-   [Example](#example)
-   [Related topics](#related-topics)

## Introduction

To maximize the area available for the document space (or view port) of a Ribbon framework application, an application can specify whether the ribbon UI is visible or hidden and, when visible, whether the ribbon is in an expanded or collapsed state.

The [framework property keys](windowsribbon-reference-properties-framework.md) listed in the following table are used to explicitly set the display characteristics of the ribbon UI in a Ribbon framework application. These properties have no effect on the display of the [Context Popup](windowsribbon-controls-contextpopup.md) control.



| Display State         | Ribbon Property Key                                                            |
|-----------------------|--------------------------------------------------------------------------------|
| Expanded or collapsed | [UI\_PKEY\_Minimized](windowsribbon-reference-properties-uipkey-minimized.md) |
| Visible or hidden     | [UI\_PKEY\_Viewable](windowsribbon-reference-properties-uipkey-viewable.md)   |



 

## Minimize the Ribbon

A Ribbon framework application can dynamically set the minimized state of the ribbon command bar by setting the value of the [UI\_PKEY\_Minimized](windowsribbon-reference-properties-uipkey-minimized.md) property key to **true** or **false**.



| Display State | Property Key Value |
|---------------|--------------------|
| Expanded      | **false**          |
| Collapsed     | **true**           |



 

When the ribbon UI is in a minimized state, the ribbon Tab row remains visible and fully functional.

The following screen shot shows the ribbon in the minimized state.

![screen shot showing the ribbon ui minimized.](images/overviews/ribbon-minimized.png)

> [!Note]  
> The Ribbon framework exposes this functionality to the end user through the "Minimize the Ribbon" selection of the ribbon context menu.

 

## Hide the Ribbon

A Ribbon framework application can dynamically set the viewable state of the ribbon command bar by setting the value of the [UI\_PKEY\_Viewable](windowsribbon-reference-properties-uipkey-viewable.md) property key to **true** or **false**.



| Display State | Property Key Value |
|---------------|--------------------|
| Visible       | **false**          |
| Hidden        | **true**           |



 

In contrast to the [UI\_PKEY\_Minimized](windowsribbon-reference-properties-uipkey-minimized.md) property, setting [UI\_PKEY\_Viewable](windowsribbon-reference-properties-uipkey-viewable.md) to **false** renders the ribbon UI invisible and completely unusable to an end user.

The following screen shot shows the ribbon in the hidden state.

![screen shot showing the ribbon ui hidden.](images/overviews/ribbon-viewable.png)

## Example

The following example demonstrates how to set the state of the ribbon UI at run time.

In this case, the [**IUICommandHandler::Execute**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-execute) function is used to expand or collapse the ribbon UI based on the toggle state of a [Toggle Button](windowsribbon-controls-togglebutton.md).


```C++
//
//  FUNCTION: Execute()
//
//  PURPOSE: Called by the Ribbon framework when a Command is executed 
//           by the user. 
//           This example demonstrates a handler for a Toggle Button
//           that sets the minimized state of the ribbon UI.
//
//  NOTES: g_pFramework is a global pointer to an IUIFramework object 
//         that is assigned when the Ribbon framework is initialized.
//
//         g_pRibbon is a global pointer to the IUIRibbon object
//         that is assigned when the Ribbon framework is initialized.
//
STDMETHODIMP CCommandHandler::Execute(
    UINT nCmdID,
    UI_EXECUTIONVERB verb,
    __in_opt const PROPERTYKEY* key,
    __in_opt const PROPVARIANT* ppropvarValue,
    __in_opt IUISimplePropertySet* pCommandExecutionProperties)
{
    HRESULT hr = E_FAIL;

    if (verb == UI_EXECUTIONVERB_EXECUTE)
    {
        switch (nCmdID)
        {
            // Minimize ribbon Command handler.
            case IDR_CMD_MINIMIZE:
                if (g_pFramework)
                {
                    IPropertyStore *pPropertyStore = NULL;
                    hr = g_pRibbon->QueryInterface(__uuidof(IPropertyStore), 
                                                   (void**)&pPropertyStore);
                    if (SUCCEEDED(hr))
                    {
                        if (ppropvarValue != NULL)
                        {
                            // Is the ToggleButton state on or off?
                            BOOL fToggled;
                            hr = UIPropertyToBoolean(*key, *ppropvarValue, &fToggled);

                            if (SUCCEEDED(hr))
                            {
                                // Set the ribbon display state based on the toggle state.
                                PROPVARIANT propvar;
                                PropVariantInit(&propvar);
                                UIInitPropertyFromBoolean(UI_PKEY_Minimized, 
                                                          fToggled, 
                                                          &propvar);
                                hr = pPropertyStore->SetValue(UI_PKEY_Minimized, 
                                                              propvar);
                                pPropertyStore->Commit();
                            }
                            pPropertyStore->Release();
                        }
                    }
                }
                break;
        }
    }
    return hr;
}
```



## Related topics

<dl> <dt>

[Ribbon Properties](windowsribbon-reference-properties-ribbon.md)
</dt> </dl>

 

 