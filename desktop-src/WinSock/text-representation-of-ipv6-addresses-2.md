---
description: This section is copied from &\#0034;IPv6 Addressing Architecture&\#0034; by R.
ms.assetid: 52faecb9-0d7a-40fa-a021-3cc6816a4db8
title: Text Representation of IPv6 Addresses
ms.topic: article
ms.date: 05/31/2018
---

# Text Representation of IPv6 Addresses

This section is copied from "IPv6 Addressing Architecture" by R. Hinden and S. Deering. There are three conventional forms for representing IPv6 addresses as text strings:

-   The preferred form is x:x:x:x:x:x:x:x, where the 'x's are the hexadecimal values of the eight 16-bit pieces of the address.

    Examples:

    <dl> FEDC:BA98:7654:3210:FEDC:BA98:7654:3210  
    1080:0:0:0:8:800:200C:417A  
    </dl>

> [!Note]  
> It is not necessary to write the leading zeros in an individual field, but there must be at least one numeral in every field (except for the case described in the second form).

 

-   Due to the method of allocating certain styles of IPv6 addresses, it is common for addresses to contain long strings of zero bits. In order to make writing addresses containing zero bits easier, a special syntax is available to compress the zeros. The use of double colons ("::") indicates multiple groups of 16-bits of zeros.

    For example, the multicast address

    <dl> FF01:0:0:0:0:0:0:43  
    </dl>

    may be represented as:

    <dl> FF01::43  
    </dl>

    The double quotation marks ("::") can only appear once in an address. They can be used to compress leading or trailing zeros in an address.

-   An alternative form that may be more convenient when dealing with a mixed environment of IPv4 and IPv6 nodes is x:x:x:x:x:x:d.d.d.d, where the 'x's are the hexadecimal values of the six high-order 16-bit pieces of the address, and the 'd's are the decimal values of the four low-order 8-bit pieces of the address (standard IPv4 representation).

    Examples:

    <dl> 0:0:0:0:0:0:13.1.68.3  
    0:0:0:0:0:FFFF:129.144.52.38  
    </dl>

    or in compressed form:

    <dl> ::13.1.68.3  
    ::FFFF:129.144.52.38  
    </dl>

 

 



