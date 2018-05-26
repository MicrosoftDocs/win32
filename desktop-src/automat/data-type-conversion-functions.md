---
title: Data Type Conversion Functions
description: The following low-level functions convert variant data types. Higher-level variant manipulation functions (such as VariantChangeType) use these functions, but they can also be called directly.
ms.assetid: b69504cf-6c80-4de1-a26e-9281ab848c71
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Data Type Conversion Functions

The following low-level functions convert variant data types. Higher-level variant manipulation functions (such as [**VariantChangeType**](/windows/previous-versions/OleAuto/nf-oleauto-variantchangetype?branch=master)) use these functions, but they can also be called directly.

## Functions to convert to type char



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned char**  | [**VarI1FromUI1**](/windows/previous-versions/OleAuto/nf-oleauto-vari1fromui1?branch=master)   |
| **unsigned short** | [**VarI1FromUI2**](/windows/previous-versions/OleAuto/nf-oleauto-vari1fromui2?branch=master)   |
| **unsigned long**  | [**VarI1FromUI4**](/windows/previous-versions/OleAuto/nf-oleauto-vari1fromui4?branch=master)   |
| **ULONG64**        | [**VarI1FromUI8**](/windows/previous-versions/OleAuto/nf-oleauto-vari1fromui8?branch=master)   |
| **short**          | [**VarI1FromI2**](/windows/previous-versions/OleAuto/nf-oleauto-vari1fromi2?branch=master)     |
| **long**           | [**VarI1FromI4**](/windows/previous-versions/OleAuto/nf-oleauto-vari1fromi4?branch=master)     |
| **LONG64**         | [**VarI1FromI8**](/windows/previous-versions/OleAuto/nf-oleauto-vari1fromi8?branch=master)     |
| **float**          | [**VarI1FromR4**](/windows/previous-versions/OleAuto/nf-oleauto-vari1fromr4?branch=master)     |
| **double**         | [**VarI1FromR8**](/windows/previous-versions/OleAuto/nf-oleauto-vari1fromr8?branch=master)     |
| **CURRENCY**       | [**VarI1FromCy**](/windows/previous-versions/OleAuto/nf-oleauto-vari1fromcy?branch=master)     |
| **DECIMAL**        | [**VarI1FromDec**](/windows/previous-versions/OleAuto/nf-oleauto-vari1fromdec?branch=master)   |
| **DATE**           | [**VarI1FromDate**](/windows/previous-versions/OleAuto/nf-oleauto-vari1fromdate?branch=master) |
| **OLECHAR \***     | [**VarI1FromStr**](/windows/previous-versions/OleAuto/nf-oleauto-vari1fromstr?branch=master)   |
| **IDispatch \***   | [**VarI1FromDisp**](/windows/previous-versions/OleAuto/nf-oleauto-vari1fromdisp?branch=master) |
| **BOOL**           | [**VarI1FromBool**](/windows/previous-versions/OleAuto/nf-oleauto-vari1frombool?branch=master) |



 

## Functions to convert to type unsigned char



