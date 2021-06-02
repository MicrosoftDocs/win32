---
description: The following sections contain an alphabetic list of functions grouped by area. The information for each function includes a list of the valid call states on entry of the function and typical call state transitions when the request is complete.
ms.assetid: 555d6af2-b440-4636-b90e-da297a369753
title: TAPI Functions
ms.topic: article
ms.date: 05/31/2018
---

# TAPI Functions

The following sections contain an alphabetic list of functions grouped by area. The information for each function includes a list of the valid call states on entry of the function and typical call state transitions when the request is complete.

-   [Assisted Telephony Functions](assisted-telephony-functions.md)
-   [Call Center Functions](call-center-functions.md)
-   [Line Device Functions](line-device-functions.md)
-   [Phone Device Functions](phone-device-functions.md)

For TAPI functions categorized by service level and task, see [TAPI Quick Function Reference](tapi-quick-function-reference.md).

Please note that service provider limitations may exist concerning the actual states in which a function can be performed. Applications must check the **dwCallFeatures** member in the [**LINECALLSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linecallstatus) structure, the **dwAddressFeatures** member in the [**LINEADDRESSSTATUS**](/windows/desktop/api/Tapi/ns-tapi-lineaddressstatus) structure, and the **dwLineFeatures** member in the [**LINEDEVSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linedevstatus) structure to determine whether or not a function is permitted within the current call state.

 

 



