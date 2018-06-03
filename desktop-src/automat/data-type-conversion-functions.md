---
title: Data Type Conversion Functions
description: The following low-level functions convert variant data types. Higher-level variant manipulation functions (such as VariantChangeType) use these functions, but they can also be called directly.
ms.assetid: b69504cf-6c80-4de1-a26e-9281ab848c71
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Data Type Conversion Functions

The following low-level functions convert variant data types. Higher-level variant manipulation functions (such as [**VariantChangeType**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-variantchangetype)) use these functions, but they can also be called directly.

## Functions to convert to type char



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned char**  | [**VarI1FromUI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1fromui1)   |
| **unsigned short** | [**VarI1FromUI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1fromui2)   |
| **unsigned long**  | [**VarI1FromUI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1fromui4)   |
| **ULONG64**        | [**VarI1FromUI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1fromui8)   |
| **short**          | [**VarI1FromI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1fromi2)     |
| **long**           | [**VarI1FromI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1fromi4)     |
| **LONG64**         | [**VarI1FromI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1fromi8)     |
| **float**          | [**VarI1FromR4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1fromr4)     |
| **double**         | [**VarI1FromR8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1fromr8)     |
| **CURRENCY**       | [**VarI1FromCy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1fromcy)     |
| **DECIMAL**        | [**VarI1FromDec**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1fromdec)   |
| **DATE**           | [**VarI1FromDate**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1fromdate) |
| **OLECHAR \***     | [**VarI1FromStr**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1fromstr)   |
| **IDispatch \***   | [**VarI1FromDisp**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1fromdisp) |
| **BOOL**           | [**VarI1FromBool**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1frombool) |



 

## Functions to convert to type unsigned char



| From type          | Function                                 |
|--------------------|------------------------------------------|
| **unsigned short** | [**VarUI1FromUI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui1fromui2)   |
| **unsigned long**  | [**VarUI1FromUI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui1fromui4)   |
| **ULONG64**        | [**VarI1FromUI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari1fromui8)     |
| **char**           | [**VarUI1FromI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui1fromi1)     |
| **short**          | [**VarUI1FromI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui1fromi2)     |
| **long**           | [**VarUI1FromI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui1fromi4)     |
| **LONG64**         | [**VarUI1FromI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui1fromi8)     |
| **float**          | [**VarUI1FromR4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui1fromr4)     |
| **double**         | [**VarUI1FromR8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui1fromr8)     |
| **CURRENCY**       | [**VarUI1FromCy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui1fromcy)     |
| **DECIMAL**        | [**VarUI1FromDec**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui1fromdec)   |
| **DATE**           | [**VarUI1FromDate**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui1fromdate) |
| **OLECHAR \***     | [**VarUI1FromStr**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui1fromstr)   |
| **IDispatch \***   | [**VarUI1FromDisp**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui1fromdisp) |
| **BOOL**           | [**VarUI1FromBool**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui1frombool) |



 

## Functions to convert to type short



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned char**  | [**VarI2FromUI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari2fromui1)   |
| **unsigned short** | [**VarI2FromUI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari2fromui2)   |
| **unsigned long**  | [**VarI2FromUI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari2fromui4)   |
| **ULONG64**        | [**VarI2FromUI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari2fromui8)   |
| **char**           | [**VarI2FromI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari2fromi1)     |
| **long**           | [**VarI2FromI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari2fromi4)     |
| **LONG64**         | [**VarI2FromI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari2fromi8)     |
| **float**          | [**VarI2FromR4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari2fromr4)     |
| **double**         | [**VarI2FromR8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari2fromr8)     |
| **CURRENCY**       | [**VarI2FromCy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari2fromcy)     |
| **DECIMAL**        | [**VarI2FromDec**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari2fromdec)   |
| **DATE**           | [**VarI2FromDate**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari2fromdate) |
| **OLECHAR \***     | [**VarI2FromStr**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari2fromstr)   |
| **IDispatch \***   | [**VarI2FromDisp**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari2fromdisp) |
| **BOOL**           | [**VarI2FromBool**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari2frombool) |



 

## Functions to convert to type unsigned short



