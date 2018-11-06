---
title: Appendix G Active Accessibility Bridge to UI Automation
description: This appendix contains information about the Microsoft Active Accessibility Bridge.
ms.assetid: f19036c7-5a18-4faa-a98d-564e5e63a94f
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

The Microsoft Active Accessibility default role is [**ROLE\_SYSTEM\_CLIENT**](object-roles.md). If no default action is found for a control type, the Active Accessibility Bridge will also use the following available control patterns: [Invoke](uiauto-implementinginvoke.md), [ExpandCollapse](uiauto-implementingexpandcollapse.md), and [Toggle](uiauto-implementingtoggle.md). For example, a groupbox control has no default action. If it supports ExpandCollapse, then the Active Accessibility Bridge will use that for the default action.



| UI Automation control type                              | accRole                                                                     | Default action                                           |
|---------------------------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------|
| [Button](uiauto-supportbuttoncontroltype.md)           | [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md)     | Press                                                    |
| [Calendar](uiauto-supportcalendarcontroltype.md)       | [**ROLE\_SYSTEM\_CLIENT**](object-roles.md)             | None                                                     |
| [CheckBox](uiauto-supportcheckboxcontroltype.md)       | [**ROLE\_SYSTEM\_CHECKBUTTON**](object-roles.md)   | Check/Uncheck (toggle)                                   |
| [ComboBox](uiauto-supportcomboboxcontroltype.md)       | [**ROLE\_SYSTEM\_COMBOBOX**](object-roles.md)         | None                                                     |
| Custom                                                  | [**ROLE\_SYSTEM\_CLIENT**](object-roles.md)             | None                                                     |
| [DataGrid](uiauto-supportdatagridcontroltype.md)       | [**ROLE\_SYSTEM\_LIST**](object-roles.md)                 | None                                                     |
| [DataItem](uiauto-supportdataitemcontroltype.md)       | [**ROLE\_SYSTEM\_LISTITEM**](object-roles.md)         | None                                                     |
| [Document](uiauto-supportdocumentcontroltype.md)       | [**ROLE\_SYSTEM\_DOCUMENT**](object-roles.md)         | None                                                     |
| [Edit](uiauto-supporteditcontroltype.md)               | [**ROLE\_SYSTEM\_TEXT**](object-roles.md)                 | None                                                     |
| [Group](uiauto-supportgroupcontroltype.md)             | [**ROLE\_SYSTEM\_GROUPING**](object-roles.md)         | None                                                     |
| [Header](uiauto-supportheadercontroltype.md)           | [**ROLE\_SYSTEM\_LIST**](object-roles.md)                 | None                                                     |
| [HeaderItem](uiauto-supportheaderitemcontroltype.md)   | [**ROLE\_SYSTEM\_COLUMNHEADER**](object-roles.md) | Click                                                    |
| [Hyperlink](uiauto-supporthyperlinkcontroltype.md)     | [**ROLE\_SYSTEM\_LINK**](object-roles.md)                 | Jump (maps to Invoke)                                    |
| [Image](uiauto-supportimagecontroltype.md)             | [**ROLE\_SYSTEM\_GRAPHIC**](object-roles.md)           | None                                                     |
| [List](uiauto-supportlistcontroltype.md)               | [**ROLE\_SYSTEM\_LIST**](object-roles.md)                 | None                                                     |
| [ListItem](uiauto-supportlistitemcontroltype.md)       | [**ROLE\_SYSTEM\_LISTITEM**](object-roles.md)         | Double click                                             |
| [Menu](uiauto-supportmenucontroltype.md)               | [**ROLE\_SYSTEM\_MENUPOPUP**](object-roles.md)       | None                                                     |
| [MenuBar](uiauto-supportmenubarcontroltype.md)         | [**ROLE\_SYSTEM\_MENUBAR**](object-roles.md)           | None                                                     |
| [MenuItem](uiauto-supportmenuitemcontroltype.md)       | [**ROLE\_SYSTEM\_MENUITEM**](object-roles.md)         | Execute or Open/Close for menu items that have children. |
| [Pane](uiauto-supportpanecontroltype.md)               | [**ROLE\_SYSTEM\_PANE**](object-roles.md)                 | None                                                     |
| [ProgressBar](uiauto-supportprogressbarcontroltype.md) | [**ROLE\_SYSTEM\_PROGRESSBAR**](object-roles.md)   | None                                                     |
| [RadioButton](uiauto-supportradiobuttoncontroltype.md) | [**ROLE\_SYSTEM\_RADIOBUTTON**](object-roles.md)   | Check                                                    |
| [ScrollBar](uiauto-supportscrollbarcontroltype.md)     | [**ROLE\_SYSTEM\_SCROLLBAR**](object-roles.md)       | None                                                     |
| [Slider](uiauto-supportslidercontroltype.md)           | [**ROLE\_SYSTEM\_SLIDER**](object-roles.md)             | None                                                     |
| [Spinner](uiauto-supportspinnercontroltype.md)         | [**ROLE\_SYSTEM\_SPINBUTTON**](object-roles.md)     | None                                                     |
| [SplitButton](uiauto-supportsplitbuttoncontroltype.md) | [**ROLE\_SYSTEM\_SPLITBUTTON**](object-roles.md)   | None                                                     |
| [StatusBar](uiauto-supportstatusbarcontroltype.md)     | [**ROLE\_SYSTEM\_STATUSBAR**](object-roles.md)       | None                                                     |
| [Tab](uiauto-supporttabcontroltype.md)                 | [**ROLE\_SYSTEM\_PAGETABLIST**](object-roles.md)   | None                                                     |
| [TabItem](uiauto-supporttabitemcontroltype.md)         | [**ROLE\_SYSTEM\_PAGETAB**](object-roles.md)           | Switch                                                   |
| [Table](uiauto-supporttablecontroltype.md)             | [**ROLE\_SYSTEM\_TABLE**](object-roles.md)               | None                                                     |
| [Text](uiauto-supporttextcontroltype.md)               | [**ROLE\_SYSTEM\_STATICTEXT**](object-roles.md)     | None                                                     |
| [Thumb](uiauto-supportthumbcontroltype.md)             | [**ROLE\_SYSTEM\_INDICATOR**](object-roles.md)       | None                                                     |
| [TitleBar](uiauto-supporttitlebarcontroltype.md)       | [**ROLE\_SYSTEM\_TITLEBAR**](object-roles.md)         | None                                                     |
| [ToolBar](uiauto-supporttoolbarcontroltype.md)         | [**ROLE\_SYSTEM\_TOOLBAR**](object-roles.md)           | None                                                     |
| [ToolTip](uiauto-supporttooltipcontroltype.md)         | [**ROLE\_SYSTEM\_TOOLTIP**](object-roles.md)           | None                                                     |
| [Tree](uiauto-supporttreecontroltype.md)               | [**ROLE\_SYSTEM\_OUTLINE**](object-roles.md)           | None                                                     |
| [TreeItem](uiauto-supporttreeitemcontroltype.md)       | [**ROLE\_SYSTEM\_OUTLINEITEM**](object-roles.md)   | Expand or Collapse                                       |
| [Window](uiauto-supportwindowcontroltype.md)           | [**ROLE\_SYSTEM\_WINDOW**](object-roles.md)             | None                                                     |



 

