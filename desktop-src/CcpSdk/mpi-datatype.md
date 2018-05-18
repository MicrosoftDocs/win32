---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'FA174D3F-F696-4A0F-89C7-2193A88EF799'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Datatype enumeration'
---

# MPI\_Datatype enumeration

TBD

## Syntax


```C++
typedef enum _MPI_Datatype { 
  MPI_DATATYPE_NULL          = 0x0c000000,
  MPI_CHAR                   = 0x4c000101,
  MPI_UNSIGNED_CHAR          = 0x4c000102,
  MPI_SHORT                  = 0x4c000203,
  MPI_UNSIGNED_SHORT         = 0x4c000204,
  MPI_INT                    = 0x4c000405,
  MPI_UNSIGNED               = 0x4c000406,
  MPI_LONG                   = 0x4c000407,
  MPI_UNSIGNED_LONG          = 0x4c000408,
  MPI_LONG_LONG_INT          = 0x4c000809,
  MPI_LONG_LONG              = MPI_LONG_LONG_INT,
  MPI_FLOAT                  = 0x4c00040a,
  MPI_DOUBLE                 = 0x4c00080b,
  MPI_LONG_DOUBLE            = 0x4c00080c,
  MPI_BYTE                   = 0x4c00010d,
  MPI_WCHAR                  = 0x4c00020e,
  MPI_PACKED                 = 0x4c00010f,
  MPI_LB                     = 0x4c000010,
  MPI_UB                     = 0x4c000011,
  MPI_C_COMPLEX              = 0x4c000812,
  MPI_C_FLOAT_COMPLEX        = 0x4c000813,
  MPI_C_DOUBLE_COMPLEX       = 0x4c001614,
  MPI_C_LONG_DOUBLE_COMPLEX  = 0x4c001615,
  MPI_2INT                   = 0x4c000816,
  MPI_C_BOOL                 = 0x4c000117,
  MPI_SIGNED_CHAR            = 0x4c000118,
  MPI_UNSIGNED_LONG_LONG     = 0x4c000819,
  MPI_CHARACTER              = 0x4c00011a,
  MPI_INTEGER                = 0x4c00041b,
  MPI_REAL                   = 0x4c00041c,
  MPI_LOGICAL                = 0x4c00041d,
  MPI_COMPLEX                = 0x4c00081e,
  MPI_DOUBLE_PRECISION       = 0x4c00081f,
  MPI_2INTEGER               = 0x4c000820,
  MPI_2REAL                  = 0x4c000821,
  MPI_DOUBLE_COMPLEX         = 0x4c001022,
  MPI_2DOUBLE_PRECISION      = 0x4c001023,
  MPI_2COMPLEX               = 0x4c001024,
  MPI_2DOUBLE_COMPLEX        = 0x4c002025,
  MPI_REAL2                  = MPI_DATATYPE_NULL,
  MPI_REAL4                  = 0x4c000427,
  MPI_COMPLEX8               = 0x4c000828,
  MPI_REAL8                  = 0x4c000829,
  MPI_COMPLEX16              = 0x4c00102a,
  MPI_REAL16                 = MPI_DATATYPE_NULL,
  MPI_COMPLEX32              = MPI_DATATYPE_NULL,
  MPI_INTEGER1               = 0x4c00012d,
  MPI_COMPLEX4               = MPI_DATATYPE_NULL,
  MPI_INTEGER2               = 0x4c00022f,
  MPI_INTEGER4               = 0x4c000430,
  MPI_INTEGER8               = 0x4c000831,
  MPI_INTEGER16              = MPI_DATATYPE_NULL,
  MPI_INT8_T                 = 0x4c000133,
  MPI_INT16_T                = 0x4c000234,
  MPI_INT32_T                = 0x4c000435,
  MPI_INT64_T                = 0x4c000836,
  MPI_UINT8_T                = 0x4c000137,
  MPI_UINT16_T               = 0x4c000238,
  MPI_UINT32_T               = 0x4c000439,
  MPI_UINT64_T               = 0x4c00083a,
  MPI_AINT                   = 0x4c00083b (_WIN64), 0x4c00043b,
  MPI_OFFSET                 = 0x4c00083c,
  MPI_FLOAT_INT              = 0x8c000000,
  MPI_DOUBLE_INT             = 0x8c000001,
  MPI_LONG_INT               = 0x8c000002,
  MPI_SHORT_INT              = 0x8c000003,
  MPI_LONG_DOUBLE_INT        = 0x8c000004
} MPI_Datatype;
```