| From type          | Function                                 |
|--------------------|------------------------------------------|
| **unsigned short** | [**VarUI1FromUI2**](/windows/previous-versions/OleAuto/nf-oleauto-varui1fromui2?branch=master)   |
| **unsigned long**  | [**VarUI1FromUI4**](/windows/previous-versions/OleAuto/nf-oleauto-varui1fromui4?branch=master)   |
| **ULONG64**        | [**VarI1FromUI8**](/windows/previous-versions/OleAuto/nf-oleauto-vari1fromui8?branch=master)     |
| **char**           | [**VarUI1FromI1**](/windows/previous-versions/OleAuto/nf-oleauto-varui1fromi1?branch=master)     |
| **short**          | [**VarUI1FromI2**](/windows/previous-versions/OleAuto/nf-oleauto-varui1fromi2?branch=master)     |
| **long**           | [**VarUI1FromI4**](/windows/previous-versions/OleAuto/nf-oleauto-varui1fromi4?branch=master)     |
| **LONG64**         | [**VarUI1FromI8**](/windows/previous-versions/OleAuto/nf-oleauto-varui1fromi8?branch=master)     |
| **float**          | [**VarUI1FromR4**](/windows/previous-versions/OleAuto/nf-oleauto-varui1fromr4?branch=master)     |
| **double**         | [**VarUI1FromR8**](/windows/previous-versions/OleAuto/nf-oleauto-varui1fromr8?branch=master)     |
| **CURRENCY**       | [**VarUI1FromCy**](/windows/previous-versions/OleAuto/nf-oleauto-varui1fromcy?branch=master)     |
| **DECIMAL**        | [**VarUI1FromDec**](/windows/previous-versions/OleAuto/nf-oleauto-varui1fromdec?branch=master)   |
| **DATE**           | [**VarUI1FromDate**](/windows/previous-versions/OleAuto/nf-oleauto-varui1fromdate?branch=master) |
| **OLECHAR \***     | [**VarUI1FromStr**](/windows/previous-versions/OleAuto/nf-oleauto-varui1fromstr?branch=master)   |
| **IDispatch \***   | [**VarUI1FromDisp**](/windows/previous-versions/OleAuto/nf-oleauto-varui1fromdisp?branch=master) |
| **BOOL**           | [**VarUI1FromBool**](/windows/previous-versions/OleAuto/nf-oleauto-varui1frombool?branch=master) |



 

## Functions to convert to type short



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned char**  | [**VarI2FromUI1**](/windows/previous-versions/OleAuto/nf-oleauto-vari2fromui1?branch=master)   |
| **unsigned short** | [**VarI2FromUI2**](/windows/previous-versions/OleAuto/nf-oleauto-vari2fromui2?branch=master)   |
| **unsigned long**  | [**VarI2FromUI4**](/windows/previous-versions/OleAuto/nf-oleauto-vari2fromui4?branch=master)   |
| **ULONG64**        | [**VarI2FromUI8**](/windows/previous-versions/OleAuto/nf-oleauto-vari2fromui8?branch=master)   |
| **char**           | [**VarI2FromI1**](/windows/previous-versions/OleAuto/nf-oleauto-vari2fromi1?branch=master)     |
| **long**           | [**VarI2FromI4**](/windows/previous-versions/OleAuto/nf-oleauto-vari2fromi4?branch=master)     |
| **LONG64**         | [**VarI2FromI8**](/windows/previous-versions/OleAuto/nf-oleauto-vari2fromi8?branch=master)     |
| **float**          | [**VarI2FromR4**](/windows/previous-versions/OleAuto/nf-oleauto-vari2fromr4?branch=master)     |
| **double**         | [**VarI2FromR8**](/windows/previous-versions/OleAuto/nf-oleauto-vari2fromr8?branch=master)     |
| **CURRENCY**       | [**VarI2FromCy**](/windows/previous-versions/OleAuto/nf-oleauto-vari2fromcy?branch=master)     |
| **DECIMAL**        | [**VarI2FromDec**](/windows/previous-versions/OleAuto/nf-oleauto-vari2fromdec?branch=master)   |
| **DATE**           | [**VarI2FromDate**](/windows/previous-versions/OleAuto/nf-oleauto-vari2fromdate?branch=master) |
| **OLECHAR \***     | [**VarI2FromStr**](/windows/previous-versions/OleAuto/nf-oleauto-vari2fromstr?branch=master)   |
| **IDispatch \***   | [**VarI2FromDisp**](/windows/previous-versions/OleAuto/nf-oleauto-vari2fromdisp?branch=master) |
| **BOOL**           | [**VarI2FromBool**](/windows/previous-versions/OleAuto/nf-oleauto-vari2frombool?branch=master) |



 

## Functions to convert to type unsigned short



