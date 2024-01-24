---
description: A value map is an array linked to a property with the Value and ValueMap qualifiers.
ms.assetid: 7667e87f-b997-4fd9-81ea-b27c9d2a9335
ms.tgt_platform: multiple
title: ValueMap and Value Qualifiers
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# ValueMap and Value Qualifiers

A value map is an array linked to a property with the **Value** and **ValueMap** qualifiers.

The property acts as an index into the array, holding a value that represents one of the values in the array. Using MOF code, you can have the following types of value maps:

-   Array mapping to an integer.

    You can define an array with the **Value** qualifier and link the array directly to an integer property, as shown in the following example:

    ``` syntax
    [Values {"OK", "Error", "Degraded", "Unknown"}, Read]
    sint32 Status;
    ```

    In this example, the **Status** property value is an index into the string array defined by **Value**. The property can only take on values that correspond to the ordinal positions in the **Value** array minus 1. For example, setting **Status** to "1" maps to the "Error" value. The index property can take only values that correspond to positions in the **Value** array. For example, if the array has 10 entries, the index property can story 0 through 9, not 30 or 177.

-   Array mapping to another array mapping to an integer.

    If you wish to create an index that does not use an ordinal system of counting, use the **ValueMap** qualifier. The **ValueMap** qualifier sets up another array that holds an arbitrary index numbering system, as shown in the following example:

    ``` syntax
    [ValueMap {"1", "3", "99", "0"}, 
     Values {"OK", "Error", "Degraded", "Unknown"}, Read]
    sint32 Status;
    ```

    Although you must place the values of **ValueMap** in quotations, WMI considers the values integers. Therefore, In this example you can set the **Status** property to an integer in the **ValueMap** set: 1, 3, 99, or 0. WMI maps each integer from an ordinal position in the **ValueMap** string array to a corresponding position in the **Value** array. For example, setting **Status** to 0 maps to "Unknown".

-   Array mapping to another array mapping to a string.

    If you do not want to use an integer to index your array, you can instead use a string to hold one of the possible values in your array. To do so, you must define both a **Value** and **ValueMap** array that both contain strings, as shown in the following example:

    ``` syntax
    [ValueMap {"OK", "Error", "Degraded", "Unknown"}, 
     Values {"OK", "Error", "Degraded", "Unknown"}, Read]
    string Status;
    ```

    With a string property, the actual allowable values of the property are the entries in the **ValueMap** array. For example, you can set **Status** to "OK" or "Unknown".

It is up to the application to take advantage of mappings in a useful way. It is up to the provider to enforce a legal range of values.

## Remarks

In deciding whether to use the **ValueMap**/**Value** or **BitMap**/**BitValues** qualifiers, determine whether any of the values being indicated could occur concurrently. If multiple concurrent values can exist, you must use **BitMap**/**BitValues**. If all the values are mutually exclusive, you should use the **ValueMap**/**Value** qualifiers.

## Related topics

<dl> <dt>

[BitMap and BitValues](bitmap-and-bitvalues.md)
</dt> </dl>

 

 



