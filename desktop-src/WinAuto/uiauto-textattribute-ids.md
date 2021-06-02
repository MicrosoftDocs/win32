---
title: Text Attribute Identifiers (UIAutomationClient.h)
description: This topic describes the named constants used to identify text attributes of a Microsoft UI Automation text range.
ms.assetid: 67d86817-6a3f-4047-88d9-34f33f52a563
topic_type:
- apiref
api_name:
- UIA_AfterParagraphSpacingAttributeId
- UIA_AnimationStyleAttributeId
- UIA_AnnotationObjectsAttributeId
- UIA_AnnotationTypesAttributeId
- UIA_BackgroundColorAttributeId
- UIA_BeforeParagraphSpacingAttributeId
- UIA_BulletStyleAttributeId
- UIA_CapStyleAttributeId
- UIA_CaretBidiModeAttributeId
- UIA_CaretPositionAttributeId
- UIA_CultureAttributeId
- UIA_FontNameAttributeId
- UIA_FontSizeAttributeId
- UIA_FontWeightAttributeId
- UIA_ForegroundColorAttributeId
- UIA_HorizontalTextAlignmentAttributeId
- UIA_IndentationFirstLineAttributeId
- UIA_IndentationLeadingAttributeId
- UIA_IndentationTrailingAttributeId
- UIA_IsActiveAttributeId
- UIA_IsHiddenAttributeId
- UIA_IsItalicAttributeId
- UIA_IsReadOnlyAttributeId
- UIA_IsSubscriptAttributeId
- UIA_IsSuperscriptAttributeId
- UIA_LineSpacingAttributeId
- UIA_LinkAttributeId
- UIA_MarginBottomAttributeId
- UIA_MarginLeadingAttributeId
- UIA_MarginTopAttributeId
- UIA_MarginTrailingAttributeId
- UIA_OutlineStylesAttributeId
- UIA_OverlineColorAttributeId
- UIA_OverlineStyleAttributeId
- UIA_SelectionActiveEndAttributeId
- UIA_StrikethroughColorAttributeId
- UIA_StrikethroughStyleAttributeId
- UIA_StyleIdAttributeId
- UIA_StyleNameAttributeId
- UIA_TabsAttributeId
- UIA_TextFlowDirectionsAttributeId
- UIA_UnderlineColorAttributeId
- UIA_UnderlineStyleAttributeId
api_location:
- UIAutomationClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Text Attribute Identifiers

This topic describes the named constants used to identify text attributes of a Microsoft UI Automation text range. These constants are used with the following methods:

