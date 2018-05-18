---
title: Tape I/O Control Codes
description: Tape I/O Control Codes
ms.assetid: '452bcdcb-9884-45d9-9887-f349f1e89b95'
---

# Tape I/O Control Codes

## 

All public I/O control codes for drivers of tape devices use buffered I/O. Consequently, the input or output data for these requests is at **Irp-&gt;AssociatedIrp.SystemBuffer**.

Class drivers for tape devices handle additional public I/O control codes, along with those described in this section. For more information about requirements for storage class drivers, see [General Storage I/O Control Codes](general-storage-i-o-control-codes.md).

Tape miniclass drivers report error status using the values listed in the [**TAPE\_STATUS**](tape-status.md) enumerator. The tape class driver uses the equivalent NT status values to report status when it completes an I/O control request. For a mapping between the NT status values returned by tape I/O control requests and TAPE\_STATUS values, see [Processing Tape Device Control Requests](https://msdn.microsoft.com/library/windows/hardware/ff563934).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Tape%20I/O%20Control%20Codes%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




