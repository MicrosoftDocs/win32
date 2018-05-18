---
title: Data Type Conversion Functions
description: The following low-level functions convert variant data types. Higher-level variant manipulation functions (such as VariantChangeType) use these functions, but they can also be called directly.
ms.assetid: 'b69504cf-6c80-4de1-a26e-9281ab848c71'
---

# Data Type Conversion Functions

The following low-level functions convert variant data types. Higher-level variant manipulation functions (such as [**VariantChangeType**](variantchangetype.md)) use these functions, but they can also be called directly.

## Functions to convert to type char



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned char**  | [**VarI1FromUI1**](vari1fromui1.md)   |
| **unsigned short** | [**VarI1FromUI2**](vari1fromui2.md)   |
| **unsigned long**  | [**VarI1FromUI4**](vari1fromui4.md)   |
| **ULONG64**        | [**VarI1FromUI8**](vari1fromui8.md)   |
| **short**          | [**VarI1FromI2**](vari1fromi2.md)     |
| **long**           | [**VarI1FromI4**](vari1fromi4.md)     |
| **LONG64**         | [**VarI1FromI8**](vari1fromi8.md)     |
| **float**          | [**VarI1FromR4**](vari1fromr4.md)     |
| **double**         | [**VarI1FromR8**](vari1fromr8.md)     |
| **CURRENCY**       | [**VarI1FromCy**](vari1fromcy.md)     |
| **DECIMAL**        | [**VarI1FromDec**](vari1fromdec.md)   |
| **DATE**           | [**VarI1FromDate**](vari1fromdate.md) |
| **OLECHAR \***     | [**VarI1FromStr**](vari1fromstr.md)   |
| **IDispatch \***   | [**VarI1FromDisp**](vari1fromdisp.md) |
| **BOOL**           | [**VarI1FromBool**](vari1frombool.md) |



 

## Functions to convert to type unsigned char



| From type          | Function                                 |
|--------------------|------------------------------------------|
| **unsigned short** | [**VarUI1FromUI2**](varui1fromui2.md)   |
| **unsigned long**  | [**VarUI1FromUI4**](varui1fromui4.md)   |
| **ULONG64**        | [**VarI1FromUI8**](vari1fromui8.md)     |
| **char**           | [**VarUI1FromI1**](varui1fromi1.md)     |
| **short**          | [**VarUI1FromI2**](varui1fromi2.md)     |
| **long**           | [**VarUI1FromI4**](varui1fromi4.md)     |
| **LONG64**         | [**VarUI1FromI8**](varui1fromi8.md)     |
| **float**          | [**VarUI1FromR4**](varui1fromr4.md)     |
| **double**         | [**VarUI1FromR8**](varui1fromr8.md)     |
| **CURRENCY**       | [**VarUI1FromCy**](varui1fromcy.md)     |
| **DECIMAL**        | [**VarUI1FromDec**](varui1fromdec.md)   |
| **DATE**           | [**VarUI1FromDate**](varui1fromdate.md) |
| **OLECHAR \***     | [**VarUI1FromStr**](varui1fromstr.md)   |
| **IDispatch \***   | [**VarUI1FromDisp**](varui1fromdisp.md) |
| **BOOL**           | [**VarUI1FromBool**](varui1frombool.md) |



 

## Functions to convert to type short



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned char**  | [**VarI2FromUI1**](vari2fromui1.md)   |
| **unsigned short** | [**VarI2FromUI2**](vari2fromui2.md)   |
| **unsigned long**  | [**VarI2FromUI4**](vari2fromui4.md)   |
| **ULONG64**        | [**VarI2FromUI8**](vari2fromui8.md)   |
| **char**           | [**VarI2FromI1**](vari2fromi1.md)     |
| **long**           | [**VarI2FromI4**](vari2fromi4.md)     |
| **LONG64**         | [**VarI2FromI8**](vari2fromi8.md)     |
| **float**          | [**VarI2FromR4**](vari2fromr4.md)     |
| **double**         | [**VarI2FromR8**](vari2fromr8.md)     |
| **CURRENCY**       | [**VarI2FromCy**](vari2fromcy.md)     |
| **DECIMAL**        | [**VarI2FromDec**](vari2fromdec.md)   |
| **DATE**           | [**VarI2FromDate**](vari2fromdate.md) |
| **OLECHAR \***     | [**VarI2FromStr**](vari2fromstr.md)   |
| **IDispatch \***   | [**VarI2FromDisp**](vari2fromdisp.md) |
| **BOOL**           | [**VarI2FromBool**](vari2frombool.md) |



 

## Functions to convert to type unsigned short



