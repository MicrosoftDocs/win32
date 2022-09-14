---
title: Menu Group
description: The Menu Group organizes related Commands and controls within a menu or toolbar.
ms.assetid: 5454f2a3-275b-47f4-ae97-d10dd12da5ff
ms.topic: article
ms.date: 05/31/2018
---

# Menu Group

The Menu Group organizes related Commands and controls within a menu or toolbar.

-   [Introduction](#introduction)
-   [Menu Group Properties](#menu-group-properties)
-   [Related topics](#related-topics)

## Introduction

The Menu Group control, exposed through the [**MenuGroup**](windowsribbon-element-menugroup.md) markup element, is a logical container for groups of items or Commands in menu-based controls, including the [Context Popup](windowsribbon-controls-contextpopup.md) Mini-Toolbar.

A label can be specified for a Menu Group through the *LabelTitle* attribute or [**Command.LabelTitle**](windowsribbon-element-command-labeltitle.md) property of an associated Command declaration. The value assigned to *LabelTitle* is rendered as a category header.

The following example demonstrates the Command markup for a [Split Button](windowsribbon-controls-splitbutton.md) control that includes two Menu Group Command declarations.


```XML
<!-- SplitButton -->
<Command Name="cmdSplitButtonGroup"
         Symbol="cmdSplitButtonGroup"
         Comment="SplitButton Group"
         LabelTitle="SplitButton"/>
<Command Name="cmdSplitButton"
         Symbol="cmdSplitButton"
         Comment="SplitButton"
         LabelTitle="SplitButton"/>
<Command Name="cmdSBButtonItem"
         Symbol="cmdSBButtonItem"
         Comment="SBButtonItem"
         LabelTitle="SB ButtonItem"/>
<Command Name="cmdSBButton1"
         Symbol="cmdSBButton1"
         Comment="SBButton1"
         LabelTitle="SB Button">
  <Command.LargeImages>
    <Image Source="res/copyL_32.bmp"/>
  </Command.LargeImages>
  <Command.SmallImages>
    <Image Source="res/copyS_16.bmp"/>
  </Command.SmallImages>
  <Command.LargeHighContrastImages>
    <Image Source="res/copyLHC_32.bmp"/>
  </Command.LargeHighContrastImages>
  <Command.SmallHighContrastImages>
    <Image Source="res/copySHC_16.bmp"/>
  </Command.SmallHighContrastImages>
</Command>
<Command Name="cmdSBMajorItems"
         Comment="Major Items Category"
         LabelTitle="Major Items"/>
<Command Name="cmdSBStandardItems"
         Comment="Standard Items Category"
         LabelTitle="Standard Items"/>
```



The following example demonstrates the markup required for a [**SplitButton**](windowsribbon-element-splitbutton.md) element with three [**MenuGroup**](windowsribbon-element-menugroup.md) element declarations, two of which are associated with the Menu Group Commands from the previous example. The *Class* attribute of the **MenuGroup** element is used to specify the size of the menu items.


```XML
<Group CommandName="cmdSplitButtonGroup">
  <SplitButton CommandName="cmdSplitButton">
    <SplitButton.ButtonItem>
      <Button CommandName="cmdSBButtonItem"/>
    </SplitButton.ButtonItem>
    <SplitButton.MenuGroups>
      <MenuGroup CommandName="cmdSBMajorItems" 
                 Class="MajorItems">
        <Button CommandName="cmdSBButton1"/>
        <Button CommandName="cmdSBButton1"/>
      </MenuGroup>
      <MenuGroup CommandName="cmdSBStandardItems"
                 Class="StandardItems">
        <Button CommandName="cmdSBButton1"/>
        <Button CommandName="cmdSBButton1"/>
      </MenuGroup>
      <MenuGroup Class="StandardItems">
        <Button CommandName="cmdSBButton1"/>
        <Button CommandName="cmdSBButton1"/>
      </MenuGroup>
    </SplitButton.MenuGroups>
  </SplitButton>
</Group>
```



The following screen shot illustrates the menu (with three Menu Group controls) that is generated from the markup in the previous examples.

![screen shot of a menu with three menu group controls.](images/controls/menugroup.png)

## Menu Group Properties

The Ribbon framework defines a collection of [property keys](windowsribbon-reference-properties.md) for the Menu Group control.

Typically, a Menu Group property is updated in the ribbon UI by invalidating the Command associated with the control through a call to the [**IUIFramework::InvalidateUICommand**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand) method. The invalidation event is handled, and the property updates defined, by the [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method.

The [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method is not executed, and the application queried for an updated property value, until the property is required by the framework. For example, when a tab is activated and a control revealed in the ribbon UI, or when a tooltip is displayed.

> [!Note]  
> In some cases, a property can be retrieved through the [**IUIFramework::GetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty) method and set with the [**IUIFramework::SetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty) method.

 

The following table lists the property keys that are associated with the Menu Group control.



| Property Key                                                                                     | Notes                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UI\_PKEY\_Enabled](windowsribbon-reference-properties-uipkey-enabled.md)                       | Supports [**IUIFramework::GetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty) and [**IUIFramework::SetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty). |
| [UI\_PKEY\_Keytip](windowsribbon-reference-properties-uipkey-keytip.md)                         | Can only be updated through invalidation.                                                                                                                                                                                     |
| [UI\_PKEY\_Label](windowsribbon-reference-properties-uipkey-label.md)                           | Can only be updated through invalidation.                                                                                                                                                                                     |
| [UI\_PKEY\_TooltipDescription](windowsribbon-reference-properties-uipkey-tooltipdescription.md) | Can only be updated through invalidation.                                                                                                                                                                                     |
| [UI\_PKEY\_TooltipTitle](windowsribbon-reference-properties-uipkey-tooltiptitle.md)             | Can only be updated through invalidation.                                                                                                                                                                                     |



 

## Related topics

<dl> <dt>

[Windows Ribbon Framework Control Library](windowsribbon-controls-entry.md)
</dt> <dt>

[**MenuGroup markup element**](windowsribbon-element-menugroup.md)
</dt> </dl>

 

 