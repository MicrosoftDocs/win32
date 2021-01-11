---
description: The address filter notifies the Network Monitor driver to accept frames that have one of a variety of specified MAC address types (Ethernet, Token Ring, and FDDI).
ms.assetid: 23a38f49-2d63-4fc8-8113-29143493359c
title: Writing ADDRESSTABLE Filter Portion
ms.topic: article
ms.date: 05/31/2018
---

# Writing ADDRESSTABLE Filter Portion

The address filter notifies the Network Monitor driver to accept frames that have one of a variety of specified MAC address types (Ethernet, Token Ring, and FDDI). You can specify a maximum of eight address pairs. An address pair can specify a source, a destination, both, or neither.

The address portion of the filter consists of two structures: [**ADDRESSTABLE**](addresstable.md) and [**ADDRESSPAIR**](addresspair.md).

If you specify NO addresses, then ALL frames will pass the address filter. However, if you specify any addresses, only those frames that pass the given address filter will pass.

Building the address filter involves allocating an [**ADDRESSTABLE**](addresstable.md) structure and filling in members of the [**ADDRESSPAIR**](addresspair.md) structure.

**To build the address portion of a capture filter**

1.  Use the **CAPTUREFILTER\_FLAGS\_LOCAL\_ONLY** flag of the [**CAPTUREFILTER**](capturefilter.md) structure to restrict the capture to traffic to and from your local computer.

    Setting this flag will not set the NIC to promiscuous mode; the capture file will capture only local traffic.

2.  Use the following example code to define the [**ADDRESSTABLE**](addresstable.md) structure:

    ``` syntax
    typedef struct _ADDRESSTABLE
    {
        DWORD           nAddressPairs;
        DWORD           nNonMacAddressPairs;
        ADDRESSPAIR     AddressPair[MAX_ADDRESS_PAIRS];
    } ADDRESSTABLE;

    typedef ADDRESSTABLE *LPADDRESSTABLE;
     
    typedef struct _ADDRESSPAIR
    {
        WORD        AddressFlags;
        WORD        NalReserved;
        ADDRESS     DstAddress;
        ADDRESS     SrcAddress;
    } ADDRESSPAIR;

    typedef ADDRESSPAIR *LPADDRESSPAIR;
    ```

3.  Use the information, listed in the following table, to select an [**ADDRESSPAIR**](addresspair.md) flag type. 

    | Flag                             | Meaning                                                                               |
    |----------------------------------|---------------------------------------------------------------------------------------|
    | ADDRESS\_FLAGS\_MATCH\_DST       | Matches a destination address.                                                        |
    | ADDRESS\_FLAGS\_MATCH\_SRC       | Matches a source address                                                              |
    | ADDRESS\_FLAGS\_EXCLUDE          | Excludes the frame if this address is found (either a defined source or destination). |
    | ADDRESS\_FLAGS\_DST\_GROUP\_ADDR | Matches group bit (of the destination address) only for broadcast-type messages.      |
    | ADDRESS\_FLAGS\_MATCH\_BOTH      | Matches both the destination and source addresses.                                    |

    

     

4.  Fill in a destination address, which is evaluated against the [**ADDRESSPAIR**](addresspair.md) flag that you select.
5.  Fill in a source address, which is evaluated against the [**ADDRESSPAIR**](addresspair.md) flag that you select.
6.  Populate the [**ADDRESSTABLE**](addresstable.md) structure with an array of [**ADDRESSPAIR**](addresspair.md) structures, which includes the address pairs that the driver evaluates. All address pairs are evaluated as a logical OR statement (ADDRESSPAIR 1 \|\| ADDRESSPAIR 2). You can include a maximum of eight address pairs in a capture filter.

 

 



