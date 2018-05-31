---
error-parsing-yaml: 
---

# IVMSCSIController::Configure method

The **Configure** method configures the SCSI controller to be used on an independent or on a shared bus.

## Syntax


```C++
HRESULT Configure(
  [in] VARIANT_BOOL isBusShared,
  [in] long         SCSIID
);
```



## Parameters

<dl> <dt>

*isBusShared* \[in\]
</dt> <dd>

Set to **TRUE** to put the SCSI controller on a shared bus. The SCSI controller is on an independent bus by default. To support clustering, set *isBusShared* to **TRUE** and *SCSIID* to 6.

</dd> <dt>

*SCSIID* \[in\]
</dt> <dd>

The SCSI ID of the SCSI controller. This can be set to either 6 or 7. The SCSI ID is 7 by default. To support clustering, set *isBusShared* to **TRUE** and *SCSIID* to 6.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                             | Description                                                             |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>                  | The operation was successful.<br/>                                |
| <dl> <dt> **E\_INVALIDARG**</dt> </dl>           | The SCSI ID for the controller is not 6 or 7.<br/>                |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>       | The virtual machine for this SCSI controller does not exist.<br/> |
| <dl> <dt> **VM\_E\_PREF\_NOT\_FOUND**</dt> </dl> | The SCSI controller does not exist.<br/>                          |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl>     | An unexpected error occurred.<br/>                                |



 

## Remarks

SCSI controllers which are not shared use the default SCSI ID of 7.

When virtual machines are clustered, the respective SCSI controllers of each virtual machine is put on a shared SCSI bus. In this scenario, the controllers need to have unique IDs on the bus. The SCSI controller on the shared bus is normally set to an ID of 6.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSCSIController**](ivmscsicontroller.md)
</dt> </dl>

 

 





