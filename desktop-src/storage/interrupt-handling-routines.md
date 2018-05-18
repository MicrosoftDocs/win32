---
title: Interrupt Handling Routines
description: Interrupt Handling Routines
ms.assetid: 'C54F4602-39C9-4F4D-99D7-7AC1ED362E15'
---

# Interrupt Handling Routines

## 

This section lists the interrupt handling routines supplied by the Storport driver.

## In this section



| Topic                                                                     | Description                                                                                                                          |
|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**StorPortGetMSIInfo**](storportgetmsiinfo.md)<br/>               | The **StorPortGetMSIInfo** routine retrieves the message signaled interrupt (MSI) information for the specified message. <br/> |
| [**StorPortSynchronizeAccess**](storportsynchronizeaccess.md)<br/> | The **StorPortSynchronizeAccess** routine provides synchronized access to a miniport driver's device extension. <br/>          |
| [**StorPortInitializeDpc**](storportinitializedpc.md)<br/>         | The **StorPortInitializeDpc** routine initializes a StorPort DPC. <br/>                                                        |
| [**StorPortIssueDpc**](storportissuedpc.md)<br/>                   | The **StorPortIssueDpc** routine issues a deferred procedure call (DPC). <br/>                                                 |
| [**StorPortStallExecution**](storportstallexecution.md)<br/>       | The **StorPortStallExecution** routine stalls the miniport driver. <br/>                                                       |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Interrupt%20Handling%20Routines%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





