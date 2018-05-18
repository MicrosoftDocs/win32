---
Description: 'Given a certificate, the first step in decoding the certificate BLOB is to call CertCreateCertificateContext, passing it a pointer to the encoded certificate (BLOB).'
ms.assetid: 'b50530e2-15a0-4215-bf18-300cf67d1611'
title: 'Decoding a CERT\_INFO Structure'
---

# Decoding a CERT\_INFO Structure

Given a certificate, the first step in decoding the certificate [*BLOB*](security.b_gly#-security-blob-gly) is to call [**CertCreateCertificateContext**](certcreatecertificatecontext.md), passing it a pointer to the encoded certificate (*BLOB*). When this function is called, it creates a duplicate of the encoded certificate, creates a structure of type [**CERT\_CONTEXT**](cert-context.md), and creates a structure of type [**CERT\_INFO**](cert-info.md). As shown in the following illustration, a [*certificate context*](security.c_gly#-security-certificate-context-gly) includes the original certificate *BLOB*, a C structure of type **CERT\_CONTEXT**, and a C structure of type **CERT\_INFO**. One of the members of the **CERT\_CONTEXT** structure points to the **CERT\_INFO** structure and another to the encoded certificate BLOB.

![certificate context](images/certcntx.png)

The encoded object (data member) is always provided as the input to the [**CryptDecodeObject**](cryptdecodeobject.md) function, and the output is a C structure that may or may not have encoded members, depending on how far into the process you are.

There is one other member that requires some decoding, and that is the **Extension** member. Although it is not encoded at the [**CERT\_INFO**](cert-info.md) level, it does contain some encoded information. To decode this information, proceed as shown in the following illustration.

![decoding information](images/xtension.png)

In the [**CERT\_INFO**](cert-info.md) structure, member **rgExtension** is a pointer to an array of [**CERT\_EXTENSION**](cert-extension.md) structures. Each **CERT\_EXTENSION** structure has a **Value** member that is in encoded form and needs to be decoded. The **Value** member is passed to the [**CryptDecodeObject**](cryptdecodeobject.md) function, and then the output from the function depends on the value of the **pszObjId** member. Notice that in the illustration, two different structures are produced, one of type [**CERT\_BASIC\_CONSTRAINTS\_INFO**](cert-basic-constraints-info.md) and one of type [**CERT\_AUTHORITY\_KEY\_ID\_INFO**](cert-authority-key-id-info.md), depending on the value of **pszObjId**.

 

 



