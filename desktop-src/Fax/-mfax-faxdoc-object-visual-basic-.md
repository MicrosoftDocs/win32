---
Description: The FaxDoc object permits a Microsoft Visual Basic fax client application to transmit fax documents and cover pages, and to retrieve and set information about fax transmissions.
ms.assetid: 6bf5be89-efc8-41e7-bde9-0c0ba7f0e61c
title: FaxDoc object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxDoc object

The **FaxDoc** object permits a Microsoft Visual Basic fax client application to transmit fax documents and cover pages, and to retrieve and set information about fax transmissions. Information includes the name of the file to transmit, the fax number to which the fax server should send the fax, cover page settings, and fax recipient and sender information.

The **FaxDoc** object has the following method and properties:

-   A method to send a fax document.
-   Properties to set and retrieve individual attributes associated with a **FaxDoc** object.

## Members

The **FaxDoc** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxDoc** object has these methods.



| Method                                | Description                                                                                                                                                                                                                                                                                                                         |
|:--------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Send**](-mfax-ifaxdoc-send-vb.md) | The [**Send**](-mfax-ifaxdoc-send-vb.md) method transmits the document specified by the [**FileName**](-mfax-ifaxdoc-get-filename-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The method can send the fax to the fax number specified by the [**FaxNumber**](-mfax-ifaxdoc-get-faxnumber-vb.md) property.<br/> |



 

### Properties

The **FaxDoc** object has these properties.



| Property                                                                             | Access type           | Description                                                                                                                                                                                                                                                                                                       |
|:-------------------------------------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BillingCode**](-mfax-ifaxdoc-get-billingcode-vb.md)<br/>                   | Read/write<br/> | Sets or retrieves the [**BillingCode**](-mfax-ifaxdoc-get-billingcode-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **BillingCode** property is a null-terminated string that contains an optional billing code that applies to the fax transmission.<br/>                                   |
| [**CallHandle**](-mfax-ifaxdoc-get-callhandle-vb.md)<br/>                     | Write-only<br/> | Not currently supported.<br/>                                                                                                                                                                                                                                                                               |
| [**CoverpageName**](-mfax-ifaxdoc-get-coverpagename-vb.md)<br/>               | Read/write<br/> | Sets or retrieves the [**CoverpageName**](-mfax-ifaxdoc-get-coverpagename-vb.md) property for a [FaxDoc](-mfax-faxdoc.md) object. The **CoverpageName** property is a null-terminated string that contains the name of the cover page template file (.cov) associated with the object.<br/>               |
| [**CoverpageNote**](-mfax-ifaxdoc-get-coverpagenote-vb.md)<br/>               | Read/write<br/> | Sets or retrieves the [**CoverpageNote**](-mfax-ifaxdoc-get-coverpagenote-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **CoverpageNote** property is a null-terminated string that contains the text of a message or note from the sender that pertains to the fax transmission.<br/>       |
| [**CoverpageSubject**](-mfax-ifaxdoc-get-coverpagesubject-vb.md)<br/>         | Read/write<br/> | Sets or retrieves the [**CoverpageSubject**](-mfax-ifaxdoc-get-coverpagesubject-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **CoverpageSubject** property is a null-terminated string that contains the subject line of the fax transmission.<br/>                                         |
| [**DiscountSend**](-mfax-ifaxdoc-get-discountsend-vb.md)<br/>                 | Read/write<br/> | Sets or retrieves the [**DiscountSend**](-mfax-ifaxdoc-get-discountsend-vb.md) property for a [FaxDoc](-mfax-faxdoc.md) object. The **DiscountSend** property is a Boolean value that indicates whether the fax server transmits faxes during the discount period.<br/>                                   |
| [**DisplayName**](-mfax-ifaxdoc-get-displayname-vb.md)<br/>                   | Read/write<br/> | Sets or retrieves the [**DisplayName**](-mfax-ifaxdoc-get-displayname-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **DisplayName** property is a null-terminated string that contains the name to associate with the fax document.<br/>                                                     |
| [**EmailAddress**](-mfax-ifaxdoc-get-emailaddress-vb.md)<br/>                 | Read/write<br/> | Sets or retrieves the [**EmailAddress**](-mfax-ifaxdoc-get-emailaddress-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **EmailAddress** property is a null-terminated string that contains the email address of the sender of the fax transmission.<br/>                                      |
| [**FaxNumber**](-mfax-ifaxdoc-get-faxnumber-vb.md)<br/>                       | Read/write<br/> | Sets or retrieves the [**FaxNumber**](-mfax-ifaxdoc-get-faxnumber-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **FaxNumber** property is a null-terminated string that contains the fax number to which the fax server will send the fax transmission.<br/>                                 |
| [**FileName**](-mfax-ifaxdoc-get-filename-vb.md)<br/>                         | Read/write<br/> | Sets or retrieves the [**FileName**](-mfax-ifaxdoc-get-filename-vb.md) property for a [FaxDoc](-mfax-faxdoc.md) object. The **FileName** property is a null-terminated string that contains the name of the document file associated with the object.<br/>                                                |
| [**RecipientAddress**](-mfax-ifaxdoc-get-recipientaddress-vb.md)<br/>         | Read/write<br/> | Sets or retrieves the [**RecipientAddress**](-mfax-ifaxdoc-get-recipientaddress-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **RecipientAddress** property is a null-terminated string that contains the street address of the recipient of the fax transmission.<br/>                      |
| [**RecipientCity**](-mfax-ifaxdoc-get-recipientcity-vb.md)<br/>               | Read/write<br/> | Sets or retrieves the [**RecipientCity**](-mfax-ifaxdoc-get-recipientcity-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **RecipientCity** property is a null-terminated string that contains the city name of the recipient of the fax transmission.<br/>                                    |
| [**RecipientCompany**](-mfax-ifaxdoc-get-recipientcompany-vb.md)<br/>         | Read/write<br/> | Sets or retrieves the [**RecipientCompany**](-mfax-ifaxdoc-get-recipientcompany-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **RecipientCompany** property is a null-terminated string that contains the company name of the recipient of the fax transmission.<br/>                        |
| [**RecipientCountry**](-mfax-ifaxdoc-get-recipientcountry-vb.md)<br/>         | Read/write<br/> | Sets or retrieves the [**RecipientCountry**](-mfax-ifaxdoc-get-recipientcountry-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **RecipientCountry** property is a null-terminated string that contains the country/region of the recipient of the fax transmission.<br/>                      |
| [**RecipientDepartment**](-mfax-ifaxdoc-get-recipientdepartment-vb.md)<br/>   | Read/write<br/> | Sets or retrieves the [**RecipientDepartment**](-mfax-ifaxdoc-get-recipientdepartment-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **RecipientDepartment** property is a null-terminated string that contains the department of the recipient of the fax transmission.<br/>                 |
| [**RecipientHomePhone**](-mfax-ifaxdoc-get-recipienthomephone-vb.md)<br/>     | Read/write<br/> | Sets or retrieves the [**RecipientHomePhone**](-mfax-ifaxdoc-get-recipienthomephone-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **RecipientHomePhone** property is a null-terminated string that contains the home telephone number of the recipient of the fax transmission.<br/>         |
| [**RecipientName**](-mfax-ifaxdoc-get-recipientname-vb.md)<br/>               | Read/write<br/> | Sets or retrieves the [**RecipientName**](-mfax-ifaxdoc-get-recipientname-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **RecipientName** property is a null-terminated string that contains the name of the recipient of the fax transmission.<br/>                                         |
| [**RecipientOffice**](-mfax-ifaxdoc-get-recipientoffice-vb.md)<br/>           | Read/write<br/> | Sets or retrieves the [**RecipientOffice**](-mfax-ifaxdoc-get-recipientoffice-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **RecipientOffice** property is a null-terminated string that contains the office of the recipient of the fax transmission.<br/>                                 |
| [**RecipientOfficePhone**](-mfax-ifaxdoc-get-recipientofficephone-vb.md)<br/> | Read/write<br/> | Sets or retrieves the [**RecipientOfficePhone**](-mfax-ifaxdoc-get-recipientofficephone-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **RecipientOfficePhone** property is a null-terminated string that contains the office telephone number of the recipient of the fax transmission.<br/> |
| [**RecipientState**](-mfax-ifaxdoc-get-recipientstate-vb.md)<br/>             | Read/write<br/> | Sets or retrieves the [**RecipientState**](-mfax-ifaxdoc-get-recipientstate-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **RecipientState** property is a null-terminated string that contains the state of the recipient of the fax transmission.<br/>                                     |
| [**RecipientTitle**](-mfax-ifaxdoc-get-recipienttitle-vb.md)<br/>             | Read/write<br/> | Sets or retrieves the [**RecipientTitle**](-mfax-ifaxdoc-get-recipienttitle-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **RecipientTitle** property is a null-terminated string that contains the title of the recipient of the fax transmission.<br/>                                     |
| [**RecipientZip**](-mfax-ifaxdoc-get-recipientzip-vb.md)<br/>                 | Read/write<br/> | Sets or retrieves the [**RecipientZip**](-mfax-ifaxdoc-get-recipientzip-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **RecipientZip** property is a null-terminated string that contains the ZIP code of the recipient of the fax transmission.<br/>                                        |
| [**SendCoverpage**](-mfax-ifaxdoc-get-sendcoverpage-vb.md)<br/>               | Read/write<br/> | Sets or retrieves the [**SendCoverpage**](-mfax-ifaxdoc-get-sendcoverpage-vb.md) property for a [FaxDoc](-mfax-faxdoc.md) object. The **SendCoverpage** property is a Boolean value that indicates whether the specified cover page file is stored on the fax server.<br/>                                |
| [**SenderAddress**](-mfax-ifaxdoc-get-senderaddress-vb.md)<br/>               | Read/write<br/> | Sets or retrieves the [**SenderAddress**](-mfax-ifaxdoc-get-senderaddress-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **SenderAddress** property is a null-terminated string that contains the street address of the sender of the fax transmission.<br/>                                  |
| [**SenderCompany**](-mfax-ifaxdoc-get-sendercompany-vb.md)<br/>               | Read/write<br/> | Sets or retrieves the [**SenderCompany**](-mfax-ifaxdoc-get-sendercompany-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **SenderCompany** property is a null-terminated string that contains the company name of the sender of the fax transmission.<br/>                                    |
| [**SenderDepartment**](-mfax-ifaxdoc-get-senderdepartment-vb.md)<br/>         | Read/write<br/> | Sets or retrieves the [**SenderDepartment**](-mfax-ifaxdoc-get-senderdepartment-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **SenderDepartment** property is a null-terminated string that contains the department of the sender of the fax transmission.<br/>                             |
| [**SenderFax**](-mfax-ifaxdoc-get-senderfax-vb.md)<br/>                       | Read/write<br/> | Sets or retrieves the [**SenderFax**](-mfax-ifaxdoc-get-senderfax-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **SenderFax** property is a null-terminated string that contains the fax number of the sender of the outbound fax transmission.<br/>                                         |
| [**SenderHomePhone**](-mfax-ifaxdoc-get-senderhomephone-vb.md)<br/>           | Read/write<br/> | Sets or retrieves the [**SenderHomePhone**](-mfax-ifaxdoc-get-senderhomephone-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **SenderHomePhone** property is a null-terminated string that contains the home telephone number of the sender of the fax transmission.<br/>                     |
| [**SenderName**](-mfax-ifaxdoc-get-sendername-vb.md)<br/>                     | Read/write<br/> | Sets or retrieves the [**SenderName**](-mfax-ifaxdoc-get-sendername-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **SenderName** property is a null-terminated string that contains the name of the sender of the fax transmission.<br/>                                                     |
| [**SenderOffice**](-mfax-ifaxdoc-get-senderoffice-vb.md)<br/>                 | Read/write<br/> | Sets or retrieves the [**SenderOffice**](-mfax-ifaxdoc-get-senderoffice-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **SenderOffice** property is a null-terminated string that contains the office of the sender of the fax transmission.<br/>                                             |
| [**SenderOfficePhone**](-mfax-ifaxdoc-get-senderofficephone-vb.md)<br/>       | Read/write<br/> | Sets or retrieves the [**SenderOfficePhone**](-mfax-ifaxdoc-get-senderofficephone-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **SenderOfficePhone** property is a null-terminated string that contains the office telephone number of the sender of the fax transmission.<br/>             |
| [**SenderTitle**](-mfax-ifaxdoc-get-sendertitle-vb.md)<br/>                   | Read/write<br/> | Sets or retrieves the [**SenderTitle**](-mfax-ifaxdoc-get-sendertitle-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **SenderTitle** property is a null-terminated string that contains the title of the sender of the fax transmission.<br/>                                                 |
| [**ServerCoverpage**](-mfax-ifaxdoc-get-servercoverpage-vb.md)<br/>           | Read/write<br/> | Sets or retrieves the [**ServerCoverpage**](-mfax-ifaxdoc-get-servercoverpage-vb.md) property for a [FaxDoc](-mfax-faxdoc.md) object. The **ServerCoverpage** property is a Boolean value that indicates whether the specified cover page file is stored on the fax server.<br/>                          |
| [**Tsid**](-mfax-ifaxdoc-get-tsid-vb.md)<br/>                                 | Read/write<br/> | Sets or retrieves the [**Tsid**](-mfax-ifaxdoc-get-tsid-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The **Tsid** property is a null-terminated string that contains a user-defined TSID.<br/>                                                                                                  |



 

## Remarks

Values are not required for optional properties that appear only on the cover page. The [**FileName**](-mfax-ifaxdoc-get-filename-vb.md) and [**FaxNumber**](-mfax-ifaxdoc-get-faxnumber-vb.md) properties are required to send a fax transmission using a call to the [**Send**](-mfax-ifaxdoc-send-vb.md) method.

### When to Implement

You should not implement this class. The Microsoft standard implementation provides complete functionality. You can use the Visual Basic Object Browser to view the **FaxDoc** object's type library information in Visual Basic syntax.

### To create a FaxDoc object

1.  Call the Visual Basic [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function to create a [**FaxServer object**](-mfax-faxserver-object-visual-basic-.md).
2.  Call the [**CreateDocument**](-mfax-ifaxserver-createdocument-vb.md) method of the [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object to create a **FaxDoc** object.

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Faxcom.h</dt> </dl> |



 

 




