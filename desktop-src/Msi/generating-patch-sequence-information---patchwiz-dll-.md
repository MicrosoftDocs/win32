---
description: The version of PATCHWIZ.DLL released with Windows Installer&\#160;3.0 can automatically generate patch sequencing information and add to the MsiPatchSequence Table a new patch.
ms.assetid: 03e7eea6-1a37-4c86-a9da-109fbaf20728
title: Generating Patch Sequence Information (PATCHWIZ.DLL)
ms.topic: article
ms.date: 05/31/2018
---

# Generating Patch Sequence Information (PATCHWIZ.DLL)

The version of [PATCHWIZ.DLL](patchwiz-dll.md) released with Windows Installer 3.0 can automatically generate patch sequencing information and add to the [MsiPatchSequence Table](msipatchsequence-table.md) a new patch.

Set the SEQUENCE\_DATA\_GENERATION\_DISABLED property to 1 (one) in the [Properties Table](properties-table-patchwiz-dll-.md) of the .pcp file to prevent the automatic generation of patch sequencing information. If this property is absent, the information is automatically generated and added.

When the [PATCHWIZ.DLL](patchwiz-dll.md) released with Windows Installer 3.0 is used to automatically generate the patch sequencing information, the following occurs:

-   A new row is added to the [MsiPatchSequence Table](msipatchsequence-table.md) for each product code of a target image that is listed in the [TargetImages Table](targetimages-table-patchwiz-dll-.md).
-   The values added to the PatchFamily column in the new rows correspond to the target product codes of the target images that are listed in the [TargetImages Table](targetimages-table-patchwiz-dll-.md).
-   The values added to the Sequence columns in the new rows are generated using the highest product version targeted by the patch and the UTC time when the patch is generated. The sequence number is \<Product Minor Version\>.\<Build Major Number\>.\<Time Stamp 1\>.\<Time Stamp 2\>.
    -   The first field is the product version of the highest version of the product that is targeted by the patch.
    -   The second field is the build major number of the highest version of the product that is targeted by the patch.

    The two time stamp fields account for the 32 bit time stamp that is needed to count the seconds in Coordinated Universal Time (UTC).
    > [!Note]  
    > Product versions have the following format: \<Product Major Version\>.\<Product Minor Version\>.\<Build Major Number\>.\<Build Minor Number\> and a product with a version number 2.1.0.0 is a higher version than a product with version number 1.2.0.0

     

-   The msidbPatchSequenceSupersedeEarlier attribute is entered into the Attribute column of new rows that are generated for service packs (SP) or minor upgrade patches. The msidbPatchSequenceSupersedeEarlier attribute is not added to a QFE or small update patch.
    > [!Note]  
    > A service pack (SP) should contain the fixes of all the QFEs that were released prior to it. However, if a patch author sets the SEQUENCE\_DATA\_SUPERSEDENCE property to 0 (zero) or 1 (one) in the .pcp file, the Attributes column of all rows in the MsiPatchSequence table is set to the value that is specified for SEQUENCE\_DATA\_SUPERSEDENCE. Patch authors who require more control must author the Attributes column manually.

     

If you include a [PatchSequence Table](patchsequence-table--patchwiz-dll-.md) in the .pcp file, the SEQUENCE\_DATA\_GENERATION\_DISABLED property is ignored and the information provided in the PatchSequence Table can be added to the [MsiPatchSequence Table](msipatchsequence-table.md) of the patch.

 

 



