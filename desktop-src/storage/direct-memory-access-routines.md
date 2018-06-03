---
title: Direct Memory Access Routines
description: Direct Memory Access Routines
ms.assetid: CE01DEAF-1878-43CE-98F9-93A58418B89B
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Direct Memory Access Routines

## 

This section lists the direct memory access (DMA) routines supplied by the Storport driver.

## In this section



| Topic                                                                               | Description                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**StorPortBuildScatterGatherList**](storportbuildscattergatherlist.md)<br/> | The **StorPortBuildScatterGatherList** routine creates a scatter/gather list for the specified data buffer.<br/>                                                                                                                              |
| [**StorPortGetScatterGatherList**](storportgetscattergatherlist.md)<br/>     | The [**StorPortGetScatterGatherList**](storportgetscattergatherlist.md) routine retrieves the associated scatter/gather list for the specified SCSI request block (SRB). <br/>                                                               |
| [**StorPortPutScatterGatherList**](storportputscattergatherlist.md)<br/>     | The **StorPortPutScatterGatherList** routine releases any resources associated with a scatter/gather list that was previously created by a call to the [**StorPortBuildScatterGatherList**](storportbuildscattergatherlist.md) routine.<br/> |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Direct%20Memory%20Access%20Routines%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





