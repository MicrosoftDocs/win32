---
Description: The FaxRecipients messaging collection is used by a fax client application to manage the fax recipient objects (FaxRecipient) that represent the recipients of a single fax document. The collection also includes methods to add and remove recipients.
ms.assetid: b0210d82-5d62-4192-a05c-455c9f3adf9b
title: FaxRecipients object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxRecipients object

The **FaxRecipients** messaging collection is used by a fax client application to manage the fax recipient objects ([**FaxRecipient**](-mfax-faxrecipient.md)) that represent the recipients of a single fax document. The collection also includes methods to add and remove recipients.

## Members

The **FaxRecipients** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxRecipients** object has these methods.



| Method                                          | Description                                                                                                                                                        |
|:------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](-mfax-faxrecipients-add-vb.md)       | The [**Add**](-mfax-faxrecipients-add-vb.md) method adds a new [**FaxRecipient**](-mfax-faxrecipient.md) object to the **FaxRecipients** collection. <br/> |
| [**Remove**](-mfax-faxrecipients-remove-vb.md) | The [**Remove**](-mfax-faxrecipients-remove-vb.md) method removes an item from the **FaxRecipients** collection.<br/>                                       |



 

### Properties

The **FaxRecipients** object has these properties.



| Property                                                 | Access type          | Description                                                                                                                                                                                                                        |
|:---------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Count**](-mfax-faxrecipients-count-vb.md)<br/> | Read-only<br/> | The [**Count**](-mfax-faxrecipients-count-vb.md) property represents the number of objects in the **FaxRecipients** collection. This is the total number of recipients associated with the fax server or fax document.<br/> |
| [**Item**](-mfax-faxrecipients-item.md)<br/>      | Read-only<br/> | The [**Item**](-mfax-faxrecipients-item.md) property returns a [**FaxRecipient**](-mfax-faxrecipient.md) object from the **FaxRecipients** collection. <br/>                                                               |



 

## Remarks

A **FaxRecipients** collection is accessed through a [**FaxDocument**](-mfax-faxdocument.md) object.

![faxdocument, faxrecipients, and faxrecipient objects](images/faxrecipients.png)

To create a **FaxRecipients** object in Microsoft Visual Basic, call the [**Recipients**](-mfax-faxdocument-recipients-vb.md) property of the object.

To create a **FaxRecipients** object in C++, call the [**Recipients**](-mfax-faxdocument-recipients-vb.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxRecipients<br/>                                                         |



 

 




