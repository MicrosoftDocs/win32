---
Description: The FaxSender messaging object is used by a fax client application to retrieve and set sender information about fax senders. The object also includes methods to store sender data in and retrieve sender data from the local registry.
ms.assetid: f265cfd0-cf62-4d86-9ba5-d1842ac94baa
title: FaxSender object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxSender object

The **FaxSender** messaging object is used by a fax client application to retrieve and set sender information about fax senders. The object also includes methods to store sender data in and retrieve sender data from the local registry.

## Members

The **FaxSender** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxSender** object has these methods.



| Method                                                            | Description                                                                                                                                                        |
|:------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**LoadDefaultSender**](-mfax-faxsender-loaddefaultsender-vb.md) | The [**LoadDefaultSender**](-mfax-faxsender-loaddefaultsender-vb.md) method fills the **FaxSender** object with the default sender information.<br/>        |
| [**SaveDefaultSender**](-mfax-faxsender-savedefaultsender-vb.md) | The [**SaveDefaultSender**](-mfax-faxsender-savedefaultsender-vb.md) method stores information about the default sender from the **FaxSender** object.<br/> |



 

### Properties

The **FaxSender** object has these properties.



| Property                                                               | Access type           | Description                                                                                                                                                                     |
|:-----------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BillingCode**](-mfax-faxsender-billingcode-vb.md)<br/>       | Read/write<br/> | The [**BillingCode**](-mfax-faxsender-billingcode-vb.md) property is a null-terminated string that contains the billing code associated with the sender.<br/>            |
| [**City**](-mfax-faxsender-city-vb.md)<br/>                     | Write-only<br/> | Not currently supported.<br/>                                                                                                                                             |
| [**Company**](-mfax-faxsender-company-vb.md)<br/>               | Read/write<br/> | The [**Company**](-mfax-faxsender-company-vb.md) property is a null-terminated string that contains the company name associated with the sender.<br/>                    |
| [**Country**](-mfax-faxsender-country-vb.md)<br/>               | Write-only<br/> | Not currently supported.<br/>                                                                                                                                             |
| [**Department**](-mfax-faxsender-department-vb.md)<br/>         | Read/write<br/> | The [**Department**](-mfax-faxsender-department-vb.md) property is a null-terminated string that contains the department associated with the sender.<br/>                |
| [**Email**](-mfax-faxsender-email-vb.md)<br/>                   | Read/write<br/> | The [**Email**](-mfax-faxsender-email-vb.md) property is a null-terminated string that contains the email address associated with the sender.<br/>                       |
| [**FaxNumber**](-mfax-faxsender-faxnumber-vb.md)<br/>           | Read/write<br/> | The [**FaxNumber**](-mfax-faxsender-faxnumber-vb.md) property is a null-terminated string that contains the fax number associated with the sender.<br/>                  |
| [**HomePhone**](-mfax-faxsender-homephone-vb.md)<br/>           | Read/write<br/> | The [**HomePhone**](-mfax-faxsender-homephone-vb.md) property is a null-terminated string that contains the home telephone number associated with the sender.<br/>       |
| [**Name**](-mfax-faxsender-name-vb.md)<br/>                     | Read/write<br/> | The [**Name**](-mfax-faxsender-name-vb.md) property is a null-terminated string that contains the name of the sender.<br/>                                               |
| [**OfficeLocation**](-mfax-faxsender-officelocation-vb.md)<br/> | Read/write<br/> | The [**OfficeLocation**](-mfax-faxsender-officelocation-vb.md) property is a null-terminated string that contains the office location of the sender.<br/>                |
| [**OfficePhone**](-mfax-faxsender-officephone-vb.md)<br/>       | Read/write<br/> | The [**OfficePhone**](-mfax-faxsender-officephone-vb.md) property is a null-terminated string that contains the office telephone number associated with the sender.<br/> |
| [**State**](-mfax-faxsender-state-vb.md)<br/>                   | Write-only<br/> | Not currently supported.<br/>                                                                                                                                             |
| [**StreetAddress**](-mfax-faxsender-streetaddress-vb.md)<br/>   | Read/write<br/> | The [**StreetAddress**](-mfax-faxsender-streetaddress-vb.md) property is a null-terminated string that contains the street address associated with the sender.<br/>      |
| [**Title**](-mfax-faxsender-title-vb.md)<br/>                   | Read/write<br/> | The [**Title**](-mfax-faxsender-title-vb.md) property is a null-terminated string that contains the title associated with the sender.<br/>                               |
| [**TSID**](-mfax-faxsender-tsid-vb.md)<br/>                     | Read/write<br/> | The [**TSID**](-mfax-faxsender-tsid-vb.md) property is a null-terminated string that contains the transmitting station identifier (TSID) for the sender's device.<br/>   |
| [**ZipCode**](-mfax-faxsender-zipcode-vb.md)<br/>               | Write-only<br/> | Not currently supported.<br/>                                                                                                                                             |



 

## Remarks

A **FaxSender** object is accessed through a [**FaxDocument**](-mfax-faxdocument.md), [**FaxOutgoingJob**](-mfax-faxoutgoingjob.md), or [**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md) object.

![faxdocument, faxoutgoingmessage, faxoutgoingjob, and faxsender objects](images/faxsender.png)

To create a **FaxSender** object in Microsoft Visual Basic, call the [**Sender**](-mfax-faxdocument-sender-vb.md) property of the [**FaxDocument**](-mfax-faxdocument.md) object, the [**Sender**](-mfax-faxoutgoingjob-sender.md) property of the [**FaxOutgoingJob**](-mfax-faxoutgoingjob.md) object, or the [**Sender**](-mfax-faxoutgoingmessage-sender.md) property of the [**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md) object.

To create a **FaxSender** object in C++, call the [**Sender**](-mfax-faxdocument-sender-vb.md), [**Sender**](-mfax-faxoutgoingjob-sender.md), or [**Sender**](-mfax-faxoutgoingmessage-sender.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxSender<br/>                                                             |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**IFaxSender**](-mfax-faxsender-cpp.md)
</dt> </dl>

 

 




