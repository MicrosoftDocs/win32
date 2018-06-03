---
title: Appendix G Active Accessibility Bridge to UI Automation
description: This appendix contains information about the Microsoft Active Accessibility Bridge.
ms.assetid: f19036c7-5a18-4faa-a98d-564e5e63a94f
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Appendix G: Active Accessibility Bridge to UI Automation

This appendix contains information about the Microsoft Active Accessibility Bridge. The Active Accessibility Bridge enables applications that implement Microsoft Active Accessibility to access applications that implement Microsoft UI Automation. By bridging Microsoft Active Accessibility and UI Automation together, Microsoft Active Accessibility-based clients, such as a screenreader on Windows XP, can programmatically interact with UI Automation-based providers of UI Automation, such as a Windows Presentation Foundation (WPF) application. It is part of the UI Automation Native Core API (UIAutomationCore.dll).

The Active Accessibility Bridge maps UI Automation properties and events to those of Microsoft Active Accessibility. The following tables map the Microsoft Active Accessibility [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface methods and properties to UI Automation. Use these tables to determine appropriate coding practices for developing your Microsoft Active Accessibility-based client.

### Navigation and Hierarchy Properties



| IAccessible property                                                     | UI Automation property          |
|--------------------------------------------------------------------------|---------------------------------|
| [**get\_accChild**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchild)           | Not implemented                 |
| [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount) | Derived from UI Automation tree |
| [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)         | Derived from UI Automation tree |
| [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)              | Not implemented                 |



 

### Descriptive Properties and Methods



| IAccessible                                                                          | UI Automation                                                                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accdodefaultaction)            | See the Control Types and accRole table for details.                                                                                                                                                                                                                                                                     |
| [**get\_accDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction)       | See the Control Types and accRole table for details.                                                                                                                                                                                                                                                                     |
| [**get\_accKeyboardShortcut**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut) | AccessKeyPropertyor AcceleratorKeyProperty; if both present, AccessKeyProperty takes precedence.                                                                                                                                                                                                                         |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)                         | NameProperty                                                                                                                                                                                                                                                                                                             |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)                         | ControlTypeProperty. See the Control Types and accRole table for details.                                                                                                                                                                                                                                                |
| [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)                       | See the Control Types and accRole table for details.                                                                                                                                                                                                                                                                     |
| [**get\_accValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accvalue)                       | ValueProperty; supported on control types that support the [Value](uiauto-implementingvalue.md) control pattern or [RangeValue](uiauto-implementingrangevalue.md) control pattern control pattern. RangeValue values are consistent with Microsoft Active Accessibility behavior (0 to 100). Value items use a string. |
| [**put\_accValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-put_accvalue)                       | ValueProperty; supported on control types that support the [Value](uiauto-implementingvalue.md) control pattern or [RangeValue](uiauto-implementingrangevalue.md) control pattern                                                                                                                                      |
| [**get\_accHelp**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acchelp)                         | HelpTextProperty                                                                                                                                                                                                                                                                                                         |
| [**get\_accDescription**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdescription)           | Not implemented                                                                                                                                                                                                                                                                                                          |
| [**get\_accHelpTopic**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acchelptopic)               | Not implemented                                                                                                                                                                                                                                                                                                          |



 

### Control Types and accRole

The Microsoft Active Accessibility default role is [**ROLE\_SYSTEM\_CLIENT**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_CLIENT**). If no default action is found for a control type, the Active Accessibility Bridge will also use the following available control patterns: [Invoke](uiauto-implementinginvoke.md), [ExpandCollapse](uiauto-implementingexpandcollapse.md), and [Toggle](uiauto-implementingtoggle.md). For example, a groupbox control has no default action. If it supports ExpandCollapse, then the Active Accessibility Bridge will use that for the default action.