## Constants

<dl> <dt>

<span id="MPI_DATATYPE_NULL"></span><span id="mpi_datatype_null"></span>**MPI\_DATATYPE\_NULL**
</dt> <dd></dd> <dt>

<span id="MPI_CHAR"></span><span id="mpi_char"></span>**MPI\_CHAR**
</dt> <dd></dd> <dt>

<span id="MPI_UNSIGNED_CHAR"></span><span id="mpi_unsigned_char"></span>**MPI\_UNSIGNED\_CHAR**
</dt> <dd></dd> <dt>

<span id="MPI_SHORT"></span><span id="mpi_short"></span>**MPI\_SHORT**
</dt> <dd></dd> <dt>

<span id="MPI_UNSIGNED_SHORT"></span><span id="mpi_unsigned_short"></span>**MPI\_UNSIGNED\_SHORT**
</dt> <dd></dd> <dt>

<span id="MPI_INT"></span><span id="mpi_int"></span>**MPI\_INT**
</dt> <dd></dd> <dt>

<span id="MPI_UNSIGNED"></span><span id="mpi_unsigned"></span>**MPI\_UNSIGNED**
</dt> <dd></dd> <dt>

<span id="MPI_LONG"></span><span id="mpi_long"></span>**MPI\_LONG**
</dt> <dd></dd> <dt>

<span id="MPI_UNSIGNED_LONG"></span><span id="mpi_unsigned_long"></span>**MPI\_UNSIGNED\_LONG**
</dt> <dd></dd> <dt>

<span id="MPI_LONG_LONG_INT"></span><span id="mpi_long_long_int"></span>**MPI\_LONG\_LONG\_INT**
</dt> <dd></dd> <dt>

<span id="MPI_LONG_LONG"></span><span id="mpi_long_long"></span>**MPI\_LONG\_LONG**
</dt> <dd></dd> <dt>

<span id="MPI_FLOAT"></span><span id="mpi_float"></span>**MPI\_FLOAT**
</dt> <dd></dd> <dt>

<span id="MPI_DOUBLE"></span><span id="mpi_double"></span>**MPI\_DOUBLE**
</dt> <dd></dd> <dt>

<span id="MPI_LONG_DOUBLE"></span><span id="mpi_long_double"></span>**MPI\_LONG\_DOUBLE**
</dt> <dd></dd> <dt>

<span id="MPI_BYTE"></span><span id="mpi_byte"></span>**MPI\_BYTE**
</dt> <dd></dd> <dt>

<span id="MPI_WCHAR"></span><span id="mpi_wchar"></span>**MPI\_WCHAR**
</dt> <dd></dd> <dt>

<span id="MPI_PACKED"></span><span id="mpi_packed"></span>**MPI\_PACKED**
</dt> <dd></dd> <dt>

<span id="MPI_LB"></span><span id="mpi_lb"></span>**MPI\_LB**
</dt> <dd></dd> <dt>

<span id="MPI_UB"></span><span id="mpi_ub"></span>**MPI\_UB**
</dt> <dd></dd> <dt>

<span id="MPI_C_COMPLEX"></span><span id="mpi_c_complex"></span>**MPI\_C\_COMPLEX**
</dt> <dd></dd> <dt>

<span id="MPI_C_FLOAT_COMPLEX"></span><span id="mpi_c_float_complex"></span>**MPI\_C\_FLOAT\_COMPLEX**
</dt> <dd></dd> <dt>

