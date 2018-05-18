---
title: Appendix G Active Accessibility Bridge to UI Automation
description: This appendix contains information about the Microsoft Active Accessibility Bridge.
ms.assetid: 'f19036c7-5a18-4faa-a98d-564e5e63a94f'
---

# Appendix G: Active Accessibility Bridge to UI Automation

This appendix contains information about the Microsoft Active Accessibility Bridge. The Active Accessibility Bridge enables applications that implement Microsoft Active Accessibility to access applications that implement Microsoft UI Automation. By bridging Microsoft Active Accessibility and UI Automation together, Microsoft Active Accessibility-based clients, such as a screenreader on Windows XP, can programmatically interact with UI Automation-based providers of UI Automation, such as a Windows Presentation Foundation (WPF) application. It is part of the UI Automation Native Core API (UIAutomationCore.dll).

The Active Accessibility Bridge maps UI Automation properties and events to those of Microsoft Active Accessibility. The following tables map the Microsoft Active Accessibility [**IAccessible**](iaccessible.md) interface methods and properties to UI Automation. Use these tables to determine appropriate coding practices for developing your Microsoft Active Accessibility-based client.

### Navigation and Hierarchy Properties



| IAccessible property                                                     | UI Automation property          |
|--------------------------------------------------------------------------|---------------------------------|
| [**get\_accChild**](iaccessible-iaccessible--get-accchild.md)           | Not implemented                 |
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md) | Derived from UI Automation tree |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)         | Derived from UI Automation tree |
| [**accNavigate**](iaccessible-iaccessible--accnavigate.md)              | Not implemented                 |



 

### Descriptive Properties and Methods



| IAccessible                                                                          | UI Automation                                                                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md)            | See the Control Types and accRole table for details.                                                                                                                                                                                                                                                                     |
| [**get\_accDefaultAction**](iaccessible-iaccessible--get-accdefaultaction.md)       | See the Control Types and accRole table for details.                                                                                                                                                                                                                                                                     |
| [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md) | AccessKeyPropertyor AcceleratorKeyProperty; if both present, AccessKeyProperty takes precedence.                                                                                                                                                                                                                         |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                         | NameProperty                                                                                                                                                                                                                                                                                                             |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                         | ControlTypeProperty. See the Control Types and accRole table for details.                                                                                                                                                                                                                                                |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                       | See the Control Types and accRole table for details.                                                                                                                                                                                                                                                                     |
| [**get\_accValue**](iaccessible-iaccessible--get-accvalue.md)                       | ValueProperty; supported on control types that support the [Value](uiauto-implementingvalue.md) control pattern or [RangeValue](uiauto-implementingrangevalue.md) control pattern control pattern. RangeValue values are consistent with Microsoft Active Accessibility behavior (0 to 100). Value items use a string. |
| [**put\_accValue**](iaccessible-iaccessible--put-accvalue.md)                       | ValueProperty; supported on control types that support the [Value](uiauto-implementingvalue.md) control pattern or [RangeValue](uiauto-implementingrangevalue.md) control pattern                                                                                                                                      |
| [**get\_accHelp**](iaccessible-iaccessible--get-acchelp.md)                         | HelpTextProperty                                                                                                                                                                                                                                                                                                         |
| [**get\_accDescription**](iaccessible-iaccessible--get-accdescription.md)           | Not implemented                                                                                                                                                                                                                                                                                                          |
| [**get\_accHelpTopic**](iaccessible-iaccessible--get-acchelptopic.md)               | Not implemented                                                                                                                                                                                                                                                                                                          |



 

### Control Types and accRole

