---
title: WINBIO_BIR_FIELD Constants (Winbio\_types.h)
description: Specify a bitmask.
ms.assetid: D8D12BCF-FEB3-4E02-B751-9F3AE5048BC1
topic_type:
- apiref
api_name:
- WINBIO_BIR_FIELD_SUBHEAD_COUNT
- WINBIO_BIR_FIELD_PRODUCT_ID
- WINBIO_BIR_FIELD_PATRON_ID
- WINBIO_BIR_FIELD_INDEX
- WINBIO_BIR_FIELD_CREATION_DATE
- WINBIO_BIR_FIELD_VALIDITY_PERIOD
- WINBIO_BIR_FIELD_BIOMETRIC_TYPE
- WINBIO_BIR_FIELD_BIOMETRIC_SUBTYPE
- WINBIO_BIR_FIELD_CBEFF_HEADER_VERSION
- WINBIO_BIR_FIELD_PATRON_HEADER_VERSION
- WINBIO_BIR_FIELD_BIOMETRIC_PURPOSE
- WINBIO_BIR_FIELD_BIOMETRIC_CONDITION
- WINBIO_BIR_FIELD_QUALITY
- WINBIO_BIR_FIELD_CREATOR
- WINBIO_BIR_FIELD_CHALLENGE
- WINBIO_BIR_FIELD_PAYLOAD
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_BIR\_FIELD Constants

The following constants are used to create a bitmask for the **ValidFields** member of the [**WINBIO\_BIR\_HEADER**](winbio-bir-header.md) structure.



| Constant/value                                                                                                                                                                                                                                                                                           | Description                                                                                                                                   |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WINBIO_BIR_FIELD_SUBHEAD_COUNT"></span><span id="winbio_bir_field_subhead_count"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_SUBHEAD\_COUNT**</dt> <dt>0x0001</dt> </dl>                          | Provided for conformity with NISTIR 6529-A, the Common Biometric Exchange Formats Framework (CBEFF) Patron Format A, but not used.<br/> |
| <span id="WINBIO_BIR_FIELD_PRODUCT_ID"></span><span id="winbio_bir_field_product_id"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_PRODUCT\_ID**</dt> <dt>0x0002</dt> </dl>                                   | The **ProductId** member is valid.<br/>                                                                                                 |
| <span id="WINBIO_BIR_FIELD_PATRON_ID"></span><span id="winbio_bir_field_patron_id"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_PATRON\_ID**</dt> <dt>0x0004</dt> </dl>                                      | Provided for conformity with NISTIR 6529-A, CBEFF Patron Format A, but not used.<br/>                                                   |
| <span id="WINBIO_BIR_FIELD_INDEX"></span><span id="winbio_bir_field_index"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_INDEX**</dt> <dt>0x0008</dt> </dl>                                                   | Provided for conformity with NISTIR 6529-A, CBEFF Patron Format A, but not used.<br/>                                                   |
| <span id="WINBIO_BIR_FIELD_CREATION_DATE"></span><span id="winbio_bir_field_creation_date"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_CREATION\_DATE**</dt> <dt>0x0010</dt> </dl>                          | The **CreationDate** member is valid.<br/>                                                                                              |
| <span id="WINBIO_BIR_FIELD_VALIDITY_PERIOD"></span><span id="winbio_bir_field_validity_period"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_VALIDITY\_PERIOD**</dt> <dt>0x0020</dt> </dl>                    | The **ValidityPeriod** member is valid.<br/>                                                                                            |
| <span id="WINBIO_BIR_FIELD_BIOMETRIC_TYPE"></span><span id="winbio_bir_field_biometric_type"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_BIOMETRIC\_TYPE**</dt> <dt>0x0040</dt> </dl>                       | The **Type** member is valid.<br/>                                                                                                      |
| <span id="WINBIO_BIR_FIELD_BIOMETRIC_SUBTYPE"></span><span id="winbio_bir_field_biometric_subtype"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_BIOMETRIC\_SUBTYPE**</dt> <dt>0x0080</dt> </dl>              | The **Subtype** member is valid.<br/>                                                                                                   |
| <span id="WINBIO_BIR_FIELD_CBEFF_HEADER_VERSION"></span><span id="winbio_bir_field_cbeff_header_version"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_CBEFF\_HEADER\_VERSION**</dt> <dt>0x0100</dt> </dl>    | The **HeaderVersion** member is valid.<br/>                                                                                             |
| <span id="WINBIO_BIR_FIELD_PATRON_HEADER_VERSION"></span><span id="winbio_bir_field_patron_header_version"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_PATRON\_HEADER\_VERSION**</dt> <dt>0x0200</dt> </dl> | The **PatronHeaderVersion** member is valid.<br/>                                                                                       |
| <span id="WINBIO_BIR_FIELD_BIOMETRIC_PURPOSE"></span><span id="winbio_bir_field_biometric_purpose"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_BIOMETRIC\_PURPOSE**</dt> <dt>0x0400</dt> </dl>              | The **Purpose** member is valid.<br/>                                                                                                   |
| <span id="WINBIO_BIR_FIELD_BIOMETRIC_CONDITION"></span><span id="winbio_bir_field_biometric_condition"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_BIOMETRIC\_CONDITION**</dt> <dt>0x0800</dt> </dl>        | Provided for conformity with NISTIR 6529-A, CBEFF Patron Format A, but not used.<br/>                                                   |
| <span id="WINBIO_BIR_FIELD_QUALITY"></span><span id="winbio_bir_field_quality"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_QUALITY**</dt> <dt>0x1000</dt> </dl>                                             | The **DataQuality** member is valid.<br/>                                                                                               |
| <span id="WINBIO_BIR_FIELD_CREATOR"></span><span id="winbio_bir_field_creator"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_CREATOR**</dt> <dt>0x2000</dt> </dl>                                             | Provided for conformity with NISTIR 6529-A, CBEFF Patron Format A, but not used.<br/>                                                   |
| <span id="WINBIO_BIR_FIELD_CHALLENGE"></span><span id="winbio_bir_field_challenge"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_CHALLENGE**</dt> <dt>0x4000</dt> </dl>                                       | Provided for conformity with NISTIR 6529-A, CBEFF Patron Format A, but not used.<br/>                                                   |
| <span id="WINBIO_BIR_FIELD_PAYLOAD"></span><span id="winbio_bir_field_payload"></span><dl> <dt>**WINBIO\_BIR\_FIELD\_PAYLOAD**</dt> <dt>0x8000</dt> </dl>                                             | Provided for conformity with NISTIR 6529-A, CBEFF Patron Format A, but not used.<br/>                                                   |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Constants](client-application-constants.md)
</dt> </dl>

 

 





