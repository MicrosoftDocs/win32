---
title: Storage Silo Driver Structures
description: Storage Silo Driver Structures
ms.assetid: 'e8c5617f-1949-4d1d-ba30-5e0625653b48'
---

# Storage Silo Driver Structures

This section describes the following Storage Silo driver structures:

## In this section



| Topic                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BAND\_LOCATION\_INFO**](band-location-info.md)<br/>                      | The [**BAND\_LOCATION\_INFO**](band-location-info.md) structure specifies the location information for a band table entry query.<br/>                                                                                                                                                                                                                                                                                   |
| [**BAND\_MANAGEMENT\_CAPABILITIES**](band-management-capabilities.md)<br/>  | The [**BAND\_MANAGEMENT\_CAPABILITIES**](band-management-capabilities.md) structure contains the security capabilities available for a storage device. This structure is returned in the system buffer by the [**IOCTL\_EHSTOR\_BANDMGMT\_QUERY\_CAPABILITIES**](ioctl-ehstor-bandmgmt-query-capabilities.md) request.<br/>                                                                                            |
| [**BAND\_SECURITY\_INFO**](band-security-info.md)<br/>                      | The [**BAND\_SECURITY\_INFO**](band-security-info.md) structure specifies the security information for a band table entry query.<br/>                                                                                                                                                                                                                                                                                   |
| [**BAND\_TABLE**](band-table.md)<br/>                                       | The [**BAND\_TABLE**](band-table.md) structure contains the table of bands returned from an [**IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS**](ioctl-ehstor-bandmgmt-enumerate-bands.md) request. The bands in the band table are selected by a match condition sent as input for **IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS** in the [**ENUMERATE\_BANDS\_PARAMETERS**](enumerate-bands-parameters.md) structure.<br/> |
| [**BAND\_TABLE\_ENTRY**](band-table-entry.md)<br/>                          | Banding information entries in [**BAND\_TABLE**](band-table.md) are represented as [**BAND\_TABLE\_ENTRY**](band-table-entry.md) structures. These entries contain location and security properties for a band configuration.<br/>                                                                                                                                                                                     |
| [**CREATE\_BAND\_PARAMETERS**](create-band-parameters.md)<br/>              | The parameters to create a band on a storage device for an [**IOCTL\_EHSTOR\_BANDMGMT\_CREATE\_BAND**](ioctl-ehstor-bandmgmt-create-band.md) request are specified in a [**CREATE\_BAND\_PARAMETERS**](create-band-parameters.md) structure.<br/>                                                                                                                                                                      |
| [**DELETE\_BAND\_PARAMETERS**](delete-band-parameters.md)<br/>              | A configured band is deleted according to the parameters in a [**DELETE\_BAND\_PARAMETERS**](delete-band-parameters.md) structure. This structure is input for an [**IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND**](ioctl-ehstor-bandmgmt-delete-band.md) request.<br/>                                                                                                                                                      |
| [**ENUMERATE\_BANDS\_PARAMETERS**](enumerate-bands-parameters.md)<br/>      | The [**ENUMERATE\_BANDS\_PARAMETERS**](enumerate-bands-parameters.md) structure is used to select which band information entries are selected for return from an [**IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS**](ioctl-ehstor-bandmgmt-enumerate-bands.md) request.<br/>                                                                                                                                               |
| [**ERASE\_BAND\_PARAMETERS**](erase-band-parameters.md)<br/>                | The [**ERASE\_BAND\_PARAMETERS**](erase-band-parameters.md) structure contains the selection criteria for a band to erase. Additionally, a new authentication key can be set. This structure is input for an [**IOCTL\_EHSTOR\_BANDMGMT\_ERASE\_BAND**](ioctl-ehstor-bandmgmt-erase-band.md) request.<br/>                                                                                                             |
| [**GET\_BAND\_METADATA\_PARAMETERS**](get-band-metadata-parameters.md)<br/> | The metadata for a configured band is retrieved according to the parameters in a [**GET\_BAND\_METADATA\_PARAMETERS**](get-band-metadata-parameters.md) structure. This structure is input for an [**IOCTL\_EHSTOR\_BANDMGMT\_GET\_BAND\_METADATA**](ioctl-ehstor-bandmgmt-get-band-metadata.md) request.<br/>                                                                                                         |
| [**SET\_BAND\_LOCATION\_PARAMETERS**](set-band-location-parameters.md)<br/> | The [**SET\_BAND\_LOCATION\_PARAMETERS**](create-band-parameters.md) structure specifies the parameters to set location properties for a band on a storage device for a [**IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_LOCATION**](ioctl-ehstor-bandmgmt-set-band-location.md) request.<br/>                                                                                                                                   |
| [**SET\_BAND\_METADATA\_PARAMETERS**](set-band-metadata-parameters.md)<br/> | The metadata for a configured band is set to the parameters in a [**SET\_BAND\_METADATA\_PARAMETERS**](set-band-metadata-parameters.md) structure. This structure is input for a [**IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_METADATA**](ioctl-ehstor-bandmgmt-set-band-metadata.md) request.<br/>                                                                                                                          |
| [**SET\_BAND\_SECURITY\_PARAMETERS**](set-band-security-parameters.md)<br/> | The parameters to set security properties for a band on a storage device for a [**IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_SECURITY**](ioctl-ehstor-bandmgmt-set-band-security.md) request are specified in a [**SET\_BAND\_SECURITY\_PARAMETERS**](set-band-security-parameters.md) structure.<br/>                                                                                                                        |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Storage%20Silo%20Driver%20Structures%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





