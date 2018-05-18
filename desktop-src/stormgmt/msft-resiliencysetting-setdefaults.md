---
title: SetDefaults method of the MSFT\_ResiliencySetting class
description: Allows a user to modify the default property values of the MSFT\_ResiliencySetting object.
ms.assetid: 'E568F70B-3492-4D17-BF77-657E091046C6'
keywords: ["SetDefaults method Windows Storage Management API", "SetDefaults method Windows Storage Management API , MSFT_ResiliencySetting class", "MSFT_ResiliencySetting class Windows Storage Management API , SetDefaults method"]
topic_type:
- apiref
api_name:
- MSFT_ResiliencySetting.SetDefaults
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# SetDefaults method of the MSFT\_ResiliencySetting class

Allows a user to modify the default property values of the [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) object.

The updated values will only take effect for subsequent virtual disk creations and are not retroactively applied.

## Syntax


```mof
UInt32 SetDefaults(
  [in]  UInt16  NumberOfDataCopiesDefault,
  [in]  UInt16  PhysicalDiskRedundancyDefault,
  [in]  UInt16  NumberOfColumnsDefault,
  [in]  Boolean AutoNumberOfColumns,
  [in]  UInt64  InterleaveDefault,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*NumberOfDataCopiesDefault* \[in\]
</dt> <dd>

The desired number of full data copies to maintain. This value must be between the values of the **NumberofDataCopiesMin** and **NumberofDataCopiesMax** properties of the [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) object.

</dd> <dt>

*PhysicalDiskRedundancyDefault* \[in\]
</dt> <dd>

The desired level of physical disk failure tolerance. This value must be between the values of the **PhysicalDiskRedundancyMin** and **PhysicalDiskRedundancyMax** properties of the [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) object.

</dd> <dt>

*NumberOfColumnsDefault* \[in\]
</dt> <dd>

The desired number of physical disks to stripe data across. This value must be between the values of the **NumberOfColumnsMin** and **NumberofColumnsMax** properties of the [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) object.

</dd> <dt>

*AutoNumberOfColumns* \[in\]
</dt> <dd>

If **TRUE**, the storage provider (or subsystem) should automatically choose what it determines to be the best number of columns for this resiliency setting. If this parameter is **TRUE**, then the *NumberOfColumnsDefault* parameter must be **NULL**.

</dd> <dt>

*InterleaveDefault* \[in\]
</dt> <dd>

The desired size of a data strip on a single physical disk in a striping based resiliency setting. This value must be between the values of the **InterleaveMin** and **InterleaveMax** properties of the [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) object.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

</dd> </dl>

## Return value



| Return code/value                                                                                                                                                                                                                                        | Description                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**Success**</dt> <dt>0</dt> </dl>                                                                                                            | The method completed successfully.<br/>            |
| <dl> <dt>**Not Supported**</dt> <dt>1</dt> </dl>                                                                                                      | This method is not supported for this object.<br/> |
| <dl> <dt>**Unspecified Error**</dt> <dt>2</dt> </dl>                                                                                                  | An unspecified error has occurred.<br/>            |
| <dl> <dt>**Timeout**</dt> <dt>3</dt> </dl>                                                                                                            | The method has timed out.<br/>                     |
| <dl> <dt>**Failed**</dt> <dt>4</dt> </dl>                                                                                                             | The method failed.<br/>                            |
| <dl> <dt>**Invalid Parameter**</dt> <dt>5</dt> </dl>                                                                                                  | One or more parameter values were not valid.<br/>  |
| <dl> <dt>**Access denied**</dt> <dt>40001</dt> </dl>                                                                                                  |                                                          |
| <dl> <dt>**There are not enough resources to complete the operation.**</dt> <dt>40002</dt> </dl>                                                      |                                                          |
| <dl> <dt>**Cannot connect to the storage provider.**</dt> <dt>46000</dt> </dl>                                                                        |                                                          |
| <dl> <dt>**The storage provider cannot connect to the storage subsystem.**</dt> <dt>46001</dt> </dl>                                                  |                                                          |
| <dl> <dt>**This operation is not supported on primordial storage pools.**</dt> <dt>48000</dt> </dl>                                                   |                                                          |
| <dl> <dt>**The storage pool could not complete the operation because its health or operational status does not permit it.**</dt> <dt>48006</dt> </dl> |                                                          |
| <dl> <dt>**The storage pool could not complete the operation because its configuration is read-only.**</dt> <dt>48007</dt> </dl>                      |                                                          |
| <dl> <dt>**The value for PhysicalDiskRedundancy is outside of the supported range of values.**</dt> <dt>49002</dt> </dl>                              |                                                          |
| <dl> <dt>**The value for NumberOfDataCopies is outside of the supported range of values.**</dt> <dt>49003</dt> </dl>                                  |                                                          |
| <dl> <dt>**The value for Interleave is outside of the supported range of values.**</dt> <dt>49005</dt> </dl>                                          |                                                          |
| <dl> <dt>**The value for NumberOfColumns is outside of the supported range of values.**</dt> <dt>49006</dt> </dl>                                     |                                                          |



 

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ResiliencySetting**](msft-resiliencysetting.md)
</dt> </dl>

 

 





