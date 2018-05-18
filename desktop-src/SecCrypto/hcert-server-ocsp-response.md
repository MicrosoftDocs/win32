---
Description: 'Represents a handle to an OCSP response associated with a server certificate chain.'
ms.assetid: 'baf173f1-99dc-49f9-9a17-fee79b393db7'
title: 'HCERT\_SERVER\_OCSP\_RESPONSE'
---

# HCERT\_SERVER\_OCSP\_RESPONSE

The **HCERT\_SERVER\_OCSP\_RESPONSE** data type represents a handle to an OCSP response associated with a server certificate chain.

This type is used by the following APIs.

-   [**CertOpenServerOcspResponse**](certopenserverocspresponse.md)
-   [**CertAddRefServerOcspResponse**](certaddrefserverocspresponse.md)
-   [**CertCloseServerOcspResponse**](certcloseserverocspresponse.md)
-   [**CertGetServerOcspResponseContext**](certgetserverocspresponsecontext.md)


```C++
typedef VOID* HCERT_SERVER_OCSP_RESPONSE;
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Wincrypt.h</dt> </dl> |



 

 




