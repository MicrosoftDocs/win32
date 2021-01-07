---
description: ICE81 validates the MsiDigitalCertificate table, MsiDigitalSignature table, MsiPatchCertificate table, and MsiPackageCertificate Table.
ms.assetid: 83d8bc62-679e-410f-a95c-ffe13952b710
title: ICE81
ms.topic: article
ms.date: 05/31/2018
---

# ICE81

ICE81 validates the [MsiDigitalCertificate table](msidigitalcertificate-table.md), [MsiDigitalSignature table](msidigitalsignature-table.md), [MsiPatchCertificate table](msipatchcertificate-table.md), and [MsiPackageCertificate Table](msipackagecertificate-table.md). This ICE custom action posts warnings for digital certificates that are unused or unreferenced, and it posts an error when the signed object does not exist or when the signed object's cabinet does not point to external data.

Note that ICE03 verifies that the entry in the Table column in the MsiDigitalSignature table is "Media."

## Result

ICE81 posts the following warnings for unused or unreferenced Digital Certificates.



| ICE81 warning                                                                                                                                                      | Description                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| No reference to any of the records in the MsiDigitalCertificate table could be found in MsiDigitalSignature, MsiPackageCertificate, or MsiPatchCertificate tables. | This warning is returned if all records are unused.                |
| No reference to the Digital Certificate \[1\] could be found in MsiDigitalSignature, MsiPackageCertificate, or MsiPatchCertificate tables.                         | This warning is returned if some records, but not all, are unused. |



 

ICE81 posts the following errors.



| ICE81 error                                                                                                                                                              | Description                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Media Table does not exist. Hence all the entries in MsiDigitalSignature are incorrect                                                                                   | The signed object does not exist. This error is returned if the Media table does not exist but MsiDigitalSignature has entries.                                |
| Missing signed object \[2\] in Media Table                                                                                                                               | The signed object \[2\] does not exist. This error is returned if the Media table exists, but this entry in MsiDigitalSignature is not present in Media table. |
| The entry in table \[1\] with key \[2\] is signed. Hence the cabinet should point to an object outside the package (the value of Cabinet should NOT be prefixed with \#) | The signed object's cabinet does not point to external data. \[1\] is table name. \[2\] is key in the Media table.                                             |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



