---
Description: The IX509SCEPEnrollment interface exposes the following methods.
ms.assetid: B45B68D2-A14D-4D14-AF5F-1A1BB9921A0D
title: IX509SCEPEnrollment Methods
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IX509SCEPEnrollment Methods

The [**IX509SCEPEnrollment**](/windows/win32/Certenroll/nn-certenroll-ix509scepenrollment?branch=master) interface exposes the following methods.

## In this section



| Topic                                                                                                              | Description                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateRequestMessage method**](/windows/win32/Certenroll/nf-certenroll-ix509scepenrollment-createrequestmessage?branch=master)<br/>                         | Create a PKCS10 request message with a challenge password. The request message is in an enveloped PKCS7 encrypted with the SCEP server encryption certificate and signed by the server signing certificate.<br/> |
| [**CreateRetrieveCertificateMessage method**](/windows/win32/Certenroll/nf-certenroll-ix509scepenrollment-createretrievecertificatemessage?branch=master)<br/> | Retrieve a previously issued certificate.<br/>                                                                                                                                                                   |
| [**CreateRetrievePendingMessage method**](/windows/win32/Certenroll/nf-certenroll-ix509scepenrollment-createretrievependingmessage?branch=master)<br/>         | Create a message for certificate polling (manual enrollment).<br/>                                                                                                                                               |
| [**DeleteRequest method**](/windows/win32/Certenroll/nf-certenroll-ix509scepenrollment-deleterequest?branch=master)<br/>                                       | Delete any certificates or keys created for the request.<br/>                                                                                                                                                    |
| [**Initialize method**](/windows/win32/Certenroll/nf-certenroll-ix509scepenrollment-initialize?branch=master)<br/>                                             | Initialize the instance in preparation for a new request.<br/>                                                                                                                                                   |
| [**InitializeForPending method**](/windows/win32/Certenroll/nf-certenroll-ix509scepenrollment-initializeforpending?branch=master)<br/>                         | Initialize the instance to prepare to generate a message to either retrieve an issued certificate, or install a response for a previous request by the issuer.<br/>                                              |
| [**ProcessResponseMessage method**](/windows/win32/Certenroll/nf-certenroll-ix509scepenrollment-processresponsemessage?branch=master)<br/>                     | Process a response message and return the disposition of the message.<br/>                                                                                                                                       |



 

 

 