| From type         | Function                                 |
|-------------------|------------------------------------------|
| **char**          | [**VarUI2FromI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui2fromi1)     |
| **short**         | [**VarUI2FromI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui2fromi2)     |
| **long**          | [**VarUI2FromI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui2fromi4)     |
| **LONG64**        | [**VarUI2FromI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui2fromi8)     |
| **unsigned char** | [**VarUI2FromUI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui2fromui1)   |
| **unsigned long** | [**VarUI2FromUI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui2fromui4)   |
| **LONG64**        | [**VarUI2FromUI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui2fromui8)   |
| **float**         | [**VarUI2FromR4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui2fromr4)     |
| **double**        | [**VarUI2FromR8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui2fromr8)     |
| **CURRENCY**      | [**VarUI2FromCy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui2fromcy)     |
| **DECIMAL**       | [**VarUI2FromDec**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui2fromdec)   |
| **DATE**          | [**VarUI2FromDate**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui2fromdate) |
| **OLECHAR \***    | [**VarUI2FromStr**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui2fromstr)   |
| **IDispatch \***  | [**VarUI2FromDisp**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui2fromdisp) |
| **BOOL**          | [**VarUI2FromBool**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui2frombool) |



 

## Functions to convert to type long



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned short** | [**VarI4FromUI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4fromui2)   |
| **unsigned long**  | [**VarI4FromUI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4fromui4)   |
| **ULONG64**        | [**VarI4FromUI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4fromui8)   |
| **char**           | [**VarI4FromI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4fromi1)     |
| **unsigned char**  | [**VarI4FromUI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4fromui1)   |
| **short**          | [**VarI4FromI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4fromi2)     |
| **LONG64**         | [**VarI4FromI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4fromi8)     |
| **float**          | [**VarI4FromR4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4fromr4)     |
| **double**         | [**VarI4FromR8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4fromr8)     |
| **CURRENCY**       | [**VarI4FromCy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4fromcy)     |
| **DECIMAL**        | [**VarI4FromDec**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4fromdec)   |
| **DATE**           | [**VarI4FromDate**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4fromdate) |
| **OLECHAR \***     | [**VarI4FromStr**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4fromstr)   |
| **IDispatch \***   | [**VarI4FromDisp**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4fromdisp) |
| **BOOL**           | [**VarI4FromBool**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4frombool) |
| **INT**            | [**VarI4FromInt**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vari4fromi4)   |



 

## Functions to convert to type unsigned long



| From type          | Function                                 |
|--------------------|------------------------------------------|
| **unsigned short** | [**VarUI4FromUI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui4fromui2)   |
| **char**           | [**VarUI4FromI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui4fromi1)     |
| **short**          | [**VarUI4FromI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui4fromi2)     |
| **unsigned char**  | [**VarUI4FromUI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui4fromui1)   |
| **ULONG64**        | [**VarUI4FromUI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui4fromui8)   |
| **long**           | [**VarUI4FromI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui4fromi4)     |
| **LONG64**         | [**VarUI4FromI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui4fromi8)     |
| **float**          | [**VarUI4FromR4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui4fromr4)     |
| **double**         | [**VarUI4FromR8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui4fromr8)     |
| **CURRENCY**       | [**VarUI4FromCy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui4fromcy)     |
| **DECIMAL**        | [**VarUI4FromDec**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui4fromdec)   |
| **DATE**           | [**VarUI4FromDate**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui4fromdate) |
| **OLECHAR \***     | [**VarUI4FromStr**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui4fromstr)   |
| **IDispatch \***   | [**VarUI4FromDisp**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui4fromdisp) |
| **BOOL**           | [**VarUI4FromBool**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varui4frombool) |



 

