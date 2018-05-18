---
title: I/O Request Processing Routines
description: I/O Request Processing Routines
ms.assetid: '4EDBD130-1AC0-40F0-B3F3-CE68A430807F'
---

# I/O Request Processing Routines

## 

This section lists the I/O request processing routines supplied by the Storport driver.

## In this section



| Topic                                                                       | Description                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**StorPortBusy**](storportbusy.md)<br/>                             | The **StorPortBusy** routine notifies the port driver that the adapter is currently busy, handling outstanding requests. <br/>                                                                                                                   |
| [**StorPortCompleteRequest**](storportcompleterequest.md)<br/>       | The **StorPortCompleteRequest** routine completes all outstanding requests setting the SRB status value to **SrbStatus**. <br/>                                                                                                                  |
| [**StorPortCompleteServiceIrp**](storportcompleteserviceirp.md)<br/> | The **StorPortCompleteServiceIrp** routine is called by a Storport virtual miniport driver when it needs to complete a request that it received in its [**HwStorProcessServiceRequest**](hwstorprocessservicerequest.md) callback routine.<br/> |
| [**StorPortDeviceBusy**](storportdevicebusy.md)<br/>                 | The **StorPortDeviceBusy** routine notifies the port driver that the specified logical unit is currently busy, handling outstanding requests. <br/>                                                                                              |
| [**StorPortDeviceReady**](storportdeviceready.md)<br/>               | The **StorPortDeviceReady** routine notifies the port driver that the indicated logical unit is ready to handle new requests. <br/>                                                                                                              |
| [**StorPortFreeWorker**](storportfreeworker.md)<br/>                 | Frees a Storport work item previously allocated by the [**StorPortInitializeWorker**](storportinitializeworker.md) routine.<br/>                                                                                                                |
| [**StorPortGetRequestInfo**](storportgetrequestinfo.md)<br/>         | The **StorPortGetRequestInfo** routine retrieves the IO request information associated with a SCSI request block (SRB) and returns it in a [**STOR\_REQUEST\_INFO**](stor-request-info.md) structure. <br/>                                     |
| [**StorPortInitializeWorker**](storportinitializeworker.md)<br/>     | Creates a new Storport work item that runs in a system worker thread.<br/>                                                                                                                                                                       |
| [**StorPortQueueWorkItem**](storportqueueworkitem.md)<br/>           | Schedules a Storport work item to execute within the context of a system worker thread.<br/>                                                                                                                                                     |
| [**StorPortPause**](storportpause.md)<br/>                           | The **StorPortPause** routine pauses an adapter for the specified period of time. <br/>                                                                                                                                                          |
| [**StorPortPauseDevice**](storportpausedevice.md)<br/>               | The **StorPortPauseDevice** routine pauses a specific logical unit device for the specified period of time. <br/>                                                                                                                                |
| [**StorPortReady**](storportready.md)<br/>                           | The **StorPortReady** routine notifies the port driver that the adapter is no longer busy.<br/>                                                                                                                                                  |
| [**StorPortResume**](storportresume.md)<br/>                         | The **StorPortResume** routine resumes a paused adapter.<br/>                                                                                                                                                                                    |
| [**StorPortResumeDevice**](storportresumedevice.md)<br/>             | The **StorPortResumeDevice** routine resumes a previously paused logical unit.<br/>                                                                                                                                                              |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20I/O%20Request%20Processing%20Routines%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





