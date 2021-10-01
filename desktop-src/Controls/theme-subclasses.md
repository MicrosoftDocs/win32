---
title: Using Theme Subclasses
description: Theme classes that represent controls such as ComboBox, Edit, ExplorerBar, Rebar, Tab, and Toolbar can be subclassed in order to provide theme variations for that particular control.
ms.assetid: 4f5e26c1-72ae-48de-a407-9ac3c0d5f502
ms.topic: article
ms.date: 05/31/2018
---

# Using Theme Subclasses

Theme classes that represent controls such as ComboBox, Edit, ExplorerBar, Rebar, Tab, and Toolbar can be subclassed in order to provide theme variations for that particular control. For example, the **Button** class is subclassed as `Start::Button` in order to provide control over the theme applied to the **Start** button.

> [!Note]  
> Use caution when you create subclasses like those that are discussed in this topic. Because subclasses might be altered or unavailable in subsequent versions of Windows, you are discouraged from using them.

 

## Two Ways to Use a Theme Subclass

An application can use a subclassed theme in one of these two ways:

-   It can use the [**OpenThemeData**](/windows/desktop/api/Uxtheme/nf-uxtheme-openthemedata) function with a string of the form `subclass::class` in the *pszClassList* parameter.
-   It can call [**SetWindowTheme**](/windows/desktop/api/Uxtheme/nf-uxtheme-setwindowtheme) with the theme subclass name in the *pszSubAppName* parameter.

## Using Theme Messages That Set Visual Style

Certain controls, such as Rebar and Toolbar, provide specific messages that you can send to instruct the control to use a theme subclass. For those controls, provide a pointer to a buffer that contains the theme subclass name in the *lParam* parameter of the message. Use the generic [**CCM\_SETWINDOWTHEME**](ccm-setwindowtheme.md) message, or use a specific variant like those shown in the following table.



| Control    | Message                                             |
|------------|-----------------------------------------------------|
| Tooltip    | [**TTM\_SETWINDOWTHEME**](ttm-setwindowtheme.md)   |
| Toolbar    | [**TB\_SETWINDOWTHEME**](tb-setwindowtheme.md)     |
| Rebar      | [**RB\_SETWINDOWTHEME**](rb-setwindowtheme.md)     |
| ComboBoxEx | [**CBEM\_SETWINDOWTHEME**](cbem-setwindowtheme.md) |



 

The following table lists some of the subclasses that Windows Vista defines.




| Class | Subclasses | 
|-------|------------|
| ComboBox | <ul><li>Address</li><li>AddressComposited</li><li>InactiveAddress</li><li>InactiveAddressComposited</li><li>MaxAddress</li><li>MaxAddressComposited</li><li>MaxInactiveAddress</li><li>MaxInactiveAddressComposited</li></ul> | 
| Edit | <ul><li>Address</li><li>AddressComposited</li><li>InactiveAddress</li><li>InactiveAddressComposited</li><li>InactiveSearchBoxEdit</li><li>InactiveSearchBoxEditComposited</li><li>MaxAddress</li><li>MaxAddressComposited</li><li>MaxInactiveAddress</li><li>MaxInactiveAddressComposited</li><li>MaxInactiveSearchBoxEdit</li><li>MaxInactiveSearchBoxEditComposited</li><li>MaxSearchBoxEdit</li><li>MaxSearchBoxEditComposited</li><li>SearchBoxEdit</li><li>SearchBoxEditComposited</li></ul> | 
| Rebar | <ul><li>BrowserTabBar</li><li>InactiveNavbar</li><li>InactiveNavbarComposited</li><li>MaxInactiveNavbar</li><li>MaxInactiveNavbarComposited</li><li>MaxNavbar</li><li>MaxNavbarComposited</li><li>Navbar</li><li>NavbarComposited</li><li>NavbarNonTopmost</li></ul> | 
| Tab | <ul><li>BrowserTab</li></ul> | 
| Toolbar | <ul><li>Go</li><li>GoComposited</li><li>InactiveGo</li><li>InactiveGoComposited</li><li>MaxGo</li><li>MaxGoComposited</li><li>MaxInactiveGo</li><li>MaxInactiveGoComposited</li><li>SearchButton</li><li>SearchButtonComposited</li><li>Travel</li><li>TravelComposited</li></ul> | 




 

## Internet Explorer Subclasses

In Windows Vista, the subclasses of certain classes internal to Windows Internet Explorer and Windows Explorer are available even though the classes themselves are not. The following table lists the available subclasses.




| 
|
| AddressBand | <ul><li>AB</li><li>ABGreen</li><li>ABGreenComposited</li><li>ABRed</li><li>ABRedComposited</li><li>ABYellow</li><li>ABYellowComposited</li></ul> | 
| SearchBox | <ul><li>InactiveSearchBox</li><li>InactiveSearchBoxComposited</li><li>MaxInactiveSearchBox</li><li>MaxInactiveSearchBoxComposited</li><li>MaxSearchBox</li><li>MaxSearchBoxComposited</li><li>SearchBoxComposited</li></ul> | 




 

The following table shows the specifics of these classes.



| Control     | Part         | States                                                 |
|-------------|--------------|--------------------------------------------------------|
| ADDRESSBAND | ABBACKGROUND | NORMAL (0x1), HOT (0x2), DISABLED (0x3), FOCUSED (0x4) |
| SEARCHBOX   | SBBACKGROUND | NORMAL (0x1), HOT (0x2), DISABLED (0x3), FOCUSED (0x4) |



 

 

 




