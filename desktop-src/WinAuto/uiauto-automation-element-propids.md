---
title: Automation Element Property Identifiers (UIAutomationClient.h)
description: This topic describes the named constants that identify the properties of Microsoft UI Automation elements.
ms.assetid: f7613ad1-0b75-46fb-b9ac-b1ae9eea4193
topic_type:
- apiref
api_name:
- UIA_AcceleratorKeyPropertyId
- UIA_AccessKeyPropertyId
- UIA_AnnotationObjectsPropertyId
- UIA_AnnotationTypesPropertyId
- UIA_AriaPropertiesPropertyId
- UIA_AriaRolePropertyId
- UIA_AutomationIdPropertyId
- UIA_BoundingRectanglePropertyId
- UIA_CenterPointPropertyId
- UIA_ClassNamePropertyId
- UIA_ClickablePointPropertyId
- UIA_ControllerForPropertyId
- UIA_ControlTypePropertyId
- UIA_CulturePropertyId
- UIA_DescribedByPropertyId
- UIA_FillColorPropertyId
- UIA_FillTypePropertyId
- UIA_FlowsFromPropertyId
- UIA_FlowsToPropertyId
- UIA_FrameworkIdPropertyId
- UIA_FullDescriptionPropertyId
- UIA_HasKeyboardFocusPropertyId
- UIA_HeadingLevelPropertyId
- UIA_HelpTextPropertyId
- UIA_IsContentElementPropertyId
- UIA_IsControlElementPropertyId
- UIA_IsDataValidForFormPropertyId
- UIA_IsEnabledPropertyId
- UIA_IsKeyboardFocusablePropertyId
- UIA_IsOffscreenPropertyId
- UIA_IsPasswordPropertyId
- UIA_IsPeripheralPropertyId
- UIA_IsRequiredForFormPropertyId
- UIA_ItemStatusPropertyId
- UIA_ItemTypePropertyId
- UIA_LabeledByPropertyId
- UIA_LandmarkTypePropertyId
- UIA_LevelPropertyId
- UIA_LiveSettingPropertyId
- UIA_LocalizedControlTypePropertyId
- UIA_LocalizedLandmarkTypePropertyId
- UIA_NamePropertyId
- UIA_NativeWindowHandlePropertyId
- UIA_OptimizeForVisualContentPropertyId
- UIA_OrientationPropertyId
- UIA_OutlineColorPropertyId
- UIA_OutlineThicknessPropertyId
- UIA_PositionInSetPropertyId
- UIA_ProcessIdPropertyId
- UIA_ProviderDescriptionPropertyId
- UIA_RotationPropertyId
- UIA_RuntimeIdPropertyId
- UIA_SizePropertyId
- UIA_SizeOfSetPropertyId
- UIA_VisualEffectsPropertyId
api_location:
- UIAutomationClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Automation Element Property Identifiers

