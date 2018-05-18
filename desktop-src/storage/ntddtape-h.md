---
title: Ntddtape.h
description: This section contains reference topics for the Ntddtape.h header.
ms.assetid: '1354F26E-AB7B-4967-BFF6-700F98E5B302'
---

# Ntddtape.h

This section contains reference topics for the Ntddtape.h header.

## In this section



| Topic                                                                        | Description                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Tape I/O Control Codes](tape-i-o-control-codes.md)<br/>              |                                                                                                                                                                                                                                                                          |
| [**TAPE\_CREATE\_PARTITION**](tape-create-partition.md)<br/>          | The TAPE\_CREATE\_PARTITION structure is used in conjunction with the [**IOCTL\_TAPE\_CREATE\_PARTITION**](ioctl-tape-create-partition.md) request to create a specified number of fixed, select, or initiator partitions of a given size on the tape media.<br/> |
| [**TAPE\_DRIVE\_PROBLEM\_TYPE**](tape-drive-problem-type.md)<br/>     | The TAPE\_DRIVE\_PROBLEM\_TYPE enumerator is used to report problems with the tape drive. <br/>                                                                                                                                                                    |
| [**TAPE\_ERASE**](tape-erase.md)<br/>                                 | The TAPE\_ERASE structure is used in conjunction with the [**IOCTL\_TAPE\_ERASE**](ioctl-tape-erase.md) request to erase the current tape partition.<br/>                                                                                                         |
| [**TAPE\_GET\_DRIVE\_PARAMETERS**](tape-get-drive-parameters.md)<br/> | The TAPE\_GET\_DRIVE\_PARAMETERS structure is used in conjunction with the [**IOCTL\_TAPE\_GET\_DRIVE\_PARAMS**](ioctl-tape-get-drive-params.md) request to retrieve information about capabilities of the tape drive.<br/>                                       |
| [**TAPE\_GET\_MEDIA\_PARAMETERS**](tape-get-media-parameters.md)<br/> | The TAPE\_GET\_MEDIA\_PARAMETERS structure is used in conjunction with the [**TapeMiniGetMediaParameters**](https://msdn.microsoft.com/library/windows/hardware/ff567937) routine to retrieve tape media parameters. <br/>                                                                   |
| [**TAPE\_GET\_POSITION**](tape-get-position.md)<br/>                  | The TAPE\_GET\_POSITION structure is used in conjunction with the [**IOCTL\_TAPE\_GET\_POSITION**](ioctl-tape-get-position.md) request to retrieve the current absolute, logical, or pseudological partition and offset position on the tape.<br/>                |
| [**TAPE\_PREPARE**](tape-prepare.md)<br/>                             | The TAPE\_PREPARE structure is used in conjunction with the [**IOCTL\_TAPE\_PREPARE**](ioctl-tape-prepare.md) request to load or unload tape, reset the tape's tension, lock or unlock the ejection mechanism, or format the tape.<br/>                           |
| [**TAPE\_SET\_DRIVE\_PARAMETERS**](tape-set-drive-parameters.md)<br/> | The TAPE\_SET\_DRIVE\_PARAMETERS structure is used in conjunction with the [**IOCTL\_TAPE\_SET\_DRIVE\_PARAMS**](ioctl-tape-set-drive-params.md) request to adjust the configurable parameters of a tape drive.<br/>                                              |
| [**TAPE\_SET\_MEDIA\_PARAMETERS**](tape-set-media-parameters.md)<br/> | The TAPE\_SET\_MEDIA\_PARAMETERS structure is used in conjunction with the [**IOCTL\_TAPE\_SET\_MEDIA\_PARAMS**](ioctl-tape-set-media-params.md) request to reset the block size of the media in a tape drive.<br/>                                               |
| [**TAPE\_SET\_POSITION**](tape-set-position.md)<br/>                  | The TAPE\_SET\_POSITION structure is used in conjunction with the [**IOCTL\_TAPE\_SET\_POSITION**](ioctl-tape-set-position.md) request to move the current position on the tape to the specified partition and offset.<br/>                                       |
| [**TAPE\_STATUS**](tape-status.md)<br/>                               | The TAPE\_STATUS enumeration provides a list of the status codes that the tape class driver uses to report the status of a tape device.<br/>                                                                                                                       |
| [**TAPE\_WMI\_OPERATIONS**](tape-wmi-operations.md)<br/>              | The tape miniclass driver passes this structure to its [*TapeMiniWMIControl*](https://msdn.microsoft.com/library/windows/hardware/ff567957) routine to indicate which WMI operation must be performed by the device. <br/>                                                                           |
| [**TAPE\_WRITE\_MARKS**](tape-write-marks.md)<br/>                    | The TAPE\_WRITE\_MARKS structure is used in conjunction with an [**IOCTL\_TAPE\_WRITE\_MARKS**](ioctl-tape-write-marks.md) request to write a setmark, a filemark, a short filemark, or a long filemark to tape. <br/>                                            |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Ntddtape.h%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