| From type         | Function                                 |
|-------------------|------------------------------------------|
| **char**          | [**VarUI2FromI1**](/windows/previous-versions/OleAuto/nf-oleauto-varui2fromi1?branch=master)     |
| **short**         | [**VarUI2FromI2**](/windows/previous-versions/OleAuto/nf-oleauto-varui2fromi2?branch=master)     |
| **long**          | [**VarUI2FromI4**](/windows/previous-versions/OleAuto/nf-oleauto-varui2fromi4?branch=master)     |
| **LONG64**        | [**VarUI2FromI8**](/windows/previous-versions/OleAuto/nf-oleauto-varui2fromi8?branch=master)     |
| **unsigned char** | [**VarUI2FromUI1**](/windows/previous-versions/OleAuto/nf-oleauto-varui2fromui1?branch=master)   |
| **unsigned long** | [**VarUI2FromUI4**](/windows/previous-versions/OleAuto/nf-oleauto-varui2fromui4?branch=master)   |
| **LONG64**        | [**VarUI2FromUI8**](/windows/previous-versions/OleAuto/nf-oleauto-varui2fromui8?branch=master)   |
| **float**         | [**VarUI2FromR4**](/windows/previous-versions/OleAuto/nf-oleauto-varui2fromr4?branch=master)     |
| **double**        | [**VarUI2FromR8**](/windows/previous-versions/OleAuto/nf-oleauto-varui2fromr8?branch=master)     |
| **CURRENCY**      | [**VarUI2FromCy**](/windows/previous-versions/OleAuto/nf-oleauto-varui2fromcy?branch=master)     |
| **DECIMAL**       | [**VarUI2FromDec**](/windows/previous-versions/OleAuto/nf-oleauto-varui2fromdec?branch=master)   |
| **DATE**          | [**VarUI2FromDate**](/windows/previous-versions/OleAuto/nf-oleauto-varui2fromdate?branch=master) |
| **OLECHAR \***    | [**VarUI2FromStr**](/windows/previous-versions/OleAuto/nf-oleauto-varui2fromstr?branch=master)   |
| **IDispatch \***  | [**VarUI2FromDisp**](/windows/previous-versions/OleAuto/nf-oleauto-varui2fromdisp?branch=master) |
| **BOOL**          | [**VarUI2FromBool**](/windows/previous-versions/OleAuto/nf-oleauto-varui2frombool?branch=master) |



 

## Functions to convert to type long



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned short** | [**VarI4FromUI2**](/windows/previous-versions/OleAuto/nf-oleauto-vari4fromui2?branch=master)   |
| **unsigned long**  | [**VarI4FromUI4**](/windows/previous-versions/OleAuto/nf-oleauto-vari4fromui4?branch=master)   |
| **ULONG64**        | [**VarI4FromUI8**](/windows/previous-versions/OleAuto/nf-oleauto-vari4fromui8?branch=master)   |
| **char**           | [**VarI4FromI1**](/windows/previous-versions/OleAuto/nf-oleauto-vari4fromi1?branch=master)     |
| **unsigned char**  | [**VarI4FromUI1**](/windows/previous-versions/OleAuto/nf-oleauto-vari4fromui1?branch=master)   |
| **short**          | [**VarI4FromI2**](/windows/previous-versions/OleAuto/nf-oleauto-vari4fromi2?branch=master)     |
| **LONG64**         | [**VarI4FromI8**](/windows/previous-versions/OleAuto/nf-oleauto-vari4fromi8?branch=master)     |
| **float**          | [**VarI4FromR4**](/windows/previous-versions/OleAuto/nf-oleauto-vari4fromr4?branch=master)     |
| **double**         | [**VarI4FromR8**](/windows/previous-versions/OleAuto/nf-oleauto-vari4fromr8?branch=master)     |
| **CURRENCY**       | [**VarI4FromCy**](/windows/previous-versions/OleAuto/nf-oleauto-vari4fromcy?branch=master)     |
| **DECIMAL**        | [**VarI4FromDec**](/windows/previous-versions/OleAuto/nf-oleauto-vari4fromdec?branch=master)   |
| **DATE**           | [**VarI4FromDate**](/windows/previous-versions/OleAuto/nf-oleauto-vari4fromdate?branch=master) |
| **OLECHAR \***     | [**VarI4FromStr**](/windows/previous-versions/OleAuto/nf-oleauto-vari4fromstr?branch=master)   |
| **IDispatch \***   | [**VarI4FromDisp**](/windows/previous-versions/OleAuto/nf-oleauto-vari4fromdisp?branch=master) |
| **BOOL**           | [**VarI4FromBool**](/windows/previous-versions/OleAuto/nf-oleauto-vari4frombool?branch=master) |
| **INT**            | [**VarI4FromInt**](/windows/previous-versions/OleAuto/nf-oleauto-vari4fromi4?branch=master)   |



 

