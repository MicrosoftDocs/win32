---
description: Identifying Valid DVD Operations
ms.assetid: d368b552-7ed3-4334-b97b-ff49d6c331c3
title: Identifying Valid DVD Operations
ms.topic: article
ms.date: 05/31/2018
---

# Identifying Valid DVD Operations

Several factors determine whether you can perform a given DVD operation:

-   The current domain. Some commands are only valid in certain domains. When the domain changes, the navigator sends an EC\_DVD\_DOMAIN\_CHANGE event. You can also call [**IDvdInfo2::GetCurrentDomain**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getcurrentdomain) to get the current domain.
-   UOPS flags. These are flags written onto the disc that indicate which operations are permitted. Whenever the flags change, the navigator sends a EC\_DVD\_VALID\_UOPS\_CHANGE event with the new flags. You can also call [**IDvdInfo2::GetCurrentUOPS**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getcurrentuops) to get the current UOPS flags.
-   DVD content. Some commands may not be relevant based on the content of the DVD. For example, the [**IDvdControl2::SelectAngle**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-selectangle) method might be permitted according to the current domain and UOPS flags, yet the video might have only one angle. In that case, the **SelectAngle** call is permitted but is not a meaningful option.

When in doubt, permit an action. At worst, the [**IDvdControl2**](/windows/desktop/api/Strmif/nn-strmif-idvdcontrol2) method will fail and you can give feedback to the user. The feedback should be relatively unobtrusive. For example, you might flash a small red X to alert the user. The DVD Navigator returns VFW\_E\_DVD\_INVALIDDOMAIN when the domain prohibits an operation, and VFW\_E\_DVD\_OPERATION\_INHIBITED when the UOPS flags prohibit an operation.

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