<span id="MPI_C_DOUBLE_COMPLEX"></span><span id="mpi_c_double_complex"></span>**MPI\_C\_DOUBLE\_COMPLEX**
</dt> <dd></dd> <dt>

<span id="MPI_C_LONG_DOUBLE_COMPLEX"></span><span id="mpi_c_long_double_complex"></span>**MPI\_C\_LONG\_DOUBLE\_COMPLEX**
</dt> <dd></dd> <dt>

<span id="MPI_2INT"></span><span id="mpi_2int"></span>**MPI\_2INT**
</dt> <dd></dd> <dt>

<span id="MPI_C_BOOL"></span><span id="mpi_c_bool"></span>**MPI\_C\_BOOL**
</dt> <dd></dd> <dt>

<span id="MPI_SIGNED_CHAR"></span><span id="mpi_signed_char"></span>**MPI\_SIGNED\_CHAR**
</dt> <dd></dd> <dt>

<span id="MPI_UNSIGNED_LONG_LONG"></span><span id="mpi_unsigned_long_long"></span>**MPI\_UNSIGNED\_LONG\_LONG**
</dt> <dd></dd> <dt>

<span id="MPI_CHARACTER"></span><span id="mpi_character"></span>**MPI\_CHARACTER**
</dt> <dd></dd> <dt>

<span id="MPI_INTEGER"></span><span id="mpi_integer"></span>**MPI\_INTEGER**
</dt> <dd></dd> <dt>

<span id="MPI_REAL"></span><span id="mpi_real"></span>**MPI\_REAL**
</dt> <dd></dd> <dt>

<span id="MPI_LOGICAL"></span><span id="mpi_logical"></span>**MPI\_LOGICAL**
</dt> <dd></dd> <dt>

<span id="MPI_COMPLEX"></span><span id="mpi_complex"></span>**MPI\_COMPLEX**
</dt> <dd></dd> <dt>

<span id="MPI_DOUBLE_PRECISION"></span><span id="mpi_double_precision"></span>**MPI\_DOUBLE\_PRECISION**
</dt> <dd></dd> <dt>

<span id="MPI_2INTEGER"></span><span id="mpi_2integer"></span>**MPI\_2INTEGER**
</dt> <dd></dd> <dt>

<span id="MPI_2REAL"></span><span id="mpi_2real"></span>**MPI\_2REAL**
</dt> <dd></dd> <dt>

<span id="MPI_DOUBLE_COMPLEX"></span><span id="mpi_double_complex"></span>**MPI\_DOUBLE\_COMPLEX**
</dt> <dd></dd> <dt>

<span id="MPI_2DOUBLE_PRECISION"></span><span id="mpi_2double_precision"></span>**MPI\_2DOUBLE\_PRECISION**
</dt> <dd></dd> <dt>

<span id="MPI_2COMPLEX"></span><span id="mpi_2complex"></span>**MPI\_2COMPLEX**
</dt> <dd></dd> <dt>

<span id="MPI_2DOUBLE_COMPLEX"></span><span id="mpi_2double_complex"></span>**MPI\_2DOUBLE\_COMPLEX**
</dt> <dd></dd> <dt>

<span id="MPI_REAL2"></span><span id="mpi_real2"></span>**MPI\_REAL2**
</dt> <dd></dd> <dt>

<span id="MPI_REAL4"></span><span id="mpi_real4"></span>**MPI\_REAL4**
</dt> <dd></dd> <dt>

<span id="MPI_COMPLEX8"></span><span id="mpi_complex8"></span>**MPI\_COMPLEX8**
</dt> <dd></dd> <dt>

<span id="MPI_REAL8"></span><span id="mpi_real8"></span>**MPI\_REAL8**
</dt> <dd></dd> <dt>

<span id="MPI_COMPLEX16"></span><span id="mpi_complex16"></span>**MPI\_COMPLEX16**
</dt> <dd></dd> <dt>