## Functions to convert to type unsigned long



| From type          | Function                                 |
|--------------------|------------------------------------------|
| **unsigned short** | [**VarUI4FromUI2**](/windows/previous-versions/OleAuto/nf-oleauto-varui4fromui2?branch=master)   |
| **char**           | [**VarUI4FromI1**](/windows/previous-versions/OleAuto/nf-oleauto-varui4fromi1?branch=master)     |
| **short**          | [**VarUI4FromI2**](/windows/previous-versions/OleAuto/nf-oleauto-varui4fromi2?branch=master)     |
| **unsigned char**  | [**VarUI4FromUI1**](/windows/previous-versions/OleAuto/nf-oleauto-varui4fromui1?branch=master)   |
| **ULONG64**        | [**VarUI4FromUI8**](/windows/previous-versions/OleAuto/nf-oleauto-varui4fromui8?branch=master)   |
| **long**           | [**VarUI4FromI4**](/windows/previous-versions/OleAuto/nf-oleauto-varui4fromi4?branch=master)     |
| **LONG64**         | [**VarUI4FromI8**](/windows/previous-versions/OleAuto/nf-oleauto-varui4fromi8?branch=master)     |
| **float**          | [**VarUI4FromR4**](/windows/previous-versions/OleAuto/nf-oleauto-varui4fromr4?branch=master)     |
| **double**         | [**VarUI4FromR8**](/windows/previous-versions/OleAuto/nf-oleauto-varui4fromr8?branch=master)     |
| **CURRENCY**       | [**VarUI4FromCy**](/windows/previous-versions/OleAuto/nf-oleauto-varui4fromcy?branch=master)     |
| **DECIMAL**        | [**VarUI4FromDec**](/windows/previous-versions/OleAuto/nf-oleauto-varui4fromdec?branch=master)   |
| **DATE**           | [**VarUI4FromDate**](/windows/previous-versions/OleAuto/nf-oleauto-varui4fromdate?branch=master) |
| **OLECHAR \***     | [**VarUI4FromStr**](/windows/previous-versions/OleAuto/nf-oleauto-varui4fromstr?branch=master)   |
| **IDispatch \***   | [**VarUI4FromDisp**](/windows/previous-versions/OleAuto/nf-oleauto-varui4fromdisp?branch=master) |
| **BOOL**           | [**VarUI4FromBool**](/windows/previous-versions/OleAuto/nf-oleauto-varui4frombool?branch=master) |



 