| From type         | Function                                 |
|-------------------|------------------------------------------|
| **char**          | [**VarUI2FromI1**](varui2fromi1.md)     |
| **short**         | [**VarUI2FromI2**](varui2fromi2.md)     |
| **long**          | [**VarUI2FromI4**](varui2fromi4.md)     |
| **LONG64**        | [**VarUI2FromI8**](varui2fromi8.md)     |
| **unsigned char** | [**VarUI2FromUI1**](varui2fromui1.md)   |
| **unsigned long** | [**VarUI2FromUI4**](varui2fromui4.md)   |
| **LONG64**        | [**VarUI2FromUI8**](varui2fromui8.md)   |
| **float**         | [**VarUI2FromR4**](varui2fromr4.md)     |
| **double**        | [**VarUI2FromR8**](varui2fromr8.md)     |
| **CURRENCY**      | [**VarUI2FromCy**](varui2fromcy.md)     |
| **DECIMAL**       | [**VarUI2FromDec**](varui2fromdec.md)   |
| **DATE**          | [**VarUI2FromDate**](varui2fromdate.md) |
| **OLECHAR \***    | [**VarUI2FromStr**](varui2fromstr.md)   |
| **IDispatch \***  | [**VarUI2FromDisp**](varui2fromdisp.md) |
| **BOOL**          | [**VarUI2FromBool**](varui2frombool.md) |



 

## Functions to convert to type long



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned short** | [**VarI4FromUI2**](vari4fromui2.md)   |
| **unsigned long**  | [**VarI4FromUI4**](vari4fromui4.md)   |
| **ULONG64**        | [**VarI4FromUI8**](vari4fromui8.md)   |
| **char**           | [**VarI4FromI1**](vari4fromi1.md)     |
| **unsigned char**  | [**VarI4FromUI1**](vari4fromui1.md)   |
| **short**          | [**VarI4FromI2**](vari4fromi2.md)     |
| **LONG64**         | [**VarI4FromI8**](vari4fromi8.md)     |
| **float**          | [**VarI4FromR4**](vari4fromr4.md)     |
| **double**         | [**VarI4FromR8**](vari4fromr8.md)     |
| **CURRENCY**       | [**VarI4FromCy**](vari4fromcy.md)     |
| **DECIMAL**        | [**VarI4FromDec**](vari4fromdec.md)   |
| **DATE**           | [**VarI4FromDate**](vari4fromdate.md) |
| **OLECHAR \***     | [**VarI4FromStr**](vari4fromstr.md)   |
| **IDispatch \***   | [**VarI4FromDisp**](vari4fromdisp.md) |
| **BOOL**           | [**VarI4FromBool**](vari4frombool.md) |
| **INT**            | [**VarI4FromInt**](vari4fromint.md)   |



 

## Functions to convert to type unsigned long



| From type          | Function                                 |
|--------------------|------------------------------------------|
| **unsigned short** | [**VarUI4FromUI2**](varui4fromui2.md)   |
| **char**           | [**VarUI4FromI1**](varui4fromi1.md)     |
| **short**          | [**VarUI4FromI2**](varui4fromi2.md)     |
| **unsigned char**  | [**VarUI4FromUI1**](varui4fromui1.md)   |
| **ULONG64**        | [**VarUI4FromUI8**](varui4fromui8.md)   |
| **long**           | [**VarUI4FromI4**](varui4fromi4.md)     |
| **LONG64**         | [**VarUI4FromI8**](varui4fromi8.md)     |
| **float**          | [**VarUI4FromR4**](varui4fromr4.md)     |
| **double**         | [**VarUI4FromR8**](varui4fromr8.md)     |
| **CURRENCY**       | [**VarUI4FromCy**](varui4fromcy.md)     |
| **DECIMAL**        | [**VarUI4FromDec**](varui4fromdec.md)   |
| **DATE**           | [**VarUI4FromDate**](varui4fromdate.md) |
| **OLECHAR \***     | [**VarUI4FromStr**](varui4fromstr.md)   |
| **IDispatch \***   | [**VarUI4FromDisp**](varui4fromdisp.md) |
| **BOOL**           | [**VarUI4FromBool**](varui4frombool.md) |



 

