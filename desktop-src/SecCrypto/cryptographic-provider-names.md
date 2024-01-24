---
description: Used with the CryptAcquireContext and CryptSetProvider functions.
ms.assetid: 97e9a708-83b5-48b3-9d16-f7b54367dc4e
title: Cryptographic Provider Names (Wincrypt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Cryptographic Provider Names

The following [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) names are defined in Wincrypt.h. These constants are used with the [**CryptAcquireContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta) and [**CryptSetProvider**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetprovidera) functions.



| Constant/value                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                      |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MS_DEF_DH_SCHANNEL_PROV"></span><span id="ms_def_dh_schannel_prov"></span><dl> <dt>**MS\_DEF\_DH\_SCHANNEL\_PROV**</dt> <dt>"Microsoft DH Schannel Cryptographic Provider"</dt> </dl>      | The [Microsoft DSS and Diffie-Hellman/Schannel Cryptographic Provider](microsoft-dss-and-diffie-hellman-schannel-cryptographic-provider.md).<br/>                                         |
| <span id="MS_DEF_DSS_DH_PROV"></span><span id="ms_def_dss_dh_prov"></span><dl> <dt>**MS\_DEF\_DSS\_DH\_PROV**</dt> <dt>"Microsoft Base DSS and Diffie-Hellman Cryptographic Provider"</dt> </dl>     | The [Microsoft Base DSS and Diffie-Hellman Cryptographic Provider](microsoft-base-dss-and-diffie-hellman-cryptographic-provider.md).<br/>                                                 |
| <span id="MS_DEF_DSS_PROV"></span><span id="ms_def_dss_prov"></span><dl> <dt>**MS\_DEF\_DSS\_PROV**</dt> <dt>"Microsoft Base DSS Cryptographic Provider"</dt> </dl>                                  | The [Microsoft DSS Cryptographic Provider](microsoft-dss-cryptographic-provider.md).<br/>                                                                                                 |
| <span id="MS_DEF_PROV"></span><span id="ms_def_prov"></span><dl> <dt>**MS\_DEF\_PROV**</dt> <dt>"Microsoft Base Cryptographic Provider v1.0"</dt> </dl>                                              | The [Microsoft Base Cryptographic Provider](microsoft-base-cryptographic-provider.md).<br/>                                                                                               |
| <span id="MS_DEF_RSA_SCHANNEL_PROV"></span><span id="ms_def_rsa_schannel_prov"></span><dl> <dt>**MS\_DEF\_RSA\_SCHANNEL\_PROV**</dt> <dt>"Microsoft RSA Schannel Cryptographic Provider"</dt> </dl>  | The [Microsoft RSA/Schannel Cryptographic Provider](microsoft-rsa-schannel-cryptographic-provider.md).<br/>                                                                               |
| <span id="MS_DEF_RSA_SIG_PROV"></span><span id="ms_def_rsa_sig_prov"></span><dl> <dt>**MS\_DEF\_RSA\_SIG\_PROV**</dt> <dt>"Microsoft RSA Signature Cryptographic Provider"</dt> </dl>                | The [Microsoft RSA Signature Cryptographic Provider](microsoft-rsa-signature-cryptographic-provider.md) is not supported.<br/>                                                            |
| <span id="MS_ENH_DSS_DH_PROV"></span><span id="ms_enh_dss_dh_prov"></span><dl> <dt>**MS\_ENH\_DSS\_DH\_PROV**</dt> <dt>"Microsoft Enhanced DSS and Diffie-Hellman Cryptographic Provider"</dt> </dl> | The [Microsoft Enhanced DSS and Diffie-Hellman Cryptographic Provider](microsoft-enhanced-dss-and-diffie-hellman-cryptographic-provider.md).<br/>                                         |
| <span id="MS_ENH_RSA_AES_PROV"></span><span id="ms_enh_rsa_aes_prov"></span><dl> <dt>**MS\_ENH\_RSA\_AES\_PROV**</dt> <dt>"Microsoft Enhanced RSA and AES Cryptographic Provider"</dt> </dl>         | The [Microsoft AES Cryptographic Provider](microsoft-aes-cryptographic-provider.md).<br/> **Windows XP:  **"Microsoft Enhanced RSA and AES Cryptographic Provider (Prototype)"<br/> |
| <span id="MS_ENHANCED_PROV"></span><span id="ms_enhanced_prov"></span><dl> <dt>**MS\_ENHANCED\_PROV**</dt> <dt>"Microsoft Enhanced Cryptographic Provider v1.0"</dt> </dl>                           | The [Microsoft Enhanced Cryptographic Provider](microsoft-enhanced-cryptographic-provider.md).<br/>                                                                                       |
| <span id="MS_SCARD_PROV"></span><span id="ms_scard_prov"></span><dl> <dt>**MS\_SCARD\_PROV**</dt> <dt>"Microsoft Base Smart Card Crypto Provider"</dt> </dl>                                         | The [Microsoft Base Smart Card Cryptographic Service Provider](/previous-versions/windows/desktop/secsmart/microsoft-base-smart-card-cryptographic-service-provider).<br/>                                                    |
| <span id="MS_STRONG_PROV"></span><span id="ms_strong_prov"></span><dl> <dt>**MS\_STRONG\_PROV**</dt> <dt>"Microsoft Strong Cryptographic Provider"</dt> </dl>                                        | The [Microsoft Strong Cryptographic Provider](microsoft-strong-cryptographic-provider.md).<br/>                                                                                           |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Wincrypt.h</dt> </dl> |



 

 
