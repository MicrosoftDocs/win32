---
description: In MOF, numbers are digits that describe numerical values. MOF provides a variety of data types that translate into Automation, and also allows those numbers to be in different formats. The following table lists the numeric values that MOF supports.
ms.assetid: 7a18ed36-9c12-42be-a4ee-0f6c0097b130
ms.tgt_platform: multiple
title: Numbers (WMI)
ms.topic: article
ms.date: 05/31/2018
---

# Numbers (WMI)

In MOF, numbers are digits that describe numerical values. MOF provides a variety of data types that translate into Automation, and also allows those numbers to be in different formats. The following table lists the numeric values that MOF supports.



| Data type  | Automation type | Description                                                                                                                                                             |
|------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **sint8**  | **VT\_I2**      | Signed 8-bit integer.<br/>                                                                                                                                        |
| **sint16** | **VT\_I2**      | Signed 16-bit integer.<br/>                                                                                                                                       |
| **sint32** | VT\_I4          | Signed 32-bit integer.<br/>                                                                                                                                       |
| **sint64** | **VT\_BSTR**    | Signed 64-bit integer in string form. This type follows hexadecimal or decimal format according to the American National Standards Institute (ANSI) C rules.<br/> |
| **real32** | **VT\_R4**      | 4-byte floating-point value that follows the Institute of Electrical and Electronics Engineers, Inc. (IEEE) standard.<br/>                                        |
| **real64** | **VT\_R8**      | 8-byte floating-point value that follows the IEEE standard.<br/>                                                                                                  |
| **uint8**  | **VT\_UI1**     | Unsigned 8-bit integer.<br/>                                                                                                                                      |
| **uint16** | **VT\_I4**      | Unsigned 16-bit integer.<br/>                                                                                                                                     |
| **uint32** | **VT\_I4**      | Unsigned 32-bit integer.<br/>                                                                                                                                     |
| **uint64** | **VT\_BSTR**    | Unsigned 64-bit integer in string form. This type follows hexadecimal or decimal format according to ANSI C rules.<br/>                                           |



 

Although flexible, MOF code does encounter some changes when dealing with Automation:

-   You must encode 64-bit integers as strings.

    Automation does not support a 64-bit integral type.

-   Automation types do not always correspond in bit size to MOF data types.

    For example, Automation uses VT\_I4 to return an unsigned 16-bit value. This discrepancy exists because of sign-extension problems. If Automation used VT\_I2 instead of VT\_I4, 65,536 would appear to be the value  1, causing type and range problems. Similarly, Automation represents the **uint32** type as VT\_I4 because there exists no larger integer type to contain **uint32**.

-   You do not need to change any representation for 8-bit numeral types.

    Automation supports VT\_UI1, an unsigned 8-bit type.

MOF supports long constants. You declare a long constant using a simple series of digits with an optional negative sign. A long constant cannot exceed the size of the variable that is declared to hold it. Some examples of long constants are 1000 and  12310.

MOF also supports alternate numerical formats. The following table lists the special characters you must use to describe hexadecimal, binary, and octal constants.



| Constant               | Special character     | Example                   |
|------------------------|-----------------------|---------------------------|
| Decimal<br/>     | None<br/>       | val = 65<br/>       |
| Hexadecimal<br/> | 0x prefix<br/>  | val = 0x41<br/>     |
| Octal<br/>       | Leading 0<br/>  | val = 0101<br/>     |
| Binary<br/>      | Trailing B<br/> | val = 1000001B<br/> |



 

You can use a floating-point constant to represent scientific notation as well as fractions, as shown next:

``` syntax
3.14
-3.14
-1.2778E+02
```

WMI considers floating-point constants as **VT\_R8** types for Automation.

The following example describes class and instance declarations that illustrate how to use each of the numeric data types to set properties:

``` syntax
Class NumericDataClass
 {
   [key] uint8 Duint8;
   SInt8       Dchar;
   UInt16      Dtword;
   Sint16      Dinst16;
   UInt32      Ddword;
   Sint32      Dinst1;
   Sint32      Dinst2;
   Sint32      Dinst3;
   Sint32      Dinst4;
   Sint32      Dinst5;
   Real32      Dfloat;
   Real64      Ddouble1;
   Real64      Ddouble2;
 };

instance of NumericDataClass
 {
   Duint8   =  122;
   Dchar    = -128;
   Dtword   =  30;
   Dinst16  = -1445;
   Ddword   =  6987777;
   Dinst1   = -455589;
   Dinst2   =  23;
   Dinst3   =  03;         // Base 8
   Dinst4   =  0xFe;       // Base 16
   Dinst5   =  11b;        // Base 2
   Dfloat   =  3.1478;
   Ddouble1 =  99987.3654;
   Ddouble2 =  2.3e-2;
 };
```

 

 