## Functions to convert to type float



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned short** | [**VarR4FromUI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr4fromui2)   |
| **unsigned long**  | [**VarR4FromUI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr4fromui4)   |
| **ULONG64**        | [**VarR4FromUI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr4fromui8)   |
| **char**           | [**VarR4FromI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr4fromi1)     |
| **unsigned char**  | [**VarR4FromUI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr4fromui1)   |
| **short**          | [**VarR4FromI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr4fromi2)     |
| **long**           | [**VarR4FromI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr4fromi4)     |
| **LONG64**         | [**VarR4FromI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr4fromi8)     |
| **double**         | [**VarR4FromR8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr4fromr8)     |
| **CURRENCY**       | [**VarR4FromCy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr4fromcy)     |
| **DECIMAL**        | [**VarR4FromDec**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr4fromdec)   |
| **DATE**           | [**VarR4FromDate**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr4fromdate) |
| **OLECHAR \***     | [**VarR4FromStr**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr4fromstr)   |
| **IDispatch \***   | [**VarR4FromDisp**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr4fromdisp) |
| **BOOL**           | [**VarR4FromBool**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr4frombool) |



 

## Functions to convert to type double



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned short** | [**VarR8FromUI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr8fromui2)   |
| **unsigned long**  | [**VarR8FromUI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr8fromui4)   |
| **ULONG64**        | [**VarR8FromUI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr8fromui8)   |
| **char**           | [**VarR8FromI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr8fromi1)     |
| **unsigned char**  | [**VarR8FromUI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr8fromui1)   |
| **short**          | [**VarR8FromI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr8fromi2)     |
| **long**           | [**VarR8FromI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr8fromi4)     |
| **LONG64**         | [**VarR8FromI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr8fromi8)     |
| **float**          | [**VarR8FromR4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr8fromr4)     |
| **CURRENCY**       | [**VarR8FromCy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr8fromcy)     |
| **DECIMAL**        | [**VarR8FromDec**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr8fromdec)   |
| **DATE**           | [**VarR8FromDate**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr8fromdate) |
| **OLECHAR \***     | [**VarR8FromStr**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr8fromstr)   |
| **IDispatch \***   | [**VarR8FromDisp**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr8fromdisp) |
| **BOOL**           | [**VarR8FromBool**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varr8frombool) |



 

## Functions to convert to type DATE



| From type          | Function                                   |
|--------------------|--------------------------------------------|
| **unsigned short** | [**VarDateFromUI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardatefromui2)   |
| **unsigned long**  | [**VarDateFromUI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardatefromui4)   |
| **ULONG64**        | [**VarDateFromUI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardatefromui8)   |
| **char**           | [**VarDateFromI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardatefromi1)     |
| **unsigned char**  | [**VarDateFromUI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardatefromui1)   |
| **short**          | [**VarDateFromI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardatefromi2)     |
| **long**           | [**VarDateFromI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardatefromi4)     |
| **LONG64**         | [**VarDateFromI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardatefromi8)     |
| **float**          | [**VarDateFromR4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardatefromr4)     |
| **double**         | [**VarDateFromR8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardatefromr8)     |
| **CURRENCY**       | [**VarDateFromCy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardatefromcy)     |
| **DECIMAL**        | [**VarDateFromDec**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardatefromdec)   |
| **OLECHAR \***     | [**VarDateFromStr**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardatefromstr)   |
| **IDispatch \***   | [**VarDateFromDisp**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardatefromdisp) |
| **BOOL**           | [**VarDateFromBool**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardatefrombool) |



 

## Functions to convert to type CURRENCY



| From type          | Function                               |
|--------------------|----------------------------------------|
| **unsigned short** | [**VarCyFromUI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varcyfromui2)   |
| **unsigned long**  | [**VarCyFromUI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varcyfromui4)   |
| **ULONG64**        | [**VarCyFromUI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varcyfromui8)   |
| **char**           | [**VarCyFromI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varcyfromi1)     |
| **unsigned char**  | [**VarCyFromUI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varcyfromui1)   |
| **short**          | [**VarCyFromI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varcyfromi2)     |
| **long**           | [**VarCyFromI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varcyfromi4)     |
| **LONG64**         | [**VarCyFromI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varcyfromi8)     |
| **float**          | [**VarCyFromR4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varcyfromr4)     |
| **double**         | [**VarCyFromR8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varcyfromr8)     |
| **DECIMAL**        | [**VarCyFromDec**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varcyfromdec)   |
| **DATE**           | [**VarCyFromDate**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varcyfromdate) |
| **OLECHAR \***     | [**VarCyFromStr**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varcyfromstr)   |
| **IDispatch \***   | [**VarCyFromDisp**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varcyfromdisp) |
| **BOOL**           | [**VarCyFromBool**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varcyfrombool) |



 

