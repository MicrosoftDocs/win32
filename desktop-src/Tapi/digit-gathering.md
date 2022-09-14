---
description: Besides enabling digit monitoring and being notified of digits one at a time, an application can also request that multiple digits be collected in a buffer.
ms.assetid: db83c48a-5178-40ed-90a9-e7c8e1886fe0
title: Digit Gathering
ms.topic: article
ms.date: 05/31/2018
---

# Digit Gathering

Besides enabling digit monitoring and being notified of digits one at a time, an application can also request that multiple digits be collected in a buffer. Only when the buffer is full or when some other termination condition is met is the application notified. Digit gathering is useful for functions such as credit card number collection. It is performed when an application calls [**lineGatherDigits**](/windows/desktop/api/Tapi/nf-tapi-linegatherdigits), specifying a buffer to fill with digits. Digit gathering terminates when one of the following conditions is true:

-   The requested number of digits has been collected.
-   One of multiple termination digits is detected. The termination digits are specified to [**lineGatherDigits**](/windows/desktop/api/Tapi/nf-tapi-linegatherdigits), and the termination digit is placed in the buffer as well.
-   One of two timeouts expires. The timeouts are a first digit timeout, specifying the maximum duration before the first digit must be collected, and an inter-digit timeout, specifying the maximum duration between successive digits.
-   Digit gathering is canceled explicitly by [**lineGatherDigits**](/windows/desktop/api/Tapi/nf-tapi-linegatherdigits) again with either another set of parameters to start a new gathering request or by using a **NULL** digit buffer parameter to cancel.

When digit gathering terminates for any reason, a [**LINE\_GATHERDIGITS**](line-gatherdigits.md) message is sent to the application that requested the digit gathering. Only a single digit gathering request can be outstanding on a call at any given time across all applications that are owners of the call.

Digit gathering and digit monitoring can be enabled on the same call at the same time. In that case, the application will receive a [**LINE\_MONITORDIGITS**](line-monitordigits.md) message for each detected digit and a separate LINE\_GATHERDIGITS message when the buffer is sent back.

 

 



