---
title: Checking IAccessible Return Values
description: Client developers should not rely on the Component Object Model (COM) macros SUCCEEDED and FAILED to test IAccessible return values, because values other than S\_OK are considered a success.
ms.assetid: 0def0349-178b-4be5-aa1d-6602dc015981
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Checking IAccessible Return Values

Client developers should not rely on the Component Object Model (COM) macros [**SUCCEEDED**](https://msdn.microsoft.com/library/windows/desktop/ms687197) and [**FAILED**](https://msdn.microsoft.com/library/windows/desktop/ms693474) to test [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) return values, because values other than S\_OK are considered a success. For example, a method can return S\_FALSE, which is considered a success by the **SUCCEEDED** macro, but still receive a **NULL** pointer in an output parameter.

Client developers must guard against the possibility that some servers return error codes other than the documented values. To be safe, you must ensure that all the output parameters contain valid information and meet the following criteria:

-   All pointers are non-**NULL**.
-   The **vt** member of any [VARIANT](http://go.microsoft.com/fwlink/p/?linkid=127015) structure is not equal to VT\_EMPTY.

 

 




