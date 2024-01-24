---
description: TAPI provides access to a phones display.
ms.assetid: f6017ecc-b2a0-4a92-8c28-ce7411f8dd84
title: Display
ms.topic: article
ms.date: 05/31/2018
---

# Display

TAPI provides access to a phone's display. The display is modeled as an alphanumeric area with rows and columns. A phone's device capabilities indicate the size of a phone's display as the number of rows and the number of columns. Both these numbers are zero if the phone device does not have a display. Use [**phoneSetDisplay**](/windows/desktop/api/Tapi/nf-tapi-phonesetdisplay) to write information to the display of an open phone device, and [**phoneGetDisplay**](/windows/desktop/api/Tapi/nf-tapi-phonegetdisplay) to retrieve the current contents of a phone's display.

When the display of a phone device is changed, a [**PHONE\_STATE**](phone-state.md) message is sent to the application function to notify the application about the state change. Parameters to this message provide an indication of the change.

 

 



