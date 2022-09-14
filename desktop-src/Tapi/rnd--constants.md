---
description: The following constants may be returned as errors.
ms.assetid: 185bd906-c276-4075-9c23-eb112da2a7ca
title: RND_ Constants (Rnderr.h)
ms.topic: reference
ms.date: 05/31/2018
---

# RND\_ Constants

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The following constants may be returned as errors.

<dl> <dt>

<span id="RND_INVALID_TIME"></span><span id="rnd_invalid_time"></span>**RND\_INVALID\_TIME**
</dt> <dd> <dl> <dt>

 0xe0000200
</dt> <dt>



The time value entered is not valid.


</dt> </dl> </dd> <dt>

<span id="RND_NULL_SERVER_NAME"></span><span id="rnd_null_server_name"></span>**RND\_NULL\_SERVER\_NAME**
</dt> <dd> <dl> <dt>

 0xe0000201
</dt> <dt>



The server name is **NULL**, probably because [**ITConferenceBlob::Init**](itconferenceblob-init.md) has not been run or did not succeed.


</dt> </dl> </dd> <dt>

<span id="RND_ALREADY_CONNECTED"></span><span id="rnd_already_connected"></span>**RND\_ALREADY\_CONNECTED**
</dt> <dd> <dl> <dt>

 0xe0000202
</dt> <dt>



The [**ITDirectory::Connect**](/windows/desktop/api/Rend/nf-rend-itdirectory-connect) method was called, but a connection already exists.


</dt> </dl> </dd> <dt>

<span id="RND_NOT_CONNECTED"></span><span id="rnd_not_connected"></span>**RND\_NOT\_CONNECTED**
</dt> <dd> <dl> <dt>

 0xe0000203
</dt> <dt>



The [**ITDirectory::Connect**](/windows/desktop/api/Rend/nf-rend-itdirectory-connect) method has not been called, or failed.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|-------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                               |
| Header<br/>       | <dl> <dt>Rnderr.h</dt> </dl> |



 

 




