---
description: The SetBandwidthInfo method sets the bandwidth information.
ms.assetid: bf5db456-ea67-4a65-a681-df0741f73fc9
title: ITConnection::SetBandwidthInfo method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITConnection::SetBandwidthInfo method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **SetBandwidthInfo** method sets the bandwidth information.

## Syntax


```C++
HRESULT SetBandwidthInfo(
  [in] BSTR   pModifier,
  [in] DOUBLE Bandwidth
);
```



## Parameters

<dl> <dt>

*pModifier* \[in\]
</dt> <dd>

Pointer to a **BSTR** indicating the scope of the bandwidth being set. For more information, see the following Remarks section.

</dd> <dt>

*Bandwidth* \[in\]
</dt> <dd>

Bandwidth.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                         | Meaning                                                           |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *pModifier* or *Bandwidth* parameter is not valid.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>   |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                     |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                    |



 

## Remarks

The application must use [**SysAllocString**](/windows/win32/api/oleauto/nf-oleauto-sysallocstring) to allocate memory for the *pModifier* parameter and use [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) to free the memory when the variable is no longer needed.

Reference: RFC 2327.

The bandwidth modifier will normally be either CT or AS:

**CT Conference Total:** An implicit maximum bandwidth is associated with each [*time to live*](t-tapgloss.md) (TTL) on the Mbone or within a particular multicast administrative scope region (the Mbone bandwidth versus TTL limits are given in the MBone FAQ). If the bandwidth of a session or media in a session is different from the bandwidth implicit from the scope, a \`b=CT:...' line should be supplied for the session giving the proposed upper limit to the bandwidth used. The primary purpose of this is to give an approximate idea as to whether two or more conferences can coexist simultaneously.

**AS Application-Specific Maximum:** The bandwidth is interpreted to be application-specific, i.e., will be the application's concept of maximum bandwidth. Normally this will coincide with what is set on the application's "maximum bandwidth" control, if applicable.

Note that CT gives a total bandwidth figure for all the media at all sites. AS gives a bandwidth figure for a single media at a single site, although there may be many sites sending simultaneously.

**Extension Mechanism:** Tool writers can define experimental bandwidth modifiers by prefixing their modifiers with "X-".

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITConnection**](itconnection.md)
</dt> </dl>

 

