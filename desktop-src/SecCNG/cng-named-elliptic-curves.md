---
description: Beginning in Windows 10, CNG provides support for the following named elliptic curves (ANSI X9.62, X9.63, FIPS 186-2).
ms.assetid: 0607E8C3-6372-47E1-B16F-EF156D5EBA7D
title: CNG Named Elliptic Curves (Bcrypt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CNG Named Elliptic Curves

Beginning in Windows 10, CNG provides support for the following named elliptic curves (ANSI X9.62, X9.63, FIPS 186-2).

<dl> <dt><span id="BCRYPT_ECC_CURVE_25519"></span><span id="bcrypt_ecc_curve_25519"></span>**BCRYPT\_ECC\_CURVE\_25519**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-------------------------------------------------------------|
| Name              | curve25519                                                  |
| Standard          | [Curve 25519](https://cr.yp.to/ecdh/curve25519-20060209.pdf) |
| Key size (bits)   | 255                                                         |
| TLS capable       |                                                             |
| Object identifier | None                                                        |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_BRAINPOOLP160R1"></span><span id="bcrypt_ecc_curve_brainpoolp160r1"></span>**BCRYPT\_ECC\_CURVE\_BRAINPOOLP160R1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| Name              | brainpoolP160r1                                                                                                   |
| Standard          | [ECC Brainpool Standard Curves and Curve Generation](https://www.teletrust.de/fileadmin/files/oid/oid_ECC-Brainpool-Standard-curves-V1.pdf) |
| Key size (bits)   | 160                                                                                                               |
| TLS capable       | No                                                                                                                |
| Object identifier | 1.3.36.3.3.2.8.1.1.1                                                                                              |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_BRAINPOOLP160T1_"></span><span id="bcrypt_ecc_curve_brainpoolp160t1_"></span>**BCRYPT\_ECC\_CURVE\_BRAINPOOLP160T1** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| Name              | brainpoolP160t1                                                                                                   |
| Standard          | [ECC Brainpool Standard Curves and Curve Generation](https://www.teletrust.de/fileadmin/files/oid/oid_ECC-Brainpool-Standard-curves-V1.pdf) |
| Key size (bits)   | 160                                                                                                               |
| TLS capable       | No                                                                                                                |
| Object identifier | 1.3.36.3.3.2.8.1.1.2                                                                                              |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_BRAINPOOLP192R1"></span><span id="bcrypt_ecc_curve_brainpoolp192r1"></span>**BCRYPT\_ECC\_CURVE\_BRAINPOOLP192R1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| Name              | brainpoolP192r1                                                                                                   |
| Standard          | [ECC Brainpool Standard Curves and Curve Generation](https://www.teletrust.de/fileadmin/files/oid/oid_ECC-Brainpool-Standard-curves-V1.pdf) |
| Key size (bits)   | 192                                                                                                               |
| TLS capable       | No                                                                                                                |
| Object identifier | 1.3.36.3.3.2.8.1.1.3                                                                                              |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_BRAINPOOLP192T1"></span><span id="bcrypt_ecc_curve_brainpoolp192t1"></span>**BCRYPT\_ECC\_CURVE\_BRAINPOOLP192T1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| Name              | brainpoolP192t1                                                                                                   |
| Standard          | [ECC Brainpool Standard Curves and Curve Generation](https://www.teletrust.de/fileadmin/files/oid/oid_ECC-Brainpool-Standard-curves-V1.pdf) |
| Key size (bits)   | 192                                                                                                               |
| TLS capable       | No                                                                                                                |
| Object identifier | 1.3.36.3.3.2.8.1.1.4                                                                                              |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_BRAINPOOLP224R1"></span><span id="bcrypt_ecc_curve_brainpoolp224r1"></span>**BCRYPT\_ECC\_CURVE\_BRAINPOOLP224R1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| Name              | brainpoolP224r1                                                                                                   |
| Standard          | [ECC Brainpool Standard Curves and Curve Generation](https://www.teletrust.de/fileadmin/files/oid/oid_ECC-Brainpool-Standard-curves-V1.pdf) |
| Key size (bits)   | 224                                                                                                               |
| TLS capable       | No                                                                                                                |
| Object identifier | 1.3.36.3.3.2.8.1.1.5                                                                                              |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_BRAINPOOLP224T1"></span><span id="bcrypt_ecc_curve_brainpoolp224t1"></span>**BCRYPT\_ECC\_CURVE\_BRAINPOOLP224T1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| Name              | brainpoolP224t1                                                                                                   |
| Standard          | [ECC Brainpool Standard Curves and Curve Generation](https://www.teletrust.de/fileadmin/files/oid/oid_ECC-Brainpool-Standard-curves-V1.pdf) |
| Key size (bits)   | 224                                                                                                               |
| TLS capable       | No                                                                                                                |
| Object identifier | 1.3.36.3.3.2.8.1.1.6                                                                                              |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_BRAINPOOLP256R1"></span><span id="bcrypt_ecc_curve_brainpoolp256r1"></span>**BCRYPT\_ECC\_CURVE\_BRAINPOOLP256R1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| Name              | brainpoolP256r1                                                                                                   |
| Standard          | [ECC Brainpool Standard Curves and Curve Generation](https://www.teletrust.de/fileadmin/files/oid/oid_ECC-Brainpool-Standard-curves-V1.pdf) |
| Key size (bits)   | 256                                                                                                               |
| TLS capable       | Yes                                                                                                               |
| Object identifier | 1.3.36.3.3.2.8.1.1.7                                                                                              |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_BRAINPOOLP256T1"></span><span id="bcrypt_ecc_curve_brainpoolp256t1"></span>**BCRYPT\_ECC\_CURVE\_BRAINPOOLP256T1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| Name              | brainpoolP256t1                                                                                                   |
| Standard          | [ECC Brainpool Standard Curves and Curve Generation](https://www.teletrust.de/fileadmin/files/oid/oid_ECC-Brainpool-Standard-curves-V1.pdf) |
| Key size (bits)   | 256                                                                                                               |
| TLS capable       | No                                                                                                                |
| Object identifier | 1.3.36.3.3.2.8.1.1.8                                                                                              |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_BRAINPOOLP320R1"></span><span id="bcrypt_ecc_curve_brainpoolp320r1"></span>**BCRYPT\_ECC\_CURVE\_BRAINPOOLP320R1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| Name              | brainpoolP320r1                                                                                                   |
| Standard          | [ECC Brainpool Standard Curves and Curve Generation](https://www.teletrust.de/fileadmin/files/oid/oid_ECC-Brainpool-Standard-curves-V1.pdf) |
| Key size (bits)   | 320                                                                                                               |
| TLS capable       | No                                                                                                                |
| Object identifier | 1.3.36.3.3.2.8.1.1.9                                                                                              |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_BRAINPOOLP32_0T1"></span><span id="bcrypt_ecc_curve_brainpoolp32_0t1"></span>**BCRYPT\_ECC\_CURVE\_BRAINPOOLP32 0T1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| Name              | brainpoolP320t1                                                                                                   |
| Standard          | [ECC Brainpool Standard Curves and Curve Generation](https://www.teletrust.de/fileadmin/files/oid/oid_ECC-Brainpool-Standard-curves-V1.pdf) |
| Key size (bits)   | 320                                                                                                               |
| TLS capable       | No                                                                                                                |
| Object identifier | 1.3.36.3.3.2.8.1.1.10                                                                                             |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_BRAINPOOLP384R1_"></span><span id="bcrypt_ecc_curve_brainpoolp384r1_"></span>**BCRYPT\_ECC\_CURVE\_BRAINPOOLP384R1** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| Name              | brainpoolP384r1                                                                                                   |
| Standard          | [ECC Brainpool Standard Curves and Curve Generation](https://www.teletrust.de/fileadmin/files/oid/oid_ECC-Brainpool-Standard-curves-V1.pdf) |
| Key size (bits)   | 384                                                                                                               |
| TLS capable       | Yes                                                                                                               |
| Object identifier | 1.3.36.3.3.2.8.1.1.11                                                                                             |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_BRAINPOOLP384T1"></span><span id="bcrypt_ecc_curve_brainpoolp384t1"></span>**BCRYPT\_ECC\_CURVE\_BRAINPOOLP384T1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| Name              | brainpoolP384t1                                                                                                   |
| Standard          | [ECC Brainpool Standard Curves and Curve Generation](https://www.teletrust.de/fileadmin/files/oid/oid_ECC-Brainpool-Standard-curves-V1.pdf) |
| Key size (bits)   | 384                                                                                                               |
| TLS capable       | No                                                                                                                |
| Object identifier | 1.3.36.3.3.2.8.1.1.12                                                                                             |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_BRAINPOOLP512R1"></span><span id="bcrypt_ecc_curve_brainpoolp512r1"></span>**BCRYPT\_ECC\_CURVE\_BRAINPOOLP512R1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| Name              | brainpoolP512r1                                                                                                   |
| Standard          | [ECC Brainpool Standard Curves and Curve Generation](https://www.teletrust.de/fileadmin/files/oid/oid_ECC-Brainpool-Standard-curves-V1.pdf) |
| Key size (bits)   | 512                                                                                                               |
| TLS capable       | Yes                                                                                                               |
| Object identifier | 1.3.36.3.3.2.8.1.1.13                                                                                             |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_BRAINPOOLP512T1"></span><span id="bcrypt_ecc_curve_brainpoolp512t1"></span>**BCRYPT\_ECC\_CURVE\_BRAINPOOLP512T1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| Name              | brainpoolP512t1                                                                                                   |
| Standard          | [ECC Brainpool Standard Curves and Curve Generation](https://www.teletrust.de/fileadmin/files/oid/oid_ECC-Brainpool-Standard-curves-V1.pdf) |
| Key size (bits)   | 512                                                                                                               |
| TLS capable       | No                                                                                                                |
| Object identifier | 1.3.36.3.3.2.8.1.1.14                                                                                             |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_EC192WAPI_"></span><span id="bcrypt_ecc_curve_ec192wapi_"></span>**BCRYPT\_ECC\_CURVE\_EC192WAPI** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|----------------------------------------------------------------|
| Name              | ec192wapi                                                      |
| Standard          | Chinese National Standard for Wireless LANs (GB 15629.11-2003) |
| Key size (bits)   | 192                                                            |
| TLS capable       | No                                                             |
| Object identifier | 1.2.156.11235.1.1.2.1                                          |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_NISTP192"></span><span id="bcrypt_ecc_curve_nistp192"></span>**BCRYPT\_ECC\_CURVE\_NISTP192**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------------------------------------------|
| Name              | nistP192                                                                                                                     |
| Standard          | [Recommended Elliptic Curves for Federal Government Use](https://csrc.nist.gov/groups/ST/toolkit/documents/dss/NISTReCur.pdf) |
| Key size (bits)   | 192                                                                                                                          |
| TLS capable       | Yes                                                                                                                          |
| Object identifier | 1.2.840.10045.3.1.1                                                                                                          |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_NISTP224_"></span><span id="bcrypt_ecc_curve_nistp224_"></span>**BCRYPT\_ECC\_CURVE\_NISTP224** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------------------------------------------|
| Name              | nistP224                                                                                                                     |
| Standard          | [Recommended Elliptic Curves for Federal Government Use](https://csrc.nist.gov/groups/ST/toolkit/documents/dss/NISTReCur.pdf) |
| Key size (bits)   | 224                                                                                                                          |
| TLS capable       | Yes                                                                                                                          |
| Object identifier | 1.3.132.0.33                                                                                                                 |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_NISTP256"></span><span id="bcrypt_ecc_curve_nistp256"></span>**BCRYPT\_ECC\_CURVE\_NISTP256**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------------------------------------------|
| Name              | nistP256                                                                                                                     |
| Standard          | [Recommended Elliptic Curves for Federal Government Use](https://csrc.nist.gov/groups/ST/toolkit/documents/dss/NISTReCur.pdf) |
| Key size (bits)   | 256                                                                                                                          |
| TLS capable       | Yes                                                                                                                          |
| Object identifier | 1.2.840.10045.3.1.7                                                                                                          |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_NISTP384_"></span><span id="bcrypt_ecc_curve_nistp384_"></span>**BCRYPT\_ECC\_CURVE\_NISTP384** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------------------------------------------|
| Name              | nistP384                                                                                                                     |
| Standard          | [Recommended Elliptic Curves for Federal Government Use](https://csrc.nist.gov/groups/ST/toolkit/documents/dss/NISTReCur.pdf) |
| Key size (bits)   | 384                                                                                                                          |
| TLS capable       | Yes                                                                                                                          |
| Object identifier | 1.3.132.0.34                                                                                                                 |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_NISTP521"></span><span id="bcrypt_ecc_curve_nistp521"></span>**BCRYPT\_ECC\_CURVE\_NISTP521**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------------------------------------------|
| Name              | nistP521                                                                                                                     |
| Standard          | [Recommended Elliptic Curves for Federal Government Use](https://csrc.nist.gov/groups/ST/toolkit/documents/dss/NISTReCur.pdf) |
| Key size (bits)   | 521                                                                                                                          |
| TLS capable       | Yes                                                                                                                          |
| Object identifier | 1.3.132.0.35                                                                                                                 |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_NUMSP256T1_"></span><span id="bcrypt_ecc_curve_numsp256t1_"></span>**BCRYPT\_ECC\_CURVE\_NUMSP256T1** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Name              | numsP256t1                                                                                                                              |
| Standard          | [Specification of Curve Selection and Supported Curve Parameters in MSR ECCLib](https://research.microsoft.com/pubs/219966/curvegen.pdf) |
| Key size (bits)   | 256                                                                                                                                     |
| TLS capable       | No                                                                                                                                      |
| Object identifier | None                                                                                                                                    |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_NUMSP384T1_"></span><span id="bcrypt_ecc_curve_numsp384t1_"></span>**BCRYPT\_ECC\_CURVE\_NUMSP384T1** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Name              | numsP384t1                                                                                                                              |
| Standard          | [Specification of Curve Selection and Supported Curve Parameters in MSR ECCLib](https://research.microsoft.com/pubs/219966/curvegen.pdf) |
| Key size (bits)   | 384                                                                                                                                     |
| TLS capable       | No                                                                                                                                      |
| Object identifier | None                                                                                                                                    |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_NUMSP512T1"></span><span id="bcrypt_ecc_curve_numsp512t1"></span>**BCRYPT\_ECC\_CURVE\_NUMSP512T1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Name              | numsP512t1                                                                                                                              |
| Standard          | [Specification of Curve Selection and Supported Curve Parameters in MSR ECCLib](https://research.microsoft.com/pubs/219966/curvegen.pdf) |
| Key size (bits)   | 512                                                                                                                                     |
| TLS capable       | No                                                                                                                                      |
| Object identifier | None                                                                                                                                    |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_SECP160K1_"></span><span id="bcrypt_ecc_curve_secp160k1_"></span>**BCRYPT\_ECC\_CURVE\_SECP160K1** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------|
| Name              | secP160k1                                                                       |
| Standard          | [Recommended Elliptic Curve Domain Parameters](https://www.secg.org/sec2-v2.pdf) |
| Key size (bits)   | 160                                                                             |
| TLS capable       | Yes                                                                             |
| Object identifier | 1.3.132.0.9                                                                     |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_SECP160R1_"></span><span id="bcrypt_ecc_curve_secp160r1_"></span>**BCRYPT\_ECC\_CURVE\_SECP160R1** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------|
| Name              | secP160r1                                                                       |
| Standard          | [Recommended Elliptic Curve Domain Parameters](https://www.secg.org/sec2-v2.pdf) |
| Key size (bits)   | 160                                                                             |
| TLS capable       | Yes                                                                             |
| Object identifier | 1.3.132.0.8                                                                     |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_SECP160R1_"></span><span id="bcrypt_ecc_curve_secp160r1_"></span>**BCRYPT\_ECC\_CURVE\_SECP160R1** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------|
| Name              | secP160r2                                                                       |
| Standard          | [Recommended Elliptic Curve Domain Parameters](https://www.secg.org/sec2-v2.pdf) |
| Key size (bits)   | 160                                                                             |
| TLS capable       | Yes                                                                             |
| Object identifier | 1.3.132.0.30                                                                    |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_SECP192K1"></span><span id="bcrypt_ecc_curve_secp192k1"></span>**BCRYPT\_ECC\_CURVE\_SECP192K1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------|
| Name              | secP192k1                                                                       |
| Standard          | [Recommended Elliptic Curve Domain Parameters](https://www.secg.org/sec2-v2.pdf) |
| Key size (bits)   | 192                                                                             |
| TLS capable       | Yes                                                                             |
| Object identifier | 1.3.132.0.31                                                                    |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_SECP192R1_"></span><span id="bcrypt_ecc_curve_secp192r1_"></span>**BCRYPT\_ECC\_CURVE\_SECP192R1** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------|
| Name              | secP192r1                                                                       |
| Standard          | [Recommended Elliptic Curve Domain Parameters](https://www.secg.org/sec2-v2.pdf) |
| Key size (bits)   | 192                                                                             |
| TLS capable       | Yes                                                                             |
| Object identifier | 1.2.840.10045.3.1.1                                                             |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_SECP224K1"></span><span id="bcrypt_ecc_curve_secp224k1"></span>**BCRYPT\_ECC\_CURVE\_SECP224K1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------|
| Name              | secP224k1                                                                       |
| Standard          | [Recommended Elliptic Curve Domain Parameters](https://www.secg.org/sec2-v2.pdf) |
| Key size (bits)   | 224                                                                             |
| TLS capable       | Yes                                                                             |
| Object identifier | 1.3.132.0.32                                                                    |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_SECP224R1"></span><span id="bcrypt_ecc_curve_secp224r1"></span>**BCRYPT\_ECC\_CURVE\_SECP224R1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------|
| Name              | secP224r1                                                                       |
| Standard          | [Recommended Elliptic Curve Domain Parameters](https://www.secg.org/sec2-v2.pdf) |
| Key size (bits)   | 224                                                                             |
| TLS capable       | Yes                                                                             |
| Object identifier | 1.3.132.0.33                                                                    |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_SECP256K1"></span><span id="bcrypt_ecc_curve_secp256k1"></span>**BCRYPT\_ECC\_CURVE\_SECP256K1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------|
| Name              | secP256k1                                                                       |
| Standard          | [Recommended Elliptic Curve Domain Parameters](https://www.secg.org/sec2-v2.pdf) |
| Key size (bits)   | 256                                                                             |
| TLS capable       | Yes                                                                             |
| Object identifier | 1.3.132.0.10                                                                    |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_SECP256R1"></span><span id="bcrypt_ecc_curve_secp256r1"></span>**BCRYPT\_ECC\_CURVE\_SECP256R1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------|
| Name              | secP256r1                                                                       |
| Standard          | [Recommended Elliptic Curve Domain Parameters](https://www.secg.org/sec2-v2.pdf) |
| Key size (bits)   | 256                                                                             |
| TLS capable       | Yes                                                                             |
| Object identifier | 1.2.840.10045.3.1.7                                                             |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_SECP384R1_"></span><span id="bcrypt_ecc_curve_secp384r1_"></span>**BCRYPT\_ECC\_CURVE\_SECP384R1** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------|
| Name              | secP384r1                                                                       |
| Standard          | [Recommended Elliptic Curve Domain Parameters](https://www.secg.org/sec2-v2.pdf) |
| Key size (bits)   | 384                                                                             |
| TLS capable       | Yes                                                                             |
| Object identifier | 1.3.132.0.34                                                                    |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_SECP521R1"></span><span id="bcrypt_ecc_curve_secp521r1"></span>**BCRYPT\_ECC\_CURVE\_SECP521R1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------|
| Name              | secP521r1                                                                       |
| Standard          | [Recommended Elliptic Curve Domain Parameters](https://www.secg.org/sec2-v2.pdf) |
| Key size (bits)   | 521                                                                             |
| TLS capable       | Yes                                                                             |
| Object identifier | 1.3.132.0.35                                                                    |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_WTLS12"></span><span id="bcrypt_ecc_curve_wtls12"></span>**BCRYPT\_ECC\_CURVE\_WTLS12**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|--------------|
| Name              | wtls12       |
| Standard          | WTLS         |
| Key size (bits)   | 224          |
| TLS capable       | No           |
| Object identifier | 1.3.132.0.33 |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_WTLS7"></span><span id="bcrypt_ecc_curve_wtls7"></span>**BCRYPT\_ECC\_CURVE\_WTLS7**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|--------------|
| Name              | wtls7        |
| Standard          | WTLS         |
| Key size (bits)   | 160          |
| TLS capable       | No           |
| Object identifier | 1.3.132.0.30 |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_WTLS9_"></span><span id="bcrypt_ecc_curve_wtls9_"></span>**BCRYPT\_ECC\_CURVE\_WTLS9** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------|
| Name              | wtls9         |
| Standard          | WTLS          |
| Key size (bits)   | 160           |
| TLS capable       | No            |
| Object identifier | 2.23.43.1.4.9 |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_X962P192V1"></span><span id="bcrypt_ecc_curve_x962p192v1"></span>**BCRYPT\_ECC\_CURVE\_X962P192V1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------|
| Name              | x962P192v1          |
| Standard          | ANSI X9.62          |
| Key size (bits)   | 192                 |
| TLS capable       | No                  |
| Object identifier | 1.2.840.10045.3.1.1 |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_X962P192V2_"></span><span id="bcrypt_ecc_curve_x962p192v2_"></span>**BCRYPT\_ECC\_CURVE\_X962P192V2** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------|
| Name              | x962P192v2          |
| Standard          | ANSI X9.62          |
| Key size (bits)   | 192                 |
| TLS capable       | No                  |
| Object identifier | 1.2.840.10045.3.1.2 |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_X962P192V3"></span><span id="bcrypt_ecc_curve_x962p192v3"></span>**BCRYPT\_ECC\_CURVE\_X962P192V3**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------|
| Name              | x962P192v3          |
| Standard          | ANSI X9.62          |
| Key size (bits)   | 192                 |
| TLS capable       | No                  |
| Object identifier | 1.2.840.10045.3.1.3 |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_X962P239V1_"></span><span id="bcrypt_ecc_curve_x962p239v1_"></span>**BCRYPT\_ECC\_CURVE\_X962P239V1** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------|
| Name              | x962P239v1          |
| Standard          | ANSI X9.62          |
| Key size (bits)   | 239                 |
| TLS capable       | No                  |
| Object identifier | 1.2.840.10045.3.1.4 |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_X962P239V2_"></span><span id="bcrypt_ecc_curve_x962p239v2_"></span>**BCRYPT\_ECC\_CURVE\_X962P239V2** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------|
| Name              | x962P239v2          |
| Standard          | ANSI X9.62          |
| Key size (bits)   | 239                 |
| TLS capable       | No                  |
| Object identifier | 1.2.840.10045.3.1.5 |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_X962P239V3_"></span><span id="bcrypt_ecc_curve_x962p239v3_"></span>**BCRYPT\_ECC\_CURVE\_X962P239V3** </dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------|
| Name              | x962P239v3          |
| Standard          | ANSI X9.62          |
| Key size (bits)   | 239                 |
| TLS capable       | No                  |
| Object identifier | 1.2.840.10045.3.1.6 |



 

</dt> </dl> </dd> <dt><span id="BCRYPT_ECC_CURVE_X962P256V1"></span><span id="bcrypt_ecc_curve_x962p256v1"></span>**BCRYPT\_ECC\_CURVE\_X962P256V1**</dt> <dd> <dl> <dt> 

| Requirement | Value |
|-------------------|---------------------|
| Name              | x962P256v1          |
| Standard          | ANSI X9.62          |
| Key size (bits)   | 256                 |
| TLS capable       | No                  |
| Object identifier | 1.2.840.10045.3.1.7 |



 


</dt> </dl> </dd> </dl>

## Remarks

To use a named curve, call [**BCryptOpenAlgorithmProvider**](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptopenalgorithmprovider) using either the **BCRYPT\_ECDSA\_ALGORITHM** or the **BCRYPT\_ECDH\_ALGORITHM** as the algorithm ID. Then, call [**BCryptSetProperty**](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptsetproperty) and set the **BCRYPT\_ECC\_CURVE\_NAME** property to one of the above curves or any named curves registered on the computer as shown by the `certutil -displayEccCurve` command.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Bcrypt.h</dt> </dl> |



## See also

<dl> <dt>

[**BCryptOpenAlgorithmProvider**](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptopenalgorithmprovider)
</dt> <dt>

[**NCryptCreatePersistedKey**](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptcreatepersistedkey)
</dt> </dl>

 

 