This topic describes the named constants that identify the properties of Microsoft UI Automation elements.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Constant/value</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_AcceleratorKeyPropertyId"></span><span id="uia_acceleratorkeypropertyid"></span><span id="UIA_ACCELERATORKEYPROPERTYID"></span><dl> <dt><strong>UIA_AcceleratorKeyPropertyId</strong></dt> <dt>30006</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>AcceleratorKey</strong> property, which is a string containing the accelerator key (also called shortcut key) combinations for the automation element. <br/> Shortcut key combinations invoke an action. For example, CTRL+O is often used to invoke the Open file common dialog box. An automation element that has the <strong>AcceleratorKey</strong> property can implement the <a href="uiauto-implementinginvoke.md">Invoke</a> control pattern for the action that is equivalent to the shortcut command.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_AccessKeyPropertyId"></span><span id="uia_accesskeypropertyid"></span><span id="UIA_ACCESSKEYPROPERTYID"></span><dl> <dt><strong>UIA_AccessKeyPropertyId</strong></dt> <dt>30007</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>AccessKey</strong> property, which is a string containing the access key character for the automation element.<br/> An access key (sometimes called a mnemonic) is a character in the text of a menu, menu item, or label of a control such as a button, that activates the associated menu function. For example, to open the File menu, for which the access key is typically F, the user would press ALT+F.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_AnnotationObjectsPropertyId"></span><span id="uia_annotationobjectspropertyid"></span><span id="UIA_ANNOTATIONOBJECTSPROPERTYID"></span><dl> <dt><strong>UIA_AnnotationObjectsPropertyId</strong></dt> <dt>30156</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>AnnotationObjects</strong> property, which is a list of annotation objects in a document, such as comment, header, footer, and so on.<br/> Variant type: <strong>VT_I4</strong> | <strong>VT_ARRAY</strong><br/> Default value: empty array<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_AnnotationTypesPropertyId"></span><span id="uia_annotationtypespropertyid"></span><span id="UIA_ANNOTATIONTYPESPROPERTYID"></span><dl> <dt><strong>UIA_AnnotationTypesPropertyId</strong></dt> <dt>30155</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>AnnotationTypes</strong> property, which is a list of the types of annotations in a document, such as comment, header, footer, and so on.<br/> Variant type: <strong>VT_I4</strong> | <strong>VT_ARRAY</strong><br/> Default value: empty array<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_AriaPropertiesPropertyId"></span><span id="uia_ariapropertiespropertyid"></span><span id="UIA_ARIAPROPERTIESPROPERTYID"></span><dl> <dt><strong>UIA_AriaPropertiesPropertyId</strong></dt> <dt>30102</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>AriaProperties</strong> property, which is a formatted string containing the Accessible Rich Internet Application (ARIA) property information for the automation element. For more information about mapping ARIA states and properties to UI Automation properties and functions, see <a href="uiauto-ariaspecification.md">UI Automation for W3C Accessible Rich Internet Applications Specification</a>.<br/> <strong>AriaProperties</strong> is a collection of Name/Value pairs with delimiters of <strong>=</strong> (equals) and <strong>;</strong> (semicolon), for example, &quot;checked=true;disabled=false&quot;. The <strong>\</strong> (backslash) is used as an escape character when these delimiter characters or <strong>\</strong> appear in the values. For security and other reasons, the provider implementation of this property can take steps to validate the original ARIA properties; however, it is not required.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_AriaRolePropertyId"></span><span id="uia_ariarolepropertyid"></span><span id="UIA_ARIAROLEPROPERTYID"></span><dl> <dt><strong>UIA_AriaRolePropertyId</strong></dt> <dt>30101</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>AriaRole</strong> property, which is a string containing the Accessible Rich Internet Application (ARIA) role information for the automation element. For more information about mapping ARIA roles to UI Automation control types, see <a href="uiauto-ariaspecification.md">UI Automation for W3C Accessible Rich Internet Applications Specification</a>.<br/>
<blockquote>
[!Note]<br />
As an option, the user agent can also offer a localized description of the W3C ARIA role in the <strong>LocalizedControlType</strong> property. When the localized string is not specified, the system will provide the default <strong>LocalizedControlType</strong> string for the element.
</blockquote>
<br/> <br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_AutomationIdPropertyId"></span><span id="uia_automationidpropertyid"></span><span id="UIA_AUTOMATIONIDPROPERTYID"></span><dl> <dt><strong>UIA_AutomationIdPropertyId</strong></dt> <dt>30011</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>AutomationId</strong> property, which is a string containing the UI Automation identifier (ID) for the automation element.<br/> When it is available, the <strong>AutomationId</strong> of an element must be the same in any instance of the application, regardless of the local language. The value should be unique among sibling elements, but not necessarily unique across the entire desktop. For example, multiple instances of an application, or multiple folder views in Microsoft Windows Explorer, can contain elements with the same <strong>AutomationId</strong> property, such as &quot;SystemMenuBar&quot;.<br/> Although support for <strong>AutomationId</strong> is always recommended for better automated testing support, this property is not mandatory. Where it is supported, <strong>AutomationId</strong> is useful for creating a test automation script that runs regardless of the UI language. Clients should make no assumptions regarding the <strong>AutomationId</strong> values exposed by other applications. <strong>AutomationId</strong> is not guaranteed to be stable across different releases or builds of an application.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_BoundingRectanglePropertyId"></span><span id="uia_boundingrectanglepropertyid"></span><span id="UIA_BOUNDINGRECTANGLEPROPERTYID"></span><dl> <dt><strong>UIA_BoundingRectanglePropertyId</strong></dt> <dt>30001</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>BoundingRectangle</strong> property, which specifies the coordinates of the rectangle that completely encloses the automation element. The rectangle is expressed in physical screen coordinates. It can contain points that are not clickable if the shape or clickable region of the UI item is irregular, or if the item is obscured by other UI elements.<br/> Variant type: <strong>VT_R8</strong> | <strong>VT_ARRAY</strong><br/> Default value: [0,0,0,0]<br/>
<blockquote>
[!Note]<br />
This property is <strong>NULL</strong> if the item is not currently displaying a UI.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_CenterPointPropertyId"></span><span id="uia_centerpointpropertyid"></span><span id="UIA_CENTERPOINTPROPERTYID"></span><dl> <dt><strong>UIA_CenterPointPropertyId</strong></dt> <dt>30165</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>CenterPoint</strong> property, which specifies the center X and Y point coordinates of the automation element. The coordinate space is what the provider logically considers a page.<br/> Variant type: <strong>VT_R8</strong> | <strong>VT_ARRAY</strong><br/> Default value: <strong>VT_EMPTY</strong><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_ClassNamePropertyId"></span><span id="uia_classnamepropertyid"></span><span id="UIA_CLASSNAMEPROPERTYID"></span><dl> <dt><strong>UIA_ClassNamePropertyId</strong></dt> <dt>30012</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>ClassName</strong> property, which is a string containing the class name for the automation element as assigned by the control developer.<br/> The class name depends on the implementation of the UI Automation provider and therefore is not always in a standard format. However, if the class name is known, it can be used to verify that an application is working with the expected automation element.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_ClickablePointPropertyId"></span><span id="uia_clickablepointpropertyid"></span><span id="UIA_CLICKABLEPOINTPROPERTYID"></span><dl> <dt><strong>UIA_ClickablePointPropertyId</strong></dt> <dt>30014</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>ClickablePoint</strong> property, which is a point on the automation element that can be clicked. An element cannot be clicked if it is completely or partially obscured by another window.<br/> Variant type: <strong>VT_R8</strong> | <strong>VT_ARRAY</strong><br/> Default value: <strong>VT_EMPTY</strong><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_ControllerForPropertyId"></span><span id="uia_controllerforpropertyid"></span><span id="UIA_CONTROLLERFORPROPERTYID"></span><dl> <dt><strong>UIA_ControllerForPropertyId</strong></dt> <dt>30104</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>ControllerFor</strong> property, which is an array of automation elements that are manipulated by the automation element that supports this property.<br/> <strong>ControllerFor</strong> is used when an automation element affects one or more segments of the application UI or the desktop; otherwise, it is hard to associate the impact of the control operation with UI elements.<br/> This identifier is commonly used for <a href="/windows/uwp/design/accessibility/accessible-text-requirements">Auto-suggest accessibility</a>.<br/> Variant type for providers: <strong>VT_UNKNOWN</strong> | <strong>VT_ARRAY</strong><br/> Variant type for clients: <strong>VT_UNKNOWN</strong> (<a href="/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelementarray"><strong>IUIAutomationElementArray</strong></a> )<br/> Default value: empty array<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_ControlTypePropertyId"></span><span id="uia_controltypepropertyid"></span><span id="UIA_CONTROLTYPEPROPERTYID"></span><dl> <dt><strong>UIA_ControlTypePropertyId</strong></dt> <dt>30003</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>ControlType</strong> property, which is a class that identifies the type of the automation element. <strong>ControlType</strong> defines characteristics of the UI elements by well known UI control primitives such as button or check box. <br/> Variant type: <strong>VT_I4</strong><br/> Default value: <a href="uiauto-controltype-ids.md"><strong>UIA_CustomControlTypeId</strong></a><br/>
<blockquote>
[!Note]<br />
Use the default value only if the automation element represents a completely new type of control.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_CulturePropertyId"></span><span id="uia_culturepropertyid"></span><span id="UIA_CULTUREPROPERTYID"></span><dl> <dt><strong>UIA_CulturePropertyId</strong></dt> <dt>30015</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>Culture</strong> property, which contains a locale identifier for the automation element (for example, <code>0x0409</code> for &quot;en-US&quot; or English (United States)).<br/> Each locale has a unique identifier, a 32-bit value that consists of a language identifier and a sort order identifier. The locale identifier is a standard international numeric abbreviation and has the components necessary to uniquely identify one of the installed operating system-defined locales. For more information, see <a href="/windows/desktop/Intl/language-identifier-constants-and-strings">Language Identifier Constants and Strings</a>.<br/> This property may exist on a per-control basis, but typically is only available on an application level.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_DescribedByPropertyId"></span><span id="uia_describedbypropertyid"></span><span id="UIA_DESCRIBEDBYPROPERTYID"></span><dl> <dt><strong>UIA_DescribedByPropertyId</strong></dt> <dt>30105</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>DescribedBy</strong> property, which is an array of elements that provide more information about the automation element.<br/> <strong>DescribedBy</strong> is used when an automation element is explained by another segment of the application UI. For example, the property can point to a text element of &quot;2,529 items in 85 groups, 10 items selected&quot; from a complex custom list object. Instead of using the object model for clients to digest similar information, the <strong>DescribedBy</strong> property can offer quick access to the UI element that may already offer useful end-user information that describes the UI element.<br/> Variant type for providers: <strong>VT_UNKNOWN</strong> | <strong>VT_ARRAY</strong><br/> Variant type for clients: <strong>VT_UNKNOWN</strong> (<a href="/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelementarray"><strong>IUIAutomationElementArray</strong></a>)<br/> Default value: empty array<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_FillColorPropertyId"></span><span id="uia_fillcolorpropertyid"></span><span id="UIA_FILLCOLORPROPERTYID"></span><dl> <dt><strong>UIA_FillColorPropertyId</strong></dt> <dt>30160</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>FillColor</strong> property, which specifies the color used to fill the automation element. This attribute is specified as a COLORREF, a 32-bit value used to specify an RGB or RGBA color.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_FillTypePropertyId"></span><span id="uia_filltypepropertyid"></span><span id="UIA_FILLTYPEPROPERTYID"></span><dl> <dt><strong>UIA_FillTypePropertyId</strong></dt> <dt>30162</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>FillType</strong> property, which specifies the pattern used to fill the automation element, such as none, color, gradient, picture, pattern, and so on.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_FlowsFromPropertyId"></span><span id="uia_flowsfrompropertyid"></span><span id="UIA_FLOWSFROMPROPERTYID"></span><dl> <dt><strong>UIA_FlowsFromPropertyId</strong></dt> <dt>30148</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>FlowsFrom</strong> property, which is an array of automation elements that suggests the reading order before the current automation element. Supported starting with Windows 8.<br/> The <strong>FlowsFrom</strong> property specifies the reading order when automation elements are not exposed or structured in the same reading order as perceived by the user. While the <strong>FlowsFrom</strong> property can specify multiple preceding elements, it typically contains only the prior element in the reading order.<br/> Variant type for providers: <strong>VT_UNKNOWN</strong> | <strong>VT_ARRAY</strong><br/> Variant type for clients: <strong>VT_UNKNOWN</strong> (<a href="/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelementarray"><strong>IUIAutomationElementArray</strong></a>)<br/> Default value: empty array<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_FlowsToPropertyId"></span><span id="uia_flowstopropertyid"></span><span id="UIA_FLOWSTOPROPERTYID"></span><dl> <dt><strong>UIA_FlowsToPropertyId</strong></dt> <dt>30106</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>FlowsTo</strong> property, which is an array of automation elements that suggests the reading order after the current automation element.<br/> The <strong>FlowsTo</strong> property specifies the reading order when automation elements are not exposed or structured in the same reading order as perceived by the user. While the <strong>FlowsTo</strong> property can specify multiple succeeding elements, it typically contains only the next element in the reading order.<br/> Variant type for providers: <strong>VT_UNKNOWN</strong> | <strong>VT_ARRAY</strong><br/> Variant type for clients: <strong>VT_UNKNOWN</strong> (<a href="/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelementarray"><strong>IUIAutomationElementArray</strong></a>)<br/> Default value: empty array<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_FrameworkIdPropertyId"></span><span id="uia_frameworkidpropertyid"></span><span id="UIA_FRAMEWORKIDPROPERTYID"></span><dl> <dt><strong>UIA_FrameworkIdPropertyId</strong></dt> <dt>30024</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>FrameworkId</strong> property, which is a string containing the name of the underlying UI framework that the automation element belongs to.<br/> The <strong>FrameworkId</strong> enables client applications to process automation elements differently depending on the particular UI framework. Examples of property values include &quot;Win32&quot;, &quot;WinForm&quot;, and &quot;DirectUI&quot;.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_FullDescriptionPropertyId"></span><span id="uia_fulldescriptionpropertyid"></span><span id="UIA_FULLDESCRIPTIONPROPERTYID"></span><dl> <dt><strong>UIA_FullDescriptionPropertyId</strong></dt> <dt>30159</dt> </dl></td>
<td style="text-align: left;">The <strong>FullDescription</strong> property exposes a localized string which can contain extended description text for an element. <strong>FullDescription</strong> can contain a more complete description of an element than may be appropriate for the element <strong>Name</strong>.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_HasKeyboardFocusPropertyId"></span><span id="uia_haskeyboardfocuspropertyid"></span><span id="UIA_HASKEYBOARDFOCUSPROPERTYID"></span><dl> <dt><strong>UIA_HasKeyboardFocusPropertyId</strong></dt> <dt>30008</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>HasKeyboardFocus</strong> property, which is a Boolean value that indicates whether the automation element has keyboard focus.<br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_HeadingLevelPropertyId"></span><span id="uia_headinglevelpropertyid"></span><span id="UIA_HEADINGLEVELPROPERTYID"></span><dl> <dt><strong>UIA_HeadingLevelPropertyId</strong></dt> <dt>30173</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>HeadingLevel</strong> property, which indicates the heading level of a UI Automation element.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: <strong>HeadingLevel_None</strong><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_HelpTextPropertyId"></span><span id="uia_helptextpropertyid"></span><span id="UIA_HELPTEXTPROPERTYID"></span><dl> <dt><strong>UIA_HelpTextPropertyId</strong></dt> <dt>30013</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>HelpText</strong> property, which is a help text string associated with the automation element.<br/> The <strong>HelpText</strong> property can be supported with placeholder text appearing in edit or list controls. For example, &quot;Type text here for search&quot; is a good candidate the <strong>HelpText</strong> property for an edit control that places the text prior to the user's actual input. However, it is not adequate for the name property of the edit control.<br/> When <strong>HelpText</strong> is supported, the string must match the application UI language or the operating system default UI language.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_IsContentElementPropertyId"></span><span id="uia_iscontentelementpropertyid"></span><span id="UIA_ISCONTENTELEMENTPROPERTYID"></span><dl> <dt><strong>UIA_IsContentElementPropertyId</strong></dt> <dt>30017</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsContentElement</strong> property, which is a Boolean value that specifies whether the element appears in the content view of the automation element tree. For more information, see <a href="uiauto-treeoverview.md">UI Automation Tree Overview</a>.<br/>
<blockquote>
[!Note]<br />
For an element to appear in the content view, both the <strong>IsContentElement</strong> property and the <strong>IsControlElement</strong> property must be <strong>TRUE</strong>.
</blockquote>
<br/> <br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>TRUE</strong><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_IsControlElementPropertyId"></span><span id="uia_iscontrolelementpropertyid"></span><span id="UIA_ISCONTROLELEMENTPROPERTYID"></span><dl> <dt><strong>UIA_IsControlElementPropertyId</strong></dt> <dt>30016</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsControlElement</strong> property, which is a Boolean value that specifies whether the element appears in the control view of the automation element tree. For more information, see <a href="uiauto-treeoverview.md">UI Automation Tree Overview</a>.<br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>TRUE</strong><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_IsDataValidForFormPropertyId"></span><span id="uia_isdatavalidforformpropertyid"></span><span id="UIA_ISDATAVALIDFORFORMPROPERTYID"></span><dl> <dt><strong>UIA_IsDataValidForFormPropertyId</strong></dt> <dt>30103</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsDataValidForForm</strong> property, which is a Boolean value that indicates whether the entered or selected value is valid for the form rule associated with the automation element. For example, if the user entered &quot;425-555-5555&quot; for a zip code field that requires 5 or 9 digits, the <strong>IsDataValidForForm</strong> property can be set to <strong>FALSE</strong> to indicate that the data is not valid.<br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>