### UI Automation Properties and accState



| accState                                                                                      | UI Automation property                                                                                                                                                        | Triggers state change |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| [**STATE\_SYSTEM\_CHECKED**](object-state-constants.md)                 | For ControlType = "checkbox" use ToggleState.On. For "radiobutton" use [**SelectionItemPattern::IsSelected**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionitempattern-get_currentisselected) | Yes                   |
| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md)             | IsKeyboardFocusableProperty                                                                                                                                                   | No                    |
| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md)                 | HasKeyboardFocusProperty                                                                                                                                                      | No                    |
| [**STATE\_SYSTEM\_PROTECTED**](object-state-constants.md)             | IsPasswordProperty                                                                                                                                                            | No                    |
| [**STATE\_SYSTEM\_READONLY**](object-state-constants.md)               | IsReadOnlyProperty (Value control pattern and RangeValue control pattern)                                                                                                     | No                    |
| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md)         | IsEnabledProperty                                                                                                                                                             | Yes                   |
| [**STATE\_SYSTEM\_LINKED**](object-state-constants.md)                   | ControlTypeProperty = "hyperlink"                                                                                                                                             | No                    |
| [**STATE\_SYSTEM\_SELECTABLE**](object-state-constants.md)           | SelectionItemPattern is supported                                                                                                                                             | No                    |
| [**STATE\_SYSTEM\_SELECTED**](object-state-constants.md)               | IsSelectedProperty (SelectionItem control pattern)                                                                                                                            | No                    |
| [**STATE\_SYSTEM\_COLLAPSED**](object-state-constants.md)             | ExpandCollapseState = Collapsed                                                                                                                                               | Yes                   |
| [**STATE\_SYSTEM\_EXPANDED**](object-state-constants.md)               | ExpandCollapseState = Expanded or PartiallyExpanded                                                                                                                           | Yes                   |
| [**STATE\_SYSTEM\_HASPOPUP**](object-state-constants.md)               | Menu items that support Expand/Collapse                                                                                                                                       | No                    |
| [**STATE\_SYSTEM\_MIXED**](object-state-constants.md)                     | ToggleState = Indeterminate                                                                                                                                                   | No                    |
| [**STATE\_SYSTEM\_SIZEABLE**](object-state-constants.md)               | [**IUIAutomationTransformPattern::CanResize**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtransformpattern-get_currentcanresize)                                                                     | No                    |
| [**STATE\_SYSTEM\_MOVEABLE**](object-state-constants.md)               | [**IUIAutomationTransformPattern::CanMove**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtransformpattern-get_currentcanmove)                                                                         | No                    |
| [**STATE\_SYSTEM\_MULTISELECTABLE**](object-state-constants.md) | [**IUIAutomationSelectionPattern::CanSelectMultiple**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionpattern-get_currentcanselectmultiple)                                                     | No                    |



 

