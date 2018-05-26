---
Description: The FaxRecipient messaging object is used by a fax client application to retrieve and set the personal information for fax recipients.
ms.assetid: e418dbaf-9b07-40a9-bab8-7b4561b63325
title: FaxRecipient object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxRecipient object

The **FaxRecipient** messaging object is used by a fax client application to retrieve and set the personal information for fax recipients.

## Members

The **FaxRecipient** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxRecipient** object has these properties.



| Property                                                        | Access type           | Description                                                                                                                                                           |
|:----------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FaxNumber**](-mfax-faxrecipient-faxnumber-vb.md)<br/> | Read/write<br/> | The [**FaxNumber**](-mfax-faxrecipient-faxnumber-vb.md) property is a null-terminated string that contains the fax number associated with the recipient. <br/> |
| [**Name**](-mfax-faxrecipient-name-vb.md)<br/>           | Read/write<br/> | The [**Name**](-mfax-faxrecipient-name-vb.md) property is a null-terminated string that contains the name of the recipient. <br/>                              |



 

## Remarks

A **FaxRecipient** object is accessed through a [**FaxRecipients**](-mfax-faxrecipients.md), [**FaxOutgoingJob**](-mfax-faxoutgoingjob.md), or [**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md) object.

![faxoutgoingmessage, faxrecipients, faxoutgoingjob, and faxrecipient objects](images/faxrecipient.png)

To create a **FaxRecipient** object in Microsoft Visual Basic, call the [**Recipients**](-mfax-faxdocument-recipients-vb.md) property of the [**FaxDocument**](-mfax-faxdocument.md) object, the [**Add**](-mfax-faxrecipients-add-vb.md) method of the [**FaxRecipients**](-mfax-faxrecipients.md) object, the [**Recipient**](-mfax-faxoutgoingjob-recipient.md) property of the [**FaxOutgoingJob**](-mfax-faxoutgoingjob.md) object, or the [**Recipient**](-mfax-faxoutgoingmessage-recipient.md) property of the [**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md) object.

To create a **FaxRecipient** object in C++, call the [**Recipients**](-mfax-faxdocument-recipients-vb.md), [**Add**](-mfax-faxrecipients-add-vb.md), [**Recipient**](-mfax-faxoutgoingjob-recipient.md), or [**Recipient**](-mfax-faxoutgoingmessage-recipient.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxRecipient<br/>                                                          |



 

 




