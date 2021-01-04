---
title: Annotation Type Identifiers (UIAutomationClient.h)
description: This topic describes the named constants that are used to identify types of annotations in a document.
ms.assetid: 46948B7C-EC9F-4B55-B769-62EE8BE11D33
topic_type:
- apiref
api_name:
- AnnotationType_AdvancedProofingIssue
- AnnotationType_Author
- AnnotationType_CircularReferenceError
- AnnotationType_Comment
- AnnotationType_ConflictingChange
- AnnotationType_DataValidationError
- AnnotationType_DeletionChange
- AnnotationType_EditingLockedChange
- AnnotationType_Endnote
- AnnotationType_ExternalChange
- AnnotationType_Footer
- AnnotationType_Footnote
- AnnotationType_FormatChange
- AnnotationType_FormulaError
- AnnotationType_GrammarError
- AnnotationType_Header
- AnnotationType_Highlighted
- AnnotationType_InsertionChange
- AnnotationType_Mathematics
- AnnotationType_MoveChange
- AnnotationType_SpellingError
- AnnotationType_TrackChanges
- AnnotationType_Unknown
- AnnotationType_UnsyncedChange
api_location:
- UIAutomationClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Annotation Type Identifiers

This topic describes the named constants that are used to identify types of annotations in a document.