| UI Automation control type                              | accRole                                                                     | Default action                                           |
|---------------------------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------|
| [Button](uiauto-supportbuttoncontroltype.md)           | [**ROLE\_SYSTEM\_PUSHBUTTON**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_PUSHBUTTON**)     | Press                                                    |
| [Calendar](uiauto-supportcalendarcontroltype.md)       | [**ROLE\_SYSTEM\_CLIENT**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_CLIENT**)             | None                                                     |
| [CheckBox](uiauto-supportcheckboxcontroltype.md)       | [**ROLE\_SYSTEM\_CHECKBUTTON**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_CHECKBUTTON**)   | Check/Uncheck (toggle)                                   |
| [ComboBox](uiauto-supportcomboboxcontroltype.md)       | [**ROLE\_SYSTEM\_COMBOBOX**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_COMBOBOX**)         | None                                                     |
| Custom                                                  | [**ROLE\_SYSTEM\_CLIENT**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_CLIENT**)             | None                                                     |
| [DataGrid](uiauto-supportdatagridcontroltype.md)       | [**ROLE\_SYSTEM\_LIST**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_LIST**)                 | None                                                     |
| [DataItem](uiauto-supportdataitemcontroltype.md)       | [**ROLE\_SYSTEM\_LISTITEM**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_LISTITEM**)         | None                                                     |
| [Document](uiauto-supportdocumentcontroltype.md)       | [**ROLE\_SYSTEM\_DOCUMENT**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_DOCUMENT**)         | None                                                     |
| [Edit](uiauto-supporteditcontroltype.md)               | [**ROLE\_SYSTEM\_TEXT**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_TEXT**)                 | None                                                     |
| [Group](uiauto-supportgroupcontroltype.md)             | [**ROLE\_SYSTEM\_GROUPING**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_GROUPING**)         | None                                                     |
| [Header](uiauto-supportheadercontroltype.md)           | [**ROLE\_SYSTEM\_LIST**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_LIST**)                 | None                                                     |
| [HeaderItem](uiauto-supportheaderitemcontroltype.md)   | [**ROLE\_SYSTEM\_COLUMNHEADER**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_COLUMNHEADER**) | Click                                                    |
| [Hyperlink](uiauto-supporthyperlinkcontroltype.md)     | [**ROLE\_SYSTEM\_LINK**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_LINK**)                 | Jump (maps to Invoke)                                    |
| [Image](uiauto-supportimagecontroltype.md)             | [**ROLE\_SYSTEM\_GRAPHIC**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_GRAPHIC**)           | None                                                     |
| [List](uiauto-supportlistcontroltype.md)               | [**ROLE\_SYSTEM\_LIST**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_LIST**)                 | None                                                     |
| [ListItem](uiauto-supportlistitemcontroltype.md)       | [**ROLE\_SYSTEM\_LISTITEM**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_LISTITEM**)         | Double click                                             |
| [Menu](uiauto-supportmenucontroltype.md)               | [**ROLE\_SYSTEM\_MENUPOPUP**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_MENUPOPUP**)       | None                                                     |
| [MenuBar](uiauto-supportmenubarcontroltype.md)         | [**ROLE\_SYSTEM\_MENUBAR**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_MENUBAR**)           | None                                                     |
| [MenuItem](uiauto-supportmenuitemcontroltype.md)       | [**ROLE\_SYSTEM\_MENUITEM**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_MENUITEM**)         | Execute or Open/Close for menu items that have children. |
| [Pane](uiauto-supportpanecontroltype.md)               | [**ROLE\_SYSTEM\_PANE**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_PANE**)                 | None                                                     |
| [ProgressBar](uiauto-supportprogressbarcontroltype.md) | [**ROLE\_SYSTEM\_PROGRESSBAR**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_PROGRESSBAR**)   | None                                                     |
| [RadioButton](uiauto-supportradiobuttoncontroltype.md) | [**ROLE\_SYSTEM\_RADIOBUTTON**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_RADIOBUTTON**)   | Check                                                    |
| [ScrollBar](uiauto-supportscrollbarcontroltype.md)     | [**ROLE\_SYSTEM\_SCROLLBAR**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_SCROLLBAR**)       | None                                                     |
| [Slider](uiauto-supportslidercontroltype.md)           | [**ROLE\_SYSTEM\_SLIDER**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_SLIDER**)             | None                                                     |
| [Spinner](uiauto-supportspinnercontroltype.md)         | [**ROLE\_SYSTEM\_SPINBUTTON**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_SPINBUTTON**)     | None                                                     |
| [SplitButton](uiauto-supportsplitbuttoncontroltype.md) | [**ROLE\_SYSTEM\_SPLITBUTTON**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_SPLITBUTTON**)   | None                                                     |
| [StatusBar](uiauto-supportstatusbarcontroltype.md)     | [**ROLE\_SYSTEM\_STATUSBAR**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_STATUSBAR**)       | None                                                     |
| [Tab](uiauto-supporttabcontroltype.md)                 | [**ROLE\_SYSTEM\_PAGETABLIST**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_PAGETABLIST**)   | None                                                     |
| [TabItem](uiauto-supporttabitemcontroltype.md)         | [**ROLE\_SYSTEM\_PAGETAB**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_PAGETAB**)           | Switch                                                   |
| [Table](uiauto-supporttablecontroltype.md)             | [**ROLE\_SYSTEM\_TABLE**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_TABLE**)               | None                                                     |
| [Text](uiauto-supporttextcontroltype.md)               | [**ROLE\_SYSTEM\_STATICTEXT**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_STATICTEXT**)     | None                                                     |
| [Thumb](uiauto-supportthumbcontroltype.md)             | [**ROLE\_SYSTEM\_INDICATOR**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_INDICATOR**)       | None                                                     |
| [TitleBar](uiauto-supporttitlebarcontroltype.md)       | [**ROLE\_SYSTEM\_TITLEBAR**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_TITLEBAR**)         | None                                                     |
| [ToolBar](uiauto-supporttoolbarcontroltype.md)         | [**ROLE\_SYSTEM\_TOOLBAR**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_TOOLBAR**)           | None                                                     |
| [ToolTip](uiauto-supporttooltipcontroltype.md)         | [**ROLE\_SYSTEM\_TOOLTIP**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_TOOLTIP**)           | None                                                     |
| [Tree](uiauto-supporttreecontroltype.md)               | [**ROLE\_SYSTEM\_OUTLINE**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_OUTLINE**)           | None                                                     |
| [TreeItem](uiauto-supporttreeitemcontroltype.md)       | [**ROLE\_SYSTEM\_OUTLINEITEM**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_OUTLINEITEM**)   | Expand or Collapse                                       |
| [Window](uiauto-supportwindowcontroltype.md)           | [**ROLE\_SYSTEM\_WINDOW**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_WINDOW**)             | None                                                     |



 

