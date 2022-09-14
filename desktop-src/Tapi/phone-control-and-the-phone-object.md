---
description: TAPI 3.1 introduces COM-based phone controls. Familiarity with COM, OLE Automation, and scripting is assumed, as is knowledge of the TAPI 3 object model. Knowledge of the TAPI 2 phone control functions is also helpful.
ms.assetid: e56aef54-e358-429b-9f0f-c8776507d95f
title: Phone Control and the Phone Object
ms.topic: article
ms.date: 05/31/2018
---

# Phone Control and the Phone Object

TAPI 3.1 introduces COM-based phone controls. Familiarity with COM, OLE Automation, and scripting is assumed, as is knowledge of the TAPI 3 object model. Knowledge of the TAPI 2 phone control functions is also helpful.

Phone control is implemented at three levels of features, each of which builds upon the previous one:

-   Phone object. The first level defines how TAPI 2.x's phone devices (APIs, constants, and messages beginning with "phone") are exposed in the TAPI 3.1 object model. This involves a new phone object exposed from TAPI 3.1, with [**ITPhone**](/windows/desktop/api/tapi3if/nn-tapi3if-itphone) as the default interface on the new object. The **ITPhone** interface, along with its associated constants, enumerated types, and events, generally exposes the same level of detail and functionality as the TAPI 2.x functions, constants, structures, and messages that begin with the word "phone." This level also involves new interfaces on several existing TAPI 3.x objects to facilitate creation of phone objects and association of phone objects with other objects to which they are related.
-   Automated phone control and call handling. The second level consists of an additional interface called [**ITAutomatedPhoneControl**](/windows/desktop/api/tapi3if/nn-tapi3if-itautomatedphonecontrol) and its associated constants, enumerated types, and events. This is a secondary interface on the phone object. If the phone device was opened with owner privilege, use the **QueryInterface** method on the [**ITPhone**](/windows/desktop/api/tapi3if/nn-tapi3if-itphone) interface to obtain an **ITAutomatedPhoneControl** interface pointer.
-   Windows 2000 Phone Dialer. The third level consists of changes to the Windows 2000 Phone Dialer application to implement specific user interactions.

Microsoft or third party developers can use the TAPI 3.1 object model to implement more advanced applications or services involving phones, including a service that enables universal serial bus (USB) handsets, for example, to be used for phone calls even if no user is logged in and no other TAPI application has been explicitly started.

In TAPI 3.0, a Phone MSP attempted to improve phone devices associated with lines used for TAPI 3.0 calls. This development intended to support modems with software-switchable speakerphones. TAPI 3.1 applications that use this modem type should use the TAPI 3.1 phone objects to manipulate the modem hookswitch state.

For more information and a list of all interfaces associated with the Phone object, see [Phone Object Interfaces](phone-object-interfaces.md). The phone control interfaces expose methods that enable control over phone sets using COM.

 

 



