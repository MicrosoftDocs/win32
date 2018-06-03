---
title: Remote Assistance
description: The Rendezvous API provides communication between an instant messaging (IM) application, such as Live Messenger, and two-person interactive applications, such as Windows Remote Assistance.
ms.assetid: 27f8ceda-4414-475d-b8c4-101ecc140cdb
keywords:
- Rendezvous
- Windows Live
- Windows Remote Assistance
- Offer Remote Assistance
- Ask for Remote Assistance
- instant messaging (IM)
- IM (instant messaging)
- remote assistance
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remote Assistance

The Rendezvous API provides communication between an instant messaging (IM) application, such as Live Messenger, and two-person interactive applications, such as Windows Remote Assistance. Windows Remote Assistance connects two computers so that one person can help troubleshoot or fix problems on the other person's computer. A remote assistance session begins after one person either offers or asks for assistance and the other person accepts.

The Rendezvous API consists of the Component Object Model (COM) interfaces [**IRendezvousApplication**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvousapplication), [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) and [**DRendezvousSessionEvents**](/previous-versions/windows/desktop/api/RendezvousSession/). A peer-to-peer application like Windows Remote Assistance implements the **IRendezvousApplication** interface. An IM application implements the **IRendezvousSession** and **DRendezvousSessionEvents** interface.

This topic contains the following sections:

-   [Remote Assistance Rendezvous Objects Registration](#remote-assistance-rendezvous-objects-registration)
    -   [Offer Remote Assistance Key](#offer-remote-assistance-key)
    -   [Ask for Remote Assistance Key](#ask-for-remote-assistance-key)
-   [Launching the Windows Remote Assistance IRendezvousApplication Based Object](#launching-the-windows-remote-assistance-irendezvousapplication-based-object)
-   [Implementing Rendezvous APIs for Instant Messaging Applications](#implementing-rendezvous-apis-for-instant-messaging-applications)
-   [Implementing Rendezvous APIs for Remote Assistance Applications](#implementing-rendezvous-apis-for-remote-assistance-applications)
-   [Steps in the IM/Request Remote Assistance Interaction](#steps-in-the-imrequest-remote-assistance-interaction)
-   [Steps in the IM/Offer Remote Assistance Interaction](#steps-in-the-imoffer-remote-assistance-interaction)
-   [Related topics](#related-topics)

## Remote Assistance Rendezvous Objects Registration

Windows Remote Assistance implements two [**IRendezvousApplication**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvousapplication) based objects. This is because Windows Remote Assistance provides two different functionalities. These are "Offer Remote Assistance" and "Ask for Remote Assistance". In order for the IM application to locate and launch a Windows Remote Assistance object, Windows Remote Assistance writes information for its two Rendezvous objects to the windows registry. The registration information is as follows:

### Offer Remote Assistance Key

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         RendezvousApps
            {703EA1A8-D73E-43e3-852C-EE85B5D872C2}
               Name = Offer RemoteAssistance
               Icon = 0x00000000 (0)
               RendezvousComponent = {49010C18-B110-421a-9047-ADCA421CBC40}
               Path = $(runtime.system32)\RAServer.exe
               URL = http://www.microsoft.com
```

### Ask for Remote Assistance Key

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         RendezvousApps
            {56b994a7-380f-410b-9985-c809d78c1bdc}
               Name = Ask for RemoteAssistance
               Icon = 0x00000001 (1)
               RendezvousComponent = {C0B3C446-3032-4016-926F-9BAE48BEBFBE}
               Path = $(runtime.system32)\RAServer.exe
               URL = http://www.microsoft.com
```

The Name and Icon from the registration information is displayed in the IM UI.

> [!Note]  
> The IM application can display the small icon associated with a Remote Assistance functionality by passing the Icon and Path values to the [ExtractIconEx](http://msdn.microsoft.com/library/ms648069(VS.85).aspx) function.

 

The RendezvousComponent value is the COM object GUID of the Windows Remote Assistance object implementing the [**IRendezvousApplication**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvousapplication). This GUID is used in the [CoCreateInstance](http://msdn.microsoft.com/library/ms686615(VS.85).aspx) call as explained below.

## Launching the Windows Remote Assistance IRendezvousApplication Based Object

In response to the Windows Remote Assistance Rendezvous functionality, that is, "Ask for Remote Assistance" or "Offer Remote Assistance", selected by the user from the IM UI, the IM application looks up the corresponding RendezvousComponent GUID for launching the Windows Remote AssistanceÂ [**RendezvousApplication**](remoteassist-rendezvousapplication.md) based COM object. The GUID is used during the [CoCreateInstance](http://msdn.microsoft.com/library/ms686615(VS.85).aspx) call to create the [**IRendezvousApplication**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvousapplication) based COM object and obtain its interface pointer. The IM application then calls the [**SetRendezvousSession**](https://www.bing.com/search?q=**SetRendezvousSession**) method of the Windows Remote AssistanceÂ COM object passing in the pointer to IM applications [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) based COM object. This initiates the IM/Windows Remote Assistance interaction.

## Implementing Rendezvous APIs for Instant Messaging Applications

For your IM application to integrate with Remote Assistance (that implements the [**IRendezvousApplication**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvousapplication) interface and supports the Rendezvous APIs), it must implement the [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) interface and provide a connection point for [**DRendezvousSessionEvents**](/previous-versions/windows/desktop/api/RendezvousSession/) interface.

Remote Assistance registers its [**IRendezvousApplication**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvousapplication) based COM objects into the registry. The IM application should use the RendezvousComponent GUID to make a [CoCreateInstance](http://msdn.microsoft.com/library/ms686615(VS.85).aspx) call and launch the Remote Assistance object.

After the Remote Assistance object launches, the IM application should call its implementation of [**SetRendezvousSession**](https://www.bing.com/search?q=**SetRendezvousSession**) to pass a pointer to the IM application's [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) object to the Remote Assistance object.

The Remote Assistance object uses the [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) object to communicate the [**RendezvousApplication**](remoteassist-rendezvousapplication.md) specific data during the session, and also uses the [**DRendezvousSessionEvents**](/previous-versions/windows/desktop/api/RendezvousSession/) connection point to subscribe to events associated with the session.

When Remote Assistance is finished using the messenger transport and ready to establish its own transport, it terminates the RendezvousSession by calling the [**Terminate**](/previous-versions/windows/desktop/api/RendezvousSession/nf-rendezvoussession-irendezvoussession-terminate) method. In response to this, the IM application should release the pointer to the object it originally obtained via the [CoCreateInstance](http://msdn.microsoft.com/library/ms686615(VS.85).aspx) call and close down the session.

## Implementing Rendezvous APIs for Remote Assistance Applications

If you are writing your own peer-to-peer application based on the Rendezvous API, then you might want to implement the [**IRendezvousApplication**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvousapplication)Â COM interface. You also need to add the required registration information to the windows registry on both the local and the remote computers. IM applications that are Rendezvous API aware and implement the [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) interface can then locate and launch your peer-to-peer COM object using the RendezvousComponent GUID. Windows Remote Assistance implements this interface and enables IM applications to integrate Remote Assistance.

As part of the [**IRendezvousApplication**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvousapplication) implementation, peer-to-peer applications implement the [**SetRendezvousSession**](https://www.bing.com/search?q=**SetRendezvousSession**) method. The IM applications pass in their COM object implementing the [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) and [**DRendezvousSessionEvents**](/previous-versions/windows/desktop/api/RendezvousSession/) interface to the peer-to-peer application by calling this **SetRendezvousSession** method . When the IM provider application initiates a session, it calls the **SetRendezvousSession** method. This method passes a pointer to the provider's **IRendezvousSession** object, which is used to communicate between the two peer-to-peer applications as long as the session is valid. As part of the same object it also passes in a pointer to **DRendezvousSessionEvents** interface.

When your application receives the pointer to the [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) object, it should call **IRendezvousSession**-&gt;[**AddRef**](https://msdn.microsoft.com/library/windows/desktop/ms691379) to keep the session alive. Using the [**DRendezvousSessionEvents**](/previous-versions/windows/desktop/api/RendezvousSession/) interface it should also establish a connection with the RendezvousSession event source object and subscribe to events associated with the IM session.

When your application finishes using the messenger transport and is ready to establish its own transport, it should call [**Terminate**](/previous-versions/windows/desktop/api/RendezvousSession/nf-rendezvoussession-irendezvoussession-terminate) to notify the IM application that you are done using the Session. Your application should also disconnect itself from the event source. Corresponding to the initial [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession)-&gt;[**AddRef**](https://msdn.microsoft.com/library/windows/desktop/ms691379) , it should call **IRendezvousSession**-&gt;[**Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317). This helps the IM application clean up the **IRendezvousSession**Â COM object. The peer-to-peer application should take care of cleaning up the [**IRendezvousApplication**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvousapplication) based COM object.

## Steps in the IM/Request Remote Assistance Interaction

The following graphic shows the sequence of steps in the interaction between an IM application and a Remote Assistance application (RA).

![steps in the im/request remote assistance interaction](https://www.bing.com/search?q=steps in the im/request remote assistance interaction)

1.  IM looks up Request RA registration info from the Windows Registry and populates the "Name" in its UI.
2.  From the IM UI, IM Buddy A (RA Novice) sends "Request RemoteAssistance" invitation to the IM buddy B (RA Expert).
3.  IM Buddy B (in this case, RA Expert) accepts the invitation.
4.  IM sends ACK to IM Buddy A (that is, RA Novice).
5.  IM A creates [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) based COM object.
6.  IM A creates [**IRendezvousApplication**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvousapplication) based Request RemoteAssistance COM object using its RendezvousComponent GUID `{C0B3C446-3032-4016-926F-9BAE48BEBFBE}`.
7.  IM A calls [**SetRendezvousSession**](https://www.bing.com/search?q=**SetRendezvousSession**) method of the Remote Assistance COM object passing in the pointer to the object that implements [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) and [**DRendezvousSessionEvents**](/previous-versions/windows/desktop/api/RendezvousSession/) interfaces.
8.  IM B creates [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) based COM object.
9.  IM B creates [**IRendezvousApplication**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvousapplication) based Request RemoteAssistance COM object using its RendezvousComponent GUID `{C0B3C446-3032-4016-926F-9BAE48BEBFBE}`.
10. IM B calls [**SetRendezvousSession**](https://www.bing.com/search?q=**SetRendezvousSession**) method of the Remote Assistance COM object passing in the pointer to the object that implements [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) and [**DRendezvousSessionEvents**](/previous-versions/windows/desktop/api/RendezvousSession/)interfaces.
11. RA application (A) implements Event Object to sink [**DRendezvousSessionEvents**](/previous-versions/windows/desktop/api/RendezvousSession/) generated by the IM application. In the [**SetRendezvousSession**](https://www.bing.com/search?q=**SetRendezvousSession**) method, using the **DRendezvousSessionEvents** object, RA establishes a connection between the RendezvousSessionEvent Source and the Request RA Event object (Event Sink).
12. RA (A) queries for the [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) messenger interface. Does an [**AddRef**](https://msdn.microsoft.com/library/windows/desktop/ms691379) on the **IRendezvousSession** object pointer. IM application releases the **IRendezvousSession** pointer at the end of the [**SetRendezvousSession**](https://www.bing.com/search?q=**SetRendezvousSession**) method.
13. RA (A) Calls the [**Flags**](/previous-versions/windows/desktop/api/RendezvousSession/nf-rendezvoussession-irendezvoussession-get_flags) method of [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) to check whether it is **RSF\_INVITER** or **RSF\_INVITEE**. In the Request RA scenario, **RSF\_INVITER** is RA Novice (IM A), **RSF\_INVITEE** is RA Expert (IM B).
14. RA (A) calls the [**RemoteUser**](/previous-versions/windows/desktop/api/RendezvousSession/nf-rendezvoussession-irendezvoussession-get_remoteuser). This is for RA Expert to get the RA Novice name and vice versa.
15. RA application (B) implements Event Object to sink [**DRendezvousSessionEvents**](/previous-versions/windows/desktop/api/RendezvousSession/) generated by the IM application. In the [**SetRendezvousSession**](https://www.bing.com/search?q=**SetRendezvousSession**) method, using the **DRendezvousSessionEvents** object, RA establishes a connection between the RendezvousSessionEvent Source and the Request RA Event object (Event Sink).
16. RA (B) queries for the [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) messenger interface and does an [**AddRef**](https://msdn.microsoft.com/library/windows/desktop/ms691379) on the **IRendezvousSession** object pointer. IM application releases the **IRendezvousSession** pointer at the end of the [**SetRendezvousSession**](https://www.bing.com/search?q=**SetRendezvousSession**) method.
17. RA (B) calls the [**Flags**](/previous-versions/windows/desktop/api/RendezvousSession/nf-rendezvoussession-irendezvoussession-get_flags) method of [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) to check whether it is **RSF\_INVITER** or **RSF\_INVITEE**. In the Request RA scenario, **RSF\_INVITER** is RA Novice (IM A), **RSF\_INVITEE** is RA Expert (IM B).
18. RA (B) calls the [**RemoteUser**](/previous-versions/windows/desktop/api/RendezvousSession/nf-rendezvoussession-irendezvoussession-get_remoteuser). This is for RA Expert to get the RA Novice name and vice-versa.
19. RA (A) receives a state change event **RSS\_CONNECTED**. This signals RA that the two RA RendezvousApplication objects are connected and data can be sent/received now.
20. RA (B) receives a state change event **RSS\_CONNECTED**. This signals RA that the two RA RendezvousApplication objects are connected and data can be sent/received now.
21. RA request application (A) calls the [**SendContextData**](/previous-versions/windows/desktop/api/RendezvousSession/nf-rendezvoussession-irendezvoussession-sendcontextdata) method to send RA specific data to the remote RA request application (B).
22. RA specific data goes to the IM layer.
23. RA data is sent over IM transport layer.
24. RA data is received by IM (B).
25. RA (B) receives data via [**DISPID\_EVENT\_ON\_CONTEXT\_DATA**](remoteassist-drendezvoussessionevents-oncontextdata.md). RA specific data is sent and received between A and B over the IM RendezvousSession.
26. When the RA protocol completes, RA (A) calls [**Terminate**](/previous-versions/windows/desktop/api/RendezvousSession/nf-rendezvoussession-irendezvoussession-terminate) method.
27. TerminateSession message reaches IM(A) layer.
28. TerminateSession message sent to remote IM (B) over IM transport.
29. RA (A) receives the [**OnStateChanged**](remoteassist-drendezvoussessionevents-onstatechanged.md) event with **RSS\_CANCELED** state.
30. RA (A) disconnects from the event source.
31. RA (A) also calls [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession)-&gt;[**Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317). RA RendezvousApplication COM object's refcount goes to 0 and it automatically terminates.
32. TerminateSession message received by IM(B) layer.
33. RA (B) receives the [**OnStateChanged**](remoteassist-drendezvoussessionevents-onstatechanged.md) event with **RSS\_CANCELED** state.
34. RA (B) disconnects from the event source.
35. RA (A) also calls [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession)-&gt;[**Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317). RA RendezvousApplication COM object's reference count goes to 0 and it automatically terminates.

## Steps in the IM/Offer Remote Assistance Interaction

1.  IM looks up Offer RA registration info from the windows registry and populates the "Name" in its UI.
2.  From the IM UI, IM Buddy B (RA Expert) sends "Offer RemoteAssistance" invitation to the IM buddy A (RA Novice).
3.  IM Buddy A (RA Novice) accepts the invitation.
4.  IM sends ACK to IM Buddy B (RA Expert).
5.  IM B creates [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) based COM object.
6.  IM B creates [**IRendezvousApplication**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvousapplication) based Offer RemoteAssistance COM object using its RendezvousComponent GUID {49010C18-B110-421a-9047-ADCA421CBC40}.

After this the sequence of steps is similar to those listed in the [Steps in the IM/Request Remote Assistance Interaction](#steps-in-the-imrequest-remote-assistance-interaction) section.

## Related topics

<dl> <dt>

[Remote Assistance Sample Code](remoteassist-sample-code.md)
</dt> </dl>

 

 




