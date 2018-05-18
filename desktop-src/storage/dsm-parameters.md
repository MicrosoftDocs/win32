---
title: DSM\_PARAMETERS structure
description: The DSM\_PARAMETERS structure holds the DSM version and timer counters information.
ms.assetid: '948331f1-1398-4e6e-85cb-27bbbd79630e'
keywords: ["DSM_PARAMETERS structure Storage Devices", "PDSM_PARAMETERS structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DSM_PARAMETERS
api_location:
- mpiowmi.h
api_type:
- HeaderDef
---

# DSM\_PARAMETERS structure

The DSM\_PARAMETERS structure holds the DSM version and timer counters information.

## Syntax


```C++
typedef struct _DSM_PARAMETERS {
  WCHAR        DsmName[63 + 1];
  ULONGLONG    DsmContext;
  DSM_VERSION  DsmVersion;
  DSM_COUNTERS DsmCounters;
} DSM_PARAMETERS, *PDSM_PARAMETERS;
```



## Members

<dl> <dt>

**DsmName**
</dt> <dd>

A string field of maximum length 63 characters that returns the friendly name of the DSM.

</dd> <dt>

**DsmContext**
</dt> <dd>

An unsigned 64-bitfield that represents a unique identifier as used by MPIO to address a particular DSM.

</dd> <dt>

**DsmVersion**
</dt> <dd>

A field that contains an instance of the DSM\_VERSION structure with version information for the DSM.

</dd> <dt>

**DsmCounters**
</dt> <dd>

A field that contains an instance of the DSM\_COUNTERS structure with timer counters information that is specific to the particular DSM.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DSM_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





