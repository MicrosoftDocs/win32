---
title: DSM\_QueryLBPolicy\_V2 structure
description: The DSM\_QueryLBPolicy\_V2 structure is used to query a LUN's current load balance policy. It is basically the same as the DSM\_QueryLBPolicy structure except that it returns the load balance information by using the DSM\_Load\_Balance\_Policy\_V2 structure.
ms.assetid: 'f02f3442-e9c2-4f60-833d-e470de62118e'
keywords: ["DSM_QueryLBPolicy_V2 structure Storage Devices", "PDSM_QueryLBPolicy_V2 structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DSM_QueryLBPolicy_V2
api_location:
- mpiodisk.h
api_type:
- HeaderDef
---

# DSM\_QueryLBPolicy\_V2 structure

The DSM\_QueryLBPolicy\_V2 structure is used to query a LUN's current load balance policy. It is basically the same as the DSM\_QueryLBPolicy structure except that it returns the load balance information by using the DSM\_Load\_Balance\_Policy\_V2 structure.

## Syntax


```C++
typedef struct _DSM_QueryLBPolicy_V2 {
  DSM_Load_Balance_Policy_V2 LoadBalancePolicy;
} DSM_QueryLBPolicy_V2, *PDSM_QueryLBPolicy_V2;
```



## Members

<dl> <dt>

**LoadBalancePolicy**
</dt> <dd>

An instance of the DSM\_Load\_Balance\_Policy\_V2 structure that has information about the current load balance policy that is being applied by the DSM on the targeted pseudo-LUN.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiodisk.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DSM_QueryLBPolicy_V2%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