-   [**ITextRangeProvider::FindAttribute**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextrangeprovider-findattribute)
-   [**ITextRangeProvider::GetAttributeValue**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextrangeprovider-getattributevalue)
-   [**IUIAutomationTextRange::FindAttribute**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextrange-findattribute)
-   [**IUIAutomationTextRange::GetAttributeValue**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextrange-getattributevalue)



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
<td style="text-align: left;"><span id="UIA_AfterParagraphSpacingAttributeId"></span><span id="uia_afterparagraphspacingattributeid"></span><span id="UIA_AFTERPARAGRAPHSPACINGATTRIBUTEID"></span><dl> <dt><strong>UIA_AfterParagraphSpacingAttributeId</strong></dt> <dt>40042</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>AfterParagraphSpacing</strong> text attribute, which specifies the size of spacing after the paragraph.<br/> Variant type: <strong>VT_R8</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_AnimationStyleAttributeId"></span><span id="uia_animationstyleattributeid"></span><span id="UIA_ANIMATIONSTYLEATTRIBUTEID"></span><dl> <dt><strong>UIA_AnimationStyleAttributeId</strong></dt> <dt>40000</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>AnimationStyle</strong> text attribute, which specifies the type of animation applied to the text. This attribute is specified as a value from the <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-animationstyle"><strong>AnimationStyle</strong></a> enumerated type. <br/> Variant type: <strong>VT_I4</strong><br/> Default value: <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-animationstyle"><strong>AnimationStyle_None</strong></a><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_AnnotationObjectsAttributeId"></span><span id="uia_annotationobjectsattributeid"></span><span id="UIA_ANNOTATIONOBJECTSATTRIBUTEID"></span><dl> <dt><strong>UIA_AnnotationObjectsAttributeId</strong></dt> <dt>40032</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>AnnotationObjects</strong> text attribute, which maintains an array of <a href="/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement2"><strong>IUIAutomationElement2</strong></a> interfaces, one for each element in the current text range that implements the <a href="uiauto-implementingannotation.md">Annotation</a> control pattern. Each element might also implement other control patterns as needed to describe the annotation. For example, an annotation that is a comment would also support the <a href="uiauto-implementingtextandtextrange.md">Text</a> control pattern. Supported starting with Windows 8.<br/> Variant type: <strong>VT_UNKNOWN</strong><br/> Default value: empty array <br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_AnnotationTypesAttributeId"></span><span id="uia_annotationtypesattributeid"></span><span id="UIA_ANNOTATIONTYPESATTRIBUTEID"></span><dl> <dt><strong>UIA_AnnotationTypesAttributeId</strong></dt> <dt>40031</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>AnnotationTypes</strong> text attribute, which maintains a list of annotation type identifiers for a range of text. For a list of possible values, see <a href="uiauto-annotation-type-identifiers.md"><strong>Annotation Type Identifiers</strong></a>. Supported starting with Windows 8.<br/> Variant type: <strong>VT_ARRAY</strong> | <strong>VT_I4</strong><br/> Default value: empty array <br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_BackgroundColorAttributeId"></span><span id="uia_backgroundcolorattributeid"></span><span id="UIA_BACKGROUNDCOLORATTRIBUTEID"></span><dl> <dt><strong>UIA_BackgroundColorAttributeId</strong></dt> <dt>40001</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>BackgroundColor</strong> text attribute, which specifies the background color of the text. This attribute is specified as a <a href="/windows/win32/gdi/colorref">COLORREF</a>; a 32-bit value used to specify an RGB or RGBA color. <br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0 <br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_BeforeParagraphSpacingAttributeId"></span><span id="uia_beforeparagraphspacingattributeid"></span><span id="UIA_BEFOREPARAGRAPHSPACINGATTRIBUTEID"></span><dl> <dt><strong>UIA_BeforeParagraphSpacingAttributeId</strong></dt> <dt>40041</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>BeforeParagraphSpacing</strong> text attribute, which specifies the size of spacing before the paragraph.<br/> Variant type: <strong>VT_R8</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_BulletStyleAttributeId"></span><span id="uia_bulletstyleattributeid"></span><span id="UIA_BULLETSTYLEATTRIBUTEID"></span><dl> <dt><strong>UIA_BulletStyleAttributeId</strong></dt> <dt>40002</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>BulletStyle</strong> text attribute, which specifies the style of bullets used in the text range. This attribute is specified as a value from the <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-bulletstyle"><strong>BulletStyle</strong></a> enumerated type.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-bulletstyle"><strong>BulletStyle_None</strong></a><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_CapStyleAttributeId"></span><span id="uia_capstyleattributeid"></span><span id="UIA_CAPSTYLEATTRIBUTEID"></span><dl> <dt><strong>UIA_CapStyleAttributeId</strong></dt> <dt>40003</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>CapStyle</strong> text attribute, which specifies the capitalization style for the text. This attribute is specified as a value from the <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-capstyle"><strong>CapStyle</strong></a> enumerated type. <br/> Variant type: <strong>VT_I4</strong><br/> Default value: <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-capstyle"><strong>CapStyle_None</strong></a><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_CaretBidiModeAttributeId"></span><span id="uia_caretbidimodeattributeid"></span><span id="UIA_CARETBIDIMODEATTRIBUTEID"></span><dl> <dt><strong>UIA_CaretBidiModeAttributeId</strong></dt> <dt>40039</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>CaretBidiMode</strong> text attribute, which indicates the direction of text flow in the text range. This attribute is specified as a value from the <a href="/windows/desktop/api/uiautomationcore/ne-uiautomationcore-caretbidimode"><strong>CaretBidiMode</strong></a> enumerated type. Supported starting with Windows 8.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: <a href="/windows/desktop/api/uiautomationcore/ne-uiautomationcore-caretbidimode"><strong>CaretBidiMode_LTR</strong></a><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_CaretPositionAttributeId"></span><span id="uia_caretpositionattributeid"></span><span id="UIA_CARETPOSITIONATTRIBUTEID"></span><dl> <dt><strong>UIA_CaretPositionAttributeId</strong></dt> <dt>40038</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>CaretPosition</strong> text attribute, which indicates whether the caret is at the beginning or the end of a line of text in the text range. This attribute is specified as a value from the <a href="/windows/desktop/api/uiautomationcore/ne-uiautomationcore-caretposition"><strong>CaretPosition</strong></a> enumerated type. Supported starting with Windows 8.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: <a href="/windows/desktop/api/uiautomationcore/ne-uiautomationcore-caretposition"><strong>CaretPosition_Unknown</strong></a><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_CultureAttributeId"></span><span id="uia_cultureattributeid"></span><span id="UIA_CULTUREATTRIBUTEID"></span><dl> <dt><strong>UIA_CultureAttributeId</strong></dt> <dt>40004</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>Culture</strong> text attribute, which specifies the locale of the text by locale identifier (LCID). <br/> Variant type: <strong>VT_I4</strong><br/> Default value: locale of the application UI<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_FontNameAttributeId"></span><span id="uia_fontnameattributeid"></span><span id="UIA_FONTNAMEATTRIBUTEID"></span><dl> <dt><strong>UIA_FontNameAttributeId</strong></dt> <dt>40005</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>FontName</strong> text attribute, which specifies the name of the font. Examples: &quot;Arial Black&quot;; &quot;Arial Narrow&quot;. The font name string is not localized. <br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_FontSizeAttributeId"></span><span id="uia_fontsizeattributeid"></span><span id="UIA_FONTSIZEATTRIBUTEID"></span><dl> <dt><strong>UIA_FontSizeAttributeId</strong></dt> <dt>40006</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>FontSize</strong> text attribute, which specifies the point size of the font. <br/> Variant type: <strong>VT_R8</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_FontWeightAttributeId"></span><span id="uia_fontweightattributeid"></span><span id="UIA_FONTWEIGHTATTRIBUTEID"></span><dl> <dt><strong>UIA_FontWeightAttributeId</strong></dt> <dt>40007</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>FontWeight</strong> text attribute, which specifies the relative stroke, thickness, or boldness of the font. The <strong>FontWeight</strong> attribute is modeled after the <strong>lfWeight</strong> member of the GDI <a href="/windows/win32/api/wingdi/ns-wingdi-logfonta">LOGFONT</a> structure, and related standards, and can be one of the following values:
<ul>
<li>0 = <strong>DontCare</strong></li>
<li>100 = <strong>Thin</strong></li>
<li>200 = <strong>ExtraLight</strong> or <strong>UltraLight</strong></li>
<li>300 = <strong>Light</strong></li>
<li>400 = <strong>Normal</strong> or <strong>Regular</strong></li>
<li>500 = <strong>Medium</strong></li>
<li>600 = <strong>SemiBold</strong></li>
<li>700 = <strong>Bold</strong></li>
<li>800 = <strong>ExtraBold</strong> or <strong>UltraBold</strong></li>
<li>900 = <strong>Heavy</strong> or <strong>Black</strong></li>
</ul>
<br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_ForegroundColorAttributeId"></span><span id="uia_foregroundcolorattributeid"></span><span id="UIA_FOREGROUNDCOLORATTRIBUTEID"></span><dl> <dt><strong>UIA_ForegroundColorAttributeId</strong></dt> <dt>40008</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>ForegroundColor</strong> text attribute, which specifies the foreground color of the text. This attribute is specified as a <a href="/windows/win32/gdi/colorref">COLORREF</a>, a 32-bit value used to specify an RGB or RGBA color. <br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_HorizontalTextAlignmentAttributeId"></span><span id="uia_horizontaltextalignmentattributeid"></span><span id="UIA_HORIZONTALTEXTALIGNMENTATTRIBUTEID"></span><dl> <dt><strong>UIA_HorizontalTextAlignmentAttributeId</strong></dt> <dt>40009</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>HorizontalTextAlignment</strong> text attribute, which specifies how the text is aligned horizontally. This attribute is specified as a value from the <a href="/previous-versions/windows/desktop/legacy/ee671233(v=vs.85)"><strong>HorizontalTextAlignmentEnum</strong></a> enumerated type. <br/> Variant type: <strong>VT_I4</strong><br/> Default value: <a href="/previous-versions/windows/desktop/legacy/ee671233(v=vs.85)"><strong>HorizontalTextAlignment_Left</strong></a><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_IndentationFirstLineAttributeId"></span><span id="uia_indentationfirstlineattributeid"></span><span id="UIA_INDENTATIONFIRSTLINEATTRIBUTEID"></span><dl> <dt><strong>UIA_IndentationFirstLineAttributeId</strong></dt> <dt>40010</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IndentationFirstLine</strong> text attribute, which specifies how far, in points, to indent the first line of a paragraph. <br/> Variant type: <strong>VT_R8</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_IndentationLeadingAttributeId"></span><span id="uia_indentationleadingattributeid"></span><span id="UIA_INDENTATIONLEADINGATTRIBUTEID"></span><dl> <dt><strong>UIA_IndentationLeadingAttributeId</strong></dt> <dt>40011</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IndentationLeading</strong> text attribute, which specifies the leading indentation, in points. <br/> Variant type: <strong>VT_R8</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_IndentationTrailingAttributeId"></span><span id="uia_indentationtrailingattributeid"></span><span id="UIA_INDENTATIONTRAILINGATTRIBUTEID"></span><dl> <dt><strong>UIA_IndentationTrailingAttributeId</strong></dt> <dt>40012</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IndentationTrailing</strong> text attribute, which specifies the trailing indentation, in points. <br/> Variant type: <strong>VT_R8</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_IsActiveAttributeId"></span><span id="uia_isactiveattributeid"></span><span id="UIA_ISACTIVEATTRIBUTEID"></span><dl> <dt><strong>UIA_IsActiveAttributeId</strong></dt> <dt>40036</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsActive</strong> text attribute, which indicates whether the control that contains the text range has the keyboard focus (<strong>TRUE</strong>) or not (<strong>FALSE</strong>). Supported starting with Windows 8.<br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_IsHiddenAttributeId"></span><span id="uia_ishiddenattributeid"></span><span id="UIA_ISHIDDENATTRIBUTEID"></span><dl> <dt><strong>UIA_IsHiddenAttributeId</strong></dt> <dt>40013</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsHidden</strong> text attribute, which indicates whether the text is hidden (<strong>TRUE</strong>) or visible (<strong>FALSE</strong>). <br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_IsItalicAttributeId"></span><span id="uia_isitalicattributeid"></span><span id="UIA_ISITALICATTRIBUTEID"></span><dl> <dt><strong>UIA_IsItalicAttributeId</strong></dt> <dt>40014</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsItalic</strong> text attribute, which indicates whether the text is italic (<strong>TRUE</strong>) or not (<strong>FALSE</strong>). <br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_IsReadOnlyAttributeId"></span><span id="uia_isreadonlyattributeid"></span><span id="UIA_ISREADONLYATTRIBUTEID"></span><dl> <dt><strong>UIA_IsReadOnlyAttributeId</strong></dt> <dt>40015</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsReadOnly</strong> text attribute, which indicates whether the text is read-only (<strong>TRUE</strong>) or can be modified (<strong>FALSE</strong>). <br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_IsSubscriptAttributeId"></span><span id="uia_issubscriptattributeid"></span><span id="UIA_ISSUBSCRIPTATTRIBUTEID"></span><dl> <dt><strong>UIA_IsSubscriptAttributeId</strong></dt> <dt>40016</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsSubscript</strong> text attribute, which indicates whether the text is subscript (<strong>TRUE</strong>) or not (<strong>FALSE</strong>). <br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_IsSuperscriptAttributeId"></span><span id="uia_issuperscriptattributeid"></span><span id="UIA_ISSUPERSCRIPTATTRIBUTEID"></span><dl> <dt><strong>UIA_IsSuperscriptAttributeId</strong></dt> <dt>40017</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>IsSuperscript</strong> text attribute, which indicates whether the text is subscript (<strong>TRUE</strong>) or not (<strong>FALSE</strong>). <br/> Variant type: <strong>VT_BOOL</strong><br/> Default value: <strong>FALSE</strong><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_LineSpacingAttributeId"></span><span id="uia_linespacingattributeid"></span><span id="UIA_LINESPACINGATTRIBUTEID"></span><dl> <dt><strong>UIA_LineSpacingAttributeId</strong></dt> <dt>40040</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>LineSpacing</strong> text attribute, which specifies the spacing between lines of text.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: &quot;LineSpacingAttributeDefault&quot;<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_LinkAttributeId"></span><span id="uia_linkattributeid"></span><span id="UIA_LINKATTRIBUTEID"></span><dl> <dt><strong>UIA_LinkAttributeId</strong></dt> <dt>40035</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>Link</strong> text attribute, which contains the <a href="/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationtextrange"><strong>IUIAutomationTextRange</strong></a> interface of the text range that is the target of an internal link in a document. Supported starting with Windows 8.<br/> Variant type: <strong>VT_UNKNOWN</strong><br/> Default value: <strong>NULL</strong><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_MarginBottomAttributeId"></span><span id="uia_marginbottomattributeid"></span><span id="UIA_MARGINBOTTOMATTRIBUTEID"></span><dl> <dt><strong>UIA_MarginBottomAttributeId</strong></dt> <dt>40018</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>MarginBottom</strong> text attribute, which specifies the size, in points, of the bottom margin applied to the page associated with the text range. <br/> Variant type: <strong>VT_R8</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_MarginLeadingAttributeId"></span><span id="uia_marginleadingattributeid"></span><span id="UIA_MARGINLEADINGATTRIBUTEID"></span><dl> <dt><strong>UIA_MarginLeadingAttributeId</strong></dt> <dt>40019</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>MarginLeading</strong> text attribute, which specifies the size, in points, of the leading margin applied to the page associated with the text range. <br/> Variant type: <strong>VT_R8</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_MarginTopAttributeId"></span><span id="uia_margintopattributeid"></span><span id="UIA_MARGINTOPATTRIBUTEID"></span><dl> <dt><strong>UIA_MarginTopAttributeId</strong></dt> <dt>40020</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>MarginTop</strong> text attribute, which specifies the size, in points, of the top margin applied to the page associated with the text range. <br/> Variant type: <strong>VT_R8</strong><br/> Ddefault value: 0<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_MarginTrailingAttributeId"></span><span id="uia_margintrailingattributeid"></span><span id="UIA_MARGINTRAILINGATTRIBUTEID"></span><dl> <dt><strong>UIA_MarginTrailingAttributeId</strong></dt> <dt>40021</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>MarginTrailing</strong> text attribute, which specifies the size, in points, of the trailing margin applied to the page associated with the text range. <br/> Variant type: <strong>VT_R8</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_OutlineStylesAttributeId"></span><span id="uia_outlinestylesattributeid"></span><span id="UIA_OUTLINESTYLESATTRIBUTEID"></span><dl> <dt><strong>UIA_OutlineStylesAttributeId</strong></dt> <dt>40022</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>OutlineStyles</strong> text attribute, which specifies the outline style of the text. This attribute is specified as a value from the <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-outlinestyles"><strong>OutlineStyles</strong></a> enumerated type. <br/> Variant type: <strong>VT_I4</strong><br/> Default value: <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-outlinestyles"><strong>OutlineStyles_None</strong></a><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_OverlineColorAttributeId"></span><span id="uia_overlinecolorattributeid"></span><span id="UIA_OVERLINECOLORATTRIBUTEID"></span><dl> <dt><strong>UIA_OverlineColorAttributeId</strong></dt> <dt>40023</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>OverlineColor</strong> text attribute, which specifies the color of the overline text decoration. This attribute is specified as a <a href="/windows/win32/gdi/colorref">COLORREF</a>, a 32-bit value used to specify an RGB or RGBA color. <br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_OverlineStyleAttributeId"></span><span id="uia_overlinestyleattributeid"></span><span id="UIA_OVERLINESTYLEATTRIBUTEID"></span><dl> <dt><strong>UIA_OverlineStyleAttributeId</strong></dt> <dt>40024</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>OverlineStyle</strong> text attribute, which specifies the style of the overline text decoration. This attribute is specified as a value from the <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textdecorationlinestyle"><strong>TextDecorationLineStyleEnum</strong></a> enumerated type. <br/> Variant type: <strong>VT_I4</strong><br/> Default value: <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textdecorationlinestyle"><strong>TextDecorationLineStyle_None</strong></a><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_SelectionActiveEndAttributeId"></span><span id="uia_selectionactiveendattributeid"></span><span id="UIA_SELECTIONACTIVEENDATTRIBUTEID"></span><dl> <dt><strong>UIA_SelectionActiveEndAttributeId</strong></dt> <dt>40037</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>SelectionActiveEnd</strong> text attribute, which indicates the location of the caret relative to a text range that represents the currently selected text. This attribute is specified as a value from the <a href="/windows/desktop/api/uiautomationcore/ne-uiautomationcore-activeend"><strong>ActiveEnd</strong></a> enumeration. Supported starting with Windows 8.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: <a href="/windows/desktop/api/uiautomationcore/ne-uiautomationcore-activeend"><strong>ActiveEnd_None</strong></a><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_StrikethroughColorAttributeId"></span><span id="uia_strikethroughcolorattributeid"></span><span id="UIA_STRIKETHROUGHCOLORATTRIBUTEID"></span><dl> <dt><strong>UIA_StrikethroughColorAttributeId</strong></dt> <dt>40025</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>StrikethroughColor</strong> text attribute, which specifies the color of the strikethrough text decoration. This attribute is specified as a <a href="/windows/win32/gdi/colorref">COLORREF</a>, a 32-bit value used to specify an RGB or RGBA color. <br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_StrikethroughStyleAttributeId"></span><span id="uia_strikethroughstyleattributeid"></span><span id="UIA_STRIKETHROUGHSTYLEATTRIBUTEID"></span><dl> <dt><strong>UIA_StrikethroughStyleAttributeId</strong></dt> <dt>40026</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>StrikethroughStyle</strong> text attribute, which specifies the style of the strikethrough text decoration. This attribute is specified as a value from the <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textdecorationlinestyle"><strong>TextDecorationLineStyleEnum</strong></a> enumerated type. <br/> Variant type: <strong>VT_I4</strong><br/> Default value: <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textdecorationlinestyle"><strong>TextDecorationLineStyle_None</strong></a><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_StyleIdAttributeId"></span><span id="uia_styleidattributeid"></span><span id="UIA_STYLEIDATTRIBUTEID"></span><dl> <dt><strong>UIA_StyleIdAttributeId</strong></dt> <dt>40034</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>StyleId</strong> text attribute, which indicates the text styles in use for a text range. For a list of possible values, see <a href="uiauto-style-identifiers.md"><strong>Style Identifiers</strong></a>. Supported starting with Windows 8.<br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0 <br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_StyleNameAttributeId"></span><span id="uia_stylenameattributeid"></span><span id="UIA_STYLENAMEATTRIBUTEID"></span><dl> <dt><strong>UIA_StyleNameAttributeId</strong></dt> <dt>40033</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>StyleName</strong> text attribute, which identifies the localized name of the text style in use for a text range. Supported starting with Windows 8.<br/> Variant type: <strong>VT_BSTR</strong><br/> Default value: empty string<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_TabsAttributeId"></span><span id="uia_tabsattributeid"></span><span id="UIA_TABSATTRIBUTEID"></span><dl> <dt><strong>UIA_TabsAttributeId</strong></dt> <dt>40027</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>Tabs</strong> text attribute, which is an array specifying the tab stops for the text range. Each array element specifies a distance, in points, from the leading margin. <br/> Variant type: <strong>VT_ARRAY | VT_R8</strong><br/> Default value: empty array<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_TextFlowDirectionsAttributeId"></span><span id="uia_textflowdirectionsattributeid"></span><span id="UIA_TEXTFLOWDIRECTIONSATTRIBUTEID"></span><dl> <dt><strong>UIA_TextFlowDirectionsAttributeId</strong></dt> <dt>40028</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>TextFlowDirections</strong> text attribute, which specifies the direction of text flow. This attribute is specified as a combination of values from the <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-flowdirections"><strong>FlowDirections</strong></a> enumerated type. <br/> Variant type: <strong>VT_I4</strong><br/> Default value: <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-flowdirections"><strong>FlowDirections_Default</strong></a><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="UIA_UnderlineColorAttributeId"></span><span id="uia_underlinecolorattributeid"></span><span id="UIA_UNDERLINECOLORATTRIBUTEID"></span><dl> <dt><strong>UIA_UnderlineColorAttributeId</strong></dt> <dt>40029</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>UnderlineColor</strong> text attribute, which specifies the color of the underline text decoration. This attribute is specified as a <a href="/windows/win32/gdi/colorref">COLORREF</a>, a 32-bit value used to specify an RGB or RGBA color. <br/> Variant type: <strong>VT_I4</strong><br/> Default value: 0<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="UIA_UnderlineStyleAttributeId"></span><span id="uia_underlinestyleattributeid"></span><span id="UIA_UNDERLINESTYLEATTRIBUTEID"></span><dl> <dt><strong>UIA_UnderlineStyleAttributeId</strong></dt> <dt>40030</dt> </dl></td>
<td style="text-align: left;">Identifies the <strong>UnderlineStyle</strong> text attribute, which specifies the style of the underline text decoration. This attribute is specified as a value from the <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textdecorationlinestyle"><strong>TextDecorationLineStyleEnum</strong></a> enumerated type. <br/> Variant type: <strong>VT_I4</strong><br/> Default value: <a href="/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textdecorationlinestyle"><strong>TextDecorationLineStyle_None</strong></a><br/></td>
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

**Reference**
</dt> <dt>

[**ITextRangeProvider::FindAttribute**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextrangeprovider-findattribute)
</dt> <dt>

[**ITextRangeProvider::GetAttributeValue**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextrangeprovider-getattributevalue)
</dt> <dt>

[**IUIAutomation::FindAttribute**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextrange-findattribute)
</dt> <dt>

[**IUIAutomation::GetAttributeValue**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextrange-getattributevalue)
</dt> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Support for Textual Content](uiauto-ui-automation-textpattern-overview.md)
</dt> </dl>
