---
description: 'The second step in a COM+ application design process is to break the conceptual model out into the logical tiers of the three-tier architecture: the presentation tier, or user services; the middle tier, or business services; and the data tier, or data services. If you are unfamiliar with three-tier architecture, see Using a Three-Tier Architecture Model.'
ms.assetid: 6dc0a0ab-2cfa-4cc9-92a6-0d7554dd3397
title: 'The Logical Model: Application Definition and Planning'
ms.topic: article
ms.date: 05/31/2018
---

# The Logical Model: Application Definition and Planning

The second step in a COM+ application design process is to break the conceptual model out into the logical tiers of the three-tier architecture: the *presentation tier*, or user services; the *middle tier*, or business services; and the *data tier*, or data services. If you are unfamiliar with three-tier architecture, see [Using a Three-Tier Architecture Model](using-a-three-tier-architecture-model.md).

Begin this process by looking through the conceptual model for nouns and verbs. The nouns can often translate into business objects (classes), and the verbs associated with them can translate into actions (methods of the classes). While it can be difficult to define all the nouns as business objects, omissions or mistakes will become obvious by the time you complete the logical model.

Most of the business objects will end up in the business services tier, with the remaining objects divided between user interface objects in the user services tier and data objects in the data services tier. When creating a logical model using the three-tier architecture, keep the following in mind:

-   Some of the nouns in the conceptual design will not represent actual physical pieces of data but may represent an action on the system or a business object's role on the system. A business object can also be a service that performs some sort of system control, such as a login ID for security.
-   Avoid creating vague business objects by "reading between the lines" in the [conceptual model](the-conceptual-model--application-requirements.md). Such business objects may not be correct, and you should consider them carefully before including them in the logical model. If they appear correct, add them to the conceptual model explicitly.
-   Avoid creating business objects that express the same information or function; duplication can be costly in terms of application speed and performance.
-   Determine object dependencies. Some nouns in the conceptual model may simply be attributes of other business objects. Decide if the attribute can exist independently. If so, it should become its own business object; if not, it should be combined with the appropriate business object.
-   Avoid creating business objects that try to do too much. Overloading business objects can mean more time spent separating code later and can be a maintenance headache. Distinct objects in the conceptual model should not be combined; they should remain separate business objects. You can handle any similarities by using code to delegate their common functions to a business object.
-   Remove any business objects that are not used in any usage scenarios. If the objects are intended to accommodate future growth, consider implementing them after the initial application is completed.

At this point, you can start thinking in terms of the computers and code. From these business services, determine the display and input functionality you need to provide as user services. Define what tables and stored procedures need to be provided as data services. To complete the logical model, define the interfaces for each service and include definitions of each data field and their validation rules. Also include all functions, their syntax, and their parameters.

The service or object definition should not include any aspect of the physical implementation. The intent is to provide a clear guideline for the logical component builders to work from and to enable other programmers to code pieces of the application that may use the component before it is actually completed. In the logical model design, you should document every screen, function, and object. Do not proceed to the physical model or implementation until you meet these criteria. If you proceed while the conceptual model and logical model are not in agreement, you will have serious problems later in the development cycle.

Incremental development of a COM+ application is common. This involves creating a subset of the final, known components and testing them through each layer of the application: client, business, and data tiers—through to data storage. This working model provides insight into additional requirements by the customer and implementation considerations. Often this working model is tested on a single computer.

## Related topics

<dl> <dt>

[The Conceptual Model: Application Requirements](the-conceptual-model--application-requirements.md)
</dt> <dt>

[The Physical Model: Application Architecture](the-physical-model--application-architecture.md)
</dt> <dt>

[Using a Three-Tier Architecture Model](using-a-three-tier-architecture-model.md)
</dt> </dl>

 

 



