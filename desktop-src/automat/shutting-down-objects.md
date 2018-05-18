---
title: Shutting Down Objects
description: Describes how to shut down an ActiveX object.
ms.assetid: '10e92b01-1ffc-441b-bcf5-e6781ff12cdd'
---

# Shutting Down Objects

ActiveX objects must shut down in the following way:

-   If the object's application is visible, the object should shut down only in response to an explicit user command (for example, clicking **Exit** on the **File** menu) or the equivalent command from an ActiveX client.

-   If the object's application is not visible, the object should shut down only when the last external reference is gone.

-   If the object's application is visible and is controlled by an ActiveX client, it should become invisible when the user shuts it down (for example, clicking **Exit** on the **File** menu). This behavior allows the controller to continue to control the object. The controller should shut down only when the last external reference to the object has disappeared.

 

 




