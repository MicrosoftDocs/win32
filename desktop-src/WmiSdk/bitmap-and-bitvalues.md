---
description: Is an integer linked to a property with the BitMap and BitValue qualifiers.
ms.assetid: 14c34909-2419-41a1-a1ed-3b647a3c5e75
ms.tgt_platform: multiple
title: BitMap and BitValue Qualifiers
ms.topic: article
ms.date: 05/31/2018
---

# BitMap and BitValue Qualifiers

A bitmap is an integer linked to a property with the **BitMap** and **BitValue** qualifiers. Each bit of the property value acts as an index into the array of values in the **BitValue** list. Because multiple bits in the property value can be "on" at the same time, it is possible to use a single property value to indicate multiple concurrent values.

For example, the following MOF code example establishes the **FileType** property as having the **BitMap** and **BitValues** qualifiers. It further establishes that the low-order bit (bit 0) corresponds to the value "Read Only". The next bit (bit 1) corresponds to "Hidden", and so on. (Not all bits must be significant. In this eight-bit system, the two high-order bits, 6 and 7, have no significance.)

``` syntax
[BitMap("0","1","2","3","4","5"),
 BitValues("Read Only",
           "Hidden",
           "System",
           "Volume Label",
           "Subdirectory",
           "Archive")]
byte FileType;
```

If the **FileType** property reports the value 7 (bits 0000 0111), the file is "Read Only", "System", and "Hidden". If the **FileType** property reports the value 18 (0x12, bits 0001 0010), it is a hidden subdirectory.

There are two different types of bitmaps using MOF code:

-   Consecutive significant bits beginning with the low-order bit (bit 0)

    You can define an array of bit values without explicitly specifying the significant bits if the significant bits begin with the low-order bit (bit 0) and progress upward without interruption through all items in the **BitValue** array. The following MOF code example performs the same function as the previous example.

    ``` syntax
    [BitValues("Read Only",
               "Hidden",
               "System",
               "Volume Label",
               "Subdirectory",
               "Archive")]
    byte FileType;
    ```

-   Significant bit preceded by a non-significant bit

    If the low-order bit is insignificant, or the sequence of significant bits is not continuous, you must specify both the **BitMap** and **BitValues** qualifiers. The following MOF code example shows a situation in which the low-order bit is not significant and there is a gap in the sequence of significant bits.

    ``` syntax
    [BitMap("1","4","5"),
     BitValues("Follow-up","Delivery receipt","Read receipt")]
    sint32 MailOptions;
    ```

    In this case, setting the low-order bit (bit 0) has no significance and is ignored. However, setting bit 1 (0x2) indicates that this email message is flagged for follow up, setting bit 4 (0x8) indicates that a delivery receipt should be sent to the sender when the email message has arrived at the recipient's mailbox, and setting bit 5 (0x10) specifies that a read receipt should be sent to the sender when the email message is opened by the recipient. Setting all three significant bits (0x1A) specifies all three conditions for the email message.

## Remarks

In deciding whether to use the **BitMap**/**BitValues** or **ValueMap**/**Values** qualifiers, determine whether any of the values being indicated could occur concurrently. If multiple concurrent values can exist, you must use **BitMap**/**BitValues**. If all the values are mutually exclusive, you should use the **ValueMap**/**Values** qualifiers.

## Related topics

<dl> <dt>

[ValueMap and Value Qualifiers](value-map.md)
</dt> </dl>

 

 