### Selection and Focus



| IAccessible                                                            | UI Automation                                                                          |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus)         | [**IUIAutomation::FocusedElement**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-getfocusedelement)        |
| [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect)                | See the UI Automation Properties and accSelect SELFLAGs table for details.             |
| [**get\_accSelection**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accselection) | [**SelectionPattern::GetSelection**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextpattern-getselection) |



 

### UI Automation Properties and accSelect SELFLAGs



| accSelect SELFLAGs                                                  | UI Automation property                                                                                                         |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**SELFLAG\_NONE**](selflag.md)                       | Not available                                                                                                                  |
| SELFLAG\_TAKFOCUS                                                   | [**IUIAutomationElement::SetFocus**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-setfocus)                                                 |
| [**SELFLAG\_TAKESELECTION**](selflag.md)     | [**IUIAutomationSelectionItemPattern::Select**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionitempattern-select)                           |
| [**SELFLAG\_ADDSELECTION**](selflag.md)       | [**IUIAutomationSelectionItemPattern::AddToSelection**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionitempattern-addtoselection)           |
| SELFLAG\_TAKEREMOVESELECTION                                        | [**IUIAutomationSelectionItemPattern::RemoveFromSelection**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionitempattern-removefromselection) |
| [**SELFLAG\_EXTENDSELECTION**](selflag.md) | Not available                                                                                                                  |



 

### Spatial Mapping



| IAccessible                                                 | UI Automation                                                                                                                        |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation) | BoundingRectangleProperty                                                                                                            |
| [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)   | [**IRawElementProviderFragmentRoot::ElementProviderFromPoint**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementproviderfragmentroot-elementproviderfrompoint) |



 

### Events