<span id="MPI_REAL16"></span><span id="mpi_real16"></span>**MPI\_REAL16**
</dt> <dd></dd> <dt>

<span id="MPI_COMPLEX32"></span><span id="mpi_complex32"></span>**MPI\_COMPLEX32**
</dt> <dd></dd> <dt>

<span id="MPI_INTEGER1"></span><span id="mpi_integer1"></span>**MPI\_INTEGER1**
</dt> <dd></dd> <dt>

<span id="MPI_COMPLEX4"></span><span id="mpi_complex4"></span>**MPI\_COMPLEX4**
</dt> <dd></dd> <dt>

<span id="MPI_INTEGER2"></span><span id="mpi_integer2"></span>**MPI\_INTEGER2**
</dt> <dd></dd> <dt>

<span id="MPI_INTEGER4"></span><span id="mpi_integer4"></span>**MPI\_INTEGER4**
</dt> <dd></dd> <dt>

<span id="MPI_INTEGER8"></span><span id="mpi_integer8"></span>**MPI\_INTEGER8**
</dt> <dd></dd> <dt>

<span id="MPI_INTEGER16"></span><span id="mpi_integer16"></span>**MPI\_INTEGER16**
</dt> <dd></dd> <dt>

<span id="MPI_INT8_T"></span><span id="mpi_int8_t"></span>**MPI\_INT8\_T**
</dt> <dd></dd> <dt>

<span id="MPI_INT16_T"></span><span id="mpi_int16_t"></span>**MPI\_INT16\_T**
</dt> <dd></dd> <dt>

<span id="MPI_INT32_T"></span><span id="mpi_int32_t"></span>**MPI\_INT32\_T**
</dt> <dd></dd> <dt>

<span id="MPI_INT64_T"></span><span id="mpi_int64_t"></span>**MPI\_INT64\_T**
</dt> <dd></dd> <dt>

<span id="MPI_UINT8_T"></span><span id="mpi_uint8_t"></span>**MPI\_UINT8\_T**
</dt> <dd></dd> <dt>

<span id="MPI_UINT16_T"></span><span id="mpi_uint16_t"></span>**MPI\_UINT16\_T**
</dt> <dd></dd> <dt>

<span id="MPI_UINT32_T"></span><span id="mpi_uint32_t"></span>**MPI\_UINT32\_T**
</dt> <dd></dd> <dt>

<span id="MPI_UINT64_T"></span><span id="mpi_uint64_t"></span>**MPI\_UINT64\_T**
</dt> <dd></dd> <dt>

<span id="MPI_AINT"></span><span id="mpi_aint"></span>**MPI\_AINT**
</dt> <dd></dd> <dt>

<span id="MPI_OFFSET"></span><span id="mpi_offset"></span>**MPI\_OFFSET**
</dt> <dd></dd> <dt>

<span id="MPI_FLOAT_INT"></span><span id="mpi_float_int"></span>**MPI\_FLOAT\_INT**
</dt> <dd></dd> <dt>

<span id="MPI_DOUBLE_INT"></span><span id="mpi_double_int"></span>**MPI\_DOUBLE\_INT**
</dt> <dd></dd> <dt>

<span id="MPI_LONG_INT"></span><span id="mpi_long_int"></span>**MPI\_LONG\_INT**
</dt> <dd></dd> <dt>

<span id="MPI_SHORT_INT"></span><span id="mpi_short_int"></span>**MPI\_SHORT\_INT**
</dt> <dd></dd> <dt>

<span id="MPI_LONG_DOUBLE_INT"></span><span id="mpi_long_double_int"></span>**MPI\_LONG\_DOUBLE\_INT**
</dt> <dd></dd> </dl>

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h</dt> </dl>                                                                                                         |



## See also

<dl> <dt>

[MPI Enumerations](mpi-enumerations.md)
</dt> </dl>

 

 