### UI Automation Properties and accState



| accState                                                                                      | UI Automation property                                                                                                                                                        | Triggers state change |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| [**STATE\_SYSTEM\_CHECKED**](https://www.bing.com/search?q=**STATE\_SYSTEM\_CHECKED**)                 | For ControlType = "checkbox" use ToggleState.On. For "radiobutton" use [**SelectionItemPattern::IsSelected**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionitempattern-get_currentisselected) | Yes                   |
| [**STATE\_SYSTEM\_FOCUSABLE**](https://www.bing.com/search?q=**STATE\_SYSTEM\_FOCUSABLE**)             | IsKeyboardFocusableProperty                                                                                                                                                   | No                    |
| [**STATE\_SYSTEM\_FOCUSED**](https://www.bing.com/search?q=**STATE\_SYSTEM\_FOCUSED**)                 | HasKeyboardFocusProperty                                                                                                                                                      | No                    |
| [**STATE\_SYSTEM\_PROTECTED**](https://www.bing.com/search?q=**STATE\_SYSTEM\_PROTECTED**)             | IsPasswordProperty                                                                                                                                                            | No                    |
| [**STATE\_SYSTEM\_READONLY**](https://www.bing.com/search?q=**STATE\_SYSTEM\_READONLY**)               | IsReadOnlyProperty (Value control pattern and RangeValue control pattern)                                                                                                     | No                    |
| [**STATE\_SYSTEM\_UNAVAILABLE**](https://www.bing.com/search?q=**STATE\_SYSTEM\_UNAVAILABLE**)         | IsEnabledProperty                                                                                                                                                             | Yes                   |
| [**STATE\_SYSTEM\_LINKED**](https://www.bing.com/search?q=**STATE\_SYSTEM\_LINKED**)                   | ControlTypeProperty = "hyperlink"                                                                                                                                             | No                    |
| [**STATE\_SYSTEM\_SELECTABLE**](https://www.bing.com/search?q=**STATE\_SYSTEM\_SELECTABLE**)           | SelectionItemPattern is supported                                                                                                                                             | No                    |
| [**STATE\_SYSTEM\_SELECTED**](https://www.bing.com/search?q=**STATE\_SYSTEM\_SELECTED**)               | IsSelectedProperty (SelectionItem control pattern)                                                                                                                            | No                    |
| [**STATE\_SYSTEM\_COLLAPSED**](https://www.bing.com/search?q=**STATE\_SYSTEM\_COLLAPSED**)             | ExpandCollapseState = Collapsed                                                                                                                                               | Yes                   |
| [**STATE\_SYSTEM\_EXPANDED**](https://www.bing.com/search?q=**STATE\_SYSTEM\_EXPANDED**)               | ExpandCollapseState = Expanded or PartiallyExpanded                                                                                                                           | Yes                   |
| [**STATE\_SYSTEM\_HASPOPUP**](https://www.bing.com/search?q=**STATE\_SYSTEM\_HASPOPUP**)               | Menu items that support Expand/Collapse                                                                                                                                       | No                    |
| [**STATE\_SYSTEM\_MIXED**](https://www.bing.com/search?q=**STATE\_SYSTEM\_MIXED**)                     | ToggleState = Indeterminate                                                                                                                                                   | No                    |
| [**STATE\_SYSTEM\_SIZEABLE**](https://www.bing.com/search?q=**STATE\_SYSTEM\_SIZEABLE**)               | [**IUIAutomationTransformPattern::CanResize**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtransformpattern-get_currentcanresize)                                                                     | No                    |
| [**STATE\_SYSTEM\_MOVEABLE**](https://www.bing.com/search?q=**STATE\_SYSTEM\_MOVEABLE**)               | [**IUIAutomationTransformPattern::CanMove**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtransformpattern-get_currentcanmove)                                                                         | No                    |
| [**STATE\_SYSTEM\_MULTISELECTABLE**](https://www.bing.com/search?q=**STATE\_SYSTEM\_MULTISELECTABLE**) | [**IUIAutomationSelectionPattern::CanSelectMultiple**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionpattern-get_currentcanselectmultiple)                                                     | No                    |



 

### Selection and Focus



| IAccessible                                                            | UI Automation                                                                          |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus)         | [**IUIAutomation::FocusedElement**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-getfocusedelement)        |
| [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect)                | See the UI Automation Properties and accSelect SELFLAGs table for details.             |
| [**get\_accSelection**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accselection) | [**SelectionPattern::GetSelection**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextpattern-getselection) |



 

### UI Automation Properties and accSelect SELFLAGs



| accSelect SELFLAGs                                                  | UI Automation property                                                                                                         |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**SELFLAG\_NONE**](https://www.bing.com/search?q=**SELFLAG\_NONE**)                       | Not available                                                                                                                  |
| SELFLAG\_TAKFOCUS                                                   | [**IUIAutomationElement::SetFocus**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-setfocus)                                                 |
| [**SELFLAG\_TAKESELECTION**](https://www.bing.com/search?q=**SELFLAG\_TAKESELECTION**)     | [**IUIAutomationSelectionItemPattern::Select**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionitempattern-select)                           |
| [**SELFLAG\_ADDSELECTION**](https://www.bing.com/search?q=**SELFLAG\_ADDSELECTION**)       | [**IUIAutomationSelectionItemPattern::AddToSelection**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionitempattern-addtoselection)           |
| SELFLAG\_TAKEREMOVESELECTION                                        | [**IUIAutomationSelectionItemPattern::RemoveFromSelection**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionitempattern-removefromselection) |
| [**SELFLAG\_EXTENDSELECTION**](https://www.bing.com/search?q=**SELFLAG\_EXTENDSELECTION**) | Not available                                                                                                                  |



 

### Spatial Mapping



| IAccessible                                                 | UI Automation                                                                                                                        |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation) | BoundingRectangleProperty                                                                                                            |
| [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)   | [**IRawElementProviderFragmentRoot::ElementProviderFromPoint**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementproviderfragmentroot-elementproviderfrompoint) |



 

### Events



| System-Level Event Constants                                                             | UI Automation                                                                                                           |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [**EVENT\_SYSTEM\_MENUPOPUPSTART**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_MENUPOPUPSTART**)     | [**UIA\_MenuOpenedEventId**](https://www.bing.com/search?q=**UIA\_MenuOpenedEventId**) (Note: Must check if this is a pop-up window.) |
| [**EVENT\_SYSTEM\_MENUPOPUPEND**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_MENUPOPUPEND**)         | [**UIA\_MenuClosedEventId**](https://www.bing.com/search?q=**UIA\_MenuClosedEventId**)                                                |
| [**EVENT\_SYSTEM\_MENUSTART**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_MENUSTART**)               | [**UIA\_MenuModeStartEventId**](https://www.bing.com/search?q=**UIA\_MenuModeStartEventId**)                                          |
| [**EVENT\_SYSTEM\_MENUEND**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_MENUEND**)                   | [**UIA\_MenuModeEndEventId**](https://www.bing.com/search?q=**UIA\_MenuModeEndEventId**)                                              |
| [**EVENT\_SYSTEM\_SOUND**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_SOUND**)                       |                                                                                                                         |
| [**EVENT\_SYSTEM\_ALERT**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_ALERT**)                       |                                                                                                                         |
| [**EVENT\_SYSTEM\_CAPTURESTART**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_CAPTURESTART**)         |                                                                                                                         |
| [**EVENT\_SYSTEM\_CAPTUREEND**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_CAPTUREEND**)             |                                                                                                                         |
| [**EVENT\_SYSTEM\_DIALOGSTART**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_DIALOGSTART**)           |                                                                                                                         |
| [**EVENT\_SYSTEM\_DIALOGEND**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_DIALOGEND**)               |                                                                                                                         |
| [**EVENT\_SYSTEM\_MOVESIZESTART**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_MOVESIZESTART**)       |                                                                                                                         |
| [**EVENT\_SYSTEM\_MOVESIZEEND**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_MOVESIZEEND**)           |                                                                                                                         |
| [**EVENT\_SYSTEM\_CONTEXTHELPSTART**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_CONTEXTHELPSTART**) |                                                                                                                         |
| [**EVENT\_SYSTEM\_CONTEXTHELPEND**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_CONTEXTHELPEND**)     | Not relevant                                                                                                            |
| [**EVENT\_SYSTEM\_DRAGDROPSTART**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_DRAGDROPSTART**)       |                                                                                                                         |
| [**EVENT\_SYSTEM\_DRAGDROPEND**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_DRAGDROPEND**)           |                                                                                                                         |
| [**EVENT\_SYSTEM\_SWITCHSTART**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_SWITCHSTART**)           | Not relevant                                                                                                            |
| [**EVENT\_SYSTEM\_SWITCHEND**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_SWITCHEND**)               | Not relevant                                                                                                            |
| [**EVENT\_SYSTEM\_MINIMIZESTART**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_MINIMIZESTART**)       |                                                                                                                         |
| [**EVENT\_SYSTEM\_MINIMIZEEND**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_MINIMIZEEND**)           |                                                                                                                         |
| [**EVENT\_SYSTEM\_FOREGROUND**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_FOREGROUND**)             |                                                                                                                         |
| [**EVENT\_SYSTEM\_SCROLLINGSTART**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_SCROLLINGSTART**)     | Not available                                                                                                           |
| [**EVENT\_SYSTEM\_SCROLLINGEND**](https://www.bing.com/search?q=**EVENT\_SYSTEM\_SCROLLINGEND**)         | Not available                                                                                                           |



 



| Object-Level Event Constants                                                           | UI Automation                                                                          |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**EVENT\_OBJECT\_FOCUS**](https://www.bing.com/search?q=**EVENT\_OBJECT\_FOCUS**)                     | AutomationFocusChangedEvent                                                            |
| [**EVENT\_OBJECT\_VALUECHANGE**](https://www.bing.com/search?q=**EVENT\_OBJECT\_VALUECHANGE**)         | ValueProperty (Value control pattern and RangeValue control pattern)                   |
| [**EVENT\_OBJECT\_SELECTION**](https://www.bing.com/search?q=**EVENT\_OBJECT\_SELECTION**)             | ElementSelectedEvent (SelectionItem control pattern)                                   |
| [**EVENT\_OBJECT\_SELECTIONADD**](https://www.bing.com/search?q=**EVENT\_OBJECT\_SELECTIONADD**)       | ElementAddedToSelectionEvent (SelectionItem control pattern)                           |
| [**EVENT\_OBJECT\_SELECTIONREMOVE**](https://www.bing.com/search?q=**EVENT\_OBJECT\_SELECTIONREMOVE**) | ElementRemovedFromSelectionEvent                                                       |
| [**EVENT\_OBJECT\_SELECTIONWITHIN**](https://www.bing.com/search?q=**EVENT\_OBJECT\_SELECTIONWITHIN**) | EventsSelectionInvalidatedEvent                                                        |
| [**EVENT\_OBJECT\_STATECHANGE**](https://www.bing.com/search?q=**EVENT\_OBJECT\_STATECHANGE**)         | See UI Automation Properties and accState table for states that trigger a state change |



 

 

 




