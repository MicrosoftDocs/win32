---
description: The application can request one of two operating modes when opening a phone device.
ms.assetid: 2bb16fbe-883e-4734-a071-f14f5e5737e3
title: Operating Modes and Privileges
ms.topic: article
ms.date: 05/31/2018
---

# Operating Modes and Privileges

The application can request one of two operating modes when opening a phone device. These modes reflect the privileges the application requests for the device:

-   Opening a phone for monitor privileges lets the application determine the status of the phone device. Messages are sent to the application when status changes on the phone device are detected.
-   An application that opens a phone device for owner privileges can use operations that modify the state of the phone device. Owner privilege automatically includes full monitor privileges as well. At any time, a given phone device can be open only once for owner privileges, but multiple times for monitor privileges. All **phoneSet** operations require owner privileges, while all **phoneGet** operations require only monitor privileges.

 

 



