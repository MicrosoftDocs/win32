---
title: Error Codes
description: The following table provides error codes, a description of the error code, and if applicable, the action that the application should take in the event the error is encountered.
ms.assetid: '18b2b037-5a0d-4d47-8eab-25075f248081'
---

# Error Codes

The following table provides error codes, a description of the error code, and if applicable, the action that the application should take in the event the error is encountered.

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows.

 



| Error code               | Description                                          | Application response                                                                                          |
|--------------------------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| GQOS\_NO\_ERRORCODE      | No error occurred, or the error code is unavailable. |                                                                                                               |
| GQOS\_RSVP               | The error occurred in the local RSVP engine.         | Check the QOS call sequence.                                                                                  |
| GQOS\_KERNEL\_TC         | The error occurred in local traffic control.         | Depending on the specific error value, the application may retry the operation with reduced QOS requirements. |
| GQOS\_NET\_ADMISSION     | Admission failure, due to the SBM (part of the ACS). | Stop the operation, retry with reduced QOS requirements, or try later.                                        |
| GQOS\_NET\_POLICY        | A policy-related error occurred.                     | Stop or retry with reduced QOS requirements (depending on the specific error value).                          |
| GQOS\_ERRORCODE\_UNKNOWN |                                                      |                                                                                                               |
| GQOS\_API                |                                                      |                                                                                                               |
| GQOS\_RSVP\_SYS          |                                                      |                                                                                                               |
| GQOS\_KERNEL\_TC         |                                                      |                                                                                                               |



 

 

 

 




