---
title: Locking Routines
description: Locking Routines
ms.assetid: 8F413951-F936-4595-AFCB-26782DD06443
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Locking Routines

## 

This section lists the locking routines supplied by the Storport driver.

## In this section



| Topic                                                                       | Description                                                                                                                                                   |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**StorPortAcquireMSISpinLock**](storportacquiremsispinlock.md)<br/> | The **StorPortAcquireMSISpinLock** routine acquires the message signaled interrupt (MSI) spin lock that is associated with the specified message. <br/> |
| [**StorPortAcquireSpinLock**](storportacquirespinlock.md)<br/>       | The **StorPortAcquireSpinLock** routine acquires the specified spin lock. <br/>                                                                         |
| [**StorPortReleaseMSISpinLock**](storportreleasemsispinlock.md)<br/> | The **StorPortReleaseMSISpinLock** routine releases a previously acquired message signaled interrupt (MSI) spin lock for the specified message. <br/>   |
| [**StorPortReleaseSpinLock**](storportreleasespinlock.md)<br/>       | The **StorPortReleaseSpinLock** routine releases a spinlock acquired by [**StorPortAcquireSpinLock**](storportacquirespinlock.md).<br/>                |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Locking%20Routines%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





