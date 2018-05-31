---
Description: The fax service creates fax documents as Tagged Image File Format Class F (TIFF Class F) (for facsimile) files based on the Tagged Image File Format (TIFF) 6.0 specification.
ms.assetid: d7840c10-6059-40ed-9040-50eefefc7349
title: Fax Image Format
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Fax Image Format

The fax service creates fax documents as Tagged Image File Format Class F (TIFF Class F) (for facsimile) files based on the Tagged Image File Format (TIFF) 6.0 specification.

In addition to the requirements of the TIFF 6.0 specification, the fax service has the following requirements for TIFF Class F files:

-   TIFF files must have the Modified Modified READ (MMR) two-dimensional encoding data compression format. This format is defined by CCITT (The International Telegraph and Telephone Consultative Committee) Group 4.
-   The byte-ordering format of TIFF files must match the byte-ordering format of the CPU processing the file. For example, if a little-endian CPU is receiving the TIFF file, the file must be in little-endian format.
-   The TIFF field (tag) RowsPerStrip must contain a value of 1. This is because the fax service does not support transmission of data image strips. The RowsPerStrip describes the number of scan lines per image strip in the facsimile image.

For current information about required and recommended tags for TIFF Class F files, or for the complete specification for TIFF files, contact Adobe Systems Incorporated.

 

 



