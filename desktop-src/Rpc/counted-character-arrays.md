---
title: Counted Character Arrays
description: The \ size\_is\ attribute indicates the upper bound of the array while the \ length\_is\ attribute indicates the number of array elements to transmit.
ms.assetid: bed10259-3034-4be8-91f5-5201c2e19c6b
ms.topic: article
ms.date: 05/31/2018
---

# Counted Character Arrays

The \[ [size\_is](/windows/desktop/Midl/size-is)\] attribute indicates the upper bound of the array while the \[ [length\_is](/windows/desktop/Midl/length-is)\] attribute indicates the number of array elements to transmit. In addition to the array, the remote procedure prototype must include any variables representing length or size that determine the transmitted array elements (they can be separate parameters or bundled with the string in a structure). These attributes can be used with wide-character or single-byte character arrays just as they would be with arrays of other types.

The information in this section describes remote procedure parameter prototypes for character arrays. It is divided into the following topics:

-   [\[in, out, size\_is\] Prototype](-in-out-size-is-prototype.md)
-   [\[in, size\_is and out, size\_is\] Prototype](-in-size-is-and-out-size-is-prototype.md)

 

 