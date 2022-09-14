---
title: Quick Access Toolbar
description: The Quick Access Toolbar (QAT) is a small, customizable toolbar that exposes a set of Commands that are specified by the application or selected by the user.
ms.assetid: b2adf4e9-0de1-4c4d-9293-693d0f7cf6fe
ms.topic: article
ms.date: 05/31/2018
---

# Quick Access Toolbar

The Quick Access Toolbar (QAT) is a small, customizable toolbar that exposes a set of Commands that are specified by the application or selected by the user.

- [Introduction](#introduction)
- [Implement the Quick Access Toolbar](#implement-the-quick-access-toolbar)
  - [Markup](#markup)
  - [Code](#code)
- [QAT Persistence](#qat-persistence)
- [Quick Access Toolbar Properties](#quick-access-toolbar-properties)
- [Related topics](#related-topics)

## Introduction

By default, the Quick Access Toolbar (QAT) is located in the title bar of the application window but can be configured to display below the ribbon. In addition to exposing Commands, the Quick Access Toolbar (QAT) also includes a customizable drop-down menu that contains the complete set of default Quick Access Toolbar (QAT) Commands (whether hidden or displayed in the Quick Access Toolbar (QAT)) and a set of Quick Access Toolbar (QAT) and ribbon options.

The following screen shot shows an example of the Ribbon Quick Access Toolbar (QAT).

![screen shot of the qat in the microsoft paint ribbon.](images/markup/qat-and-menu.png)

The Quick Access Toolbar (QAT) consists of a combination of up to 20 Commands either specified by the application (known as the application defaults list) or selected by the user. The Quick Access Toolbar (QAT) can contain unique Commands that are not available elsewhere in the ribbon UI.

> [!Note]
> While almost all ribbon controls allow their associated Command to be added to the Quick Access Toolbar (QAT) through the context menu shown in the following screen shot, Commands exposed in a [Context Popup](windowsribbon-controls-contextpopup.md) do not provide this context menu.
>
> ![screen shot of the command context menu in the microsoft paint ribbon.](images/controls/qat-contextmenu-add.png) 

## Implement the Quick Access Toolbar

As with all Windows Ribbon framework controls, taking full advantage of the Quick Access Toolbar (QAT) requires both a markup component that controls its presentation within the ribbon and a code component that governs its functionality.

### Markup

The Quick Access Toolbar (QAT) control is declared, and associated with a Command ID, in markup through the [QuickAccessToolbar](windowsribbon-element-quickaccesstoolbar.md) element. The Command ID is used to identify and bind the Quick Access Toolbar (QAT) to a Command handler defined by the application.

In addition to the basic Command handler for primary Quick Access Toolbar (QAT) functionality, declaring the optional *CustomizeCommandName* [QuickAccessToolbar](windowsribbon-element-quickaccesstoolbar.md) element attribute causes the framework to add a **More Commands** item to the Command list of the Quick Access Toolbar (QAT) drop-down menu that requires a secondary Command handler be defined.

For consistency across Ribbon applications, it is recommended that the *CustomizeCommandName* Command handler launch a Quick Access Toolbar (QAT) customization dialog. Because the Ribbon framework only provides the launching point in the UI, the application is solely responsible for providing the customization dialog implementation when the callback notification for this Command is received.

The following screen shot shows a Quick Access Toolbar (QAT) drop-down menu with the **More Commands** Command item.

![screen shot of a qat menu with the more commands... command item.](images/markup/qat-customizecommandname.png)

The application defaults list for the Quick Access Toolbar (QAT) is specified through the [QuickAccessToolbar.ApplicationDefaults](windowsribbon-element-quickaccesstoolbar-applicationdefaults.md) property which identifies a default list of recommended Commands, all of which are listed in the Quick Access Toolbar (QAT) drop-down menu.

To display Commands from the application defaults list in the Quick Access Toolbar (QAT) toolbar, the *ApplicationDefaults.IsChecked* attribute of each control element must have a value of `true`. The preceding images show the results of setting this attribute to `true` for the **Save**, **Undo**, and **Redo** Commands.

[QuickAccessToolbar.ApplicationDefaults](windowsribbon-element-quickaccesstoolbar-applicationdefaults.md) supports three types of Ribbon controls: [Button](windowsribbon-controls-button.md), [Toggle Button](windowsribbon-controls-togglebutton.md), and [Check Box](windowsribbon-controls-checkbox.md).

> [!Note]
> Windows 8 and newer: All gallery-based controls are supported ([ComboBox](windowsribbon-element-combobox.md), [InRibbonGallery](windowsribbon-element-inribbongallery.md), [SplitButtonGallery](windowsribbon-element-splitbuttongallery.md), and [DropDownGallery](windowsribbon-element-dropdowngallery.md)).
>
> Items in a gallery control can support highlighting on hover. To support hover highlighting, the gallery must be an items gallery and use a [FlowMenuLayout](windowsribbon-element-flowmenulayout.md) of type [VerticalMenuLayout](windowsribbon-element-verticalmenulayout.md).

The following example demonstrates the basic markup for a [QuickAccessToolbar](windowsribbon-element-quickaccesstoolbar.md) element.

This section of code shows the Command declarations for a [Quick Access Toolbar (QAT)](windowsribbon-element-quickaccesstoolbar.md) element.

```XML
<Command Name="cmdQAT"
         Symbol="ID_QAT"
         Id="40000"/>
<Command Name="cmdCustomizeQAT"
         Symbol="ID_CUSTOM_QAT"
         Id="40001"/>
```

This section of code shows the control declarations for a [Quick Access Toolbar (QAT)](windowsribbon-element-quickaccesstoolbar.md) element.

```XML
      <Ribbon.QuickAccessToolbar>
        <QuickAccessToolbar CommandName="cmdQAT"
                            CustomizeCommandName="cmdCustomizeQAT">
          <QuickAccessToolbar.ApplicationDefaults>
            <Button CommandName="cmdButton1"/>
            <ToggleButton CommandName="cmdMinimize"
                          ApplicationDefaults.IsChecked="false"/>
          </QuickAccessToolbar.ApplicationDefaults>
        </QuickAccessToolbar>
      </Ribbon.QuickAccessToolbar>
```

### Code

The Ribbon framework application must provide a Command handler callback method to manipulate the Quick Access Toolbar (QAT). This handler works in a similar fashion to Command gallery handlers, except that the Quick Access Toolbar (QAT) does not support categories. For more information, see [Working with Galleries](ribbon-controls-galleries.md).

The Quick Access Toolbar (QAT) Command collection is retrieved as an [IUICollection](/windows/desktop/api/uiribbon/nn-uiribbon-iuicollection) object through the [UI\_PKEY\_ItemsSource](windowsribbon-reference-properties-uipkey-itemssource.md) property key. Adding Commands to the Quick Access Toolbar (QAT) at run time is accomplished by adding an [IUISimplePropertySet](/windows/desktop/api/uiribbon/nn-uiribbon-iuisimplepropertyset) object to the **IUICollection**.

Unlike Command galleries, a command type property ([UI\_PKEY\_CommandType](windowsribbon-reference-properties-uipkey-commandtype.md)) is not required for the Quick Access Toolbar (QAT) [IUISimplePropertySet](/windows/desktop/api/uiribbon/nn-uiribbon-iuisimplepropertyset) object. However, the Command must exist in the ribbon or Quick Access Toolbar (QAT) application defaults list; a new Command cannot be created at run time and added to the Quick Access Toolbar (QAT).

> [!Note]  
> The Ribbon application cannot replace the Quick Access Toolbar (QAT) [IUICollection](/windows/desktop/api/uiribbon/nn-uiribbon-iuicollection) with a custom collection object derived from IEnumUnknown.

The following example demonstrates a basic Quick Access Toolbar (QAT) Command handler implementation.

```C++
/* QAT COMMAND HANDLER IMPLEMENTATION */
class CQATCommandHandler
      : public CComObjectRootEx<CComMultiThreadModel>
      , public IUICommandHandler
{
  public:
    BEGIN_COM_MAP(CQATCommandHandler)
      COM_INTERFACE_ENTRY(IUICommandHandler)
    END_COM_MAP()

    // QAT command handler's Execute method
    STDMETHODIMP Execute(UINT nCmdID,
                         UI_EXECUTIONVERB verb, 
                         const PROPERTYKEY* key,
                         const PROPVARIANT* ppropvarValue,
                         IUISimplePropertySet* pCommandExecutionProperties)
    {
      UNREFERENCED_PARAMETER(nCmdID);
      UNREFERENCED_PARAMETER(verb);
      UNREFERENCED_PARAMETER(ppropvarValue);
      UNREFERENCED_PARAMETER(pCommandExecutionProperties);

      // Do not expect Execute callback for a QAT command
      return E_NOTIMPL;
    }

    // QAT command handler's UpdateProperty method
    STDMETHODIMP UpdateProperty(UINT nCmdID,
                                REFPROPERTYKEY key,
                                const PROPVARIANT* ppropvarCurrentValue,
                                PROPVARIANT* ppropvarNewValue)
    {
      UNREFERENCED_PARAMETER(nCmdID);
      UNREFERENCED_PARAMETER(ppropvarNewValue);

      HRESULT hr = E_NOTIMPL;

      if (key == UI_PKEY_ItemsSource)
      {
        ATLASSERT(ppropvarCurrentValue->vt == VT_UNKNOWN);

        CComQIPtr<IUICollection> spCollection(ppropvarCurrentValue->punkVal);

        UINT nCount;
        if (SUCCEEDED(hr = spCollection->GetCount(&nCount)))
        {
          if (nCount == 0)
          {
            // If the current Qat list is empty, then we will add a few items here.
            UINT commands[] =  { cmdSave, cmdUndo};

            int count = _countof(commands);

            for (int i = 0; i < count; i++)
            {
              PROPERTYKEY keys[1] = {UI_PKEY_CommandId};
              CComObject<CItemProperties> *pItem = NULL;
              if (SUCCEEDED(CComObject<CItemProperties>::CreateInstance(&pItem)))
              {
                PROPVARIANT vars[1];

                InitPropVariantFromUInt32(commands[i], &vars[0]);

                pItem->Initialize(NULL, _countof(vars), keys, vars);

                CComPtr<IUnknown> spUnknown;
                pItem->QueryInterface(&spUnknown);
                spCollection->Add(spUnknown);
                            
                FreePropVariantArray(_countof(vars), vars);
              }
            }
          }
          else
          {
            // Do nothing if the Qat list is not empty.
            // Return S_FALSE to indicate the callback succeeded.
            return S_FALSE; 
          }
        }
      }
    return hr;
  }
};
```

## QAT Persistence

Quick Access Toolbar (QAT) Command items and settings can be persisted across application sessions using the [IUIRibbon::SaveSettingsToStream](/windows/desktop/api/uiribbon/nf-uiribbon-iuiribbon-savesettingstostream) and [IUIRibbon::LoadSettingsFromStream](/windows/desktop/api/uiribbon/nf-uiribbon-iuiribbon-loadsettingsfromstream) functions. For more information, see [Persisting Ribbon State](ribbon-statepersistence.md).

## Quick Access Toolbar Properties

The Ribbon framework defines a collection of [property keys](windowsribbon-reference-properties.md) for the Quick Access Toolbar (QAT) control.

Typically, a Quick Access Toolbar (QAT) property is updated in the ribbon UI by invalidating the Command associated with the control through a call to the [IUIFramework::InvalidateUICommand](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand) method. The invalidation event is handled, and the property updates defined, by the [IUICommandHandler::UpdateProperty](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method.

The [IUICommandHandler::UpdateProperty](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method is not executed, and the application queried for an updated property value, until the property is required by the framework. For example, when a tab is activated and a control revealed in the ribbon UI, or when a tooltip is displayed.

> [!Note]  
> In some cases, a property can be retrieved through the [IUIFramework::GetUICommandProperty](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty) method and set with the [IUIFramework::SetUICommandProperty](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty) method.

The following table lists the property keys that are associated with the Quick Access Toolbar (QAT) control.

| Property Key | Notes |
|---|---|
| [UI\_PKEY\_ItemsSource](windowsribbon-reference-properties-uipkey-itemssource.md) | Supports [IUIFramework::GetUICommandProperty](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty) (does not support [IUIFramework::SetUICommandProperty](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty)).[IUIFramework::GetUICommandProperty](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty) returns a pointer to an IUICollection object that represents the commands in the QAT. Each Command is identified by its Command ID, which is obtained by calling the [IUISimplePropertySet::GetValue](/windows/desktop/api/uiribbon/nf-uiribbon-iuisimplepropertyset-getvalue) method and passing in the property key [UI\_PKEY\_CommandId](windowsribbon-reference-properties-uipkey-commandid.md). |

There are no property keys associated with the **More Commands** Command item of the Quick Access Toolbar (QAT) drop-down menu

## Related topics

- [Windows Ribbon Framework Control Library](windowsribbon-controls-entry.md)
- [QuickAccessToolbar markup element](windowsribbon-element-quickaccesstoolbar.md)