## Functions to convert to type float



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned short** | [**VarR4FromUI2**](/windows/previous-versions/OleAuto/nf-oleauto-varr4fromui2?branch=master)   |
| **unsigned long**  | [**VarR4FromUI4**](/windows/previous-versions/OleAuto/nf-oleauto-varr4fromui4?branch=master)   |
| **ULONG64**        | [**VarR4FromUI8**](/windows/previous-versions/OleAuto/nf-oleauto-varr4fromui8?branch=master)   |
| **char**           | [**VarR4FromI1**](/windows/previous-versions/OleAuto/nf-oleauto-varr4fromi1?branch=master)     |
| **unsigned char**  | [**VarR4FromUI1**](/windows/previous-versions/OleAuto/nf-oleauto-varr4fromui1?branch=master)   |
| **short**          | [**VarR4FromI2**](/windows/previous-versions/OleAuto/nf-oleauto-varr4fromi2?branch=master)     |
| **long**           | [**VarR4FromI4**](/windows/previous-versions/OleAuto/nf-oleauto-varr4fromi4?branch=master)     |
| **LONG64**         | [**VarR4FromI8**](/windows/previous-versions/OleAuto/nf-oleauto-varr4fromi8?branch=master)     |
| **double**         | [**VarR4FromR8**](/windows/previous-versions/OleAuto/nf-oleauto-varr4fromr8?branch=master)     |
| **CURRENCY**       | [**VarR4FromCy**](/windows/previous-versions/OleAuto/nf-oleauto-varr4fromcy?branch=master)     |
| **DECIMAL**        | [**VarR4FromDec**](/windows/previous-versions/OleAuto/nf-oleauto-varr4fromdec?branch=master)   |
| **DATE**           | [**VarR4FromDate**](/windows/previous-versions/OleAuto/nf-oleauto-varr4fromdate?branch=master) |
| **OLECHAR \***     | [**VarR4FromStr**](/windows/previous-versions/OleAuto/nf-oleauto-varr4fromstr?branch=master)   |
| **IDispatch \***   | [**VarR4FromDisp**](/windows/previous-versions/OleAuto/nf-oleauto-varr4fromdisp?branch=master) |
| **BOOL**           | [**VarR4FromBool**](/windows/previous-versions/OleAuto/nf-oleauto-varr4frombool?branch=master) |



 

## Functions to convert to type double



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned short** | [**VarR8FromUI2**](/windows/previous-versions/OleAuto/nf-oleauto-varr8fromui2?branch=master)   |
| **unsigned long**  | [**VarR8FromUI4**](/windows/previous-versions/OleAuto/nf-oleauto-varr8fromui4?branch=master)   |
| **ULONG64**        | [**VarR8FromUI8**](/windows/previous-versions/OleAuto/nf-oleauto-varr8fromui8?branch=master)   |
| **char**           | [**VarR8FromI1**](/windows/previous-versions/OleAuto/nf-oleauto-varr8fromi1?branch=master)     |
| **unsigned char**  | [**VarR8FromUI1**](/windows/previous-versions/OleAuto/nf-oleauto-varr8fromui1?branch=master)   |
| **short**          | [**VarR8FromI2**](/windows/previous-versions/OleAuto/nf-oleauto-varr8fromi2?branch=master)     |
| **long**           | [**VarR8FromI4**](/windows/previous-versions/OleAuto/nf-oleauto-varr8fromi4?branch=master)     |
| **LONG64**         | [**VarR8FromI8**](/windows/previous-versions/OleAuto/nf-oleauto-varr8fromi8?branch=master)     |
| **float**          | [**VarR8FromR4**](/windows/previous-versions/OleAuto/nf-oleauto-varr8fromr4?branch=master)     |
| **CURRENCY**       | [**VarR8FromCy**](/windows/previous-versions/OleAuto/nf-oleauto-varr8fromcy?branch=master)     |
| **DECIMAL**        | [**VarR8FromDec**](/windows/previous-versions/OleAuto/nf-oleauto-varr8fromdec?branch=master)   |
| **DATE**           | [**VarR8FromDate**](/windows/previous-versions/OleAuto/nf-oleauto-varr8fromdate?branch=master) |
| **OLECHAR \***     | [**VarR8FromStr**](/windows/previous-versions/OleAuto/nf-oleauto-varr8fromstr?branch=master)   |
| **IDispatch \***   | [**VarR8FromDisp**](/windows/previous-versions/OleAuto/nf-oleauto-varr8fromdisp?branch=master) |
| **BOOL**           | [**VarR8FromBool**](/windows/previous-versions/OleAuto/nf-oleauto-varr8frombool?branch=master) |



 

