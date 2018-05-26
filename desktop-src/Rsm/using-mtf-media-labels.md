---
Description: RSM provides a generic media label library for Microsoft Tape Format (MTF). If your application writes MTF labels on tapes, there are certain requirements it must follow in how the labels are written.
ms.assetid: bad2311d-181e-4902-9793-4744e5b72d3e
title: Using MTF Media Labels
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using MTF Media Labels

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

RSM provides a generic media label library for Microsoft Tape Format (MTF). If your application writes MTF labels on tapes, there are certain requirements it must follow in how the labels are written.

RSM has the following requirements for applications that use MTF:

-   The DBLK Type field in the Common Block Header of the Media Header must be 'TAPE'.
-   The Header Checksum value in the Common Block Header of the Media Header is set correctly.
-   RSM uses the TapeName value as the Label Application Description and the SoftwareName value as the Label Type.
-   If the Tape Media Label Bit is set in the Tape Attribute field, the label library verifies the media label field of the MTF label and checks the description/label field for a GUID (UUID) of the following form: 12345678-1234-1234-1234-123456789012.
-   If found, RSM uses the UUID as the LabelID of the side. If a GUID is not found in the field, then an MD5 algorithm is used to generate a unique ID from the MTF block and it is returned as the LabelID.

 

 



