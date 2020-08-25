---
title: Implementing a User Interface
description: This section describes some of the tasks associated with implementing a user interface for a Windows application.
ms.assetid: 889791a7-d12c-4ec6-9b04-8fed14ecdb2c
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a User Interface

This section describes some of the tasks associated with implementing a user interface for a Windows application.

-   [Prototype](#prototype)
-   [Construct](#construct)
-   [Simplify](#simplify)
    -   [Reduce, Reuse, Declutter](#reduce-reuse-declutter)
    -   [The Best UI Is No UI](#the-best-ui-is-no-ui)
    -   [Less UI Is Better UI](#less-ui-is-better-ui)
    -   [Consistent UI is Good UI](#consistent-ui-is-good-ui)

## Prototype

User interfaces (UI) should be designed from the list of user scenarios and requirements that were identified in the user analysis step.

Prototypes can be as simple as pencil sketches or as complex as interactive screen mockups. Keep all previous work as it can be useful when showing stakeholders the alternatives that were considered and explaining why they were discarded.

Try to limit this step to two or three prototypes at most. Prototypes do not have to be exhaustive; they just have to effectively simulate the experience of using the real application.

Demonstrate the prototypes and track user feedback to help identify the general usability trends. If it is possible, discard the least successful prototypes and incorporate as much useful feedback as possible into one or more of the remaining prototypes. Repeat this process as time and resources allow.

There are various prototyping tools available including [SketchFlow](/previous-versions/visualstudio/design-tools/expression-studio-3/ee341458(v=expression.30)) in Microsoft Expression Studio 3, the layout editor in Microsoft Visual Studio, and even Microsoft Paint.

## Construct

When you implement the user interface for an application, consider the following:

-   Command structure

    Determine whether to implement a traditional command structure based on menus and toolbars, or an alternative command structure based on the Windows Ribbon Framework. For more information, see [Menus](../menurc/menus.md), [Toolbars](../controls/toolbar-control-reference.md), and [Windows Ribbon Framework](../windowsribbon/-uiplat-windowsribbon-entry.md).

-   Windows and dialog boxes

    Based on the UI design and prototyping work, implement the application windows, including the main window, child windows, dialog boxes, and message boxes. Follow the UX Guidelines to determine which styles and controls to use in the windows and dialog boxes. For more information, see [Windows](../winmsg/windows.md), [Dialog Boxes](../dlgbox/dialog-boxes.md), and [Windows Controls](../controls/window-controls.md).

-   Custom controls

    Create new custom controls only if you cannot get the functionality that you want from one of the standard Windows controls. New custom controls are very costly to develop and require additional work to make them accessible. If your application requires custom controls, make sure that they are adequately exposed to assistive technologies. For more information, see [Custom Controls](../controls/user-controls-intro.md) and [Windows Automation API](../winauto/windows-automation-api-portal.md).

-   Support for standard user input devices

    Most Windows applications need to support user input through the keyboard and mouse. The ability to navigate and access all application functionality through the keyboard alone is especially important for users who are vision-impaired or have mobility issues. For more information, see [User Input](../inputdev/user-input.md) and the [Engineering Software for Accessibility eBook](https://www.microsoft.com/download/details.aspx?id=19262).

-   Visual styles, animations, and visual effects

    Windows includes several technologies that you can use to add visual interest and set the UI apart from that of other applications. These include specifying the visual styles of controls, adding animations to UI elements, and implementing various visual effects in the UI. For more information, see [Visual Styles](../controls/themes-overview.md), [Windows Animation Manager](../uianimation/-main-portal.md), and [Desktop Window Manager](../dwm/dwm-overview.md).

## Simplify

A successful user experience depends on the approach, perspective, and assumptions of the developer during the design process. Achieving a basic understanding of how an application may be used by the target audience requires the ability to think broadly, beyond the constraints of what suits the needs of the developer. Investing this time, effort, and research at the beginning of a project will pay dividends at the end.

### Reduce, Reuse, Declutter

Features only improve a product if they are actually used. In many cases, the proliferation of features may introduce complexity with the addition of more icons, menu items, toolbars, and dialog boxes interfering with efficiency and productivity rather than adding value.

### The Best UI Is No UI

UI implies that the user has to interact with the application to make something happen. In the ideal case, no interaction is necessary. From the user's perspective, it just works. If a feature can be added that safely removes a user interaction, it makes the user experience significantly better.

### Less UI Is Better UI

In many cases, it is not possible to remove UI interaction completely from the user experience. However, the less user interaction required by an application the better.

Identify the most common and essential activities that users will perform with the application and make those functions the most prominent in the UI. Relegate other functions and activities to lesser status either visually, hierarchically, or through optional application settings and user preferences.

-   Replace Rather Than Add

    The conservation of UI rule states that you add something only when you can take something away. This rule forces a developer to think critically about a new feature by considering the impact that the feature has on the whole user experience.

    New features should not be promoted because they are new: do not confuse marketing with usability. To help users find new features in your product, add an item to the **Help** menu that describes the changes that have occurred since the last version of the application.

-   The User is a Limited Resource

    The more functionality that is exposed at any one time, the more difficult it is for a user to find the functionality that they need.

-   It's Rude to Interrupt

    When an application displays a dialog box, it forces the user to stop whatever it is that they are doing and pay attention to something else. If it is possible, remove the need for a dialog box completely by avoiding error cases and other disruptive user experiences. For more information about message guidelines, see [Messages](https://msdn.microsoft.com/library/dd535525.aspx).

-   Simple Can Be Powerful

    A simple UI does not imply a lack of functionality. Typically, the result of a simpler UI is a shortened learning curve, increased efficiency, and improved productivity. This empowers a user to increase their proficiency with the application.

### Consistent UI is Good UI

Generally, it is recommended to strive for consistency throughout an application UI. Providing a consistent UI enables a user to become more proficient with an application in a much shorter time. They are able to apply their existing knowledge of the application to different situations and use unfamiliar functionality with confidence.

In rare cases, consistency provides no benefit to the user and can even degrade the user experience. Do not make the UI consistent if that consistency impairs the ability to accomplish a task. Consistency in itself does not guarantee usability. It is a mistake to think that consistency in the interface will lead to good design.

For example, video game UI is typically very specific to the kind of game. Trying to design a generic UI that works well for two specialized games, one that requires a steering wheel and another that works best with a joystick and buttons, is likely not going to be successful for either game. At best a middle ground is likely to be achieved that is not good for either.

Having good data about how things are used is the key to making this decision. Be clear about the pros and cons of each tradeoff (speed versus reliability, ease of learning versus expert proficiency, global consistency versus local optimization) and make the best decisions for the feature in relation to the whole product.

Design is choosing how to fail: optimizing for one thing means failing at another. The key to good UI design is being able to decide which characteristics of the application are the most important, and which ones can be cut.

 

 