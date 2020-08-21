---
title: Client-Side Design
description: Script in server-side HTML pages communicates with the Online Print Ordering Wizard client in which it is hosted. This communication is accomplished through methods and properties accessed by the window.external object.
ms.assetid: fa76ccee-0b94-41b5-8cc8-eb7e1818dbed
keywords:
- publishing wizards,client-side design
- window.external,publishing wizards
- publishing wizards,window.external
- publishing wizards,design considerations
- publishing wizards,Online Print Ordering Wizard
- Online Print Ordering Wizard,client-side design
ms.topic: article
ms.date: 05/31/2018
---

# Client-Side Design

Script in server-side HTML pages communicates with the Online Print Ordering Wizard client in which it is hosted. This communication is accomplished through methods and properties accessed by the **window.external** object.

The following topics are covered in this document.

-   [Methods and Properties](#methods-and-properties)
-   [Design Considerations](#design-considerations)
-   [Related topics](#related-topics)

## Methods and Properties

The following methods and properties are available through the **window.external** object.

-   [**FinalBack**](/windows/desktop/shell/iwebwizardhost-finalback)
-   [**FinalNext**](/windows/desktop/shell/iwebwizardhost-finalnext)
-   [**Cancel**](/windows/desktop/shell/iwebwizardhost-cancel)
-   [**PassportAuthenticate**](/windows/desktop/shell/inewwdevents-passportauthenticate)
-   [**SetHeaderText**](/windows/desktop/shell/iwebwizardhost-setheadertext)
-   [**SetWizardButtons**](/windows/desktop/shell/iwebwizardhost-setwizardbuttons)
-   [**Caption**](/previous-versions/windows/desktop/legacy/bb774352(v=vs.85))
-   [**Property**](/windows/desktop/shell/iwebwizardhost-property)

The server-side page's script calls these methods to notify the client of events during the publishing procedure. Let's look at [**FinalBack**](/windows/desktop/shell/iwebwizardhost-finalback) as an example. When the wizard displays the first server-side HTML page, it does so armed with knowledge of the handles for the wizard pages preceding and following the hosted HTML pages. At this point in our example, the user, sitting at that first HTML page, clicks the **Back** button. The wizard sends a notification of this event to the server. On receipt of this message, the server-side script refers to its **OnBack** handler for this event, which, as this is the first HTML page, calls the **FinalBack** method. This causes the wizard to navigate to the wizard page displayed before entering the server-side UI.

For a complete discussion of these methods and properties, see the documentation for the [**WebWizardHost**](/windows/desktop/shell/webwizardhost) and [**NewWDEvents**](/windows/desktop/shell/newwdevents) objects.

## Design Considerations

HTML making up each server-side page is displayed normally in the wizard pane. When designing these pages, bear in mind that a wizard window cannot be resized. Pages should therefore be constructed and sized so that scroll bars are avoided whenever possible to provide the user with smooth navigation through the wizard.

Each HTML page must also provide a handler for **OnBack**, **OnNext**, and **OnCancel** events. The **OnNext** handler will also handle the **Finish** event. A page that does not implement an **OnBack** function is considered invalid and will cause an error page to be displayed.

## Related topics

<dl> <dt>

[**WebWizardHost**](/windows/desktop/shell/webwizardhost)
</dt> <dt>

[**NewWDEvents**](/windows/desktop/shell/newwdevents)
</dt> <dt>

[Server-Side Design](pubwiz-server.md)
</dt> </dl>

 

 