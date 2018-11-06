---
title: Keyboard Handling in Controls
description: Keyboard Handling in Controls
ms.assetid: 33affb3f-5d52-4ada-9751-0775b31a375e
ms.topic: article
ms.date: 05/31/2018
---

# Keyboard Handling in Controls

Keyboard handling support for the following functionality is strongly recommended, although it is recognized that it is not applicable to all containers.

-   Support for OLEMISC\_ACTSLIKELABEL and OLEMISC\_ACTSLIKEBUTTON status bits.
-   Implementing the DisplayAsDefault ambient property (if it exists, it can return **FALSE**).
-   Implementing tab handling, including tab order.

Some containers will use ActiveX controls in traditional compound document scenarios. For example, a spreadsheet may allow a user to embed an ActiveX control into a worksheet. In such scenarios, the container would do keyboard handling differently, because the keyboard interface should remain consistent with the user's expectations of a spreadsheet. Documentation for such products should inform users of differences in control handling in these different scenarios. Other containers should endeavor to honor the above functionality correctly, including Mnemonic handling.

## Related topics

<dl> <dt>

[Containers](containers.md)
</dt> </dl>

 

 