## Functions to convert to type float



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned short** | [**VarR4FromUI2**](varr4fromui2.md)   |
| **unsigned long**  | [**VarR4FromUI4**](varr4fromui4.md)   |
| **ULONG64**        | [**VarR4FromUI8**](varr4fromui8.md)   |
| **char**           | [**VarR4FromI1**](varr4fromi1.md)     |
| **unsigned char**  | [**VarR4FromUI1**](varr4fromui1.md)   |
| **short**          | [**VarR4FromI2**](varr4fromi2.md)     |
| **long**           | [**VarR4FromI4**](varr4fromi4.md)     |
| **LONG64**         | [**VarR4FromI8**](varr4fromi8.md)     |
| **double**         | [**VarR4FromR8**](varr4fromr8.md)     |
| **CURRENCY**       | [**VarR4FromCy**](varr4fromcy.md)     |
| **DECIMAL**        | [**VarR4FromDec**](varr4fromdec.md)   |
| **DATE**           | [**VarR4FromDate**](varr4fromdate.md) |
| **OLECHAR \***     | [**VarR4FromStr**](varr4fromstr.md)   |
| **IDispatch \***   | [**VarR4FromDisp**](varr4fromdisp.md) |
| **BOOL**           | [**VarR4FromBool**](varr4frombool.md) |



 

## Functions to convert to type double



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned short** | [**VarR8FromUI2**](varr8fromui2.md)   |
| **unsigned long**  | [**VarR8FromUI4**](varr8fromui4.md)   |
| **ULONG64**        | [**VarR8FromUI8**](varr8fromui8.md)   |
| **char**           | [**VarR8FromI1**](varr8fromi1.md)     |
| **unsigned char**  | [**VarR8FromUI1**](varr8fromui1.md)   |
| **short**          | [**VarR8FromI2**](varr8fromi2.md)     |
| **long**           | [**VarR8FromI4**](varr8fromi4.md)     |
| **LONG64**         | [**VarR8FromI8**](varr8fromi8.md)     |
| **float**          | [**VarR8FromR4**](varr8fromr4.md)     |
| **CURRENCY**       | [**VarR8FromCy**](varr8fromcy.md)     |
| **DECIMAL**        | [**VarR8FromDec**](varr8fromdec.md)   |
| **DATE**           | [**VarR8FromDate**](varr8fromdate.md) |
| **OLECHAR \***     | [**VarR8FromStr**](varr8fromstr.md)   |
| **IDispatch \***   | [**VarR8FromDisp**](varr8fromdisp.md) |
| **BOOL**           | [**VarR8FromBool**](varr8frombool.md) |



 

## Functions to convert to type DATE



| From type          | Function                                   |
|--------------------|--------------------------------------------|
| **unsigned short** | [**VarDateFromUI2**](vardatefromui2.md)   |
| **unsigned long**  | [**VarDateFromUI4**](vardatefromui4.md)   |
| **ULONG64**        | [**VarDateFromUI8**](vardatefromui8.md)   |
| **char**           | [**VarDateFromI1**](vardatefromi1.md)     |
| **unsigned char**  | [**VarDateFromUI1**](vardatefromui1.md)   |
| **short**          | [**VarDateFromI2**](vardatefromi2.md)     |
| **long**           | [**VarDateFromI4**](vardatefromi4.md)     |
| **LONG64**         | [**VarDateFromI8**](vardatefromi8.md)     |
| **float**          | [**VarDateFromR4**](vardatefromr4.md)     |
| **double**         | [**VarDateFromR8**](vardatefromr8.md)     |
| **CURRENCY**       | [**VarDateFromCy**](vardatefromcy.md)     |
| **DECIMAL**        | [**VarDateFromDec**](vardatefromdec.md)   |
| **OLECHAR \***     | [**VarDateFromStr**](vardatefromstr.md)   |
| **IDispatch \***   | [**VarDateFromDisp**](vardatefromdisp.md) |
| **BOOL**           | [**VarDateFromBool**](vardatefrombool.md) |



 

## Functions to convert to type CURRENCY



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned short** | [**VarCyFromUI2**](varcyfromui2.md)   |
| **unsigned long**  | [**VarCyFromUI4**](varcyfromui4.md)   |
| **ULONG64**        | [**VarCyFromUI8**](varcyfromui8.md)   |
| **char**           | [**VarCyFromI1**](varcyfromi1.md)     |
| **unsigned char**  | [**VarCyFromUI1**](varcyfromui1.md)   |
| **short**          | [**VarCyFromI2**](varcyfromi2.md)     |
| **long**           | [**VarCyFromI4**](varcyfromi4.md)     |
| **LONG64**         | [**VarCyFromI8**](varcyfromi8.md)     |
| **float**          | [**VarCyFromR4**](varcyfromr4.md)     |
| **double**         | [**VarCyFromR8**](varcyfromr8.md)     |
| **DECIMAL**        | [**VarCyFromDec**](varcyfromdec.md)   |
| **DATE**           | [**VarCyFromDate**](varcyfromdate.md) |
| **OLECHAR \***     | [**VarCyFromStr**](varcyfromstr.md)   |
| **IDispatch \***   | [**VarCyFromDisp**](varcyfromdisp.md) |
| **BOOL**           | [**VarCyFromBool**](varcyfrombool.md) |



 