| System-Level Event Constants                                                             | UI Automation                                                                                                           |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [**EVENT\_SYSTEM\_MENUPOPUPSTART**](event-constants.md)     | [**UIA\_MenuOpenedEventId**](uiauto-event-ids.md) (Note: Must check if this is a pop-up window.) |
| [**EVENT\_SYSTEM\_MENUPOPUPEND**](event-constants.md)         | [**UIA\_MenuClosedEventId**](uiauto-event-ids.md)                                                |
| [**EVENT\_SYSTEM\_MENUSTART**](event-constants.md)               | [**UIA\_MenuModeStartEventId**](uiauto-event-ids.md)                                          |
| [**EVENT\_SYSTEM\_MENUEND**](event-constants.md)                   | [**UIA\_MenuModeEndEventId**](uiauto-event-ids.md)                                              |
| [**EVENT\_SYSTEM\_SOUND**](event-constants.md)                       |                                                                                                                         |
| [**EVENT\_SYSTEM\_ALERT**](event-constants.md)                       |                                                                                                                         |
| [**EVENT\_SYSTEM\_CAPTURESTART**](event-constants.md)         |                                                                                                                         |
| [**EVENT\_SYSTEM\_CAPTUREEND**](event-constants.md)             |                                                                                                                         |
| [**EVENT\_SYSTEM\_DIALOGSTART**](event-constants.md)           |                                                                                                                         |
| [**EVENT\_SYSTEM\_DIALOGEND**](event-constants.md)               |                                                                                                                         |
| [**EVENT\_SYSTEM\_MOVESIZESTART**](event-constants.md)       |                                                                                                                         |
| [**EVENT\_SYSTEM\_MOVESIZEEND**](event-constants.md)           |                                                                                                                         |
| [**EVENT\_SYSTEM\_CONTEXTHELPSTART**](event-constants.md) |                                                                                                                         |
| [**EVENT\_SYSTEM\_CONTEXTHELPEND**](event-constants.md)     | Not relevant                                                                                                            |
| [**EVENT\_SYSTEM\_DRAGDROPSTART**](event-constants.md)       |                                                                                                                         |
| [**EVENT\_SYSTEM\_DRAGDROPEND**](event-constants.md)           |                                                                                                                         |
| [**EVENT\_SYSTEM\_SWITCHSTART**](event-constants.md)           | Not relevant                                                                                                            |
| [**EVENT\_SYSTEM\_SWITCHEND**](event-constants.md)               | Not relevant                                                                                                            |
| [**EVENT\_SYSTEM\_MINIMIZESTART**](event-constants.md)       |                                                                                                                         |
| [**EVENT\_SYSTEM\_MINIMIZEEND**](event-constants.md)           |                                                                                                                         |
| [**EVENT\_SYSTEM\_FOREGROUND**](event-constants.md)             |                                                                                                                         |
| [**EVENT\_SYSTEM\_SCROLLINGSTART**](event-constants.md)     | Not available                                                                                                           |
| [**EVENT\_SYSTEM\_SCROLLINGEND**](event-constants.md)         | Not available                                                                                                           |



 



| Object-Level Event Constants                                                           | UI Automation                                                                          |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**EVENT\_OBJECT\_FOCUS**](event-constants.md)                     | AutomationFocusChangedEvent                                                            |
| [**EVENT\_OBJECT\_VALUECHANGE**](event-constants.md)         | ValueProperty (Value control pattern and RangeValue control pattern)                   |
| [**EVENT\_OBJECT\_SELECTION**](event-constants.md)             | ElementSelectedEvent (SelectionItem control pattern)                                   |
| [**EVENT\_OBJECT\_SELECTIONADD**](event-constants.md)       | ElementAddedToSelectionEvent (SelectionItem control pattern)                           |
| [**EVENT\_OBJECT\_SELECTIONREMOVE**](event-constants.md) | ElementRemovedFromSelectionEvent                                                       |
| [**EVENT\_OBJECT\_SELECTIONWITHIN**](event-constants.md) | EventsSelectionInvalidatedEvent                                                        |
| [**EVENT\_OBJECT\_STATECHANGE**](event-constants.md)         | See UI Automation Properties and accState table for states that trigger a state change |



 

 

 




