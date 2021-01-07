---
description: The IX509SCEPEnrollment interface exposes the following methods.
ms.assetid: B45B68D2-A14D-4D14-AF5F-1A1BB9921A0D
title: IX509SCEPEnrollment Methods
ms.topic: reference
ms.date: 05/31/2018
---

# IX509SCEPEnrollment Methods

The [**IX509SCEPEnrollment**](/windows/desktop/api/Certenroll/nn-certenroll-ix509scepenrollment) interface exposes the following methods.

## In this section



| Topic                                                                                                              | Description                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateRequestMessage method**](/windows/desktop/api/Certenroll/nf-certenroll-ix509scepenrollment-createrequestmessage)<br/>                         | Create a PKCS10 request message with a challenge password. The request message is in an enveloped PKCS7 encrypted with the SCEP server encryption certificate and signed by the server signing certificate.<br/> |
| [**CreateRetrieveCertificateMessage method**](/windows/desktop/api/Certenroll/nf-certenroll-ix509scepenrollment-createretrievecertificatemessage)<br/> | Retrieve a previously issued certificate.<br/>                                                                                                                                                                   |
| [**CreateRetrievePendingMessage method**](/windows/desktop/api/Certenroll/nf-certenroll-ix509scepenrollment-createretrievependingmessage)<br/>         | Create a message for certificate polling (manual enrollment).<br/>                                                                                                                                               |
| [**DeleteRequest method**](/windows/desktop/api/Certenroll/nf-certenroll-ix509scepenrollment-deleterequest)<br/>                                       | Delete any certificates or keys created for the request.<br/>                                                                                                                                                    |
| [**Initialize method**](/windows/desktop/api/Certenroll/nf-certenroll-ix509scepenrollment-initialize)<br/>                                             | Initialize the instance in preparation for a new request.<br/>                                                                                                                                                   |
| [**InitializeForPending method**](/windows/desktop/api/Certenroll/nf-certenroll-ix509scepenrollment-initializeforpending)<br/>                         | Initialize the instance to prepare to generate a message to either retrieve an issued certificate, or install a response for a previous request by the issuer.<br/>                                              |
| [**ProcessResponseMessage method**](/windows/desktop/api/Certenroll/nf-certenroll-ix509scepenrollment-processresponsemessage)<br/>                     | Process a response message and return the disposition of the message.<br/>                                                                                                                                       |



 

 

 




