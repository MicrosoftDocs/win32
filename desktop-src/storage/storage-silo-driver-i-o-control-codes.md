---
title: Storage Silo Driver I/O Control Codes
description: Storage Silo Driver I/O Control Codes
ms.assetid: 'c5e5a131-c960-4ca1-a724-5ad026efbea6'
---

# Storage Silo Driver I/O Control Codes

Storage silo driver clients use the IOCTLs in this section to communicate with storage silo drivers.

This section consists of the following topics:

## In this section



| Topic                                                                                                       | Description                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOCTL\_EHSTOR\_BANDMGMT\_ACTIVATE**](ioctl-ehstor-bandmgmt-activate.md)<br/>                      | This [**IOCTL\_EHSTOR\_BANDMGMT\_ACTIVATE**](ioctl-ehstor-bandmgmt-activate.md) request is sent to activate the security features and band management on a storage device. The request includes activation options and the authentication key.<br/>                                                                              |
| [**IOCTL\_EHSTOR\_BANDMGMT\_CREATE\_BAND**](ioctl-ehstor-bandmgmt-create-band.md)<br/>               | New bands are created on a band-managed storage device with the [**IOCTL\_EHSTOR\_BANDMGMT\_CREATE\_BAND**](ioctl-ehstor-bandmgmt-create-band.md) request. A new band is added to the table of band entries, which includes band location and security properties.<br/>                                                          |
| [**IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND**](ioctl-ehstor-bandmgmt-delete-band.md)<br/>               | A configured band on a storage device is deleted with the [**IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND**](ioctl-ehstor-bandmgmt-delete-band.md) request. An erase option in the input parameters allows the request to perform a cryptographic erase of the band data.<br/>                                                          |
| [**IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS**](ioctl-ehstor-bandmgmt-enumerate-bands.md)<br/>       | This [**IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS**](ioctl-ehstor-bandmgmt-enumerate-bands.md) request is sent to retrieve the list of bands for a storage device under band management. Banding information is returned in a table of band entries that includes band location and security properties.<br/>                    |
| [**IOCTL\_EHSTOR\_BANDMGMT\_ERASE\_BAND**](ioctl-ehstor-bandmgmt-erase-band.md)<br/>                 | The **IOCTL\_EHSTOR\_BANDMGMT\_ERASE\_BAND** request will cryptographically erase and reset the authentication key of a band. The remaining configuration of the band is left unmodified.<br/>                                                                                                                                    |
| [**IOCTL\_EHSTOR\_BANDMGMT\_GET\_BAND\_METADATA**](ioctl-ehstor-bandmgmt-get-band-metadata.md)<br/>  | Metadata associated with a band is retrieved with an [**IOCTL\_EHSTOR\_BANDMGMT\_GET\_BAND\_METADATA**](ioctl-ehstor-bandmgmt-get-band-metadata.md) request. The metadata for a band serves as a data area for a key manager application.<br/>                                                                                   |
| [**IOCTL\_EHSTOR\_BANDMGMT\_QUERY\_CAPABILITIES**](ioctl-ehstor-bandmgmt-query-capabilities.md)<br/> | The [**IOCTL\_EHSTOR\_BANDMGMT\_QUERY\_CAPABILITIES**](ioctl-ehstor-bandmgmt-query-capabilities.md) request retrieves the banded security capabilities for a storage device. The IOCTL returns the capabilities as a [**BAND\_MANAGEMENT\_CAPABILITIES**](band-management-capabilities.md) structure in the system buffer.<br/> |
| [**IOCTL\_EHSTOR\_BANDMGMT\_REVERT**](ioctl-ehstor-bandmgmt-revert.md)<br/>                          | This [**IOCTL\_EHSTOR\_BANDMGMT\_REVERT**](ioctl-ehstor-bandmgmt-revert.md) request is sent to deactivate the security features and band management on a storage device. The request includes revert options and the authentication key.<br/>                                                                                    |
| [**IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_LOCATION**](ioctl-ehstor-bandmgmt-set-band-location.md)<br/>  | The location properties of bands in a band-managed storage device are modified with the [**IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_LOCATION**](ioctl-ehstor-bandmgmt-set-band-location.md) request.<br/>                                                                                                                             |
| [**IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_METADATA**](ioctl-ehstor-bandmgmt-set-band-metadata.md)<br/>  | Metadata associated with a band is set with an [**IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_METADATA**](ioctl-ehstor-bandmgmt-set-band-metadata.md) request. The metadata for a band serves as a data area for a key manager application.<br/>                                                                                         |
| [**IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_SECURITY**](ioctl-ehstor-bandmgmt-set-band-security.md)<br/>  | The security properties of bands in a band-managed storage device are modified with the [**IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_SECURITY**](ioctl-ehstor-bandmgmt-set-band-security.md) request.<br/>                                                                                                                             |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Storage%20Silo%20Driver%20I/O%20Control%20Codes%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





