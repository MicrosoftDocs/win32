---
description: These APIs provide infrastructure for component health.
title: Test In Production (TIP) APIs
ms.topic: article
ms.date: 04/27/2023
---

# Test In Production (TIP) APIs

Test in Production APIs provide infrastructure to monitor component health.

These APIs emit [Event Tracing for Windows (ETW)](/windows-hardware/drivers/devtest/event-tracing-for-windows--etw-) events to the provider `50109fbd-6d85-5815-731e-c907eca1607b`. It is strongly recommended that you instead use the ETW APIs directly with a different provider.

These functions have no associated import library or header file; these functions must be invoked using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## In this section


### Functions

- [TestClose Function](tip-testclose-function.md)
- [TestControlReporting Function](tip-testcontrolreporting-function.md)
- [TestCreate Function](tip-testcreate-function.md)
- [TestOpen Function](tip-testopen-function.md)
- [TestQueryData Function](tip-testquerydata-function.md)
- [TestReport Function](tip-testreport-function.md)
- [TestUnlockData Function](tip-testunlockdata-function.md)

### Structures

- [TestInfo Structure](tip-testinfo-structure.md)
- [TipReportingInfo Structure](tip-tipreportinginfo-structure.md)