## Functions to convert to type DATE



| From type          | Function                                   |
|--------------------|--------------------------------------------|
| **unsigned short** | [**VarDateFromUI2**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromui2?branch=master)   |
| **unsigned long**  | [**VarDateFromUI4**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromui4?branch=master)   |
| **ULONG64**        | [**VarDateFromUI8**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromui8?branch=master)   |
| **char**           | [**VarDateFromI1**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromi1?branch=master)     |
| **unsigned char**  | [**VarDateFromUI1**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromui1?branch=master)   |
| **short**          | [**VarDateFromI2**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromi2?branch=master)     |
| **long**           | [**VarDateFromI4**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromi4?branch=master)     |
| **LONG64**         | [**VarDateFromI8**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromi8?branch=master)     |
| **float**          | [**VarDateFromR4**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromr4?branch=master)     |
| **double**         | [**VarDateFromR8**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromr8?branch=master)     |
| **CURRENCY**       | [**VarDateFromCy**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromcy?branch=master)     |
| **DECIMAL**        | [**VarDateFromDec**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromdec?branch=master)   |
| **OLECHAR \***     | [**VarDateFromStr**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromstr?branch=master)   |
| **IDispatch \***   | [**VarDateFromDisp**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromdisp?branch=master) |
| **BOOL**           | [**VarDateFromBool**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefrombool?branch=master) |



 

## Functions to convert to type CURRENCY



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned short** | [**VarCyFromUI2**](/windows/previous-versions/OleAuto/nf-oleauto-varcyfromui2?branch=master)   |
| **unsigned long**  | [**VarCyFromUI4**](/windows/previous-versions/OleAuto/nf-oleauto-varcyfromui4?branch=master)   |
| **ULONG64**        | [**VarCyFromUI8**](/windows/previous-versions/OleAuto/nf-oleauto-varcyfromui8?branch=master)   |
| **char**           | [**VarCyFromI1**](/windows/previous-versions/OleAuto/nf-oleauto-varcyfromi1?branch=master)     |
| **unsigned char**  | [**VarCyFromUI1**](/windows/previous-versions/OleAuto/nf-oleauto-varcyfromui1?branch=master)   |
| **short**          | [**VarCyFromI2**](/windows/previous-versions/OleAuto/nf-oleauto-varcyfromi2?branch=master)     |
| **long**           | [**VarCyFromI4**](/windows/previous-versions/OleAuto/nf-oleauto-varcyfromi4?branch=master)     |
| **LONG64**         | [**VarCyFromI8**](/windows/previous-versions/OleAuto/nf-oleauto-varcyfromi8?branch=master)     |
| **float**          | [**VarCyFromR4**](/windows/previous-versions/OleAuto/nf-oleauto-varcyfromr4?branch=master)     |
| **double**         | [**VarCyFromR8**](/windows/previous-versions/OleAuto/nf-oleauto-varcyfromr8?branch=master)     |
| **DECIMAL**        | [**VarCyFromDec**](/windows/previous-versions/OleAuto/nf-oleauto-varcyfromdec?branch=master)   |
| **DATE**           | [**VarCyFromDate**](/windows/previous-versions/OleAuto/nf-oleauto-varcyfromdate?branch=master) |
| **OLECHAR \***     | [**VarCyFromStr**](/windows/previous-versions/OleAuto/nf-oleauto-varcyfromstr?branch=master)   |
| **IDispatch \***   | [**VarCyFromDisp**](/windows/previous-versions/OleAuto/nf-oleauto-varcyfromdisp?branch=master) |
| **BOOL**           | [**VarCyFromBool**](/windows/previous-versions/OleAuto/nf-oleauto-varcyfrombool?branch=master) |



 

