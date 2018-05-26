---
title: Error Values
description: The following table provides error values, a description of the error value, and if applicable, the action that the application should take in the event the error is encountered.
ms.assetid: 51f2f5da-69cd-483c-851a-78770f25e7c1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Error Values

The following table provides error values, a description of the error value, and if applicable, the action that the application should take in the event the error is encountered.

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows.

 



| Error value                                                 | Description                                                                              | Application response                                             |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| GQOS\_NO\_ERRORVALUE                                        | No error occurred, or the error value is unavailable.                                    |                                                                  |
| GQOS\_ERRORVALUE\_UNKNOWN                                   |                                                                                          |                                                                  |
| Admission (resource) Error Values                           |                                                                                          |                                                                  |
| GQOS\_OTHER                                                 |                                                                                          |                                                                  |
| GQOS\_DELAYBND                                              | An upstream QOS-enabled device cannot meet the specified delay-bound requirement.        | Retry the operation with a more relaxed delay-bound requirement. |
| GQOS\_BANDWIDTH                                             | An upstream QOS-enabled device cannot meet bandwidth requirement.                        | Retry the operation with a more relaxed bandwidth requirement.   |
| GQOS\_MTU                                                   | The Maximum Transmission Unit (MTU) in [**FLOWSPEC**](/windows/previous-versions/Qos/ns-qos-_flowspec?branch=master) is too large.        | Adjust the packet size and retry the operation.                  |
| GQOS\_FLOW\_RATE                                            | An upstream QOS-enabled device cannot meet bandwidth requirement.                        | Retry the operation with a more relaxed bandwidth requirement.   |
| GQOS\_PEAK\_RATE                                            | An upstream QOS-enabled device cannot meet bandwidth requirement.                        | Retry the operation with a more relaxed bandwidth requirement.   |
| Policy Errors                                               |                                                                                          |                                                                  |
| GQOS\_POLICY\_ERROR\_UNKNOWN                                | A policy error occurred for an unknown reason.                                           |                                                                  |
| GQOS\_POLICY\_GLOBAL\_DEF\_FLOW\_COUNT<br/>           | Policy error: the operation would exceed the global default policy flow count.           | Abort or retry at a later time.                                  |
| GQOS\_POLICY\_GLOBAL\_GRP\_FLOW\_COUNT<br/>           | Policy error: the operation would exceed the global group policy flow count.             | Abort or retry at a later time.                                  |
| GQOS\_POLICY\_GLOBAL\_USER\_FLOW\_COUNT<br/>          | Policy error: the operation would exceed the global user policy flow count.              | Abort or retry at a later time.                                  |
| GQOS\_POLICY\_GLOBAL\_UNK\_USER\_FLOW\_COUNT<br/>     | Policy error: the operation would exceed the unknown user policy flow count.             | Abort or retry at a later time.                                  |
| GQOS\_POLICY\_SUBNET\_DEF\_FLOW\_COUNT<br/>           | Policy error: the operation would exceed the subnet default policy flow count.           | Abort or retry at a later time.                                  |
| GQOS\_POLICY\_SUBNET\_GRP\_FLOW\_COUNT<br/>           | Policy error: the operation would exceed the subnet default policy flow count.           | Abort or retry at a later time.                                  |
| GQOS\_POLICY\_SUBNET\_USER\_FLOW\_COUNT<br/>          | Policy error: the operation would exceed the subnet default policy flow count.           | Abort or retry at a later time.                                  |
| GQOS\_POLICY\_SUBNET\_UNK\_USER\_FLOW\_COUNT<br/>     | Policy error: the operation would exceed the subnet default policy flow count.           | Abort or retry at a later time.                                  |
| GQOS\_POLICY\_GLOBAL\_ DEF\_FLOW\_DURATION<br/>       | Policy error: the operation would exceed the global default policy flow duration.        | Abort.                                                           |
| GQOS\_POLICY\_GLOBAL\_GRP\_FLOW\_DURATION<br/>        | Policy error: the operation would exceed the global group policy flow duration.          | Abort.                                                           |
| GQOS\_POLICY\_GLOBAL\_ USER\_FLOW\_DURATION<br/>      | Policy error: the operation would exceed the global user policy flow duration.           | Abort.                                                           |
| GQOS\_POLICY\_GLOBAL\_UNK\_USER\_FLOW\_DURATION<br/>  | Policy error: the operation would exceed the unknown user policy flow duration.          | Abort.                                                           |
| GQOS\_POLICY\_SUBNET\_DEF\_FLOW\_DURATION<br/>        | Policy error: the operation would exceed the subnet default policy flow duration.        | Abort.                                                           |
| GQOS\_POLICY\_SUBNET\_ GRP\_FLOW\_DURATION<br/>       | Policy error: the operation would exceed the subnet group policy flow duration.          | Abort.                                                           |
| GQOS\_POLICY\_SUBNET\_ USER\_FLOW\_DURATION<br/>      | Policy error: the operation would exceed the subnet user policy flow duration.           | Abort.                                                           |
| GQOS\_POLICY\_SUBNET\_UNK\_USER\_FLOW\_DURATION<br/>  | Policy error: the operation would exceed the subnet unknown user policy flow duration.   | Abort.                                                           |
| GQOS\_POLICY\_GLOBAL\_DEF\_FLOW\_RATE<br/>            | Policy error: the operation would exceed the global default policy flow rate.            | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_GLOBAL\_GRP\_FLOW\_RATE<br/>            | Policy error: the operation would exceed the global group policy flow rate.              | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_GLOBAL\_USER\_FLOW\_RATE<br/>           | Policy error: the operation would exceed the global user policy flow rate.               | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_GLOBAL\_UNK\_USER\_FLOW\_RATE<br/>      | Policy error: the operation would exceed the unknown user policy flow rate.              | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_DEF\_FLOW\_RATE<br/>            | Policy error: the operation would exceed the subnet default policy flow rate.            | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_GRP\_FLOW\_RATE<br/>            | Policy error: the operation would exceed the subnet group policy flow rate.              | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_USER\_FLOW\_RATE<br/>           | Policy error: the operation would exceed the subnet user policy flow rate.               | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_UNK\_USER\_FLOW\_RATE<br/>      |                                                                                          |                                                                  |
| GQOS\_POLICY\_GLOBAL\_DEF\_PEAK\_RATE<br/>            | Policy error: the operation would exceed the global default policy peak rate.            | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_GLOBAL\_GRP\_PEAK\_RATE<br/>            | Policy error: the operation would exceed the global group policy peak rate.              | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_GLOBAL\_USER\_PEAK\_RATE<br/>           | Policy error: the operation would exceed the global user policy peak rate.               | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_GLOBAL\_UNK\_USER\_PEAK\_RATE<br/>      | Policy error: the operation would exceed the unknown user policy peak rate.              | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_DEF\_PEAK\_RATE<br/>            | Policy error: the operation would exceed the subnet default policy peak rate.            | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_GRP\_PEAK\_RATE<br/>            | Policy error: the operation would exceed the subnet default policy peak rate.            | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_USER\_PEAK\_RATE<br/>           | Policy error: the operation would exceed the subnet default policy peak rate.            | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_UNK\_USER\_PEAK\_RATE<br/>      | Policy error: the operation would exceed the subnet default policy peak rate.            | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_GLOBAL\_DEF\_SUM\_FLOW\_RATE<br/>       | Policy error: the operation would exceed the global default policy total flow rate.      | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_GLOBAL\_GRP\_SUM\_FLOW\_RATE<br/>       | Policy error: the operation would exceed the global group policy total flow rate.        | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_GLOBAL\_USER\_SUM\_FLOW\_RATE<br/>      | Policy error: the operation would exceed the global user policy total flow rate.         | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_GLOBAL\_UNK\_USER\_SUM\_FLOW\_RATE<br/> | Policy error: the operation would exceed the unknown user policy total flow rate.        | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_DEF\_SUM\_FLOW\_RATE<br/>       | Policy error: the operation would exceed the subnet default policy total flow rate.      | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_GRP\_SUM\_FLOW\_RATE<br/>       | Policy error: the operation would exceed the subnet group policy total flow rate.        | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_UNK\_USER\_SUM\_FLOW\_RATE<br/> | Policy error: the operation would exceed the subnet unknown user policy total flow rate. | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_ USER\_SUM\_FLOW\_RATE<br/>     | Policy error: the operation would exceed the subnet user policy total flow rate.         | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_GLOBAL\_DEF\_PEAK\_RATE<br/>            | Policy error: the operation would exceed the global default policy total peak rate.      | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_GLOBAL\_GRP\_SUM\_PEAK\_RATE<br/>       | Policy error: the operation would exceed the global default policy total peak rate.      | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_GLOBAL\_USER\_SUM\_PEAK\_RATE<br/>      | Policy error: the operation would exceed the global default policy total peak rate.      | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_GLOBAL\_UNK\_USER\_SUM\_PEAK\_RATE<br/> | Policy error: the operation would exceed the global default policy total peak rate.      | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_DEF\_SUM\_PEAK\_RATE<br/>       | Policy error: the operation would exceed the subnet default policy total peak rate.      | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_GRP\_SUM\_PEAK\_RATE<br/>       | Policy error: the operation would exceed the subnet default policy total peak rate.      | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_USER\_SUM\_PEAK\_RATE<br/>      | Policy error: the operation would exceed the subnet default policy total peak rate.      | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_SUBNET\_UNK\_USER\_SUM\_PEAK\_RATE<br/> | Policy error: the operation would exceed the subnet default policy total peak rate.      | Abort or retry with reduced QOS requirements.                    |
| GQOS\_POLICY\_UNKNOWN\_USER                                 | Policy error: the user is unknown.                                                       | Check the user's identification and security attributes.         |
| GQOS\_POLICY\_NO\_PRIVILEGES                                | Policy error: the user has no privilege.                                                 | Abort. Possible shut down on sender or receiver.                 |
| GQOS\_POLICY\_EXPIRED\_USER\_TOKEN                          | Policy error: the user identification token has expired.                                 | Abort or retry.                                                  |
| GQOS\_POLICY\_NO\_RESOURCES                                 | Policy error: LPM out of resources (memory).                                             | Abort or retry at a later time.                                  |
| GQOS\_POLICY\_PRE\_EMPTED                                   | Policy error: the operation was pre-empted by a higher priority request.                 | Abort or retry at a later time.                                  |
| GQOS\_POLICY\_USER\_CHANGED                                 | Policy error: user identification has changed after the reservation was approved.        | Abort.                                                           |
| GQOS\_POLICY\_NO\_ACCEPTS                                   | Policy error: the operation was rejected by all policy modules.                          | Abort.                                                           |
| GQOS\_POLICY\_NO\_MEMORY                                    | Policy error: LPM out of memory.                                                         | Abort or retry at a later time.                                  |
| GQOS\_POLICY\_CRAZY\_FLOWSPEC                               | Policy error: invalid [**FLOWSPEC**](/windows/previous-versions/Qos/ns-qos-_flowspec?branch=master).                                      | Check the [**FLOWSPEC**](/windows/previous-versions/Qos/ns-qos-_flowspec?branch=master) structure.                |
| GQOS\_POLICY\_ERROR\_USERID                                 | Unable to understand the user ID                                                         | Abort.                                                           |
| RSVP Errors                                                 |                                                                                          |                                                                  |
| GQOS\_NO\_PATH                                              | No matching path state for the reservation request.                                      | Check the QOS call sequence.                                     |
| GQOS\_NO\_SENDER                                            | No sender information for the reservation request.                                       | Check the QOS call sequence.                                     |
| GQOS\_BAD\_STYLE                                            | Mismatch in Resv style.                                                                  | Check the RESV filter specifications.                            |
| GQOS\_UNKNOWN\_STYLE                                        | The Resv style is unknown.                                                               | Check the RESV filter specifications.                            |
| GQOS\_BAD\_DSTPORT                                          | Conflicting or invalid destination port.                                                 | Check the QOS call sequence.                                     |
| GQOS\_BAD\_SNDPORT                                          | Conflicting or invalid source port.                                                      | Check the QOS call sequence.                                     |
| GQOS\_AMBIG\_FILTER                                         | Ambiguous filter specification in RESV.                                                  | Check the RESV filter specifications.                            |
| GQOS\_PREEMPTED                                             | Service preempted due to a higher priority reservation.                                  | Try to invoke QOS again at a later time.                         |
| GQOS\_UNKN\_OBJ\_CLASS                                      | Invalid RSVP syntax in objects                                                           | Abort                                                            |
| GQOS\_UNKNOWN\_CTYPE                                        | Invalid RSVP syntax in objects                                                           | Abort                                                            |
| GQOS\_INVALID                                               | Invalid operation or parameters.                                                         |                                                                  |
| API Errors                                                  |                                                                                          |                                                                  |
| GQOS\_API\_BADSEND                                          |                                                                                          |                                                                  |
| GQOS\_API\_BADRECV                                          |                                                                                          |                                                                  |
| GQOS\_API\_BADSPORT                                         |                                                                                          |                                                                  |
| Traffic Control System Errors                               |                                                                                          |                                                                  |
| GQOS\_TC\_GENERIC                                           |                                                                                          |                                                                  |
| GQOS\_TC\_INVALID                                           |                                                                                          |                                                                  |
| GQOS\_NO\_MEMORY                                            | Not enough memory available to execute the requested RSVP/traffic control operation      | Abort the operation or retry at a later time.                    |
| GQOS\_BAD\_ADDRESSTYPE                                      | Traffic control error: invalid address type.                                             | Check the address type of the socket.                            |
| GQOS\_BAD\_DUPLICATE                                        |                                                                                          |                                                                  |
| GQOS\_CONFLICT                                              |                                                                                          |                                                                  |
| GQOS\_NOTREADY                                              |                                                                                          |                                                                  |
| GQOS\_WOULDBLOCK                                            | RSVP/traffic control operation would block.                                              | Retry at a later time.                                           |
| GQOS\_INCOMPATIBLE                                          |                                                                                          |                                                                  |
| GQOS\_BAD\_SDMODE                                           |                                                                                          |                                                                  |
| GQOS\_BAD\_QOSPRIORITY                                      | Traffic control error: invalid internal priority.                                        | Check the traffic control priority object.                       |
| GQOS\_BAD\_TRAFFICCLASS                                     |                                                                                          |                                                                  |
| GQOS\_NO\_SYS\_RESOURCES                                    | Traffic control error: out of system resources.                                          | Abort or retry at a later time.                                  |
| RSVP System Errors                                          |                                                                                          |                                                                  |
| GQOS\_OTHER\_SYS                                            |                                                                                          |                                                                  |
| GQOS\_MEMORY\_SYS                                           |                                                                                          |                                                                  |
| GQOS\_API\_SYS                                              |                                                                                          |                                                                  |
| GQOS\_SETQOS\_NO\_LOCAL\_APPS                               |                                                                                          |                                                                  |
| Traffic Control Errors                                      |                                                                                          |                                                                  |
| GQOS\_CONFLICT\_SERV                                        | Conflicting traffic control filters.                                                     | Check the QOS specifications.                                    |
| GQOS\_NO\_SERV                                              | The service is unknown to local traffic control.                                         | Check the Service Type parameter.                                |
| GQOS\_BAD\_FLOWSPEC                                         |                                                                                          |                                                                  |
| GQOS\_BAD\_TSPEC                                            |                                                                                          |                                                                  |
| GQOS\_BAD\_ADSPEC                                           |                                                                                          |                                                                  |
| WSAIoctl Errors                                             |                                                                                          |                                                                  |
| GQOS\_IOCTL\_SYSTEMFAILURE                                  |                                                                                          |                                                                  |
| GQOS\_IOCTL\_NOBYTESRETURNED                                |                                                                                          |                                                                  |
| GQOS\_IOCTL\_INVALIDSOCKET                                  |                                                                                          |                                                                  |
| SIO\_SET\_QOS Errors                                        |                                                                                          |                                                                  |
| GQOS\_SETQOS\_BADINBUFFER                                   |                                                                                          |                                                                  |
| GQOS\_SETQOS\_BADFLOWSPEC                                   |                                                                                          |                                                                  |
| GQOS\_SETQOS\_COLLISION                                     |                                                                                          |                                                                  |
| GQOS\_SETQOS\_BADPROVSPECBUF                                |                                                                                          |                                                                  |
| GQOS\_SETQOS\_ILLEGALOP                                     |                                                                                          |                                                                  |
| GQOS\_SETQOS\_INVALIDADDRESS                                |                                                                                          |                                                                  |
| GQOS\_SETQOS\_OUTOFMEMORY                                   |                                                                                          |                                                                  |
| GQOS\_SETQOS\_EXCEPTION                                     |                                                                                          |                                                                  |
| GQOS\_SETQOS\_BADADDRLEN                                    |                                                                                          |                                                                  |
| GQOS\_SETQOS\_NOSOCKNAME                                    |                                                                                          |                                                                  |
| GQOS\_SETQOS\_IPTOSFAIL                                     |                                                                                          |                                                                  |
| GQOS\_SETQOS\_OPENSESSIONFAIL                               |                                                                                          |                                                                  |
| GQOS\_SETQOS\_SENDFAIL                                      |                                                                                          |                                                                  |
| GQOS\_SETQOS\_RECVFAIL                                      |                                                                                          |                                                                  |
| GQOS\_SETQOS\_BADPOLICYOBJECT                               |                                                                                          |                                                                  |
| GQOS\_SETQOS\_UNKNOWNFILTEROBJ                              |                                                                                          |                                                                  |
| GQOS\_SETQOS\_BADFILTERTYPE                                 |                                                                                          |                                                                  |
| GQOS\_SETQOS\_BADFILTERCOUNT                                |                                                                                          |                                                                  |
| GQOS\_SETQOS\_BADOBJLENGTH                                  |                                                                                          |                                                                  |
| GQOS\_SETQOS\_BADFLOWCOUNT                                  |                                                                                          |                                                                  |
| GQOS\_SETQOS\_UNKNOWNPSOBJ                                  |                                                                                          |                                                                  |
| GQOS\_SETQOS\_BADPOLICYOBJ                                  |                                                                                          |                                                                  |
| GQOS\_SETQOS\_BADFLOWDESC                                   |                                                                                          |                                                                  |
| GQOS\_SETQOS\_BADPROVSPECOBJ                                |                                                                                          |                                                                  |
| GQOS\_SETQOS\_NOLOOPBACK                                    |                                                                                          |                                                                  |
| GQOS\_SETQOS\_MODENOTSUPPORTED                              |                                                                                          |                                                                  |
| GQOS\_SETQOS\_MISSINGFLOWDESC                               |                                                                                          |                                                                  |
| SIO\_GET\_QOS Errors                                        |                                                                                          |                                                                  |
| GQOS\_GETQOS\_BADOUTBUFFER                                  |                                                                                          |                                                                  |
| GQOS\_GETQOS\_SYSTEMFAILURE                                 |                                                                                          |                                                                  |
| GQOS\_GETQOS\_EXCE;TION                                     |                                                                                          |                                                                  |
| GQOS\_GETQOS\_INTERNALFAILURE                               |                                                                                          |                                                                  |
| SIO\_CHK\_QOS Errors                                        |                                                                                          |                                                                  |
| GQOS\_CHKQOS\_BADINBUFFER                                   |                                                                                          |                                                                  |
| GQOS\_ CHKQOS\_BADOUTBUFFER                                 |                                                                                          |                                                                  |
| GQOS\_ CHKQOS\_SYSTEMFAILURE                                |                                                                                          |                                                                  |
| GQOS\_ CHKQOS\_INTERNALFAILURE                              |                                                                                          |                                                                  |
| GQOS\_ CHKQOS\_BADPARAMETER                                 |                                                                                          |                                                                  |
| GQOS\_ CHKQOS\_EXCEPTION                                    |                                                                                          |                                                                  |



 

 

 

 





