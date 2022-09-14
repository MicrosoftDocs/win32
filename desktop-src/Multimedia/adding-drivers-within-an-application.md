---
title: Adding Drivers Within an Application
description: Adding Drivers Within an Application
ms.assetid: cd9bd0a8-652b-440b-a197-81e20a9d71f1
keywords:
- audio compression manager (ACM),adding drivers
- ACM (audio compression manager),adding drivers
- ACM examples,adding drivers
- adding drivers
- acmDriverAdd function
- global drivers
- local drivers
- audio compression manager (ACM),global drivers
- ACM (audio compression manager),global drivers
- audio compression manager (ACM),local drivers
- ACM (audio compression manager),local drivers
ms.topic: article
ms.date: 05/31/2018
---

# Adding Drivers Within an Application

If you need your application to implement its own compression routines internally, the application can add drivers to the ACM by calling the [**acmDriverAdd**](/windows/desktop/api/Msacm/nf-msacm-acmdriveradd) function. The application implements the driver by providing a function that conforms to the [**acmDriverProc**](/windows/desktop/api/Msacm/nc-msacm-acmdriverproc) prototype. After the application has added the driver, the application can use the driver through the ACM as it would use any other driver.

The ACM treats drivers as either global or local. An application specifies whether a driver should be added as global or local when it calls **acmDriverAdd**. There are two differences between global and local drivers:

-   Drivers added as global drivers are not shared with other applications.
-   An application can directly alter the priority of a global driver (but not a local driver) by calling the [**acmDriverPriority**](/windows/desktop/api/Msacm/nf-msacm-acmdriverpriority) function. The ACM conducts a prioritized search when seeking an appropriate driver to provide an implementation of a function call. The ACM always gives local drivers higher priority than global drivers. The most recently added local driver has highest priority.

 

 




