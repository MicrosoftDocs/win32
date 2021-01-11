---
description: Schannel returns the following error messages when the corresponding alert is received from the Transport Layer Security (TLS) or Secure Sockets Layer (SSL) protocols.
ms.assetid: 0a6ac61d-a00c-4fc8-a995-d25d17e405df
title: Schannel Error Codes for TLS and SSL Alerts
ms.topic: article
ms.date: 05/31/2018
---

# Schannel Error Codes for TLS and SSL Alerts

[*Schannel*](../secgloss/s-gly.md) returns the following error messages when the corresponding alert is received from the [*Transport Layer Security*](../secgloss/t-gly.md) (TLS) or [*Secure Sockets Layer*](../secgloss/s-gly.md) (SSL) protocols. The error messages are defined in Winerror.h.



| TLS or SSL alert                                           | Schannel error code                                                   |
|------------------------------------------------------------|-----------------------------------------------------------------------|
| SSL3\_ALERT\_UNEXPECTED\_MESSAGE<br/> 10<br/>  | SEC\_E\_ILLEGAL\_MESSAGE<br/> 0x80090326<br/>             |
| TLS1\_ALERT\_BAD\_RECORD\_MAC<br/> 20<br/>     | SEC\_E\_MESSAGE\_ALTERED<br/> 0x8009030F<br/>             |
| TLS1\_ALERT\_DECRYPTION\_FAILED<br/> 21<br/>   | SEC\_E\_DECRYPT\_FAILURE<br/> 0x80090330<br/>             |
| TLS1\_ALERT\_RECORD\_OVERFLOW<br/> 22<br/>     | SEC\_E\_ILLEGAL\_MESSAGE<br/> 0x80090326<br/>             |
| SSL3\_ALERT\_DECOMPRESSION\_FAIL<br/> 30<br/>  | SEC\_E\_MESSAGE\_ALTERED<br/> 0x8009030F<br/>             |
| SSL3\_ALERT\_HANDSHAKE\_FAILURE<br/> 40<br/>   | SEC\_E\_ILLEGAL\_MESSAGE<br/> 0x80090326<br/>             |
| TLS1\_ALERT\_BAD\_CERTIFICATE<br/> 42<br/>     | SEC\_E\_CERT\_UNKNOWN<br/> 0x80090327<br/>                |
| TLS1\_ALERT\_UNSUPPORTED\_CERT<br/> 43<br/>    | SEC\_E\_CERT\_UNKNOWN<br/> 0x80090327<br/>                |
| TLS1\_ALERT\_CERTIFICATE\_REVOKED<br/> 44<br/> | CRYPT\_E\_REVOKED<br/> 0x80092010<br/>                    |
| TLS1\_ALERT\_CERTIFICATE\_EXPIRED<br/> 45<br/> | SEC\_E\_CERT\_EXPIRED<br/> 0x80090328<br/>                |
| TLS1\_ALERT\_CERTIFICATE\_UNKNOWN<br/> 46<br/> | SEC\_E\_CERT\_UNKNOWN<br/> 0x80090327<br/>                |
| SSL3\_ALERT\_ILLEGAL\_PARAMETER<br/>                 | SEC\_E\_ILLEGAL\_MESSAGE<br/> 0x80090326<br/>             |
| TLS1\_ALERT\_UNKNOWN\_CA<br/> 48<br/>          | SEC\_E\_UNTRUSTED\_ROOT<br/> 0x80090325<br/>              |
| TLS1\_ALERT\_ACCESS\_DENIED<br/> 49<br/>       | SEC\_E\_LOGON\_DENIED<br/> 0x8009030C<br/>                |
| TLS1\_ALERT\_DECODE\_ERROR<br/> 50<br/>        | SEC\_E\_ILLEGAL\_MESSAGE<br/> 0x80090326<br/>             |
| TLS1\_ALERT\_DECRYPT\_ERROR<br/> 51<br/>       | SEC\_E\_DECRYPT\_FAILURE<br/> 0x80090330<br/>             |
| TLS1\_ALERT\_EXPORT\_RESTRICTION<br/> 60<br/>  | SEC\_E\_ILLEGAL\_MESSAGE<br/> 0x80090326<br/>             |
| TLS1\_ALERT\_PROTOCOL\_VERSION<br/> 70<br/>    | SEC\_E\_UNSUPPORTED\_FUNCTION<br/> 0x80090302<br/>        |
| TLS1\_ALERT\_INSUFFIENT\_SECURITY<br/> 71<br/> | SEC\_E\_ALGORITHM\_MISMATCH<br/> 0x80090331<br/>          |
| TLS1\_ALERT\_INTERNAL\_ERROR<br/> 80<br/>      | SEC\_E\_INTERNAL\_ERROR<br/> 0x80090304<br/>              |
| TLS1\_ALERT\_USER\_CANCELED<br/> 90<br/>       | SEC\_E\_UNFINISHED\_CONTEXT\_DELETED<br/> 0x80090333<br/> |
| TLS1\_ALERT\_NO\_RENEGOTIATION<br/> 100<br/>   | SEC\_E\_ILLEGAL\_MESSAGE<br/> 0x80090326<br/>             |
| TLS1\_ALERT\_UNSUPPORTED\_EXT<br/> 110<br/>    | SEC\_E\_ILLEGAL\_MESSAGE<br/> 0x80090326<br/>             |
| Default<br/>                                         | SEC\_E\_ILLEGAL\_MESSAGE<br/> 0x80090326<br/>             |



 

 

 
