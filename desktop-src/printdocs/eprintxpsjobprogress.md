---
description: Specifies what the spooler is currently doing as it processes an XPS print job.
ms.assetid: 4fa5b749-e4f9-4f08-97b5-e58f82d0b485
title: EPrintXPSJobProgress enumeration (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EPrintXPSJobProgress
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# EPrintXPSJobProgress enumeration

Specifies what the spooler is currently doing as it processes an XPS print job.

## Syntax


```C++
typedef enum tagEPrintXPSJobProgress { 
  kAddingDocumentSequence,
  kDocumentSequenceAdded,
  kAddingFixedDocument,
  kFixedDocumentAdded,
  kAddingFixedPage,
  kFixedPageAdded,
  kResourceAdded,
  kFontAdded,
  kImageAdded,
  kXpsDocumentCommitted
} EPrintXPSJobProgress;
```



## Constants

<dl> <dt>

<span id="kAddingDocumentSequence"></span><span id="kaddingdocumentsequence"></span><span id="KADDINGDOCUMENTSEQUENCE"></span>**kAddingDocumentSequence**
</dt> <dd>

A document sequence is about to be added to the XPS job.

</dd> <dt>

<span id="kDocumentSequenceAdded"></span><span id="kdocumentsequenceadded"></span><span id="KDOCUMENTSEQUENCEADDED"></span>**kDocumentSequenceAdded**
</dt> <dd>

A document sequence has been added to the XPS job.

</dd> <dt>

<span id="kAddingFixedDocument"></span><span id="kaddingfixeddocument"></span><span id="KADDINGFIXEDDOCUMENT"></span>**kAddingFixedDocument**
</dt> <dd>

A fixed document is about to be added to the XPS job.

</dd> <dt>

<span id="kFixedDocumentAdded"></span><span id="kfixeddocumentadded"></span><span id="KFIXEDDOCUMENTADDED"></span>**kFixedDocumentAdded**
</dt> <dd>

A fixed document has been added to the XPS job.

</dd> <dt>

<span id="kAddingFixedPage"></span><span id="kaddingfixedpage"></span><span id="KADDINGFIXEDPAGE"></span>**kAddingFixedPage**
</dt> <dd>

A page is about to be added to the XPS job.

</dd> <dt>

<span id="kFixedPageAdded"></span><span id="kfixedpageadded"></span><span id="KFIXEDPAGEADDED"></span>**kFixedPageAdded**
</dt> <dd>

A page has been added to the XPS job.

</dd> <dt>

<span id="kResourceAdded"></span><span id="kresourceadded"></span><span id="KRESOURCEADDED"></span>**kResourceAdded**
</dt> <dd>

A resource had been added to the XPS job.

</dd> <dt>

<span id="kFontAdded"></span><span id="kfontadded"></span><span id="KFONTADDED"></span>**kFontAdded**
</dt> <dd>

A font has been added to the XPS job.

</dd> <dt>

<span id="kImageAdded"></span><span id="kimageadded"></span><span id="KIMAGEADDED"></span>**kImageAdded**
</dt> <dd>

An image has been added to the XPS job.

</dd> <dt>

<span id="kXpsDocumentCommitted"></span><span id="kxpsdocumentcommitted"></span><span id="KXPSDOCUMENTCOMMITTED"></span>**kXpsDocumentCommitted**
</dt> <dd>

The data for the XPS job has been committed.

</dd> </dl>

## Remarks

This enumeration is primarily used as a parameter for the [**ReportJobProcessingProgress**](reportjobprocessingprogress.md) function.

These values can refer to either the spooling or the rendering phase of a print job.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |



 

 




