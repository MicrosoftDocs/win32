---
description: Sending COPP Status Requests
ms.assetid: 9f9950ff-469f-4cea-924e-3f9471eb4838
title: Sending COPP Status Requests
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Sending COPP Status Requests

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To send a Certified Output Protection Protocol (COPP) status request, fill in an [**AMCOPPStatusInput**](/windows/win32/api/strmif/ns-strmif-amcoppstatusinput) structure with the request data. The structure members are:

-   **rApp**. A 128-bit random number, typed as a GUID. The same number is returned in the driver's response. You should allocate the random number on the heap and then copy it into structure. This guards against attacks where the attacker modifies the contents of the [**AMCOPPStatusInput**](/windows/win32/api/strmif/ns-strmif-amcoppstatusinput) structure.
-   **guidStatusRequestID**. A GUID that identifies the request. See [COPP Query Reference](copp-query-reference.md).
-   **dwSequence**. The status sequence number. Increment this value after each status request. (In the section [Initiating a COPP Session](initiating-a-copp-session.md), this value is shown as *uStatusSeq* in the code examples.)
-   **cbSizeData**. The size, in bytes, of any additional data needed for the request.
-   **StatusData**. Data for the status request.

Pass the [**AMCOPPStatusInput**](/windows/win32/api/strmif/ns-strmif-amcoppstatusinput) structure to the [**IAMCertifiedOutputProtection::ProtectionStatus**](/windows/desktop/api/Strmif/nf-strmif-iamcertifiedoutputprotection-protectionstatus) method. For example, the following code sends a status request that queries which protection mechanisms are available:


```C++
AMCOPPStatusInput input;
AMCOPPStatusOutput output;

// Create a 128-bit random number.
GUID *pGuid = new GUID();
if (pGuid == NULL)
{
    // Handle out-of-memory condition.
}
CryptGenRandom(hCSP, sizeof(GUID), (BYTE*)pGuid);  

// Copy the random number into the command structure.
memcpy(&input.rApp, pGuid, sizeof(GUID));

// Fill in the other data.
input.guidStatusRequestID = DXVA_COPPQueryProtectionType; // Request type.
input.dwSequence = uStatusSeq;  // Status sequence number.
input.cbSizeData = 0            // No other data for this query.

// Send the request.
hr = pCOPP->ProtectionStatus(&input, &output);

// Increment the sequence number each time.
++uStatusSeq;
```



The response is written into the **COPPStatus** member of the [**AMCOPPStatusOutput**](/windows/win32/api/strmif/ns-strmif-amcoppstatusoutput) structure. The size of the valid data in the response is given in the **cbSizeData** member. To ensure the integrity of the message, the driver computes a message authentication code (MAC) using the OMAC 1 algorithm, and returns this value in the structure's **macKDI** member. The application should verify this value as follows:

1.  Calculate the OMAC tag for the block of data that appears after the **macKDI** member of the [**AMCOPPStatusOutput**](/windows/win32/api/strmif/ns-strmif-amcoppstatusoutput) structure (in other words, **cbSizeData** plus **COPPStatus**).
2.  Compare this tag with the value in **macKDI**, using a straight **memcmp**.

The OMAC 1 algorithm is described in detail at [https://www.nuee.nagoya-u.ac.jp/labs/tiwata/omac/omac.html](https://www.nuee.nagoya-u.ac.jp/labs/tiwata/omac/omac.html). COPP uses the following OMAC-1 parameters:

-   E = AES
-   t = 128 bits

The data returned from the status request always starts with two items:

-   The same value of **rApp** that was passed by the application. You should verify that this value matches the original value stored on the heap.
-   A [**COPP\_StatusFlags**](/windows/desktop/api/dxva9typ/ne-dxva9typ-copp_statusflags) value that indicates whether the output protection status has changed.

Because the connection can be lost or reconfigured, the application should periodically poll the driver for the current status. If the COPP\_RenegotiationRequired flag is set, the application should attempt to reset the protection level. If the COPP\_LinkLost flag is set, the application should stop playing the content. For example, the COPP\_LinkLost flag can be returned because the user disconnected the output connector. The application should release the current instance of the VMR, create a new instance of the VMR, and establish a new COPP session (including key exchange and certificate validation).

## Related topics

<dl> <dt>

[Using Certified Output Protection Protocol (COPP)](using-certified-output-protection-protocol--copp.md)
</dt> </dl>

 

 