| Constant/value                                                                                                                                                                                                                                                                                                                                           | Description                                                                                        |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------|
| <span id="AnnotationType_AdvancedProofingIssue"></span><span id="annotationtype_advancedproofingissue"></span><span id="ANNOTATIONTYPE_ADVANCEDPROOFINGISSUE"></span><dl> <dt>**AnnotationType\_AdvancedProofingIssue**</dt> <dt>60020</dt> </dl>     | An advanced proofing issue.<br/>                                                             |
| <span id="AnnotationType_Author"></span><span id="annotationtype_author"></span><span id="ANNOTATIONTYPE_AUTHOR"></span><dl> <dt>**AnnotationType\_Author**</dt> <dt>60019</dt> </dl>                                                                 | The author of the document.<br/>                                                             |
| <span id="AnnotationType_CircularReferenceError"></span><span id="annotationtype_circularreferenceerror"></span><span id="ANNOTATIONTYPE_CIRCULARREFERENCEERROR"></span><dl> <dt>**AnnotationType\_CircularReferenceError**</dt> <dt>60022</dt> </dl> | A circular reference error that occurred.<br/>                                               |
| <span id="AnnotationType_Comment"></span><span id="annotationtype_comment"></span><span id="ANNOTATIONTYPE_COMMENT"></span><dl> <dt>**AnnotationType\_Comment**</dt> <dt>60003</dt> </dl>                                                             | A comment. Comments can take different forms depending on the application.<br/>              |
| <span id="AnnotationType_ConflictingChange"></span><span id="annotationtype_conflictingchange"></span><span id="ANNOTATIONTYPE_CONFLICTINGCHANGE"></span><dl> <dt>**AnnotationType\_ConflictingChange**</dt> <dt>60018</dt> </dl>                     | A conflicting change that was made to the document.<br/>                                     |
| <span id="AnnotationType_DataValidationError"></span><span id="annotationtype_datavalidationerror"></span><span id="ANNOTATIONTYPE_DATAVALIDATIONERROR"></span><dl> <dt>**AnnotationType\_DataValidationError**</dt> <dt>60021</dt> </dl>             | A data validation error that occurred.<br/>                                                  |
| <span id="AnnotationType_DeletionChange"></span><span id="annotationtype_deletionchange"></span><span id="ANNOTATIONTYPE_DELETIONCHANGE"></span><dl> <dt>**AnnotationType\_DeletionChange**</dt> <dt>60012</dt> </dl>                                 | A deletion change that was made to the document.<br/>                                        |
| <span id="AnnotationType_EditingLockedChange"></span><span id="annotationtype_editinglockedchange"></span><span id="ANNOTATIONTYPE_EDITINGLOCKEDCHANGE"></span><dl> <dt>**AnnotationType\_EditingLockedChange**</dt> <dt>60016</dt> </dl>             | An editing locked change that was made to the document.<br/>                                 |
| <span id="AnnotationType_Endnote"></span><span id="annotationtype_endnote"></span><span id="ANNOTATIONTYPE_ENDNOTE"></span><dl> <dt>**AnnotationType\_Endnote**</dt> <dt>60009</dt> </dl>                                                             | The endnote for a document.<br/>                                                             |
| <span id="AnnotationType_ExternalChange"></span><span id="annotationtype_externalchange"></span><span id="ANNOTATIONTYPE_EXTERNALCHANGE"></span><dl> <dt>**AnnotationType\_ExternalChange**</dt> <dt>60017</dt> </dl>                                 | An external change that was made to the document.<br/>                                       |
| <span id="AnnotationType_Footer"></span><span id="annotationtype_footer"></span><span id="ANNOTATIONTYPE_FOOTER"></span><dl> <dt>**AnnotationType\_Footer**</dt> <dt>60007</dt> </dl>                                                                 | The footer for a page in a document.<br/>                                                    |
| <span id="AnnotationType_Footnote"></span><span id="annotationtype_footnote"></span><span id="ANNOTATIONTYPE_FOOTNOTE"></span><dl> <dt>**AnnotationType\_Footnote**</dt> <dt>60010</dt> </dl>                                                         | The footnote for a page in a document.<br/>                                                  |
| <span id="AnnotationType_FormatChange"></span><span id="annotationtype_formatchange"></span><span id="ANNOTATIONTYPE_FORMATCHANGE"></span><dl> <dt>**AnnotationType\_FormatChange**</dt> <dt>60014</dt> </dl>                                         | A format change that was made.<br/>                                                          |
| <span id="AnnotationType_FormulaError"></span><span id="annotationtype_formulaerror"></span><span id="ANNOTATIONTYPE_FORMULAERROR"></span><dl> <dt>**AnnotationType\_FormulaError**</dt> <dt>60004</dt> </dl>                                         | An error in a formula. Formula errors typically include red text and exclamation marks.<br/> |
| <span id="AnnotationType_GrammarError"></span><span id="annotationtype_grammarerror"></span><span id="ANNOTATIONTYPE_GRAMMARERROR"></span><dl> <dt>**AnnotationType\_GrammarError**</dt> <dt>60002</dt> </dl>                                         | A grammatical error, often denoted by a green squiggly line. <br/>                           |
| <span id="AnnotationType_Header"></span><span id="annotationtype_header"></span><span id="ANNOTATIONTYPE_HEADER"></span><dl> <dt>**AnnotationType\_Header**</dt> <dt>60006</dt> </dl>                                                                 | The header for a page in a document.<br/>                                                    |
| <span id="AnnotationType_Highlighted"></span><span id="annotationtype_highlighted"></span><span id="ANNOTATIONTYPE_HIGHLIGHTED"></span><dl> <dt>**AnnotationType\_Highlighted**</dt> <dt>60008</dt> </dl>                                             | Highlighted content, typically denoted by a contrasting background color.<br/>               |
| <span id="AnnotationType_InsertionChange"></span><span id="annotationtype_insertionchange"></span><span id="ANNOTATIONTYPE_INSERTIONCHANGE"></span><dl> <dt>**AnnotationType\_InsertionChange**</dt> <dt>60011</dt> </dl>                             | An insertion change that was made to the document.<br/>                                      |
| <span id="AnnotationType_Mathematics"></span><span id="annotationtype_mathematics"></span><span id="ANNOTATIONTYPE_MATHEMATICS"></span><dl> <dt>**AnnotationType\_Mathematics**</dt> <dt>60023</dt> </dl>                                             | A text range containing mathematics.<br/>                                                    |
| <span id="AnnotationType_MoveChange"></span><span id="annotationtype_movechange"></span><span id="ANNOTATIONTYPE_MOVECHANGE"></span><dl> <dt>**AnnotationType\_MoveChange**</dt> <dt>60013</dt> </dl>                                                 | A move change that was made to the document.<br/>                                            |
| <span id="AnnotationType_SpellingError"></span><span id="annotationtype_spellingerror"></span><span id="ANNOTATIONTYPE_SPELLINGERROR"></span><dl> <dt>**AnnotationType\_SpellingError**</dt> <dt>60001</dt> </dl>                                     | A spelling error, often denoted by a red squiggly line. <br/>                                |
| <span id="AnnotationType_TrackChanges"></span><span id="annotationtype_trackchanges"></span><span id="ANNOTATIONTYPE_TRACKCHANGES"></span><dl> <dt>**AnnotationType\_TrackChanges**</dt> <dt>60005</dt> </dl>                                         | A change that was made to the document.<br/>                                                 |
| <span id="AnnotationType_Unknown"></span><span id="annotationtype_unknown"></span><span id="ANNOTATIONTYPE_UNKNOWN"></span><dl> <dt>**AnnotationType\_Unknown**</dt> <dt>60000</dt> </dl>                                                             | The annotation type is unknown.<br/>                                                         |
| <span id="AnnotationType_UnsyncedChange"></span><span id="annotationtype_unsyncedchange"></span><span id="ANNOTATIONTYPE_UNSYNCEDCHANGE"></span><dl> <dt>**AnnotationType\_UnsyncedChange**</dt> <dt>60015</dt> </dl>                                 | An unsynced change that was made to the document.<br/>                                       |



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                            |
| Header<br/>                   | <dl> <dt>UIAutomationClient.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**IAnnotationProvider::AnnotationTypeId**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-iannotationprovider-get_annotationtypeid)
</dt> <dt>

[**ISpreadsheetItemProvider::GetAnnotationTypes**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-ispreadsheetitemprovider-getannotationtypes)
</dt> <dt>

[**IUIAutomationPattern::CachedAnnotationTypeId**](/windows/desktop/api/uiautomationclient/nf-uiautomationclient-iuiautomationannotationpattern-get_cachedannotationtypeid)
</dt> <dt>

[**IUIAutomationPattern::CurrentAnnotationTypeId**](/windows/desktop/api/uiautomationclient/nf-uiautomationclient-iuiautomationannotationpattern-get_currentannotationtypeid)
</dt> <dt>

[**IUIAutomationSpreadsheetItemPattern::GetCachedAnnotationType**](/windows/desktop/api/uiautomationclient/nf-uiautomationclient-iuiautomationspreadsheetitempattern-getcachedannotationtypes)
</dt> <dt>

[**IUIAutomationSpreadsheetItemPattern::GetCurrentAnnotationType**](/windows/desktop/api/uiautomationclient/nf-uiautomationclient-iuiautomationspreadsheetitempattern-getcurrentannotationtypes)
</dt> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Support for Textual Content](uiauto-ui-automation-textpattern-overview.md)
</dt> </dl>

 

