---
title: Notification Routines
description: Notification Routines
ms.assetid: '993C0AB1-8A78-47A1-ABA7-A173B2EF0096'
---

# Notification Routines

## 

This section lists the port driver notification routines supplied by the Storport driver.

## In this section



| Topic                                                                                     | Description                                                                                                                                             |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**StorPortAsyncNotificationDetected**](storportasyncnotificationdetected.md)<br/> | A storage miniport driver calls **StorPortAsyncNotificationDetected** to notify the Storport driver of a storage device status change event.<br/> |
| [**StorPortNotification**](storportnotification.md)<br/>                           | The miniport driver uses the **StorPortNotification** routine to notify the Storport driver of certain events and conditions.<br/>                |
| [**StorPortStateChangeDetected**](storportstatechangedetected.md)<br/>             | Notifies the Storport port driver of a state change for a logical unit number (LUN), host bus adapter (HBA) port, or target device.<br/>          |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Notification%20Routines%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





