---
title: Deprecated GUIDs
description: This topic describes the GUIDs that are used with the UiaLookupId function.
ms.assetid: b8e9e33c-9781-4f50-bbb7-a9950409f2e6
ms.topic: article
ms.date: 05/31/2018
---

# Deprecated GUIDs

This topic describes the GUIDs that are used with the [**UiaLookupId**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uialookupid) function.

> [!Note]  
> The [**UiaLookupId**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uialookupid) function and the GUIDs described in this topic are deprecated. Instead, applications should use the identifiers described in the following sections:

 

-   [Control Pattern Identifiers](uiauto-controlpattern-ids.md)
-   [Control Type Identifiers](uiauto-controltype-ids.md)
-   [Event Identifiers](uiauto-event-ids.md)
-   [Property Identifiers](uiauto-entry-propids.md)
-   [Text Attribute Identifiers](uiauto-textattribute-ids.md)

This section lists the following GUIDs:

-   [PATTERNID GUIDs](#patternid-guids)
-   [CONTROLTYPEID GUIDs](#controltypeid-guids)
-   [EVENTID GUIDs](#eventid-guids)
-   [PROPERTYID GUIDs](#propertyid-guids)
-   [TEXTATTRIBUTEID GUIDs](#textattributeid-guids)

## PATTERNID GUIDs

The PATTERNID GUIDs that represent control patterns in the [**UiaLookupId**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uialookupid) function are listed in the following table.



| PATTERNID GUIDs                  |
|----------------------------------|
| Annotation\_Pattern\_GUID        |
| Dock\_Pattern\_GUID              |
| Drag\_Pattern\_GUID              |
| DropTarget\_Pattern\_GUID        |
| ExpandCollpase\_Pattern\_GUID    |
| Grid\_Pattern\_GUID              |
| GridItem\_Pattern\_GUID          |
| Invoke\_Pattern\_GUID            |
| ItemContainer\_Pattern\_GUID     |
| LegacyIAccessible\_Pattern\_GUID |
| ObjectModel\_Pattern\_GUID       |
| RangeValue\_Pattern\_GUID        |
| Scroll\_Pattern\_GUID            |
| ScrollItem\_Pattern\_GUID        |
| Selection\_Pattern               |
| SelectionItem\_Pattern\_GUID     |
| Spreadsheet\_Pattern\_GUID       |
| SpreadsheetItem\_Pattern\_GUID   |
| SynchronizedInput\_Pattern\_GUID |
| Styles\_Pattern\_GUID            |
| Table\_Pattern\_GUID             |
| TableItem\_Pattern\_GUID         |
| TextChild\_Pattern\_GUID         |
| Text\_Pattern\_GUID              |
| Text\_Pattern2\_GUID             |
| Toggle\_Pattern\_GUID            |
| Transform\_Pattern               |
| Transform\_Pattern2\_GUID        |
| Value\_Pattern\_GUID             |
| VirtualizedItem\_Pattern\_GUID   |
| Window\_Pattern\_GUID            |



 

## CONTROLTYPEID GUIDs

The CONTROLTYPEID GUIDs that represent control types in the [**UiaLookupId**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uialookupid) function are listed in the following table.



| CONTROLTYPEID GUIDs        |
|----------------------------|
| Button\_Control\_GUID      |
| Calendar\_Control\_GUID    |
| CheckBox\_Control\_GUID    |
| ComboBox\_Control\_GUID    |
| Custom\_Control\_GUID      |
| DataGrid\_Control\_GUID    |
| DataItem\_Control\_GUID    |
| Document\_Control\_GUID    |
| Edit\_Control\_GUID        |
| Group\_Control\_GUID       |
| Header\_Control\_GUID      |
| HeaderItem\_Control\_GUID  |
| Hyperlink\_Control\_GUID   |
| Image\_Control\_GUID       |
| List\_Control\_GUID        |
| ListItem\_Control\_GUID    |
| Menu\_Control\_GUID        |
| MenuBar\_Control\_GUID     |
| MenuItem\_Control\_GUID    |
| Pane\_Control\_GUID        |
| ProgressBar\_Control\_GUID |
| RadioButton\_Control\_GUID |
| ScrollBar\_Control\_GUID   |
| Separator\_Control\_GUID   |
| Slider\_Control\_GUID      |
| Spinner\_Control\_GUID     |
| SplitButton\_Control\_GUID |
| StatusBar\_Control\_GUID   |
| Tab\_Control\_GUID         |
| TabItem\_Control\_GUID     |
| Table\_Control\_GUID       |
| Text\_Control\_GUID        |
| Thumb\_Control\_GUID       |
| TitleBar\_Control\_GUID    |
| ToolBar\_Control\_GUID     |
| ToolTip\_Control\_GUID     |
| Tree\_Control\_GUID        |
| TreeItem\_Control\_GUID    |
| Window\_Control\_GUID      |



 

## EVENTID GUIDs

The EVENTID GUIDs that represent Microsoft UI Automation events in the [**UiaLookupId**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uialookupid) function are listed in the following table.



| EVENTID GUIDs                                                |
|--------------------------------------------------------------|
| AsyncContentLoaded\_Event\_GUID                              |
| AutomationFocusChanged\_Event\_GUID                          |
| AutomationPropertyChanged\_Event\_GUID                       |
| Drag\_DragCancel\_Event\_GUID                                |
| Drag\_DragComplete\_Event\_GUID                              |
| Drag\_DragStart\_Event\_GUID                                 |
| DropTarget\_DragEnter\_Event\_GUID                           |
| DropTarget\_DragLeave\_Event\_GUID                           |
| DropTarget\_Dropped\_Event\_GUID                             |
| HostedFragmentRootsInvalidated\_Event\_GUID                  |
| InputDiscarded\_Event\_GUID                                  |
| InputReachedOtherElement\_Event\_GUID                        |
| InputReachedTarget\_Event\_GUID                              |
| Invoke\_Invoked\_Event\_GUID                                 |
| LayoutInvalidated\_Event\_GUID                               |
| LiveRegionChanged\_Event\_GUID                               |
| MenuClosed\_Event\_GUID                                      |
| MenuModeEnd\_Event\_GUID                                     |
| MenuModeStart\_Event\_GUID                                   |
| MenuOpened\_Event\_GUID                                      |
| Selection\_InvalidatedEvent\_Event\_GUID                     |
| SelectionItem\_ElementAddedToSelectionEvent\_Event\_GUID     |
| SelectionItem\_ElementRemovedFromSelectionEvent\_Event\_GUID |
| SelectionItem\_ElementSelectedEvent\_Event\_GUID             |
| StructureChanged\_Event\_GUID                                |
| SystemAlert\_Event\_GUID                                     |
| Text\_TextChangedEvent\_Event\_GUID                          |
| Text\_TextSelectionChangedEvent\_Event\_GUID                 |
| ToolTipClosed\_Event\_GUID                                   |
| Window\_WindowOpened\_Event\_GUID                            |
| ToolTipOpened\_Event\_GUID                                   |
| Window\_WindowClosed\_Event\_GUID                            |



 

## PROPERTYID GUIDs

The PROPERTYID GUIDs that represent UI Automation properties in the [**UiaLookupId**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uialookupid) function are listed in the following table.



| PROPERTYID GUIDs                                    |
|-----------------------------------------------------|
| AcceleratorKey\_Property\_GUID                      |
| AccessKey\_Property\_GUID                           |
| Annotation\_AnnotationTypeId\_Property\_GUID        |
| Annotation\_AnnotationTypeName\_Property\_GUID      |
| Annotation\_Author\_Property\_GUID                  |
| Annotation\_DateTime\_Property\_GUID                |
| Annotation\_Target\_Property\_GUID                  |
| AriaProperties\_Property\_GUID                      |
| AriaRole\_Property\_GUID                            |
| AutomationId\_Property\_GUID                        |
| BoundingRectangle\_Property\_GUID                   |
| ClassName\_Property\_GUID                           |
| ClickablePoint\_Property\_GUID                      |
| ControllerFor\_Property\_GUID                       |
| ControlType\_Property\_GUID                         |
| Culture\_Property\_GUID                             |
| DescribedBy\_Property\_GUID                         |
| Dock\_DockPosition\_Property\_GUID                  |
| Drag\_DropEffect\_Property\_GUID                    |
| Drag\_DropEffects\_Property\_GUID                   |
| Drag\_GrabbedItems\_Property\_GUID                  |
| Drag\_IsGrabbed\_Property\_GUID                     |
| DropTarget\_DropTargetEffect\_Property\_GUID        |
| DropTarget\_DropTargetEffects\_Property\_GUID       |
| ExpandCollapse\_ExpandCollapseState\_Property\_GUID |
| FlowsTo\_Property\_GUID                             |
| FrameworkId\_Property\_GUID                         |
| Grid\_ColumnCount\_Property\_GUID                   |
| Grid\_RowCount\_Property\_GUID                      |
| GridItem\_Column\_Property\_GUID                    |
| GridItem\_ColumnSpan\_Property\_GUID                |
| GridItem\_Parent\_Property\_GUID                    |
| GridItem\_Row\_Property\_GUID                       |
| GridItem\_RowSpan\_Property\_GUID                   |
| HasKeyboardFocus\_Property\_GUID                    |
| HelpText\_Property\_GUID                            |
| IsAnnotationPatternAvailable\_Property\_GUID        |
| IsContentElement\_Property\_GUID                    |
| IsControlElement\_Property\_GUID                    |
| IsDataValidForForm\_Property\_GUID                  |
| IsDockPatternAvailable\_Property\_GUID              |
| IsDragPatternAvailable\_Property\_GUID              |
| IsDropTargetPatternAvailable\_Property\_GUID        |
| IsEnabled\_Property\_GUID                           |
| IsExpandCollapsePatternAvailable\_Property\_GUID    |
| IsGridItemPatternAvailable\_Property\_GUID          |
| IsGridPatternAvailable\_Property\_GUID              |
| IsInvokePatternAvailable\_Property\_GUID            |
| IsItemContainerPatternAvailable\_Property\_GUID     |
| IsKeyboardFocusable\_Property\_GUID                 |
| IsLegacyIAccessiblePatternAvailable\_Property\_GUID |
| IsMultipleViewPatternAvailable\_Property\_GUID      |
| IsObjectModelPatternAvailable\_Property\_GUID       |
| IsOffscreen\_Property\_GUID                         |
| IsPassword\_Property\_GUID                          |
| IsRangeValuePatternAvailable\_Property\_GUID        |
| IsRequiredForForm\_Property\_GUID                   |
| IsScrollItemPatternAvailable\_Property\_GUID        |
| IsScrollPatternAvailable\_Property\_GUID            |
| IsSelectionItemPatternAvailable\_Property\_GUID     |
| IsSelectionPatternAvailable\_Property\_GUID         |
| IsSpreadsheetPatternAvailable\_Property\_GUID       |
| IsSpreadsheetItemPatternAvailable\_Property\_GUID   |
| IsStylesPatternAvailable\_Property\_GUID            |
| IsSynchronizedInputPatternAvailable\_Property\_GUID |
| IsTableItemPatternAvailable\_Property\_GUID         |
| IsTablePatternAvailable\_Property\_GUID             |
| IsTextChildPatternAvailable\_Property\_GUID         |
| IsTextPatternAvailable\_Property\_GUID              |
| IsTextPattern2Available\_Property\_GUID             |
| IsTogglePatternAvailable\_Property\_GUID            |
| IsTransformPatternAvailable\_Property\_GUID         |
| IsTransformPattern2Available\_Property\_GUID        |
| IsValuePatternAvailable\_Property\_GUID             |
| IsVirtualizedItemPatternAvailable\_Property\_GUID   |
| IsWindowPatternAvailable\_Property\_GUID            |
| ItemStatus\_Property\_GUID                          |
| ItemType\_Property\_GUID                            |
| LabeledBy\_Property\_GUID                           |
| LegacyIAccessible\_ChildId\_Property\_GUID          |
| LegacyIAccessible\_DefaultAction\_Property\_GUID    |
| LegacyIAccessible\_Description\_Property\_GUID      |
| LegacyIAccessible\_Help\_Property\_GUID             |
| LegacyIAccessible\_KeyboardShortcut\_Property\_GUID |
| LegacyIAccessible\_Name\_Property\_GUID             |
| LegacyIAccessible\_Role\_Property\_GUID             |
| LegacyIAccessible\_Selection\_Property\_GUID        |
| LegacyIAccessible\_State\_Property\_GUID            |
| LegacyIAccessible\_Value\_Property\_GUID            |
| LiveSetting\_Property\_GUID                         |
| LocalizedControlType\_Property\_GUID                |
| MultipleView\_CurrentView\_Property\_GUID           |
| MultipleView\_SupportedViews\_Property\_GUID        |
| Name\_Property\_GUID                                |
| NewNativeWindowHandle\_Property\_GUID               |
| OptimizeForVisualContent\_Property\_GUID            |
| Orientation\_Property\_GUID                         |
| ProcessId\_Property\_GUID                           |
| ProviderDescription\_Property\_GUID                 |
| RangeValue\_IsReadOnly\_Property\_GUID              |
| RangeValue\_LargeChange\_Property\_GUID             |
| RangeValue\_Maximum\_Property\_GUID                 |
| RangeValue\_Minimum\_Property\_GUID                 |
| RangeValue\_SmallChange\_Property\_GUID             |
| RangeValue\_Value\_Property\_GUID                   |
| RuntimeId\_Property\_GUID                           |
| Scroll\_HorizontallyScrollable\_Property\_GUID      |
| Scroll\_HorizontalScrollPercent\_Property\_GUID     |
| Scroll\_HorizontalViewSize\_Property\_GUID          |
| Scroll\_VerticallyScrollable\_Property\_GUID        |
| Scroll\_VerticalScrollPercent\_Property\_GUID       |
| Scroll\_VerticalViewSize\_Property\_GUID            |
| Selection\_CanSelectMultiple\_Property\_GUID        |
| Selection\_IsSelectionRequired\_Property\_GUID      |
| Selection\_Selection\_Property\_GUID                |
| SelectionItem\_IsSelected\_Property\_GUID           |
| SelectionItem\_SelectionContainer\_Property\_GUID   |
| SpreadsheetItem\_AnnotationObjects\_Property\_GUID  |
| SpreadsheetItem\_AnnotationTypes\_Property\_GUID    |
| SpreadsheetItem\_Formula\_Property\_GUID            |
| Styles\_ExtendedProperties\_Property\_GUID          |
| Styles\_FillColor\_Property\_GUID                   |
| Styles\_FillPatternColor\_Property\_GUID            |
| Styles\_FillPatternStyle\_Property\_GUID            |
| Styles\_Shape\_Property\_GUID                       |
| Styles\_StyleId\_Property\_GUID                     |
| Styles\_StyleName\_Property\_GUID                   |
| Table\_ColumnHeaders\_Property\_GUID                |
| Table\_RowHeaders\_Property\_GUID                   |
| Table\_RowOrColumnMajor\_Property\_GUID             |
| TableItem\_ColumnHeaderItems\_Property\_GUID        |
| TableItem\_RowHeaderItems\_Property\_GUID           |
| Toggle\_ToggleState\_Property\_GUID                 |
| Transform\_CanMove\_Property\_GUID                  |
| Transform\_CanResize\_Property\_GUID                |
| Transform\_CanRotate\_Property\_GUID                |
| Transform2\_CanZoom\_Property\_GUID                 |
| Transform2\_ZoomLevel\_Property\_GUID               |
| Transform2\_ZoomMaximum\_Property\_GUID             |
| Transform2\_ZoomMinimum\_Property\_GUID             |
| Value\_IsReadOnly\_Property\_GUID                   |
| Value\_Value\_Property\_GUID                        |
| Window\_CanMaximize\_Property\_GUID                 |
| Window\_CanMinimize\_Property\_GUID                 |
| Window\_IsModal\_Property\_GUID                     |
| Window\_IsTopmost\_Property\_GUID                   |
| Window\_WindowInteractionState\_Property\_GUID      |
| Window\_WindowVisualState\_Property\_GUID           |



 

## TEXTATTRIBUTEID GUIDs

The TEXTATTRIBUTEID GUIDs that represent text attributes in the [**UiaLookupId**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uialookupid) function are listed in the following table.



| TEXTATTRIBUTEID GUIDs                          |
|------------------------------------------------|
| Text\_AnimationStyle\_Attribute\_GUID          |
| Text\_AnnotationObjects\_Attribute\_GUID       |
| Text\_AnnotationTypes\_Attribute\_GUID         |
| Text\_BackgroundColor\_Attribute\_GUID         |
| Text\_BulletStyle\_Attribute\_GUID             |
| Text\_CapStyle\_Attribute\_GUID                |
| Text\_CaretBidiMode\_Attribute\_GUID           |
| Text\_CaretPosition\_Attribute\_GUID           |
| Text\_Culture\_Attribute\_GUID                 |
| Text\_FontName\_Attribute\_GUID                |
| Text\_FontSize\_Attribute\_GUID                |
| Text\_FontWeight\_Attribute\_GUID              |
| Text\_ForegroundColor\_Attribute\_GUID         |
| Text\_HorizontalTextAlignment\_Attribute\_GUID |
| Text\_IndentationFirstLine\_Attribute\_GUID    |
| Text\_IndentationLeading\_Attribute\_GUID      |
| Text\_IndentationTrailing\_Attribute\_GUID     |
| Text\_IsActive\_Attribute\_GUID                |
| Text\_IsHidden\_Attribute\_GUID                |
| Text\_IsItalic\_Attribute\_GUID                |
| Text\_IsReadOnly\_Attribute\_GUID              |
| Text\_IsSubscript\_Attribute\_GUID             |
| Text\_IsSuperscript\_Attribute\_GUID           |
| Text\_Link\_Attribute\_GUID                    |
| Text\_MarginBottom\_Attribute\_GUID            |
| Text\_MarginLeading\_Attribute\_GUID           |
| Text\_MarginTop\_Attribute\_GUID               |
| Text\_MarginTrailing\_Attribute\_GUID          |
| Text\_OutlineStyles\_Attribute\_GUID           |
| Text\_OverlineColor\_Attribute\_GUID           |
| Text\_OverlineStyle\_Attribute\_GUID           |
| Text\_SelectionActiveEnd\_Attribute\_GUID      |
| Text\_StrikethroughColor\_Attribute\_GUID      |
| Text\_StrikethroughStyle\_Attribute\_GUID      |
| Text\_StyleId\_Attribute\_GUID                 |
| Text\_StyleName\_Attribute\_GUID               |
| Text\_Tabs\_Attribute\_GUID                    |
| Text\_TextFlowDirection\_Attribute\_GUID       |
| Text\_UnderlineColor\_Attribute\_GUID          |
| Text\_UnderlineStyle\_Attribute\_GUID          |



 

 

 




