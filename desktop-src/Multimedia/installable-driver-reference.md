---
title: Installable Driver Reference
description: Installable Driver Reference
ms.assetid: 869b92f1-2711-4198-9911-3df1ebc58d5f
keywords:
- Windows multimedia,installable driver reference
- multimedia,installable driver reference
- installable drivers,reference
- installable driver reference,about
- reference for installable drivers,about
ms.topic: article
ms.date: 05/31/2018
---

# Installable Driver Reference

The functions and messages associated with installable drivers are grouped as follows.

## Loading and Unloading Drivers

-   [GetDriverModuleHandle](/windows/win32/api/mmiscapi/nf-mmiscapi-getdrivermodulehandle)
-   [OpenDriver](/windows/win32/api/mmiscapi/nf-mmiscapi-opendriver)
-   [SendDriverMessage](/windows/win32/api/mmiscapi/nf-mmiscapi-senddrivermessage)

## CloseDriver

-   [**DRV\_CLOSE**](drv-close.md)
-   [**DRV\_DISABLE**](drv-disable.md)
-   [**DRV\_ENABLE**](drv-enable.md)
-   [**DRV\_FREE**](drv-free.md)
-   [**DRV\_LOAD**](drv-load.md)
-   [**DRV\_OPEN**](drv-open.md)

## Configuring a Driver

-   [**DRV\_CONFIGURE**](drv-configure.md)
-   [**DRV\_QUERYCONFIGURE**](drv-queryconfigure.md)
-   [**DRVCONFIGINFO**](/windows/win32/api/mmiscapi/ns-mmiscapi-drvconfiginfo)

## Installing a Driver

-   [**DRV\_INSTALL**](drv-install.md)
-   [**DRV\_REMOVE**](drv-remove.md)

## Driver Functions

-   [DefDriverProc](/windows/win32/api/mmiscapi/nf-mmiscapi-defdriverproc)
-   [DriverCallback](/windows/win32/api/mmiscapi/nf-mmiscapi-drivercallback)
-   [DriverProc](/windows/win32/api/mmiscapi/nc-mmiscapi-driverproc)

## Related topics

<dl> <dt>

[Installable Drivers](installable-drivers.md)
</dt> </dl>

 

 