## Functions to convert to type BSTR



| From type          | Function                                   |
|--------------------|--------------------------------------------|
| **unsigned short** | [**VarBstrFromUI2**](/windows/previous-versions/OleAuto/nf-oleauto-varbstrfromui2?branch=master)   |
| **unsigned long**  | [**VarBstrFromUI4**](/windows/previous-versions/OleAuto/nf-oleauto-varbstrfromui4?branch=master)   |
| **ULONG64**        | [**VarBstrFromUI8**](/windows/previous-versions/OleAuto/nf-oleauto-varbstrfromui8?branch=master)   |
| **char**           | [**VarBstrFromI1**](/windows/previous-versions/OleAuto/nf-oleauto-varbstrfromi1?branch=master)     |
| **unsigned char**  | [**VarBstrFromUI1**](/windows/previous-versions/OleAuto/nf-oleauto-varbstrfromui1?branch=master)   |
| **short**          | [**VarBstrFromI2**](/windows/previous-versions/OleAuto/nf-oleauto-varbstrfromi2?branch=master)     |
| **long**           | [**VarBstrFromI4**](/windows/previous-versions/OleAuto/nf-oleauto-varbstrfromi4?branch=master)     |
| **LONG64**         | [**VarBstrFromI8**](/windows/previous-versions/OleAuto/nf-oleauto-varbstrfromi8?branch=master)     |
| **float**          | [**VarBstrFromR4**](/windows/previous-versions/OleAuto/nf-oleauto-varbstrfromr4?branch=master)     |
| **double**         | [**VarBstrFromR8**](/windows/previous-versions/OleAuto/nf-oleauto-varbstrfromr8?branch=master)     |
| **CURRENCY**       | [**VarBstrFromCy**](/windows/previous-versions/OleAuto/nf-oleauto-varbstrfromcy?branch=master)     |
| **DECIMAL**        | [**VarBstrFromDec**](/windows/previous-versions/OleAuto/nf-oleauto-varbstrfromdec?branch=master)   |
| **DATE**           | [**VarBstrFromDate**](/windows/previous-versions/OleAuto/nf-oleauto-varbstrfromdate?branch=master) |
| **IDispatch \***   | [**VarBstrFromDisp**](/windows/previous-versions/OleAuto/nf-oleauto-varbstrfromdisp?branch=master) |
| **BOOL**           | [**VarBstrFromBool**](/windows/previous-versions/OleAuto/nf-oleauto-varbstrfrombool?branch=master) |



 

## Functions to convert to type BOOL



| From type          | Function                                   |
|--------------------|--------------------------------------------|
| **unsigned short** | [**VarBoolFromUI2**](/windows/previous-versions/OleAuto/nf-oleauto-varboolfromui2?branch=master)   |
| **unsigned long**  | [**VarBoolFromUI4**](/windows/previous-versions/OleAuto/nf-oleauto-varboolfromui4?branch=master)   |
| **ULONG64**        | [**VarBoolFromUI8**](/windows/previous-versions/OleAuto/nf-oleauto-varboolfromui8?branch=master)   |
| **char**           | [**VarBoolFromI1**](/windows/previous-versions/OleAuto/nf-oleauto-varboolfromi1?branch=master)     |
| **unsigned char**  | [**VarBoolFromUI1**](/windows/previous-versions/OleAuto/nf-oleauto-varboolfromui1?branch=master)   |
| **short**          | [**VarBoolFromI2**](/windows/previous-versions/OleAuto/nf-oleauto-varboolfromi2?branch=master)     |
| **long**           | [**VarBoolFromI4**](/windows/previous-versions/OleAuto/nf-oleauto-varboolfromi4?branch=master)     |
| **LONG64**         | [**VarBoolFromI8**](/windows/previous-versions/OleAuto/nf-oleauto-varboolfromi8?branch=master)     |
| **float**          | [**VarBoolFromR4**](/windows/previous-versions/OleAuto/nf-oleauto-varboolfromr4?branch=master)     |
| **double**         | [**VarBoolFromR8**](/windows/previous-versions/OleAuto/nf-oleauto-varboolfromr8?branch=master)     |
| **CURRENCY**       | [**VarBoolFromCy**](/windows/previous-versions/OleAuto/nf-oleauto-varboolfromcy?branch=master)     |
| **DECIMAL**        | [**VarBoolFromDec**](/windows/previous-versions/OleAuto/nf-oleauto-varboolfromdec?branch=master)   |
| **DATE**           | [**VarBoolFromDate**](/windows/previous-versions/OleAuto/nf-oleauto-varboolfromdate?branch=master) |
| **OLECHAR \***     | [**VarBoolFromStr**](/windows/previous-versions/OleAuto/nf-oleauto-varboolfromstr?branch=master)   |
| **IDispatch \***   | [**VarBoolFromDisp**](/windows/previous-versions/OleAuto/nf-oleauto-varboolfromdisp?branch=master) |



 