The Microsoft Active Accessibility default role is [**ROLE\_SYSTEM\_CLIENT**](object-roles.md#role-system-client). If no default action is found for a control type, the Active Accessibility Bridge will also use the following available control patterns: [Invoke](uiauto-implementinginvoke.md), [ExpandCollapse](uiauto-implementingexpandcollapse.md), and [Toggle](uiauto-implementingtoggle.md). For example, a groupbox control has no default action. If it supports ExpandCollapse, then the Active Accessibility Bridge will use that for the default action.



| UI Automation control type                              | accRole                                                                     | Default action                                           |
|---------------------------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------|
| [Button](uiauto-supportbuttoncontroltype.md)           | [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md#role-system-pushbutton)     | Press                                                    |
| [Calendar](uiauto-supportcalendarcontroltype.md)       | [**ROLE\_SYSTEM\_CLIENT**](object-roles.md#role-system-client)             | None                                                     |
| [CheckBox](uiauto-supportcheckboxcontroltype.md)       | [**ROLE\_SYSTEM\_CHECKBUTTON**](object-roles.md#role-system-checkbutton)   | Check/Uncheck (toggle)                                   |
| [ComboBox](uiauto-supportcomboboxcontroltype.md)       | [**ROLE\_SYSTEM\_COMBOBOX**](object-roles.md#role-system-combobox)         | None                                                     |
| Custom                                                  | [**ROLE\_SYSTEM\_CLIENT**](object-roles.md#role-system-client)             | None                                                     |
| [DataGrid](uiauto-supportdatagridcontroltype.md)       | [**ROLE\_SYSTEM\_LIST**](object-roles.md#role-system-list)                 | None                                                     |
| [DataItem](uiauto-supportdataitemcontroltype.md)       | [**ROLE\_SYSTEM\_LISTITEM**](object-roles.md#role-system-listitem)         | None                                                     |
| [Document](uiauto-supportdocumentcontroltype.md)       | [**ROLE\_SYSTEM\_DOCUMENT**](object-roles.md#role-system-document)         | None                                                     |
| [Edit](uiauto-supporteditcontroltype.md)               | [**ROLE\_SYSTEM\_TEXT**](object-roles.md#role-system-text)                 | None                                                     |
| [Group](uiauto-supportgroupcontroltype.md)             | [**ROLE\_SYSTEM\_GROUPING**](object-roles.md#role-system-grouping)         | None                                                     |
| [Header](uiauto-supportheadercontroltype.md)           | [**ROLE\_SYSTEM\_LIST**](object-roles.md#role-system-list)                 | None                                                     |
| [HeaderItem](uiauto-supportheaderitemcontroltype.md)   | [**ROLE\_SYSTEM\_COLUMNHEADER**](object-roles.md#role-system-columnheader) | Click                                                    |
| [Hyperlink](uiauto-supporthyperlinkcontroltype.md)     | [**ROLE\_SYSTEM\_LINK**](object-roles.md#role-system-link)                 | Jump (maps to Invoke)                                    |
| [Image](uiauto-supportimagecontroltype.md)             | [**ROLE\_SYSTEM\_GRAPHIC**](object-roles.md#role-system-graphic)           | None                                                     |
| [List](uiauto-supportlistcontroltype.md)               | [**ROLE\_SYSTEM\_LIST**](object-roles.md#role-system-list)                 | None                                                     |
| [ListItem](uiauto-supportlistitemcontroltype.md)       | [**ROLE\_SYSTEM\_LISTITEM**](object-roles.md#role-system-listitem)         | Double click                                             |
| [Menu](uiauto-supportmenucontroltype.md)               | [**ROLE\_SYSTEM\_MENUPOPUP**](object-roles.md#role-system-menupopup)       | None                                                     |
| [MenuBar](uiauto-supportmenubarcontroltype.md)         | [**ROLE\_SYSTEM\_MENUBAR**](object-roles.md#role-system-menubar)           | None                                                     |
| [MenuItem](uiauto-supportmenuitemcontroltype.md)       | [**ROLE\_SYSTEM\_MENUITEM**](object-roles.md#role-system-menuitem)         | Execute or Open/Close for menu items that have children. |
| [Pane](uiauto-supportpanecontroltype.md)               | [**ROLE\_SYSTEM\_PANE**](object-roles.md#role-system-pane)                 | None                                                     |
| [ProgressBar](uiauto-supportprogressbarcontroltype.md) | [**ROLE\_SYSTEM\_PROGRESSBAR**](object-roles.md#role-system-progressbar)   | None                                                     |
| [RadioButton](uiauto-supportradiobuttoncontroltype.md) | [**ROLE\_SYSTEM\_RADIOBUTTON**](object-roles.md#role-system-radiobutton)   | Check                                                    |
| [ScrollBar](uiauto-supportscrollbarcontroltype.md)     | [**ROLE\_SYSTEM\_SCROLLBAR**](object-roles.md#role-system-scrollbar)       | None                                                     |
| [Slider](uiauto-supportslidercontroltype.md)           | [**ROLE\_SYSTEM\_SLIDER**](object-roles.md#role-system-slider)             | None                                                     |
| [Spinner](uiauto-supportspinnercontroltype.md)         | [**ROLE\_SYSTEM\_SPINBUTTON**](object-roles.md#role-system-spinbutton)     | None                                                     |
| [SplitButton](uiauto-supportsplitbuttoncontroltype.md) | [**ROLE\_SYSTEM\_SPLITBUTTON**](object-roles.md#role-system-splitbutton)   | None                                                     |
| [StatusBar](uiauto-supportstatusbarcontroltype.md)     | [**ROLE\_SYSTEM\_STATUSBAR**](object-roles.md#role-system-statusbar)       | None                                                     |
| [Tab](uiauto-supporttabcontroltype.md)                 | [**ROLE\_SYSTEM\_PAGETABLIST**](object-roles.md#role-system-pagetablist)   | None                                                     |
| [TabItem](uiauto-supporttabitemcontroltype.md)         | [**ROLE\_SYSTEM\_PAGETAB**](object-roles.md#role-system-pagetab)           | Switch                                                   |
| [Table](uiauto-supporttablecontroltype.md)             | [**ROLE\_SYSTEM\_TABLE**](object-roles.md#role-system-table)               | None                                                     |
| [Text](uiauto-supporttextcontroltype.md)               | [**ROLE\_SYSTEM\_STATICTEXT**](object-roles.md#role-system-statictext)     | None                                                     |
| [Thumb](uiauto-supportthumbcontroltype.md)             | [**ROLE\_SYSTEM\_INDICATOR**](object-roles.md#role-system-indicator)       | None                                                     |
| [TitleBar](uiauto-supporttitlebarcontroltype.md)       | [**ROLE\_SYSTEM\_TITLEBAR**](object-roles.md#role-system-titlebar)         | None                                                     |
| [ToolBar](uiauto-supporttoolbarcontroltype.md)         | [**ROLE\_SYSTEM\_TOOLBAR**](object-roles.md#role-system-toolbar)           | None                                                     |
| [ToolTip](uiauto-supporttooltipcontroltype.md)         | [**ROLE\_SYSTEM\_TOOLTIP**](object-roles.md#role-system-tooltip)           | None                                                     |
| [Tree](uiauto-supporttreecontroltype.md)               | [**ROLE\_SYSTEM\_OUTLINE**](object-roles.md#role-system-outline)           | None                                                     |
| [TreeItem](uiauto-supporttreeitemcontroltype.md)       | [**ROLE\_SYSTEM\_OUTLINEITEM**](object-roles.md#role-system-outlineitem)   | Expand or Collapse                                       |
| [Window](uiauto-supportwindowcontroltype.md)           | [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window)             | None                                                     |



 

### UI Automation Properties and accState



| accState                                                                                      | UI Automation property                                                                                                                                                        | Triggers state change |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| [**STATE\_SYSTEM\_CHECKED**](object-state-constants.md#state-system-checked)                 | For ControlType = "checkbox" use ToggleState.On. For "radiobutton" use [**SelectionItemPattern::IsSelected**](uiauto-iuiautomationselectionitempattern-currentisselected.md) | Yes                   |
| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)             | IsKeyboardFocusableProperty                                                                                                                                                   | No                    |
| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused)                 | HasKeyboardFocusProperty                                                                                                                                                      | No                    |
| [**STATE\_SYSTEM\_PROTECTED**](object-state-constants.md#state-system-protected)             | IsPasswordProperty                                                                                                                                                            | No                    |
| [**STATE\_SYSTEM\_READONLY**](object-state-constants.md#state-system-readonly)               | IsReadOnlyProperty (Value control pattern and RangeValue control pattern)                                                                                                     | No                    |
| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable)         | IsEnabledProperty                                                                                                                                                             | Yes                   |
| [**STATE\_SYSTEM\_LINKED**](object-state-constants.md#state-system-linked)                   | ControlTypeProperty = "hyperlink"                                                                                                                                             | No                    |
| [**STATE\_SYSTEM\_SELECTABLE**](object-state-constants.md#state-system-selectable)           | SelectionItemPattern is supported                                                                                                                                             | No                    |
| [**STATE\_SYSTEM\_SELECTED**](object-state-constants.md#state-system-selected)               | IsSelectedProperty (SelectionItem control pattern)                                                                                                                            | No                    |
| [**STATE\_SYSTEM\_COLLAPSED**](object-state-constants.md#state-system-collapsed)             | ExpandCollapseState = Collapsed                                                                                                                                               | Yes                   |
| [**STATE\_SYSTEM\_EXPANDED**](object-state-constants.md#state-system-expanded)               | ExpandCollapseState = Expanded or PartiallyExpanded                                                                                                                           | Yes                   |
| [**STATE\_SYSTEM\_HASPOPUP**](object-state-constants.md#state-system-haspopup)               | Menu items that support Expand/Collapse                                                                                                                                       | No                    |
| [**STATE\_SYSTEM\_MIXED**](object-state-constants.md#state-system-mixed)                     | ToggleState = Indeterminate                                                                                                                                                   | No                    |
| [**STATE\_SYSTEM\_SIZEABLE**](object-state-constants.md#state-system-sizeable)               | [**IUIAutomationTransformPattern::CanResize**](uiauto-iuiautomationtransformpattern-currentcanresize.md)                                                                     | No                    |
| [**STATE\_SYSTEM\_MOVEABLE**](object-state-constants.md#state-system-moveable)               | [**IUIAutomationTransformPattern::CanMove**](uiauto-iuiautomationtransformpattern-currentcanmove.md)                                                                         | No                    |
| [**STATE\_SYSTEM\_MULTISELECTABLE**](object-state-constants.md#state-system-multiselectable) | [**IUIAutomationSelectionPattern::CanSelectMultiple**](uiauto-iuiautomationselectionpattern-currentcanselectmultiple.md)                                                     | No                    |



 

### Selection and Focus



| IAccessible                                                            | UI Automation                                                                          |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)         | [**IUIAutomation::FocusedElement**](uiauto-iuiautomation-getfocusedelement.md)        |
| [**accSelect**](iaccessible-iaccessible--accselect.md)                | See the UI Automation Properties and accSelect SELFLAGs table for details.             |
| [**get\_accSelection**](iaccessible-iaccessible--get-accselection.md) | [**SelectionPattern::GetSelection**](uiauto-iuiautomationtextpattern-getselection.md) |



 

### UI Automation Properties and accSelect SELFLAGs



| accSelect SELFLAGs                                                  | UI Automation property                                                                                                         |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**SELFLAG\_NONE**](selflag.md#selflag-none)                       | Not available                                                                                                                  |
| SELFLAG\_TAKFOCUS                                                   | [**IUIAutomationElement::SetFocus**](uiauto-iuiautomationelement-setfocus.md)                                                 |
| [**SELFLAG\_TAKESELECTION**](selflag.md#selflag-takeselection)     | [**IUIAutomationSelectionItemPattern::Select**](uiauto-iuiautomationselectionitempattern-select.md)                           |
| [**SELFLAG\_ADDSELECTION**](selflag.md#selflag-addselection)       | [**IUIAutomationSelectionItemPattern::AddToSelection**](uiauto-iuiautomationselectionitempattern-addtoselection.md)           |
| SELFLAG\_TAKEREMOVESELECTION                                        | [**IUIAutomationSelectionItemPattern::RemoveFromSelection**](uiauto-iuiautomationselectionitempattern-removefromselection.md) |
| [**SELFLAG\_EXTENDSELECTION**](selflag.md#selflag-extendselection) | Not available                                                                                                                  |



 

### Spatial Mapping



| IAccessible                                                 | UI Automation                                                                                                                        |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**accLocation**](iaccessible-iaccessible--acclocation.md) | BoundingRectangleProperty                                                                                                            |
| [**accHitTest**](iaccessible-iaccessible--acchittest.md)   | [**IRawElementProviderFragmentRoot::ElementProviderFromPoint**](uiauto-irawelementproviderfragmentroot-elementproviderfrompoint.md) |



 

### Events



| System-Level Event Constants                                                             | UI Automation                                                                                                           |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [**EVENT\_SYSTEM\_MENUPOPUPSTART**](event-constants.md#event-system-menupopupstart)     | [**UIA\_MenuOpenedEventId**](uiauto-event-ids.md#uia-menuopenedeventid) (Note: Must check if this is a pop-up window.) |
| [**EVENT\_SYSTEM\_MENUPOPUPEND**](event-constants.md#event-system-menupopupend)         | [**UIA\_MenuClosedEventId**](uiauto-event-ids.md#uia-menuclosedeventid)                                                |
| [**EVENT\_SYSTEM\_MENUSTART**](event-constants.md#event-system-menustart)               | [**UIA\_MenuModeStartEventId**](uiauto-event-ids.md#uia-menumodestarteventid)                                          |
| [**EVENT\_SYSTEM\_MENUEND**](event-constants.md#event-system-menuend)                   | [**UIA\_MenuModeEndEventId**](uiauto-event-ids.md#uia-menumodeendeventid)                                              |
| [**EVENT\_SYSTEM\_SOUND**](event-constants.md#event-system-sound)                       |                                                                                                                         |
| [**EVENT\_SYSTEM\_ALERT**](event-constants.md#event-system-alert)                       |                                                                                                                         |
| [**EVENT\_SYSTEM\_CAPTURESTART**](event-constants.md#event-system-capturestart)         |                                                                                                                         |
| [**EVENT\_SYSTEM\_CAPTUREEND**](event-constants.md#event-system-captureend)             |                                                                                                                         |
| [**EVENT\_SYSTEM\_DIALOGSTART**](event-constants.md#event-system-dialogstart)           |                                                                                                                         |
| [**EVENT\_SYSTEM\_DIALOGEND**](event-constants.md#event-system-dialogend)               |                                                                                                                         |
| [**EVENT\_SYSTEM\_MOVESIZESTART**](event-constants.md#event-system-movesizestart)       |                                                                                                                         |
| [**EVENT\_SYSTEM\_MOVESIZEEND**](event-constants.md#event-system-movesizeend)           |                                                                                                                         |
| [**EVENT\_SYSTEM\_CONTEXTHELPSTART**](event-constants.md#event-system-contexthelpstart) |                                                                                                                         |
| [**EVENT\_SYSTEM\_CONTEXTHELPEND**](event-constants.md#event-system-contexthelpend)     | Not relevant                                                                                                            |
| [**EVENT\_SYSTEM\_DRAGDROPSTART**](event-constants.md#event-system-dragdropstart)       |                                                                                                                         |
| [**EVENT\_SYSTEM\_DRAGDROPEND**](event-constants.md#event-system-dragdropend)           |                                                                                                                         |
| [**EVENT\_SYSTEM\_SWITCHSTART**](event-constants.md#event-system-switchstart)           | Not relevant                                                                                                            |
| [**EVENT\_SYSTEM\_SWITCHEND**](event-constants.md#event-system-switchend)               | Not relevant                                                                                                            |
| [**EVENT\_SYSTEM\_MINIMIZESTART**](event-constants.md#event-system-minimizestart)       |                                                                                                                         |
| [**EVENT\_SYSTEM\_MINIMIZEEND**](event-constants.md#event-system-minimizeend)           |                                                                                                                         |
| [**EVENT\_SYSTEM\_FOREGROUND**](event-constants.md#event-system-foreground)             |                                                                                                                         |
| [**EVENT\_SYSTEM\_SCROLLINGSTART**](event-constants.md#event-system-scrollingstart)     | Not available                                                                                                           |
| [**EVENT\_SYSTEM\_SCROLLINGEND**](event-constants.md#event-system-scrollingend)         | Not available                                                                                                           |



 



| Object-Level Event Constants                                                           | UI Automation                                                                          |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**EVENT\_OBJECT\_FOCUS**](event-constants.md#event-object-focus)                     | AutomationFocusChangedEvent                                                            |
| [**EVENT\_OBJECT\_VALUECHANGE**](event-constants.md#event-object-valuechange)         | ValueProperty (Value control pattern and RangeValue control pattern)                   |
| [**EVENT\_OBJECT\_SELECTION**](event-constants.md#event-object-selection)             | ElementSelectedEvent (SelectionItem control pattern)                                   |
| [**EVENT\_OBJECT\_SELECTIONADD**](event-constants.md#event-object-selectionadd)       | ElementAddedToSelectionEvent (SelectionItem control pattern)                           |
| [**EVENT\_OBJECT\_SELECTIONREMOVE**](event-constants.md#event-object-selectionremove) | ElementRemovedFromSelectionEvent                                                       |
| [**EVENT\_OBJECT\_SELECTIONWITHIN**](event-constants.md#event-object-selectionwithin) | EventsSelectionInvalidatedEvent                                                        |
| [**EVENT\_OBJECT\_STATECHANGE**](event-constants.md#event-object-statechange)         | See UI Automation Properties and accState table for states that trigger a state change |



 

 

 




