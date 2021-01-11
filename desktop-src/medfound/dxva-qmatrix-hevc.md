---
description: Defines a quantization matrix.
ms.assetid: 44a5c81f-98d8-4b16-a467-433bae781691
title: DXVA_Qmatrix_HEVC structure (Dxva.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DXVA_Qmatrix_HEVC
api_type: 
- HeaderDef
api_location: 
- dxva.h
---

# DXVA\_Qmatrix\_HEVC structure

Defines a quantization matrix.

## Syntax


```C++
typedef struct _DXVA_Qmatrix_HEVC {
  UCHAR ucScalingLists0[6][16];
  UCHAR ucScalingLists1[6][64];
  UCHAR ucScalingLists2[6][64];
  UCHAR ucScalingLists3[2][64];
  UCHAR ucScalingListDCCoefSizeID2[6];
  UCHAR ucScalingListDCCoefSizeID3[2];
} DXVA_Qmatrix_HEVC, *LPDXVA_Qmatrix_HEVC;
```



## Members

<dl> <dt>

**ucScalingLists0\[6\]\[16\]**
</dt> <dd>

Contains the scaling lists for the 4x4 scaling process, corresponding to ScalingList\[ 0 \]\[ MatrixID \]\[ i \] in HEVC specification, where MatrixID is in the range of 0 to 5, inclusive, and i is in the range of 0 to 15, inclusive.

</dd> <dt>

**ucScalingLists1\[6\]\[64\]**
</dt> <dd>

Contains the scaling lists for the 8x8 scaling process, corresponding to ScalingList\[ 1 \]\[ MatrixID \]\[ i \] in HEVC specification, where MatrixID is in the range of 0 to 5, inclusive, and i is in the range of 0 to 63, inclusive.

</dd> <dt>

**ucScalingLists2\[6\]\[64\]**
</dt> <dd>

Contains the scaling lists for the 8x8 scaling process, corresponding to ScalingList\[ 2 \]\[ MatrixID \]\[ i \] in HEVC specification, where MatrixID is in the range of 0 to 5, inclusive, and i is in the range of 0 to 63, inclusive.

</dd> <dt>

**ucScalingLists3\[2\]\[64\]**
</dt> <dd>

Contains the scaling lists for the 8x8 scaling process, corresponding to ScalingList\[ 3 \]\[ MatrixID \]\[ i \] in HEVC specification, where MatrixID is in the range of 0 to 1, inclusive, and i is in the range of 0 to 63, inclusive.

</dd> <dt>

**ucScalingListDCCoefSizeID2**
</dt> <dd>

Contains the DC value of the scaling list for 16x16 size with sizeID equal to 2 and corresponding to scaling\_list\_dc\_coef\_minus8\[ sizeID − 2 \]\[ matrixID \] +8 with sizeID equal to 2 and matrixID in the range of 0 to 5, inclusive, in HEVC specification.

</dd> <dt>

**ucScalingListDCCoefSizeID3**
</dt> <dd>

Contains the DC value of the scaling list for 32x32 size with sizeID equal to 3, and corresponding to scaling\_list\_dc\_coef\_minus8\[ sizeID − 2 \]\[ matrixID \] +8 with sizeID equal to 3 and matrixID in the range of 0 to 1, inclusive, in HEVC specification.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                           |
| Header<br/>                   | <dl> <dt>Dxva.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Structures](media-foundation-structures.md)
</dt> </dl>

 

 




