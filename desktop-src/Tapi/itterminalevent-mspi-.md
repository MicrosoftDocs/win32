---
description: When the ITTAPIEventNotification::Event method returns TAPI\_EVENT equal to TE\_TERMINAL, the methods exposed by the ITTerminalEvent interface can be used to retrieve information concerning the terminal event that has occurred, if an MSP exists.
ms.assetid: 5277776e-0471-41b6-b662-4346a9d237ec
title: ITTerminalEvent (MSPI)
ms.topic: article
ms.date: 05/31/2018
---

# ITTerminalEvent (MSPI)

When the [**ITTAPIEventNotification::Event**](/windows/desktop/api/Tapi3if/nf-tapi3if-ittapieventnotification-event) method returns [**TAPI\_EVENT**](/windows/desktop/api/Tapi3if/ne-tapi3if-tapi_event) equal to **TE\_TERMINAL**, the methods exposed by the **ITTerminalEvent** interface can be used to retrieve information concerning the terminal event that has occurred, if an MSP exists.

The **ITTerminalEvent** interface is implemented by an MSP and is not available if there is no media service provider associated with the address. Please see **ITTerminalEvent** in the MSP Interface section for details on this interface.

 

 



