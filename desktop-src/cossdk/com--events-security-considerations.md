---
description: When using the COM+ events service, there are steps you can take to ensure that any sensitive information contained in an event is not compromised.
ms.assetid: 1f8faea0-afc2-4999-a962-d6fd10307d6c
title: COM+ Events Security Considerations
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Events Security Considerations

When using the COM+ events service, there are steps you can take to ensure that any sensitive information contained in an event is not compromised.

Event publishers should keep in mind that any party that can write to your COM+ catalog can subscribe to your events. Therefore, if the information contained in an event class object is sensitive, you should use the Component Services administration tool to verify that communications with subscribers are encrypted for the application that contains the event class components. (On the **Security** tab of the COM+ application property sheet, select **Packet Privacy** as the **Authentication Level for Calls** setting.) Also, you should use [event filters](filtering-events-in-com-.md) to help ensure that events are delivered only to the appropriate subscribers.

Event subscribers should keep in mind that a malicious party with access to your network and knowledge of your event class object could create false events. You should therefore use [role-based security](role-based-security-administration.md) to help ensure that callers of your event class object's methods have appropriate credentials to perform the actions described by your implementation.

To help protect both publishers and subscribers, use the COM+ Events service on a private network of trusted hosts that is isolated from the Internet by a firewall.

## Related topics

<dl> <dt>

[COM+ Security](com--security.md)
</dt> <dt>

[Filtering Events in COM+](filtering-events-in-com-.md)
</dt> <dt>

[The COM+ Event Class Object](the-com--event-class-object.md)
</dt> </dl>

 

 



