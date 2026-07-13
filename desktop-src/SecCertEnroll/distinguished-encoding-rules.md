---
description: Abstract Syntax Notation One (ASN.1) defines the following rule sets that govern how data structures that are being sent between computers are encoded and decoded.
ms.assetid: 47735fa1-9d75-4c6b-b14c-6c7483f43a5d
title: Distinguished Encoding Rules
ms.topic: concept-article
ms.date: 12/17/2024
---

# Distinguished Encoding Rules

Abstract Syntax Notation One (ASN.1) defines the following rule sets that govern how data structures that are being sent between computers are encoded and decoded.

- Basic Encoding Rules (BER)
- Canonical Encoding Rules (CER)
- Distinguished Encoding Rules (DER)
- Packed Encoding Rules (PER)

The original rule set was defined by the BER specification. CER and DER were developed later as specialized subsets of BER. PER was developed in response to criticisms about the amount of bandwidth required to transmit data using BER or its variants. PER provides a significant savings.

DER was created to satisfy the requirements of the X.509 specification for secure data transfer. The Certificate Enrollment API uses DER exclusively. For more information, see the following topics.

- [DER Transfer Syntax](about-der-transfer-syntax.md)
- [DER Encoding of ASN.1 Types](about-der-encoding-of-asn-1-types.md)

## Related content

[ASN.1 Type System](about-asn-1-type-system.md)

[Certificate Request Encoding](about-certificate-request-encoding.md)

[Introduction to ASN.1 Syntax and Encoding](about-introduction-to-asn-1-syntax-and-encoding.md)
