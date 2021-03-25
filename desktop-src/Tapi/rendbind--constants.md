---
description: The RENDBIND constants are flags used by the ITDirectory::Bind method to indicate types of authentication supplied.
ms.assetid: 27bcf36a-1826-4603-9821-22fcc5c1e186
title: RENDBIND_ Constants (Rend.h)
ms.topic: reference
ms.date: 05/31/2018
---

# RENDBIND\_ Constants

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The RENDBIND constants are flags used by the [**ITDirectory::Bind**](/windows/desktop/api/Rend/nf-rend-itdirectory-bind) method to indicate types of authentication supplied.

<dl> <dt>

<span id="RENDBIND_AUTHENTICATE"></span><span id="rendbind_authenticate"></span>**RENDBIND\_AUTHENTICATE**
</dt> <dd> <dl> <dt>

 0x00000001
</dt> <dt>



Authenticate user.


</dt> </dl> </dd> <dt>

<span id="RENDBIND_DEFAULTDOMAINNAME"></span><span id="rendbind_defaultdomainname"></span>**RENDBIND\_DEFAULTDOMAINNAME**
</dt> <dd> <dl> <dt>

 0x00000002
</dt> <dt>



Use default domain name.


</dt> </dl> </dd> <dt>

<span id="RENDBIND_DEFAULTUSERNAME"></span><span id="rendbind_defaultusername"></span>**RENDBIND\_DEFAULTUSERNAME**
</dt> <dd> <dl> <dt>

 0x00000004
</dt> <dt>



Use default user name.


</dt> </dl> </dd> <dt>

<span id="RENDBIND_DEFAULTPASSWORD"></span><span id="rendbind_defaultpassword"></span>**RENDBIND\_DEFAULTPASSWORD**
</dt> <dd> <dl> <dt>

 0x00000008
</dt> <dt>



Use default password.


</dt> </dl> </dd> <dt>

<span id="RENDBIND_DEFAULTCREDENTIALS"></span><span id="rendbind_defaultcredentials"></span>**RENDBIND\_DEFAULTCREDENTIALS**
</dt> <dd> <dl> <dt>

 0x0000000e
</dt> <dt>



The previous three ORed together for convenience.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Rend.h</dt> </dl> |



## See also

<dl> <dt>

[**ITDirectory**](/windows/desktop/api/Rend/nn-rend-itdirectory)
</dt> <dt>

[**ITDirectory::Bind**](/windows/desktop/api/Rend/nf-rend-itdirectory-bind)
</dt> </dl>

 

 




