---
title: IKE/AuthIP Structures
description: IKE/AuthIP Structures
ms.assetid: 3267EA3C-FD1F-4ED1-9794-92551222EFE1
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IKE/AuthIP Structures

## In this section

-   [**IKEEXT\_AUTHENTICATION\_METHOD0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_authentication_method0_)
-   [**IKEEXT\_AUTHENTICATION\_METHOD1**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_authentication_method1_)
-   [**IKEEXT\_AUTHENTICATION\_METHOD2**](/windows/desktop/api/iketypes/ns-iketypes-ikeext_authentication_method2_)
-   [**IKEEXT\_CERT\_EKUS0**](/windows/desktop/api/iketypes/ns-iketypes-ikeext_cert_ekus0_)
-   [**IKEEXT\_CERT\_NAME0**](/windows/desktop/api/iketypes/ns-iketypes-ikeext_cert_name0_)
-   [**IKEEXT\_CERT\_ROOT\_CONFIG0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_cert_root_config0_)
-   [**IKEEXT\_CERTIFICATE\_AUTHENTICATION0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_certificate_authentication0_)
-   [**IKEEXT\_CERTIFICATE\_AUTHENTICATION1**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_certificate_authentication1_)
-   [**IKEEXT\_CERTIFICATE\_AUTHENTICATION2**](/windows/desktop/api/iketypes/ns-iketypes-ikeext_certificate_authentication2_)
-   [**IKEEXT\_CERTIFICATE\_CREDENTIAL0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_certificate_credential0_)
-   [**IKEEXT\_CERTIFICATE\_CREDENTIAL1**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_certificate_credential1_)
-   [**IKEEXT\_CERTIFICATE\_CRITERIA0**](/windows/desktop/api/iketypes/ns-iketypes-ikeext_certificate_criteria0_)
-   [**IKEEXT\_CIPHER\_ALGORITHM0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_cipher_algorithm0_)
-   [**IKEEXT\_COMMON\_STATISTICS0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_common_statistics0_)
-   [**IKEEXT\_COMMON\_STATISTICS1**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_common_statistics1_)
-   [**IKEEXT\_COOKIE\_PAIR0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_cookie_pair0_)
-   [**IKEEXT\_CREDENTIAL0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_credential0_)
-   [**IKEEXT\_CREDENTIAL1**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_credential1_)
-   [**IKEEXT\_CREDENTIAL2**](/windows/desktop/api/iketypes/ns-iketypes-ikeext_credential2_)
-   [**IKEEXT\_CREDENTIALS0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_credentials0_)
-   [**IKEEXT\_CREDENTIALS1**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_credentials1_)
-   [**IKEEXT\_CREDENTIALS2**](/windows/desktop/api/iketypes/ns-iketypes-ikeext_credentials2_)
-   [**IKEEXT\_CREDENTIAL\_PAIR0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_credential_pair0_)
-   [**IKEEXT\_CREDENTIAL\_PAIR1**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_credential_pair1_)
-   [**IKEEXT\_CREDENTIAL\_PAIR2**](/windows/desktop/api/iketypes/ns-iketypes-ikeext_credential_pair2_)
-   [**IKEEXT\_EAP\_AUTHENTICATION0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_eap_authentication0__)
-   [**IKEEXT\_EM\_POLICY0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_em_policy0_)
-   [**IKEEXT\_EM\_POLICY1**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_em_policy1_)
-   [**IKEEXT\_EM\_POLICY2**](/windows/desktop/api/iketypes/ns-iketypes-ikeext_em_policy2_)
-   [**IKEEXT\_INTEGRITY\_ALGORITHM0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_integrity_algorithm0_)
-   [**IKEEXT\_IP\_VERSION\_SPECIFIC\_COMMON\_STATISTICS0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_ip_version_specific_common_statistics0_)
-   [**IKEEXT\_IP\_VERSION\_SPECIFIC\_COMMON\_STATISTICS1**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_ip_version_specific_common_statistics1_)
-   [**IKEEXT\_IP\_VERSION\_SPECIFIC\_KEYMODULE\_STATISTICS0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_ip_version_specific_keymodule_statistics0_)
-   [**IKEEXT\_IP\_VERSION\_SPECIFIC\_KEYMODULE\_STATISTICS1**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_ip_version_specific_keymodule_statistics1_)
-   [**IKEEXT\_IPV6\_CGA\_AUTHENTICATION0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_ipv6_cga_authentication0_)
-   [**IKEEXT\_KERBEROS\_AUTHENTICATION0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_kerberos_authentication0__)
-   [**IKEEXT\_KERBEROS\_AUTHENTICATION1**](/windows/desktop/api/iketypes/ns-iketypes-ikeext_kerberos_authentication1__)
-   [**IKEEXT\_KEYMODULE\_STATISTICS0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_keymodule_statistics0_)
-   [**IKEEXT\_KEYMODULE\_STATISTICS1**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_keymodule_statistics1_)
-   [**IKEEXT\_NAME\_CREDENTIAL0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_name_credential0_)
-   [**IKEEXT\_NTLM\_V2\_AUTHENTICATION0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_ntlm_v2_authentication0__)
-   [**IKEEXT\_POLICY0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_policy0_)
-   [**IKEEXT\_POLICY1**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_policy1_)
-   [**IKEEXT\_POLICY2**](/windows/desktop/api/iketypes/ns-iketypes-ikeext_policy2_)
-   [**IKEEXT\_PRESHARED\_KEY\_AUTHENTICATION0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_preshared_key_authentication0__)
-   [**IKEEXT\_PRESHARED\_KEY\_AUTHENTICATION1**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_preshared_key_authentication1__)
-   [**IKEEXT\_PROPOSAL0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_proposal0_)
-   [**IKEEXT\_RESERVED\_AUTHENTICATION0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_reserved_authentication0__)
-   [**IKEEXT\_SA\_DETAILS0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_sa_details0_)
-   [**IKEEXT\_SA\_DETAILS1**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_sa_details1_)
-   [**IKEEXT\_SA\_DETAILS2**](/windows/desktop/api/iketypes/ns-iketypes-ikeext_sa_details2_)
-   [**IKEEXT\_SA\_ENUM\_TEMPLATE0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_sa_enum_template0_)
-   [**IKEEXT\_STATISTICS0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_statistics0_)
-   [**IKEEXT\_STATISTICS1**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_statistics1_)
-   [**IKEEXT\_TRAFFIC0**](/windows/desktop/api/Iketypes/ns-iketypes-ikeext_traffic0_)

 

 




