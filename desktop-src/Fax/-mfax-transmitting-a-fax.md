---
Description: 'To signal a fax service provider (FSP) DLL that it must initiate an outgoing fax transmission, the fax service calls the FaxDevSend function.'
ms.assetid: '8914c465-4bd7-4c35-88f7-248c01b8f900'
title: Transmitting a Fax
---

# Transmitting a Fax

To signal a fax service provider (FSP) DLL that it must initiate an outgoing fax transmission, the fax service calls the [**FaxDevSend**](-mfax-faxdevsend.md) function. The provider must make the call, send the fax data stream, and terminate the call. The [**FAX\_SEND**](-mfax-fax-send-str.md) structure identifies the file that holds the outbound fax document, and it contains information about the calling and receiving fax devices.

The fax service provides a pointer to the [**FaxSendCallback**](-mfax-faxsendcallback.md) function. The FSP calls **FaxSendCallback** to notify the fax service that an outbound fax call is in progress. The **FaxSendCallback** function is also necessary for Telephony Application Programming Interface (TAPI) message routing.

The fax service calls the [**FaxDevReceive**](-mfax-faxdevreceive.md) function to notify a FSP DLL when there is an incoming fax transmission. The provider must accept the incoming call and store the fax data stream. The [**FAX\_RECEIVE**](-mfax-fax-receive-str.md) structure identifies the file in which the FSP should store the inbound fax data stream, and it contains information about the receiving fax device.

The FSP must export the [**FaxDevSend**](-mfax-faxdevsend.md), [**FaxDevReceive**](-mfax-faxdevreceive.md), and the [**FaxDevStartJob**](-mfax-faxdevstartjob.md) functions. Each new job is initiated by calling **FaxDevStartJob**.

For more information, see [Using a Virtual Device to Transmit a Fax](-mfax-using-a-virtual-device-to-transmit-a-fax.md).

 

 



