---
description: 'For a Tablet PC application to operate with ink effectively, that application should be able to:'
ms.assetid: 64a7b773-35c9-42f7-aec4-7fed34fa84d9
title: Important Interoperability Scenarios
ms.topic: article
ms.date: 05/31/2018
---

# Important Interoperability Scenarios

For a Tablet PC application to operate with ink effectively, that application should be able to:

-   Save a document in the application's native binary format without losing the document's ink.
-   Save a document in any format the application normally supports (for example, HTML or Rich Text Format (RTF)) without losing the document's ink.
-   Copy ink from one application to another by using the Clipboard. This works if the other application only recognizes a specific format, such as HTML, RTF, or bitmap (BMP). It also works whether the destination application recognizes ink. If it does recognize ink, the destination application is able to interpret the ink that has been copied as ink and not just as an image.
-   Copy ink, along with text, between two applications that recognize ink, each of which has more than one [**Ink**](inkdisp-class.md) object. This requires HTML, RTF, or a similar format.
-   Copy ink between two applications, each of which has one [**Ink**](inkdisp-class.md) object. Ink Serialized Format (ISF) is sufficient for this.
-   Copy ink from an application that has more than one [**Ink**](inkdisp-class.md) object to an application that has only one **Ink** object. In this case, the application that has more than one **Ink** object must be able to produce Ink Serialized Format (ISF).
-   Copy ink from an application that has one [**Ink**](inkdisp-class.md) object to an application that has more than one **Ink** object. In this case, the application that has more than one **Ink** object must be able to recognize ISF.

 

 



