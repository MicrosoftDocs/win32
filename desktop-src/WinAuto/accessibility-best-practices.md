---
title: Accessibility Best Practices
description: Implementing the best practices described in this section helps ensure that your application is accessible to people who use assistive technology products.
ms.assetid: ef694361-49b7-424c-a583-1eadc2519db7
ms.topic: article
ms.date: 05/31/2018
---

# Accessibility Best Practices

Implementing the best practices described in this section helps ensure that your application is accessible to people who use assistive technology products. Many of these best practices focus on good UI design. Each best practice includes implementation information for controls or applications. In many cases, much of the work to meet these best practices is already included in the controls.

This topic contains the following sections.

-   [Programmatic Access](#programmatic-access)
    -   [Enable Programmatic Access to all UI Elements and Text](#enable-programmatic-access-to-all-ui-elements-and-text)
    -   [Place Names, Titles, and Descriptions on UI Objects, Frames, and Pages](#place-names-titles-and-descriptions-on-ui-objects-frames-and-pages)
    -   [Ensure Programmatic Events Are Triggered by All UI Activities](#ensure-programmatic-events-are-triggered-by-all-ui-activities)
-   [User Settings](#user-settings)
    -   [Respect All System-Wide Settings and Do Not Interfere with Accessibility Functions](#respect-all-system-wide-settings-and-do-not-interfere-with-accessibility-functions)
-   [Visual UI Design](#visual-ui-design)
    -   [Do Not Hard-Code Colors](#do-not-hard-code-colors)
    -   [Support High Contrast and all System Display Attributes](#support-high-contrast-and-all-system-display-attributes)
    -   [Ensure All UI Correctly Scales by Any DPI Setting](#ensure-all-ui-correctly-scales-by-any-dpi-setting)
-   [Keyboard Navigation](#keyboard-navigation)
    -   [Provide Keyboard Interface for All UI Elements](#provide-keyboard-interface-for-all-ui-elements)
    -   [Show the Keyboard Focus](#show-the-keyboard-focus)
    -   [Support Navigation Standards and Powerful Navigation Schemes](#support-navigation-standards-and-powerful-navigation-schemes)
    -   [Do Not Let Mouse Location Interfere with Keyboard Navigation](#do-not-let-mouse-location-interfere-with-keyboard-navigation)
-   [Multi-modal Interface](#multi-modal-interface)
    -   [Provide User-Selectable Equivalents for Non-Text Elements](#provide-user-selectable-equivalents-for-non-text-elements)
    -   [Use Color but Also Provide Alternatives to Color](#use-color-but-also-provide-alternatives-to-color)
    -   [Use Standard Input APIs with Device-Independent Calls](#use-standard-input-apis-with-device-independent-calls)
-   [Related topics](#related-topics)

## Programmatic Access

The best practices in this section enure that assistive technology products have adequate programmatic access to UI information and functionality.

### Enable Programmatic Access to all UI Elements and Text

The UI elements of your application must be programmatically accessible to assistive technology products. All UI elements must have labels, they must expose all property values, and they must raise all appropriate events. For the standard Windows controls, most of this work is already done through the Microsoft UI Automation and Microsoft Active Accessibility proxy objects. Custom controls, however, require additional work to ensure that they are fully exposed so that assistive technology vendors can identify and manipulate elements of your application UI.

Following this best practice allows assistive technology vendors to identify and manipulate elements of your product's UI.

### Place Names, Titles, and Descriptions on UI Objects, Frames, and Pages

Because assistive technology products—especially screen readers—use titles to understand the location of a frame, object, or page in the navigation scheme, the titles must be very descriptive. Good descriptive titles enable assistive technology products to identify and manipulate UI elements in controls and applications. For example, a webpage title of "Microsoft Web Page" is useless if the user has navigated deeply into a particular area. A descriptive title is crucial for users who are blind and depend on screen readers.

Following this best practice allows assistive technology products to identify and manipulate UI in sample controls and applications.

### Ensure Programmatic Events Are Triggered by All UI Activities

Your application should raise events whenever changes occur in the state or appearance of a UI element.

Following this best practice allows assistive technology products to listen for changes in the UI and notify the user about these changes.

## User Settings

The best practice in this section ensures that controls or applications do not override user settings.

### Respect All System-Wide Settings and Do Not Interfere with Accessibility Functions

Users can use Control Panel to set some system-wide flags; other flags can be set programmatically. These settings should not be changed by controls or applications. Also, applications must support the accessibility settings of their host operating system.

Following this best practice allows users to set accessibility settings and know that those settings will not be changed by applications.

## Visual UI Design

The best practices in this section ensure that controls or applications use color and images effectively and can be used by assistive technology products.

### Do Not Hard-Code Colors

People who are color blind, have low vision, or are using a black and white screen might not be able to use applications with hard-coded colors.

Following this best practice allows users to adjust color combinations based on individual needs.

### Support High Contrast and all System Display Attributes

Applications should not disrupt or disable user-selected, system-wide contrast settings, color selections, or other system-wide display settings and attributes. System-wide settings adopted by a user enhance the accessibility of applications, so they should not be disabled or disregarded by applications. Color should be used in their correct foreground-on-background combination to provide proper contrast. Unrelated colors should not be mixed, and colors should not be reversed.

Many users require specific high-contrast combinations, such as white text on a black background. Drawing these reversed, as black text on a white background causes the background to bleed over the foreground and can make reading difficult for some users.

### Ensure All UI Correctly Scales by Any DPI Setting

Ensure that all UI elements can correctly scale by any dots per inch (dpi) setting. Also, ensure that UI elements fit in a screen of 1024 x 768 with 120 dots per inch (dpi).

## Keyboard Navigation

The best practices in this section ensure that all application functionality is accessible to users who rely on the keyboard.

### Provide Keyboard Interface for All UI Elements

Tab stops, especially when carefully planned, give users another way to navigate the UI.

Applications should provide the following keyboard interfaces:

-   Tab stops for all controls that the user can interact with, such as buttons, links, or list boxes.
-   Logical tab order.

### Show the Keyboard Focus

Users need to know which object has the keyboard focus so that they can anticipate the effect of their keystrokes. To highlight the keyboard focus, use colors, fonts, or graphics such as rectangles or magnification. To audibly highlight the keyboard focus, change the volume, pitch or tonal quality.

To avoid confusion, applications should hide all visual focus indicators and dim selections that are located in inactive windows (or panes).

Applications should do the following with keyboard focus:

-   One item should always have keyboard focus.
-   Keyboard focus should be visible and obvious.
-   Selections and/or focused items should be visually highlighted.

### Support Navigation Standards and Powerful Navigation Schemes

Different aspects of keyboard navigation provide different ways for users to navigate the UI.

Applications should provide the following keyboard interfaces:

-   Shortcut keys and underlined access keys for all commands, menus, and controls.
-   Keyboard shortcuts to important links.
-   All menu items have an access key; all buttons have accelerator keys, all commands have an accelerator key.

### Do Not Let Mouse Location Interfere with Keyboard Navigation

Mouse location should not interfere with keyboard navigation. For example, if the mouse is positioned someplace and the user is navigating with the keyboard, a mouse click should not happen unless initiated by the user.

## Multi-modal Interface

The best practice in this section ensures that the application UI includes alternatives for visual elements.

### Provide User-Selectable Equivalents for Non-Text Elements

For each non-text element, provide a user-selectable equivalent for text, transcripts, or audio descriptions, such as alt text, captions, or visual feedback.

Non-text elements cover a wide range of UI elements including: images, image map regions, animations, applets, frames, scripts, graphical buttons, sounds, stand-alone audio files and video. Non-text elements are important when they contain visual information, speech, or general audio information that the user needs access to in order to understand the content of the UI.

### Use Color but Also Provide Alternatives to Color

Use color to enhance, emphasize, or reiterate information shown by other means, but do not communicate information by using color alone. Users who are color blind or have a monochrome display need alternatives to color.

### Use Standard Input APIs with Device-Independent Calls

Device-independent calls ensure that all input devices are treated equally, while providing assistive technology products with needed information about the UI.

## Related topics

<dl> <dt>

[Windows Automation API Overview](windows-automation-api-overview.md)
</dt> </dl>

 

 




