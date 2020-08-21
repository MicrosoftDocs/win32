---
title: Reconfiguring the Ribbon with Application Modes
description: The Windows Ribbon framework supports the dynamic reconfiguring and exposing of core elements of the Ribbon UI at run time, based on the application's state (also referred to as context).
ms.assetid: 8e9d85c5-33e4-4212-b9e4-2fc3b492c273
keywords:
- Windows Ribbon,reconfiguring with application modes
- Ribbon,reconfiguring with application modes
- reconfiguring Windows Ribbon with application modes
ms.topic: article
ms.date: 05/31/2018
---

# Reconfiguring the Ribbon with Application Modes

The Windows Ribbon framework supports the dynamic reconfiguring and exposing of core elements of the Ribbon UI at run time, based on the application's state (also referred to as context). Declared and associated with specific elements in markup, the various states supported by an application are referred to as application modes.

-   [Introduction](#introduction)
-   [Contextual User Interface](#contextual-user-interface)
    -   [A Simple Application Mode Scenario](#a-simple-application-mode-scenario)
-   [Implementing Application Modes](#implementing-application-modes)
    -   [Identify the Modes](#identify-the-modes)
    -   [Assign Controls to Application Modes](#assign-controls-to-application-modes)
    -   [Switch Modes at Runtime](#switch-modes-at-runtime)
-   [Remarks](#remarks)
-   [Related topics](#related-topics)

## Introduction

Application modes consist of logical groups of controls that expose some core application functionality in the Ribbon UI. These modes are dynamically enabled or disabled by the application through a call to the framework method [**IUIFramework::SetModes**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setmodes), which turns the visibility of one or more application modes on or off.

## Contextual User Interface

The Ribbon framework provides rich user experience by incorporating dynamic controls that respond seamlessly to user interaction and application context. This rich contextual UI is delivered through a combination of the following mechanisms:

-   Galleries - collection-based controls that support the dynamic manipulation of their item collections.
-   Contextual tabs - ribbon tabs that have their visibility determined by a change in workspace context, such as the selection of an image in a document.
-   Application modes - core application functionality that is dependent on application context.

In some respects, application modes appear functionally similar to contextual tabs. However, the fundamental distinction lies in the intent and scope of each.

Contextual controls are activated in response to a change of context within an application. For example, in Microsoft Paint for Windows 7, a contextual tab that contains groups of text-related commands is displayed when a user inserts a text area into the workspace. This contextual tab does not contain core commands for the application and is only exposed in the UI because the context *within* the application has changed. The core functionality of the application (the image editing commands) is still relevant and available to the user, even with the contextual tab visible.

Application modes differ from contextual controls in that they reconfigure functionality in response to changes in the context that the application is operating in. Application modes sit at a higher level of abstraction; they provide a way to reconfigure the core functionality of an application instead of temporarily exposing functionality that is not a core component of the UI. For example, in Microsoft Paint for Windows 7, a switch in application mode occurs when the **Print preview** command is invoked. When Microsoft Paint switches to **Print preview**, the context that the application is operating in changes from editing to previewing. As a result, the core functionality of the application changes until the **Print preview** is canceled and the application enters the editing context again.

### A Simple Application Mode Scenario

The following scenario demonstrates how application modes are used, in an application called RibbonApp, to expose discrete aspects of core functionality.

Two application modes are defined in RibbonApp:

-   **Simple** mode exposes basic commands throughout the Ribbon UI. These commands appear at all times, no matter which application mode is active.
-   **Advanced** mode exposes complex commands intended for expert users of the application. These advanced commands appear throughout the Ribbon UI, in addition to the simple commands.

By default, RibbonApp is set to open in **Simple** mode, and the commands required by novice users are displayed in the **Application Menu** and the **Home** tab. The following screen shots show the RibbonApp **Application Menu** and **Home** tab in **Simple** mode, highlighting the modal controls.

![screen shot showing a tab for the simple application mode.](images/overviews/appmode-hometab.png)![screen shot showing the application menu for the simple application mode.](images/overviews/appmode-simpleappmenu.png)

While these commands may be sufficient for novice users, the RibbonApp also supports expert users through an **Advanced** mode that, when activated by clicking the **Switch to Advanced Mode** button in the **Application Menu**, displays additional core functionality.

This scenario is easily implemented by binding various elements in markup to discrete application modes that can be turned on and off as required. The following screen shots show the RibbonApp **Application Menu** and **Home** tab in **Advanced** mode, highlighting the modal controls.

![screen shot showing a tab for the advanced application mode.](images/overviews/appmode-advancedtab.png)![screen shot showing the application menu for the advanced application mode.](images/overviews/appmode-advancedappmenu.png)

## Implementing Application Modes

This section outlines the three steps typically required for the implementation of Ribbon framework application modes. RibbonApp is used to provide an example for each step.

### Identify the Modes

Each mode in an application should represent a logical set of functionality that depends on the context an application is able to operate in. For example, if an application displays controls that are only relevant when a network connection is detected, those controls operate within a networking context that might justify the creation of a **Network** mode.

RibbonApp has two contexts that can be active at any given time: **Simple** and **Advanced**. Therefore, RibbonApp requires two modes: **Simple** and **Advanced**.

### Assign Controls to Application Modes

Once the application modes have been identified, assign each Ribbon control to a mode by declaring an *ApplicationModes* attribute in markup for those control elements that support application modes.

The Ribbon View allows modes to be specified on the following control elements:

-   Core [**Tab**](windowsribbon-element-tab.md) elements.
-   [**Group**](windowsribbon-element-group.md) elements that are child elements of a core [**Tab**](windowsribbon-element-tab.md) element.
-   [**Button**](windowsribbon-element-button.md), [**SplitButton**](windowsribbon-element-splitbutton.md), and [**DropDownButton**](windowsribbon-element-dropdownbutton.md) elements assigned to a [**MenuGroup**](windowsribbon-element-menugroup.md) within the [Application Menu](windowsribbon-controls-applicationmenu.md).
    > [!Note]  
    > [**Button**](windowsribbon-element-button.md), [**SplitButton**](windowsribbon-element-splitbutton.md), and [**DropDownButton**](windowsribbon-element-dropdownbutton.md) elements cannot be assigned to a mode unless hosted in the [Application Menu](windowsribbon-controls-applicationmenu.md).

     

In the Ribbon framework, these control elements are referred to as modal controls. They appear only if a mode to which they are bound is active in the UI.

Control elements that are contained within a modal control inherit the application mode behavior. For example, if a [**Group**](windowsribbon-element-group.md) modal control is assigned to an **Advanced** mode and the **Advanced** mode is not active, then that **Group** and any controls in it, modal or otherwise, will not be visible in the Ribbon UI.

With the use of the *ApplicationModes* attribute, modes are assigned to modal controls in a 1:N (one-to-many) relationship, where a single modal control can be associated with several modes.

The Ribbon framework refers to modes numerically, from 0 to 31, with mode 0 considered the default mode that is automatically activated when a Ribbon application starts. Any modal control that does not specify an *ApplicationModes* attribute is considered to be a member of the default mode.

In RibbonApp, **Simple** is the default mode, with **Advanced** mode functionality displayed only when it is initiated by the user.

The following example demonstrates the markup required for RibbonApp.


```C++
<Application.Views>
  <Ribbon>

    <!--Application Menu-->
    <Ribbon.ApplicationMenu>
      <ApplicationMenu CommandName='cmdAppMenu'>                    
        <MenuGroup>
          <Button CommandName='cmdSave'/>                        
          <Button CommandName='cmdExportMetadata' ApplicationModes='1'/>                   
        </MenuGroup>              
        <MenuGroup>
          <Button CommandName='cmdSwitchModes' ApplicationModes ='0,1'/>
          <Button CommandName='cmdExit'/>
        </MenuGroup>
      </ApplicationMenu>
    </Ribbon.ApplicationMenu>
            
    <!--Tabs-->
    <Ribbon.Tabs>
      <!--Home Tab-->
      <Tab CommandName='cmdHomeTab'>
                    
        <!--Scaling Policy for Home tab-->
        <Tab.ScalingPolicy>
          <ScalingPolicy>
            <ScalingPolicy.IdealSizes>
              <Scale Group='cmdSimpleControlsGroup' Size='Medium'/>                                
            </ScalingPolicy.IdealSizes>                     
          </ScalingPolicy>
        </Tab.ScalingPolicy>     
                    
        <!--Simple Controls Group-->
        <Group CommandName='cmdSimpleControlsGroup' SizeDefinition='ThreeButtons-OneBigAndTwoSmall'>                        
          <Button CommandName="cmdPaste" />
          <Button CommandName='cmdCut'/>                        
          <Button CommandName='cmdCopy'/>                        
        </Group>
      </Tab>
                
      <!--Advanced Tab-->
      <Tab CommandName='cmdAdvancedTab' ApplicationModes='1'>
        <!--Advanced Controls Group-->
        <Group CommandName='cmdMetadataGroup' ApplicationModes='1' SizeDefinition='TwoButtons'>
          <Button CommandName='cmdEditMetadata' />
          <Button CommandName='cmdCheckErrors' />
        </Group>
      </Tab>
    </Ribbon.Tabs>                   
                             
  </Ribbon>         
</Application.Views>
```



This example demonstrates the following:

-   Default mode 0 does not need to be explicitly declared. Because modal controls that do not specify the *ApplicationModes* attribute are automatically bound to mode 0 (**Simple** mode in the RibbonApp example), there is no need to explicitly declare the attribute for default modal controls.
-   Controls can be bound to multiple modes. For RibbonApp, the only need for the *ApplicationModes* attribute in a **Simple** mode control is the `cmdSwitchModes` button , since it is a part of both **Simple** and **Advanced** modes. If either mode is active, this control will appear in the [Application Menu](windowsribbon-controls-applicationmenu.md).
-   Modal controls do not inherit from their parents. The **Advanced** tab of RibbonApp contains a **Metadata** group; both of these modal controls are assigned to mode 1 (**Advanced** mode). Assigning the **Advanced** tab to mode 1 does not automatically assign child controls, such as the **Metadata** group, to mode 1. This allows any group within a tab to be independently enabled or disabled at runtime.
-   Non-modal controls can still rely on mode switches. The **Edit Metadata** and **Check for Errors** buttons of RibbonApp are for advanced users and available only when the user switches to **Advanced** mode. Button controls that are not hosted inside the [Application Menu](windowsribbon-controls-applicationmenu.md) are non-modal; however, because these buttons are hosted inside a modal control (the **Metadata** group), they are visible when the group is visible. Therefore, these buttons appear when the advanced mode is activated and the **Metadata** group is exposed in the Ribbon UI.

### Switch Modes at Runtime

After modes are defined in markup, they can be easily enabled or disabled in response to contextual events. As mentioned previously, Ribbon applications always start in the default mode 0. After the application has initialized and mode 0 is active, the set of active modes can be changed by calling the [**IUIFramework::SetModes**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setmodes) function. This function takes a 32-bit integer as a bitwise representation of the modes that should be active; the least significant bit represents mode 0 and the most significant bit represents mode 31. If a bit is set to zero, the mode is not active in the Ribbon UI.

In RibbonApp, when a user enables **Advanced** mode, the advanced commands are displayed alongside the simple commands. The command handler for the **Switch to Advanced Mode** button calls [**IUIFramework::SetModes**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setmodes) in order to set modes 0 (**Simple**) and 1 (**Advanced**) as active in the UI. The following example is the RibbonApp code for this function call :


```C++
const int SIMPLE_MODE = 0;
const int ADVANCED_MODE = 1;
pFramework->SetModes( UI_MAKEAPPMODE(SIMPLE_MODE) | UI_MAKEAPPMODE(ADVANCED_MODE) );
```



> [!Note]  
> The Ribbon framework UI\_MAKEAPPMODE macro simplifies the task of setting these bits correctly in preparation for the call to [**IUIFramework::SetModes**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setmodes).

 

This example demonstrates the following:

-   Use the UI\_MAKEAPPMODE macro to build a mode set.
-   Modes are set explicitly and atomically. The integer value that is passed to [**IUIFramework::SetModes**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setmodes) represents the modes that will be active after the function returns. Although the **Simple** mode was previously active, **IUIFramework::SetModes** must indicate that the **Simple** mode remain active when the **Advanced** mode is activated.
-   The default mode can be removed. Although in RibbonApp the default mode (mode 0) is never removed, it can be removed with the following call: `g_pFramework->SetModes(UI_MAKEAPPMODE(ADVANCED_MODE))`, exposing only the advanced commands in the UI.

> [!Note]  
> When the modes of an application are reconfigured, the Ribbon will attempt to preserve the previously selected tab in the UI. If the new set of modes no longer contains the tab that was selected before the call, the Ribbon will select the tab in its layout that is closest to the [Application Menu](windowsribbon-controls-applicationmenu.md). This tab is meant to contain the commands that are most relevant to the user. For more information, see [Ribbon User Experience Guidelines](https://msdn.microsoft.com/library/cc872782.aspx).

 

## Remarks

The Ribbon must have at least one active mode at all times. If an application attempts to deactivate all modes by calling [**IUIFramework::SetModes**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setmodes) with a mode value of 0, E\_FAIL is returned and the active mode set remains unchanged.

The framework requires that at least one tab exist in the Ribbon UI at all times. As a result, there must be at least one tab exposed by the default mode (mode 0) and after each mode switch.

Not all areas of the Ribbon UI are affected by application modes. For example, if disabling a mode causes the disappearance of buttons from the Ribbon that were previously added to the [Quick Access Toolbar](windowsribbon-controls-quickaccesstoolbar.md), those buttons remain in the Quick Access Toolbar, allowing users to execute the Commands bound to the buttons. As a general rule, if a Command belongs to one or more inactive modes, then that Command should also be disabled by setting the [UI\_PKEY\_Enabled](windowsribbon-reference-properties-uipkey-enabled.md) property to 0 (VARIANT\_FALSE) .

## Related topics

<dl> <dt>

[Ribbon User Experience Guidelines](https://msdn.microsoft.com/library/cc872782.aspx)
</dt> <dt>

[Displaying Contextual Tabs](ribbon-contextualtabs.md)
</dt> </dl>

 

 