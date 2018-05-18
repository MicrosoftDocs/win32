---
Description: 'The FaxOutgoingQueue configuration object is used by a fax client application to set and retrieve the configuration parameters on the outbound fax queue on a fax server.'
ms.assetid: 'bad77c9e-2ae5-41a6-ace3-b4b92eb66cc2'
title: FaxOutgoingQueue object
---

# FaxOutgoingQueue object

The **FaxOutgoingQueue** configuration object is used by a fax client application to set and retrieve the configuration parameters on the outbound fax queue on a fax server. The object also includes a method to manage the outbound fax jobs in the job queue. You can also use the **FaxOutgoingQueue** object to create and access [**FaxOutgoingJobs**](-mfax-faxoutgoingjobs.md) collection objects.

## Members

The **FaxOutgoingQueue** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxOutgoingQueue** object has these methods.



| Method                                               | Description                                                                                                                                                                                                                                                                                                 |
|:-----------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetJob**](-mfax-faxoutgoingqueue-getjob.md)      | The [**GetJob**](-mfax-faxoutgoingqueue-getjob.md) method returns an outbound fax job in the job queue according to its ID.<br/>                                                                                                                                                                     |
| [**GetJobs**](-mfax-faxoutgoingqueue-getjobs-vb.md) | The [**GetJobs**](-mfax-faxoutgoingqueue-getjobs-vb.md) method returns a collection of the outbound fax jobs in the job queue.<br/>                                                                                                                                                                  |
| [**Refresh**](-mfax-faxoutgoingqueue-refresh-vb.md) | The [**Refresh**](-mfax-faxoutgoingqueue-refresh-vb.md) method refreshes **FaxOutgoingQueue** object information from the fax server. When the **Refresh** method is called, any configuration changes made after the last [**Save**](-mfax-faxoutgoingqueue-save-vb.md) method call are lost.<br/> |
| [**Save**](-mfax-faxoutgoingqueue-save-vb.md)       | The [**Save**](-mfax-faxoutgoingqueue-save-vb.md) method saves the **FaxOutgoingQueue** object data.<br/>                                                                                                                                                                                            |



 

### Properties

The **FaxOutgoingQueue** object has these properties.



| Property                                                                                        | Access type           | Description                                                                                                                                                                                                                                                                                                                               |
|:------------------------------------------------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AgeLimit**](-mfax-faxoutgoingqueue-agelimit-vb.md)<br/>                               | Read/write<br/> | The [**AgeLimit**](-mfax-faxoutgoingqueue-agelimit-vb.md) property is a value that indicates the number of days that the fax service retains an unsent job in the fax job queue. <br/>                                                                                                                                             |
| [**AllowPersonalCoverPages**](-mfax-faxoutgoingqueue-allowpersonalcoverpages-vb.md)<br/> | Read/write<br/> | The AllowPersonalCoverPages property is a Boolean value that indicates whether fax client applications can include a user-designed cover page with fax transmissions.<br/>                                                                                                                                                          |
| [**Blocked**](-mfax-faxoutgoingqueue-blocked-vb.md)<br/>                                 | Read/write<br/> | The [**Blocked**](-mfax-faxoutgoingqueue-blocked-vb.md) property is a Boolean value that indicates whether the job queue for outgoing faxes is blocked. <br/>                                                                                                                                                                      |
| [**Branding**](-mfax-faxoutgoingqueue-branding-vb.md)<br/>                               | Read/write<br/> | The [**Branding**](-mfax-faxoutgoingqueue-branding-vb.md) property is a Boolean value that indicates whether the fax service generates a brand (banner) at the top of outgoing fax transmissions. A brand contains transmission-related information, such as the transmitting station identifier, date, time, and page count.<br/> |
| [**DiscountRateEnd**](-mfax-faxoutgoingqueue-discountrateend-vb.md)<br/>                 | Read/write<br/> | The [**DiscountRateEnd**](-mfax-faxoutgoingqueue-discountrateend-vb.md) property is a value that indicates the time at which the discount period for transmitting faxes ends. The discount period applies to outgoing faxes.<br/>                                                                                                  |
| [**DiscountRateStart**](-mfax-faxoutgoingqueue-discountratestart-vb.md)<br/>             | Read/write<br/> | The [**DiscountRateStart**](-mfax-faxoutgoingqueue-discountratestart-vb.md) property is a value that indicates the time at which the discount period for transmitting faxes begins. The discount period applies to outgoing faxes.<br/>                                                                                            |
| [**Paused**](-mfax-faxoutgoingqueue-paused-vb.md)<br/>                                   | Read/write<br/> | The [**Paused**](-mfax-faxoutgoingqueue-paused-vb.md) property is a Boolean value that indicates whether the job queue for outgoing faxes is paused. <br/>                                                                                                                                                                         |
| [**Retries**](-mfax-faxoutgoingqueue-retries-vb.md)<br/>                                 | Read/write<br/> | The [**Retries**](-mfax-faxoutgoingqueue-retries-vb.md) property is a value that indicates the number of times that the fax service attempts to retransmit an outgoing fax when the initial transmission fails.<br/>                                                                                                               |
| [**RetryDelay**](-mfax-faxoutgoingqueue-retrydelay-vb.md)<br/>                           | Read/write<br/> | The [**RetryDelay**](-mfax-faxoutgoingqueue-retrydelay-vb.md) property is a value that indicates the time interval, in minutes, that the fax service waits before attempting to retransmit an outbound fax job.<br/>                                                                                                               |
| [**UseDeviceTSID**](-mfax-faxoutgoingqueue-usedevicetsid-vb.md)<br/>                     | Read/write<br/> | The [**UseDeviceTSID**](-mfax-faxoutgoingqueue-usedevicetsid-vb.md) property is a Boolean value that indicates whether the fax service uses the device TSID instead of a sender TSID. <br/>                                                                                                                                        |



 

## Remarks

A **FaxOutgoingQueue** object is accessed through a [**FaxFolders**](-mfax-faxfolders.md) object. **FaxOutgoingQueue** objects provide access to [**FaxOutgoingJobs**](-mfax-faxoutgoingjobs.md) objects.

![faxfolders, faxoutgoingqueue, and subordinate objects to faxoutgoingqueue](images/faxoutgoingqueue.png)

To create a **FaxOutgoingQueue** object in Microsoft Visual Basic, call the [**OutgoingQueue**](-mfax-faxfolders-outgoingqueue-vb.md) property of the [**FaxFolders**](-mfax-faxfolders.md) object.

To create a **FaxOutgoingQueue** object in C++, call the [**OutgoingQueue**](-mfax-faxfolders-outgoingqueue-vb.md) method.

> [!Note]  
> Changes made to the **FaxOutgoingQueue** object will not be saved until you call the [**Save**](-mfax-faxoutgoingqueue-save-vb.md) method.

 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxOutgoingQueue<br/>                                                      |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**IFaxOutgoingQueue**](-mfax-faxoutgoingqueue-cpp.md)
</dt> </dl>

 

 