## Functions to convert to type DECIMAL



| From type          | Function                                 |
|--------------------|------------------------------------------|
| **unsigned short** | [**VarDecFromUI2**](/windows/previous-versions/OleAuto/nf-oleauto-vardecfromui2?branch=master)   |
| **unsigned long**  | [**VarDecFromUI4**](/windows/previous-versions/OleAuto/nf-oleauto-vardecfromui4?branch=master)   |
| **ULONG64**        | [**VarDecFromUI8**](/windows/previous-versions/OleAuto/nf-oleauto-vardecfromui8?branch=master)   |
| **char**           | [**VarDecFromI1**](/windows/previous-versions/OleAuto/nf-oleauto-vardecfromi1?branch=master)     |
| **usigned char**   | [**VarDecFromUI1**](/windows/previous-versions/OleAuto/nf-oleauto-vardecfromui1?branch=master)   |
| **short**          | [**VarDecFromI2**](/windows/previous-versions/OleAuto/nf-oleauto-vardecfromi2?branch=master)     |
| **long**           | [**VarDecFromI4**](/windows/previous-versions/OleAuto/nf-oleauto-vardecfromi4?branch=master)     |
| **LONG64**         | [**VarDecFromI8**](/windows/previous-versions/OleAuto/nf-oleauto-vardecfromi8?branch=master)     |
| **float**          | [**VarDecFromR4**](/windows/previous-versions/OleAuto/nf-oleauto-vardecfromr4?branch=master)     |
| **double**         | [**VarDecFromR8**](/windows/previous-versions/OleAuto/nf-oleauto-vardecfromr8?branch=master)     |
| **CURRENCY**       | [**VarDecFromCy**](/windows/previous-versions/OleAuto/nf-oleauto-vardecfromcy?branch=master)     |
| **DATE**           | [**VarDecFromDate**](/windows/previous-versions/OleAuto/nf-oleauto-vardecfromdate?branch=master) |
| **OLECHAR \***     | [**VarDecFromStr**](/windows/previous-versions/OleAuto/nf-oleauto-vardecfromstr?branch=master)   |
| **IDispatch \***   | [**VarDecFromDisp**](/windows/previous-versions/OleAuto/nf-oleauto-vardecfromdisp?branch=master) |
| **BOOL**           | [**VarDecFromBool**](/windows/previous-versions/OleAuto/nf-oleauto-vardecfrombool?branch=master) |



 

> [!Note]  
> If these functions are passed NULL pointers, there will be an access violation and the program will crash. It is your responsibility to protect these functions against NULL pointers.

 

## Related topics

<dl> <dt>

[Conversion and Manipulation Functions](conversion-and-manipulation-functions.md)
</dt> </dl>

 

 