## Functions to convert to type BSTR



| From type          | Function                                   |
|--------------------|--------------------------------------------|
| **unsigned short** | [**VarBstrFromUI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varbstrfromui2)   |
| **unsigned long**  | [**VarBstrFromUI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varbstrfromui4)   |
| **ULONG64**        | [**VarBstrFromUI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varbstrfromui8)   |
| **char**           | [**VarBstrFromI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varbstrfromi1)     |
| **unsigned char**  | [**VarBstrFromUI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varbstrfromui1)   |
| **short**          | [**VarBstrFromI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varbstrfromi2)     |
| **long**           | [**VarBstrFromI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varbstrfromi4)     |
| **LONG64**         | [**VarBstrFromI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varbstrfromi8)     |
| **float**          | [**VarBstrFromR4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varbstrfromr4)     |
| **double**         | [**VarBstrFromR8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varbstrfromr8)     |
| **CURRENCY**       | [**VarBstrFromCy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varbstrfromcy)     |
| **DECIMAL**        | [**VarBstrFromDec**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varbstrfromdec)   |
| **DATE**           | [**VarBstrFromDate**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varbstrfromdate) |
| **IDispatch \***   | [**VarBstrFromDisp**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varbstrfromdisp) |
| **BOOL**           | [**VarBstrFromBool**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varbstrfrombool) |



 

## Functions to convert to type BOOL



| From type          | Function                                   |
|--------------------|--------------------------------------------|
| **unsigned short** | [**VarBoolFromUI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varboolfromui2)   |
| **unsigned long**  | [**VarBoolFromUI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varboolfromui4)   |
| **ULONG64**        | [**VarBoolFromUI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varboolfromui8)   |
| **char**           | [**VarBoolFromI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varboolfromi1)     |
| **unsigned char**  | [**VarBoolFromUI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varboolfromui1)   |
| **short**          | [**VarBoolFromI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varboolfromi2)     |
| **long**           | [**VarBoolFromI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varboolfromi4)     |
| **LONG64**         | [**VarBoolFromI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varboolfromi8)     |
| **float**          | [**VarBoolFromR4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varboolfromr4)     |
| **double**         | [**VarBoolFromR8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varboolfromr8)     |
| **CURRENCY**       | [**VarBoolFromCy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varboolfromcy)     |
| **DECIMAL**        | [**VarBoolFromDec**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varboolfromdec)   |
| **DATE**           | [**VarBoolFromDate**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varboolfromdate) |
| **OLECHAR \***     | [**VarBoolFromStr**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varboolfromstr)   |
| **IDispatch \***   | [**VarBoolFromDisp**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varboolfromdisp) |



 

## Functions to convert to type DECIMAL



| From type          | Function                                 |
|--------------------|------------------------------------------|
| **unsigned short** | [**VarDecFromUI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardecfromui2)   |
| **unsigned long**  | [**VarDecFromUI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardecfromui4)   |
| **ULONG64**        | [**VarDecFromUI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardecfromui8)   |
| **char**           | [**VarDecFromI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardecfromi1)     |
| **usigned char**   | [**VarDecFromUI1**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardecfromui1)   |
| **short**          | [**VarDecFromI2**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardecfromi2)     |
| **long**           | [**VarDecFromI4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardecfromi4)     |
| **LONG64**         | [**VarDecFromI8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardecfromi8)     |
| **float**          | [**VarDecFromR4**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardecfromr4)     |
| **double**         | [**VarDecFromR8**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardecfromr8)     |
| **CURRENCY**       | [**VarDecFromCy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardecfromcy)     |
| **DATE**           | [**VarDecFromDate**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardecfromdate) |
| **OLECHAR \***     | [**VarDecFromStr**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardecfromstr)   |
| **IDispatch \***   | [**VarDecFromDisp**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardecfromdisp) |
| **BOOL**           | [**VarDecFromBool**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vardecfrombool) |



 

> [!Note]  
> If these functions are passed NULL pointers, there will be an access violation and the program will crash. It is your responsibility to protect these functions against NULL pointers.

 

## Related topics

<dl> <dt>

[Conversion and Manipulation Functions](conversion-and-manipulation-functions.md)
</dt> </dl>

 

 




