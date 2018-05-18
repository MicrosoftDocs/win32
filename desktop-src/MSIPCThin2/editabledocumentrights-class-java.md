---
title: EditableDocumentRights class
description: Rights that apply to editable documents.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '4d787f4a-621c-4e38-9212-6027255aea7e'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["EditableDocumentRights class"]
topic_type:
- apiref
api_name:
- EditableDocumentRights class
api_type:
- NA
---

# EditableDocumentRights class

Rights that apply to editable documents.

## Signature

``` syntax
public final class EditableDocumentRights
```

## Properties



| Name                   | Signature                                                                                                                                                                                              | Notes                                                                                                                                                                                                                         |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ALL**<br/>     | `public final static Collection<String> ALL = Collections.unmodifiableCollection(Arrays.asList(CommonRights.View,             Edit, Export, Extract, Print, Comment, CommonRights.Owner));`<br/> | Specifies all of the rights (View, Edit, Export, Extract, Comment and Print, Owner)<br/>                                                                                                                                |
| **Comment**<br/> | `public final static String Comment = "COMMENT";`<br/>                                                                                                                                           | Specifies the right to make comments on the document.<br/>                                                                                                                                                              |
| **Edit**<br/>    | `public final static String Edit = "EDIT";`<br/>                                                                                                                                                 | Specifies a right that allows the protected content to be edited and saved to the same protected format.<br/>                                                                                                           |
| **Export**<br/>  | `public final static String Export = "EXPORT";`<br/>                                                                                                                                             | Specifies a right that allows content to be extracted from a protected format and placed in a different AD RMS-protected format.<br/>                                                                                   |
| **Extract**<br/> | `public final static String Extract = "EXTRACT";`<br/>                                                                                                                                           | Specifies a right that allows content to be extracted from a protected format and placed in an unprotected, or a different protected, format. Same value as [**EmailRights.Extract**](emailrights-class-java.md).<br/> |
| **Print**<br/>   | `public final static String Print = "PRINT";`<br/>                                                                                                                                               | Specifies a right that allows protected content to be printed. Same value as [**EmailRights.Print**](emailrights-class-java.md).<br/>                                                                                  |



 

## Defined in

EditableDocumentRights.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement

## Remarks

For more information about the built-in rights and the usage restrictions associated with them that apps should observe, see [Built-in Rights Usage Restriction Reference](built-in-rights-usage-restriction-reference.md).

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





