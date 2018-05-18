---
Description: 'The IX509SCEPEnrollment interface exposes the following methods.'
ms.assetid: 'B45B68D2-A14D-4D14-AF5F-1A1BB9921A0D'
title: IX509SCEPEnrollment Methods
---

# IX509SCEPEnrollment Methods

The [**IX509SCEPEnrollment**](ix509scepenrollment.md) interface exposes the following methods.

## In this section



| Topic                                                                                                              | Description                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateRequestMessage method**](ix509scepenrollment-createrequestmessage.md)<br/>                         | Create a PKCS10 request message with a challenge password. The request message is in an enveloped PKCS7 encrypted with the SCEP server encryption certificate and signed by the server signing certificate.<br/> |
| [**CreateRetrieveCertificateMessage method**](ix509scepenrollment-createretrievecertificatemessage.md)<br/> | Retrieve a previously issued certificate.<br/>                                                                                                                                                                   |
| [**CreateRetrievePendingMessage method**](ix509scepenrollment-createretrievependingmessage.md)<br/>         | Create a message for certificate polling (manual enrollment).<br/>                                                                                                                                               |
| [**DeleteRequest method**](ix509scepenrollment-deleterequest.md)<br/>                                       | Delete any certificates or keys created for the request.<br/>                                                                                                                                                    |
| [**Initialize method**](ix509scepenrollment-initialize.md)<br/>                                             | Initialize the instance in preparation for a new request.<br/>                                                                                                                                                   |
| [**InitializeForPending method**](ix509scepenrollment-initializeforpending.md)<br/>                         | Initialize the instance to prepare to generate a message to either retrieve an issued certificate, or install a response for a previous request by the issuer.<br/>                                              |
| [**ProcessResponseMessage method**](ix509scepenrollment-processresponsemessage.md)<br/>                     | Process a response message and return the disposition of the message.<br/>                                                                                                                                       |



 

 

 




