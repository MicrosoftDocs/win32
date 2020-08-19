---
title: Server-Side Design
description: Server-side functions communicate with the client wizard through the windows.external object. Server-side script provides these functions to respond to wizard events and to retrieve information about the wizard.
ms.assetid: 7cc8b814-f230-4326-a9df-a491ed35483e
keywords:
- publishing wizards,server-side design
- window.external,publishing wizards
- publishing wizards,window.external
- publishing wizards,navigation script functions
- scripts,publishing wizards
ms.topic: article
ms.date: 05/31/2018
---

# Server-Side Design

Server-side functions communicate with the client wizard through the **windows.external** object. Server-side script provides these functions to respond to wizard events and to retrieve information about the wizard.

The following topics are covered in this document.

-   [Implementing Navigation Script Functions](#implementing-navigation-script-functions)
    -   [OnBack()](#onback)
    -   [OnNext()](#onnext)
    -   [OnCancel()](#oncancel)
-   [Other Methods and Properties](#other-methods-and-properties)
    -   [Methods](#methods)
    -   [Properties](#properties)
-   [Related topics](#related-topics)

## Implementing Navigation Script Functions

Server-side script in each HTML page responds to navigation buttons through functions for **OnBack**, **OnNext**, and **OnCancel**. These functions must be accessible through **IHTMLDocument::get\_Script** on the client and take no parameters.

### OnBack()

-   Responds when the user clicks **Back** in the wizard.
-   If the current server-side page is the first server-side page, call **window.external.FinalBack** to instruct the client to navigate to the previous client-side page.
-   If the current server-side page is not the first server-side page, navigate to the previous server-side page.
-   This function must be implemented for each page. Any page that fails to do so is considered invalid and displays an error page.

### OnNext()

-   Responds when the user clicks **Next** in the wizard.
-   If the current server-side page is the last server-side page, call **window.external.FinalNext** to instruct the client to navigate to the next client-side page or to complete the wizard.
-   If the current server-side page is not the last server-side page, navigate to the next server-side page.

### OnCancel()

-   Responds when the user clicks **Cancel** in the wizard.
-   The UI should be designed so the user can cancel at any time.
-   Once any processing in the **OnCancel** function is processed, the client closes the wizard.

## Other Methods and Properties

Client-implemented functions are accessed through **windows.external**, as are properties. Available services are as follows:

### Methods

-   [**SetHeaderText**](/windows/desktop/shell/iwebwizardhost-setheadertext)
-   [**SetWizardButtons**](/windows/desktop/shell/iwebwizardhost-setwizardbuttons)
-   [**PassportAuthenticate**](/windows/desktop/shell/inewwdevents-passportauthenticate)

### Properties

-   [**Caption**](/previous-versions/windows/desktop/legacy/bb774352(v=vs.85))
-   [**Property**](/windows/desktop/shell/iwebwizardhost-property)

The following code sample shows server-side code for a simple wizard page which implements the web service's error page.


```
<html>
    <head>
        <script language="JavaScript">
            function window.onload()
            {
                window.external.SetWizardButtons(1, 0, 0);    
                <!-- Back button enabled -->
            }

            function window.onback()
            {
                window.external.FinalBack();
            }
        </script>
    </head>
.
.
.
</html>
                    
```



## Related topics

<dl> <dt>

[Client-Side Design](pubwiz-client.md)
</dt> <dt>

[Registering a Service](pubwiz-reg.md)
</dt> </dl>

 

 