---
description: Cryptographic Message Syntax (CMS), derived from PKCS \#7 version 1.5, is the syntax used to hash, digitally sign, authenticate, and encrypt arbitrary messages.
ms.assetid: 4396d3e2-8e41-4864-a12a-a598fab82840
title: CMS Additions
ms.topic: article
ms.date: 05/31/2018
---

# CMS Additions

Cryptographic Message Syntax (CMS), derived from PKCS \#7 version 1.5, is the syntax used to [*hash*](../secgloss/h-gly.md), [*digitally sign*](../secgloss/d-gly.md), authenticate, and encrypt arbitrary messages. Where possible, backward compatibility is preserved; however, changes have been made to accommodate attribute certificate transfer and key agreement techniques for key management. CMS allows multiple encapsulation so that one encapsulation envelope can be nested inside another. Also, one party can digitally sign previously encapsulated data; arbitrary attributes, such as signing time, can be signed along with the message content; and attributes, such as [*countersignatures*](../secgloss/c-gly.md), can be associated with a signature. CMS can support a variety of architectures for certificate-based key management.

To support additional CMS capabilities, underlying data structures have been given new fields. New flags and parameter values have also been added. All data structures and all APIs using CMS are 100 percent backward compatible with PKCS \#7 version 1.5.

Additions include [Enveloped Data Additions](enveloped-data-additions.md) and [Signed Data Additions](signed-data-additions.md).

 

 
