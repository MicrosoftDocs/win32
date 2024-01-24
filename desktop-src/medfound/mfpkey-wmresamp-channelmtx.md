---
description: Specifies the channel matrix, which is used to convert the source channels into the destination channels (for example, to convert 5.1 to stereo).
ms.assetid: 2f2a82bd-f051-4b05-a9c8-37aa4403fab4
title: MFPKEY_WMRESAMP_CHANNELMTX Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMRESAMP\_CHANNELMTX Property

Specifies the channel matrix, which is used to convert the source channels into the destination channels (for example, to convert 5.1 to stereo).

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

VT\_I4 \| VT\_ARRAY

## Applies To

-   [Audio Resampler DSP](audioresampler.md)

## Remarks

The value of the property is a matrix of Ns x Nd coefficients, where Ns is the number of source channels and Nd is the number of destination channels. Coefficients are specified in decibels using the following formula:

(int)(65536\*20\*log10(dB))

The matrix is stored as an array in row-major order where the row number is the source channel and the column number is the destination channel.

Thus, if the matrix is the following:

``` syntax
00       01       ...      0(Ns-1)
10       11       ...      1(Ns-1)
...      ...      ...      ...
(Nd-1)0 (Nd-1)1 ... (Nd-1)(Ns-1)
```

then you would specify the array as:

``` syntax
[ 00, 01, ..., 0(Ns-1), 10, 11, ..., 1(Ns-1), ..., (Nd-1)0, (Nd-1)1, ..., (Nd-1)(Ns-1) ]
```

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 