## Functions to convert to type BSTR



| From type          | Function                                   |
|--------------------|--------------------------------------------|
| **unsigned short** | [**VarBstrFromUI2**](varbstrfromui2.md)   |
| **unsigned long**  | [**VarBstrFromUI4**](varbstrfromui4.md)   |
| **ULONG64**        | [**VarBstrFromUI8**](varbstrfromui8.md)   |
| **char**           | [**VarBstrFromI1**](varbstrfromi1.md)     |
| **unsigned char**  | [**VarBstrFromUI1**](varbstrfromui1.md)   |
| **short**          | [**VarBstrFromI2**](varbstrfromi2.md)     |
| **long**           | [**VarBstrFromI4**](varbstrfromi4.md)     |
| **LONG64**         | [**VarBstrFromI8**](varbstrfromi8.md)     |
| **float**          | [**VarBstrFromR4**](varbstrfromr4.md)     |
| **double**         | [**VarBstrFromR8**](varbstrfromr8.md)     |
| **CURRENCY**       | [**VarBstrFromCy**](varbstrfromcy.md)     |
| **DECIMAL**        | [**VarBstrFromDec**](varbstrfromdec.md)   |
| **DATE**           | [**VarBstrFromDate**](varbstrfromdate.md) |
| **IDispatch \***   | [**VarBstrFromDisp**](varbstrfromdisp.md) |
| **BOOL**           | [**VarBstrFromBool**](varbstrfrombool.md) |



 

## Functions to convert to type BOOL



| From type          | Function                                   |
|--------------------|--------------------------------------------|
| **unsigned short** | [**VarBoolFromUI2**](varboolfromui2.md)   |
| **unsigned long**  | [**VarBoolFromUI4**](varboolfromui4.md)   |
| **ULONG64**        | [**VarBoolFromUI8**](varboolfromui8.md)   |
| **char**           | [**VarBoolFromI1**](varboolfromi1.md)     |
| **unsigned char**  | [**VarBoolFromUI1**](varboolfromui1.md)   |
| **short**          | [**VarBoolFromI2**](varboolfromi2.md)     |
| **long**           | [**VarBoolFromI4**](varboolfromi4.md)     |
| **LONG64**         | [**VarBoolFromI8**](varboolfromi8.md)     |
| **float**          | [**VarBoolFromR4**](varboolfromr4.md)     |
| **double**         | [**VarBoolFromR8**](varboolfromr8.md)     |
| **CURRENCY**       | [**VarBoolFromCy**](varboolfromcy.md)     |
| **DECIMAL**        | [**VarBoolFromDec**](varboolfromdec.md)   |
| **DATE**           | [**VarBoolFromDate**](varboolfromdate.md) |
| **OLECHAR \***     | [**VarBoolFromStr**](varboolfromstr.md)   |
| **IDispatch \***   | [**VarBoolFromDisp**](varboolfromdisp.md) |



 

## Functions to convert to type DECIMAL



| From type          | Function                                 |
|--------------------|------------------------------------------|
| **unsigned short** | [**VarDecFromUI2**](vardecfromui2.md)   |
| **unsigned long**  | [**VarDecFromUI4**](vardecfromui4.md)   |
| **ULONG64**        | [**VarDecFromUI8**](vardecfromui8.md)   |
| **char**           | [**VarDecFromI1**](vardecfromi1.md)     |
| **usigned char**   | [**VarDecFromUI1**](vardecfromui1.md)   |
| **short**          | [**VarDecFromI2**](vardecfromi2.md)     |
| **long**           | [**VarDecFromI4**](vardecfromi4.md)     |
| **LONG64**         | [**VarDecFromI8**](vardecfromi8.md)     |
| **float**          | [**VarDecFromR4**](vardecfromr4.md)     |
| **double**         | [**VarDecFromR8**](vardecfromr8.md)     |
| **CURRENCY**       | [**VarDecFromCy**](vardecfromcy.md)     |
| **DATE**           | [**VarDecFromDate**](vardecfromdate.md) |
| **OLECHAR \***     | [**VarDecFromStr**](vardecfromstr.md)   |
| **IDispatch \***   | [**VarDecFromDisp**](vardecfromdisp.md) |
| **BOOL**           | [**VarDecFromBool**](vardecfrombool.md) |



 

> [!Note]  
> If these functions are passed NULL pointers, there will be an access violation and the program will crash. It is your responsibility to protect these functions against NULL pointers.

 

## Related topics

<dl> <dt>

[Conversion and Manipulation Functions](conversion-and-manipulation-functions.md)
</dt> </dl>

 

 




