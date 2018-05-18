---
title: EmailRights class
description: Rights that apply to emails.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '48b3083e-0b41-48b7-b58d-886c47da0764'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["EmailRights class"]
topic_type:
- apiref
api_name:
- EmailRights class
api_type:
- NA
---

# EmailRights class

Rights that apply to emails.

## Signature

``` syntax
public final class EmailRights
```

## Properties



| Name                    | Signature                                                                                                                                                                                                 | Notes                                                                                                                                                                                                                                              |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ALL**<br/>      | `public final static Collection<String> ALL = Collections.unmodifiableCollection(Arrays.asList(CommonRights.View,             CommonRights.Owner, Reply, ReplyAll, Forward, Extract, Print));`<br/> | Specifies a list of all the rights that apply to emails; Reply, Reply All, Forward, Extract and Print.<br/>                                                                                                                                  |
| **Extract**<br/>  | ` public final static String Extract = EditableDocumentRights.Extract;`<br/>                                                                                                                        | Specifies a right that allows content to be extracted from a protected email and placed in an unprotected, or a different protected, format. Same value as [**EditableDocumentRights.Extract**](editabledocumentrights-class-java.md).<br/> |
| **Forward**<br/>  | `public final static String Forward = "FORWARD";`<br/>                                                                                                                                              | Specifies a right that allows a protected email message to be forwarded.<br/>                                                                                                                                                                |
| **Print**<br/>    | ` public final static String Print = EditableDocumentRights.Print;`<br/>                                                                                                                            | Specifies a right that allows protected email content to be printed. Same value as [**EditableDocumentRights.Print**](editabledocumentrights-class-java.md).<br/>                                                                           |
| **Reply**<br/>    | ` public final static String Reply = "REPLY";`<br/>                                                                                                                                                 | Specifies a right that allows a protected email message to be replied to with a message that includes a copy of the protected content.<br/>                                                                                                  |
| **ReplyAll**<br/> | `public final static String ReplyAll = "REPLYALL";`<br/>                                                                                                                                            | Specifies a right that allows reply-all to a protected email message with a message that includes a copy of the protected content.<br/>                                                                                                      |



 

## Defined in

EmailRights.java

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

 

 





