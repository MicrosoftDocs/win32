---
description: The ITParticipantControl interface is implemented by the IPConf MSP.
ms.assetid: e617f2a4-6be8-4cb1-9f03-470c5100b834
title: ITParticipantControl interface (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipantControl interface

\[**ITParticipantControl** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITParticipantControl** interface is implemented by the IPConf MSP. This interface is exposed on the call object. This interface allows an application to retrieve pointers to the participants in a conference. The **ITParticipantControl** interface is created by calling **QueryInterface** on [**ITCallInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallinfo).

## Members

The **ITParticipantControl** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITParticipantControl** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITParticipantControl** interface has these methods.



| Method                                                                      | Description                                                                                                                                                                 |
|:----------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnumerateParticipants**](itparticipantcontrol-enumerateparticipants.md) | Enumerates participants currently involved in the conference.<br/>                                                                                                    |
| [**get\_Participants**](itparticipantcontrol-get-participants.md)          | Creates a collection of participants associated with the current conference. Provided for Automation client applications, such as those written in Visual Basic.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



 