<tr class="odd">
<td style="text-align: left;"><span id="UIA_IsDialogPropertyId"></span><span id="uia_isdialogpropertyid"></span><span id="UIA_ISDIALOGPROPERTYID"></span><dl> <dt><strong>UIA_IsDialogPropertyId</strong></dt> <dt>30174</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsDialog</strong> property, which is a Boolean value that indicates whether the automation element is a dialog window. For example, assistive technology such as screen readers typically speak the title of the dialog, the focused control in the dialog, and then the content of the dialog up to the focused control (&quot;Do you want to save your changes before closing&quot;). For standard windows, a screen reader typically speaks the window title followed by the focused control. The <strong>IsDialog</strong> property can be set to <strong>TRUE</strong> to indicate that the client application should treat the element as a dialog window.<br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>

<tr class="even">
<td style="text-align: left;"><span id="UIA_IsEnabledPropertyId"></span><span id="uia_isenabledpropertyid"></span><span id="UIA_ISENABLEDPROPERTYID"></span><dl> <dt><strong>UIA_IsEnabledPropertyId</strong></dt> <dt>30010</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsEnabled</strong> property, which is a Boolean value that indicates whether the UI item referenced by the automation element is enabled and can be interacted with.<br/> When the enabled state of a control is <strong>FALSE</strong>, it is assumed that child controls are also not enabled. Clients should not expect property-changed events from child elements when the state of the parent control changes.<br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_IsKeyboardFocusablePropertyId"></span><span id="uia_iskeyboardfocusablepropertyid"></span><span id="UIA_ISKEYBOARDFOCUSABLEPROPERTYID"></span><dl> <dt><strong>UIA_IsKeyboardFocusablePropertyId</strong></dt> <dt>30009</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsKeyboardFocusable</strong> property, which is a Boolean value that indicates whether the automation element can accept keyboard focus.<br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_IsOffscreenPropertyId"></span><span id="uia_isoffscreenpropertyid"></span><span id="UIA_ISOFFSCREENPROPERTYID"></span><dl> <dt><strong>UIA_IsOffscreenPropertyId</strong></dt> <dt>30022</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsOffscreen</strong> property, which is a Boolean value that indicates whether the automation element is entirely scrolled out of view (for example, an item in a list box that is outside the viewport of the container object) or collapsed out of view (for example, an item in a tree view or menu, or in a minimized window). If the element has a clickable point that can cause it to receive the focus, the element is considered to be on-screen while a portion of the element is off-screen.<br/> The value of the property is not affected by occlusion by other windows, or by whether the element is visible on a specific monitor.<br/> If the <strong>IsOffscreen</strong> property is <strong>TRUE</strong>, the UI element is scrolled off-screen or collapsed. The element is temporarily hidden, yet it remains in the end-user's perception and continues to be included in the UI model. The object can be brought back into view by scrolling, clicking a drop-down, and so on.<br/> Objects that the end-user does not perceive at all, or that are &quot;programmatically hidden&quot; (for example, a dialog box that has been dismissed, but the underlying object is still cached by the application) should not be in the automation element tree in the first place (instead of setting the state of <strong>IsOffscreen</strong> to <strong>TRUE</strong>).<br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_IsPasswordPropertyId"></span><span id="uia_ispasswordpropertyid"></span><span id="UIA_ISPASSWORDPROPERTYID"></span><dl> <dt><strong>UIA_IsPasswordPropertyId</strong></dt> <dt>30019</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsPassword</strong> property, which is a Boolean value that indicates whether the automation element contains protected content or a password.<br/> When the <strong>IsPassword</strong> property is <strong>TRUE</strong> and the element has the keyboard focus, a client application should disable keyboard echoing or keyboard input feedback that may expose the user's protected information. Attempting to access the <strong>Value</strong> property of the protected element (edit control) may cause an error to occur.<br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_IsPeripheralPropertyId"></span><span id="uia_isperipheralpropertyid"></span><span id="UIA_ISPERIPHERALPROPERTYID"></span><dl> <dt><strong>UIA_IsPeripheralPropertyId</strong></dt> <dt>30150</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsPeripheral</strong> property, which is a Boolean value that indicates whether the automation element represents peripheral UI. Peripheral UI appears and supports user interaction, but does not take keyboard focus when it appears. Examples of peripheral UI includes popups, flyouts, context menus, or floating notifications. Supported starting with Windows 8.1.<br/> When the <strong>IsPeripheral</strong> property is <strong>TRUE</strong>, a client application can't assume that focus was taken by the element even if it's currently keyboard-interactive.<br/> This property is relevant for these control types:<br/>
<ul>
<li><strong>UIA_GroupControlTypeId</strong></li>
<li><strong>UIA_MenuControlTypeId</strong></li>
<li><strong>UIA_PaneControlTypeId</strong></li>
<li><strong>UIA_ToolBarControlTypeId</strong></li>
<li><strong>UIA_ToolTipControlTypeId</strong></li>
<li><strong>UIA_WindowControlTypeId</strong></li>
<li><strong>UIA_CustomControlTypeId</strong></li>
</ul>
Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_IsRequiredForFormPropertyId"></span><span id="uia_isrequiredforformpropertyid"></span><span id="UIA_ISREQUIREDFORFORMPROPERTYID"></span><dl> <dt><strong>UIA_IsRequiredForFormPropertyId</strong></dt> <dt>30025</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsRequiredForForm</strong> property, which is a Boolean value that indicates whether the automation element is required to be filled out on a form.<br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_ItemStatusPropertyId"></span><span id="uia_itemstatuspropertyid"></span><span id="UIA_ITEMSTATUSPROPERTYID"></span><dl> <dt><strong>UIA_ItemStatusPropertyId</strong></dt> <dt>30026</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>ItemStatus</strong> property, which is a text string describing the status of an item of the automation element.<br/> <strong>ItemStatus</strong> enables a client to ascertain whether an element is conveying status about an item as well as what the status is. For example, an item associated with a contact in a messaging application might be &quot;Busy&quot; or &quot;Connected&quot;.<br/> When <strong>ItemStatus</strong> is supported, the string must match the application UI language or the operating system default UI language.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_ItemTypePropertyId"></span><span id="uia_itemtypepropertyid"></span><span id="UIA_ITEMTYPEPROPERTYID"></span><dl> <dt><strong>UIA_ItemTypePropertyId</strong></dt> <dt>300021</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>ItemType</strong> property, which is a text string describing the type of the automation element.<br/> <strong>ItemType</strong> is used to obtain information about items in a list, tree view, or data grid. For example, an item in a file directory view might be a &quot;Document File&quot; or a &quot;Folder&quot;.<br/> When <strong>ItemType</strong> is supported, the string must match the application UI language or the operating system default UI language.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_LabeledByPropertyId"></span><span id="uia_labeledbypropertyid"></span><span id="UIA_LABELEDBYPROPERTYID"></span><dl> <dt><strong>UIA_LabeledByPropertyId</strong></dt> <dt>30018</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>LabeledBy</strong> property, which is an automation element that contains the text label for this element.<br/> This property can be used to retrieve, for example, the static text label for a combo box.<br/> Variant type: <strong>VT_UNKNOWN</strong><br/> Default value: <strong>NULL</strong><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_LandmarkTypePropertyId"></span><span id="uia_landmarktypepropertyid"></span><span id="UIA_LANDMARKTYPEPROPERTYID"></span><dl> <dt><strong>UIA_LandmarkTypePropertyId</strong></dt> <dt>30157</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>LandmarkType</strong> property, which is a <a href="landmark-type-identifiers.md"><strong>Landmark Type Identifier</strong></a> associated with an element.<br/> The <strong>LandmarkType</strong> property describes an element that represents a group of elements. For example, a search landmark could represent a set of related controls for searching.<br/> If <a href="landmark-type-identifiers.md"><strong>UIA_CustomLandmarkTypeId</strong></a> is used then <strong>UIA_LocalizedLandmarkTypePropertyId</strong> is required to describe the custom landmark.<br/> Variant Type: <strong>VT_I4</strong><br/> Default Value: 0<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_LevelPropertyId"></span><span id="uia_levelpropertyid"></span><span id="UIA_LEVELPROPERTYID"></span><dl> <dt><strong>UIA_LevelPropertyId</strong></dt> <dt>30154</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>Level</strong> property, which is a 1-based integer associated with an automation element.<br/> The <strong>Level</strong> property describes the location of an element inside a hierarchical or broken hierarchical structures. For example a bulleted/numbered list, headings, or other structured data items can have various parent/child relationships. <strong>Level</strong> describes where in the structure the item is located.<br/> It is recommended to use the <a href="/windows/desktop/WinAuto/uiauto-implementingcustomnavigation">CustomNavigation Control Pattern</a> in tandem with <strong>Level</strong>.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_LiveSettingPropertyId"></span><span id="uia_livesettingpropertyid"></span><span id="UIA_LIVESETTINGPROPERTYID"></span><dl> <dt><strong>UIA_LiveSettingPropertyId</strong></dt> <dt>30135</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>LiveSetting</strong> property, which is supported by an automation element that represents a live region. The <strong>LiveSetting</strong> property indicates the &quot;politeness&quot; level that a client should use to notify the user of changes to the live region. This property can be one of the values from the <a href="/windows/desktop/api/uiautomationcore/ne-uiautomationcore-livesetting"><strong>LiveSetting</strong></a> enumeration. Supported starting with Windows 8.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_LocalizedControlTypePropertyId"></span><span id="uia_localizedcontroltypepropertyid"></span><span id="UIA_LOCALIZEDCONTROLTYPEPROPERTYID"></span><dl> <dt><strong>UIA_LocalizedControlTypePropertyId</strong></dt> <dt>30004</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>LocalizedControlType</strong> property, which is a text string describing the type of control that the automation element represents. The string should contain only lowercase characters:
<ul>
<li>Correct: &quot;button&quot;</li>
<li>Incorrect: &quot;Button&quot;</li>
</ul>
<br/> When <strong>LocalizedControlType</strong> is not specified by the element provider, the default localized string is supplied by the framework, according to the control type of the element (for example, &quot;button&quot; for the <a href="uiauto-supportbuttoncontroltype.md">Button</a> control type). An automation element with the <strong>Custom</strong> control type must support a localized control type string that represents the role of the element (for example, &quot;color picker&quot; for a custom control that enables users to choose and specify colors).<br/> When a custom value is supplied, the string must match the application UI language or the operating system default UI language.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_LocalizedLandmarkTypePropertyId"></span><span id="uia_localizedlandmarktypepropertyid"></span><span id="UIA_LOCALIZEDLANDMARKTYPEPROPERTYID"></span><dl> <dt><strong>UIA_LocalizedLandmarkTypePropertyId</strong></dt> <dt>30158</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>LocalizedLandmarkType</strong>, which is a text string describing the type of landmark that the automation element represents.<br/> This should be used in tandem with <a href="landmark-type-identifiers.md"><strong>UIA_CustomLandmarkTypeId</strong></a> however, <strong>LocalizedLandmarkType</strong> should always take precedence over <strong>LandmarkType</strong> and be used to describe the landmark before <strong>LandmarkType</strong>.<br/> The string must match the application UI language or the operating system default UI language.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_NamePropertyId"></span><span id="uia_namepropertyid"></span><span id="UIA_NAMEPROPERTYID"></span><dl> <dt><strong>UIA_NamePropertyId</strong></dt> <dt>30005</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>Name</strong> property, which is a string that holds the name of the automation element.<br/> The <strong>Name</strong> property should be the same as the label text on screen. For example, <strong>Name</strong> should be &quot;Browse&quot; for a button element with the label &quot;Browse&quot;. The <strong>Name</strong> property must not include the mnemonic character for the access keys (that is, &quot;&&quot;), which is underlined in the UI text presentation. Also, the <strong>Name</strong> property should not be an extended or modified version of the on-screen label because the inconsistency between the name and the label can cause confusion among client applications and users.<br/> When the corresponding label text is not visible on screen, or when it is replaced by graphics, alternative text should be chosen. The alternative text should be concise, intuitive, and localized to the application UI language, or to the operating system default UI language. The alternative text should not be a detailed description of the visual details, but a concise description of the UI function or feature as if it were labeled by simple text. For example, the Windows Start menu button is named &quot;Start&quot; (button) instead of &quot;Windows Logo on blue round sphere graphics&quot; (button). For more information, see <a href="/previous-versions/windows/desktop/dnacc/creating-text-equivalents-for-images">Creating Text Equivalents for Images</a>.<br/> When a UI label uses text graphics (for example, using &quot;>>&quot; for a button that adds an item from left to right), the <strong>Name</strong> property should be overridden by an appropriate text alternative (for example, &quot;Add&quot;). However the practice of using text graphics as a UI label is discouraged due to both localization and accessibility concerns.<br/> The <strong>Name</strong> property must not include the control role or type information, such as &quot;button&quot; or &quot;list&quot;; otherwise, it will conflict with the text from the <strong>LocalizedControlType</strong> property when these two properties are appended (many existing assistive technologies do this).<br/> The <strong>Name</strong> property cannot be used as a unique identifier among siblings. However, as long as it is consistent with the UI presentation, the same <strong>Name</strong> value can be supported among peers. For test automation, the clients should consider using the <strong>AutomationId</strong> or <strong>RuntimeId</strong> property.<br/> Text controls do not always have to have the <strong>Name</strong> property be identical to the text that is displayed within the control, so long as the <strong>Text</strong> pattern is also supported.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_NativeWindowHandlePropertyId"></span><span id="uia_nativewindowhandlepropertyid"></span><span id="UIA_NATIVEWINDOWHANDLEPROPERTYID"></span><dl> <dt><strong>UIA_NativeWindowHandlePropertyId</strong></dt> <dt>30020</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>NativeWindowHandle</strong> property, which is an integer that represents the handle (<strong>HWND</strong>) of the automation element window, if it exists; otherwise, this property is 0.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_OptimizeForVisualContentPropertyId"></span><span id="uia_optimizeforvisualcontentpropertyid"></span><span id="UIA_OPTIMIZEFORVISUALCONTENTPROPERTYID"></span><dl> <dt><strong>UIA_OptimizeForVisualContentPropertyId</strong></dt> <dt>30111</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>OptimizeForVisualContent</strong> property, which is a Boolean value that indicates whether the provider exposes only elements that are visible. A provider can use this property to optimize performance when working with very large pieces of content. For example, as the user pages through a large piece of content, the provider can destroy content elements that are no longer visible. When a content element is destroyed, the provider should return the <strong>UIA_E_ELEMENTNOTAVAILABLE</strong> error code. Supported starting with Windows 8.<br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_OrientationPropertyId"></span><span id="uia_orientationpropertyid"></span><span id="UIA_ORIENTATIONPROPERTYID"></span><dl> <dt><strong>UIA_OrientationPropertyId</strong></dt> <dt>300023</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>Orientation</strong> property, which indicates the orientation of the control represented by the automation element. The property is expressed as a value from the <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-orientationtype"><strong>OrientationType</strong></a> enumerated type.<br/> The <strong>Orientation</strong> property is supported by controls, such as scroll bars and sliders, that can have either a vertical or a horizontal orientation. Otherwise, it can always be <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-orientationtype"><strong>OrientationType_None</strong></a>, which means that the control has no orientation.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0 (<a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-orientationtype"><strong>OrientationType_None</strong></a>)<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_OutlineColorPropertyId"></span><span id="uia_outlinecolorpropertyid"></span><span id="UIA_OUTLINECOLORPROPERTYID"></span><dl> <dt><strong>UIA_OutlineColorPropertyId</strong></dt> <dt>30161</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>OutlineColor</strong> property, which specifies the color used for the outline of the automation element. This attribute is specified as a <strong>COLORREF</strong>, a 32-bit value used to specify an RGB or RGBA color.<br/> Variant type: <strong>VT_I4</strong> | <strong>VT_ARRAY</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_OutlineThicknessPropertyId"></span><span id="uia_outlinethicknesspropertyid"></span><span id="UIA_OUTLINETHICKNESSPROPERTYID"></span><dl> <dt><strong>UIA_OutlineThicknessPropertyId</strong></dt> <dt>30164</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>OutlineThickness</strong> property, which specifies the width for the outline of the automation element.<br/> Variant type: <strong>VT_R8</strong> | <strong>VT_ARRAY</strong><br/> Default value: <strong>VT_EMPTY</strong><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_PositionInSetPropertyId"></span><span id="uia_positioninsetpropertyid"></span><span id="UIA_POSITIONINSETPROPERTYID"></span><dl> <dt><strong>UIA_PositionInSetPropertyId</strong></dt> <dt>30152</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>PositionInSet</strong> property, which is a 1-based integer associated with an automation element. <strong>PositionInSet</strong> describes the ordinal location of the element within a set of elements which are considered to be siblings.<br/> <strong>PositionInSet</strong> works in coordination with the <strong>SizeOfSet</strong> property to describe the ordinal location in the set.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_ProcessIdPropertyId"></span><span id="uia_processidpropertyid"></span><span id="UIA_PROCESSIDPROPERTYID"></span><dl> <dt><strong>UIA_ProcessIdPropertyId</strong></dt> <dt>30002</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>ProcessId</strong> property, which is an integer representing the process identifier (ID) of the automation element.<br/> The process identifier (ID) is assigned by the operating system. It can be seen in the <strong>PID</strong> column of the <strong>Processes</strong> tab in Task Manager.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_ProviderDescriptionPropertyId"></span><span id="uia_providerdescriptionpropertyid"></span><span id="UIA_PROVIDERDESCRIPTIONPROPERTYID"></span><dl> <dt><strong>UIA_ProviderDescriptionPropertyId</strong></dt> <dt>30107</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>ProviderDescription</strong> property, which is a formatted string containing the source information of the UI Automation provider for the automation element, including proxy information.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_RotationPropertyId"></span><span id="uia_rotationpropertyid"></span><span id="UIA_ROTATIONPROPERTYID"></span><dl> <dt><strong>UIA_RotationPropertyId</strong></dt> <dt>30166</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>Rotation</strong> property, which specifies the angle of rotation in unspecified units.<br/> Variant type: <strong>VT_R8</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_RuntimeIdPropertyId"></span><span id="uia_runtimeidpropertyid"></span><span id="UIA_RUNTIMEIDPROPERTYID"></span><dl> <dt><strong>UIA_RuntimeIdPropertyId</strong></dt> <dt>30000</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>RuntimeId</strong> property, which is an array of integers representing the identifier for an automation element.<br/> The identifier is unique on the desktop, but it is guaranteed to be unique only within the UI of the desktop on which it was generated. Identifiers can be reused over time.<br/> The format of <strong>RuntimeId</strong> can change. The returned identifier should be treated as an opaque value and used only for comparison; for example, to determine whether an automation element is in the cache.<br/> Variant type: <strong>VT_I4</strong> | <strong>VT_ARRAY</strong><br/> Default value: <strong>VT_EMPTY</strong><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_SizePropertyId"></span><span id="uia_sizepropertyid"></span><span id="UIA_SIZEPROPERTYID"></span><dl> <dt><strong>UIA_SizePropertyId</strong></dt> <dt>30167</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>Size</strong> property, which specifies the width and height of the automation element.<br/> Variant type: <strong>VT_R8</strong> | <strong>VT_ARRAY</strong><br/> Default value: <strong>VT_EMPTY</strong><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_SizeOfSetPropertyId"></span><span id="uia_sizeofsetpropertyid"></span><span id="UIA_SIZEOFSETPROPERTYID"></span><dl> <dt><strong>UIA_SizeOfSetPropertyId</strong></dt> <dt>30153</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>SizeOfSet</strong> property, which is a 1-based integer associated with an automation element. <strong>SizeOfSet</strong> describes the count of automation elements in a group or set that are considered to be siblings.<br/> <strong>SizeOfSet</strong> works in coordination with the <strong>PositionInSet</strong> property to describe the count of items in the set.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_VisualEffectsPropertyId"></span><span id="uia_visualeffectspropertyid"></span><span id="UIA_VISUALEFFECTSPROPERTYID"></span><dl> <dt><strong>UIA_VisualEffectsPropertyId</strong></dt> <dt>30163</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>VisualEffects</strong> property, which is a bit field that specifies effects on the automation element, such as shadow, reflection, glow, soft edges, or bevel.<br/> VisualEffects:<br/>
<ul>
<li>VisualEffects_Shadow: 0x1</li>
<li>VisualEffects_Reflection: 0x2</li>
<li>VisualEffects_Glow: 0x4</li>
<li>VisualEffects_SoftEdges: 0x8</li>
<li>VisualEffects_Bevel: 0x10</li>
</ul>
Variant type: <strong>VT_I4</strong><br/> Default value: 0<br/></td>
</tr>
</tbody>
</table>



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps \| UWP apps\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps \| UWP apps\]<br/>                                     |
| Header<br/>                   | <dl> <dt>UIAutomationClient.h</dt> </dl> |



## See also

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Properties Overview](uiauto-propertiesoverview.md)
</dt> <dt>

[Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md)
</dt> </dl>
