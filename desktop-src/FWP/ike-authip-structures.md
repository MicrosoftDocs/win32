---
title: IKE/AuthIP Structures
description: IKE/AuthIP Structures
ms.assetid: 3267EA3C-FD1F-4ED1-9794-92551222EFE1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IKE/AuthIP Structures

## In this section

-   [**IKEEXT\_AUTHENTICATION\_METHOD0**](/windows/win32/Iketypes/ns-iketypes-ikeext_authentication_method0_?branch=master)
-   [**IKEEXT\_AUTHENTICATION\_METHOD1**](/windows/win32/Iketypes/ns-iketypes-ikeext_authentication_method1_?branch=master)
-   [**IKEEXT\_AUTHENTICATION\_METHOD2**](/windows/win32/iketypes/ns-iketypes-ikeext_authentication_method2_?branch=master)
-   [**IKEEXT\_CERT\_EKUS0**](/windows/win32/iketypes/ns-iketypes-ikeext_cert_ekus0_?branch=master)
-   [**IKEEXT\_CERT\_NAME0**](/windows/win32/iketypes/ns-iketypes-ikeext_cert_name0_?branch=master)
-   [**IKEEXT\_CERT\_ROOT\_CONFIG0**](/windows/win32/Iketypes/ns-iketypes-ikeext_cert_root_config0_?branch=master)
-   [**IKEEXT\_CERTIFICATE\_AUTHENTICATION0**](/windows/win32/Iketypes/ns-iketypes-ikeext_certificate_authentication0_?branch=master)
-   [**IKEEXT\_CERTIFICATE\_AUTHENTICATION1**](/windows/win32/Iketypes/ns-iketypes-ikeext_certificate_authentication1_?branch=master)
-   [**IKEEXT\_CERTIFICATE\_AUTHENTICATION2**](/windows/win32/iketypes/ns-iketypes-ikeext_certificate_authentication2_?branch=master)
-   [**IKEEXT\_CERTIFICATE\_CREDENTIAL0**](/windows/win32/Iketypes/ns-iketypes-ikeext_certificate_credential0_?branch=master)
-   [**IKEEXT\_CERTIFICATE\_CREDENTIAL1**](/windows/win32/Iketypes/ns-iketypes-ikeext_certificate_credential1_?branch=master)
-   [**IKEEXT\_CERTIFICATE\_CRITERIA0**](/windows/win32/iketypes/ns-iketypes-ikeext_certificate_criteria0_?branch=master)
-   [**IKEEXT\_CIPHER\_ALGORITHM0**](/windows/win32/Iketypes/ns-iketypes-ikeext_cipher_algorithm0_?branch=master)
-   [**IKEEXT\_COMMON\_STATISTICS0**](/windows/win32/Iketypes/ns-iketypes-ikeext_common_statistics0_?branch=master)
-   [**IKEEXT\_COMMON\_STATISTICS1**](/windows/win32/Iketypes/ns-iketypes-ikeext_common_statistics1_?branch=master)
-   [**IKEEXT\_COOKIE\_PAIR0**](/windows/win32/Iketypes/ns-iketypes-ikeext_cookie_pair0_?branch=master)
-   [**IKEEXT\_CREDENTIAL0**](/windows/win32/Iketypes/ns-iketypes-ikeext_credential0_?branch=master)
-   [**IKEEXT\_CREDENTIAL1**](/windows/win32/Iketypes/ns-iketypes-ikeext_credential1_?branch=master)
-   [**IKEEXT\_CREDENTIAL2**](/windows/win32/iketypes/ns-iketypes-ikeext_credential2_?branch=master)
-   [**IKEEXT\_CREDENTIALS0**](/windows/win32/Iketypes/ns-iketypes-ikeext_credentials0_?branch=master)
-   [**IKEEXT\_CREDENTIALS1**](/windows/win32/Iketypes/ns-iketypes-ikeext_credentials1_?branch=master)
-   [**IKEEXT\_CREDENTIALS2**](/windows/win32/iketypes/ns-iketypes-ikeext_credentials2_?branch=master)
-   [**IKEEXT\_CREDENTIAL\_PAIR0**](/windows/win32/Iketypes/ns-iketypes-ikeext_credential_pair0_?branch=master)
-   [**IKEEXT\_CREDENTIAL\_PAIR1**](/windows/win32/Iketypes/ns-iketypes-ikeext_credential_pair1_?branch=master)
-   [**IKEEXT\_CREDENTIAL\_PAIR2**](/windows/win32/iketypes/ns-iketypes-ikeext_credential_pair2_?branch=master)
-   [**IKEEXT\_EAP\_AUTHENTICATION0**](/windows/win32/Iketypes/ns-iketypes-ikeext_eap_authentication0__?branch=master)
-   [**IKEEXT\_EM\_POLICY0**](/windows/win32/Iketypes/ns-iketypes-ikeext_em_policy0_?branch=master)
-   [**IKEEXT\_EM\_POLICY1**](/windows/win32/Iketypes/ns-iketypes-ikeext_em_policy1_?branch=master)
-   [**IKEEXT\_EM\_POLICY2**](/windows/win32/iketypes/ns-iketypes-ikeext_em_policy2_?branch=master)
-   [**IKEEXT\_INTEGRITY\_ALGORITHM0**](/windows/win32/Iketypes/ns-iketypes-ikeext_integrity_algorithm0_?branch=master)
-   [**IKEEXT\_IP\_VERSION\_SPECIFIC\_COMMON\_STATISTICS0**](/windows/win32/Iketypes/ns-iketypes-ikeext_ip_version_specific_common_statistics0_?branch=master)
-   [**IKEEXT\_IP\_VERSION\_SPECIFIC\_COMMON\_STATISTICS1**](/windows/win32/Iketypes/ns-iketypes-ikeext_ip_version_specific_common_statistics1_?branch=master)
-   [**IKEEXT\_IP\_VERSION\_SPECIFIC\_KEYMODULE\_STATISTICS0**](/windows/win32/Iketypes/ns-iketypes-ikeext_ip_version_specific_keymodule_statistics0_?branch=master)
-   [**IKEEXT\_IP\_VERSION\_SPECIFIC\_KEYMODULE\_STATISTICS1**](/windows/win32/Iketypes/ns-iketypes-ikeext_ip_version_specific_keymodule_statistics1_?branch=master)
-   [**IKEEXT\_IPV6\_CGA\_AUTHENTICATION0**](/windows/win32/Iketypes/ns-iketypes-ikeext_ipv6_cga_authentication0_?branch=master)
-   [**IKEEXT\_KERBEROS\_AUTHENTICATION0**](/windows/win32/Iketypes/ns-iketypes-ikeext_kerberos_authentication0__?branch=master)
-   [**IKEEXT\_KERBEROS\_AUTHENTICATION1**](/windows/win32/iketypes/ns-iketypes-ikeext_kerberos_authentication1__?branch=master)
-   [**IKEEXT\_KEYMODULE\_STATISTICS0**](/windows/win32/Iketypes/ns-iketypes-ikeext_keymodule_statistics0_?branch=master)
-   [**IKEEXT\_KEYMODULE\_STATISTICS1**](/windows/win32/Iketypes/ns-iketypes-ikeext_keymodule_statistics1_?branch=master)
-   [**IKEEXT\_NAME\_CREDENTIAL0**](/windows/win32/Iketypes/ns-iketypes-ikeext_name_credential0_?branch=master)
-   [**IKEEXT\_NTLM\_V2\_AUTHENTICATION0**](/windows/win32/Iketypes/ns-iketypes-ikeext_ntlm_v2_authentication0__?branch=master)
-   [**IKEEXT\_POLICY0**](/windows/win32/Iketypes/ns-iketypes-ikeext_policy0_?branch=master)
-   [**IKEEXT\_POLICY1**](/windows/win32/Iketypes/ns-iketypes-ikeext_policy1_?branch=master)
-   [**IKEEXT\_POLICY2**](/windows/win32/iketypes/ns-iketypes-ikeext_policy2_?branch=master)
-   [**IKEEXT\_PRESHARED\_KEY\_AUTHENTICATION0**](/windows/win32/Iketypes/ns-iketypes-ikeext_preshared_key_authentication0__?branch=master)
-   [**IKEEXT\_PRESHARED\_KEY\_AUTHENTICATION1**](/windows/win32/Iketypes/ns-iketypes-ikeext_preshared_key_authentication1__?branch=master)
-   [**IKEEXT\_PROPOSAL0**](/windows/win32/Iketypes/ns-iketypes-ikeext_proposal0_?branch=master)
-   [**IKEEXT\_RESERVED\_AUTHENTICATION0**](/windows/win32/Iketypes/ns-iketypes-ikeext_reserved_authentication0__?branch=master)
-   [**IKEEXT\_SA\_DETAILS0**](/windows/win32/Iketypes/ns-iketypes-ikeext_sa_details0_?branch=master)
-   [**IKEEXT\_SA\_DETAILS1**](/windows/win32/Iketypes/ns-iketypes-ikeext_sa_details1_?branch=master)
-   [**IKEEXT\_SA\_DETAILS2**](/windows/win32/iketypes/ns-iketypes-ikeext_sa_details2_?branch=master)
-   [**IKEEXT\_SA\_ENUM\_TEMPLATE0**](/windows/win32/Iketypes/ns-iketypes-ikeext_sa_enum_template0_?branch=master)
-   [**IKEEXT\_STATISTICS0**](/windows/win32/Iketypes/ns-iketypes-ikeext_statistics0_?branch=master)
-   [**IKEEXT\_STATISTICS1**](/windows/win32/Iketypes/ns-iketypes-ikeext_statistics1_?branch=master)
-   [**IKEEXT\_TRAFFIC0**](/windows/win32/Iketypes/ns-iketypes-ikeext_traffic0_?branch=master)

 

 




