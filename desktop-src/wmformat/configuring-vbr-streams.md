---
title: Configuring VBR Streams
description: Configuring VBR Streams
ms.assetid: 83caabb7-b7fa-4b0a-a608-d5a86e4101b8
keywords:
- streams,configuring VBR streams
- streams,variable bit rate (VBR)
- variable bit rate (VBR),streams
- VBR (variable bit rate),streams
- streams,IWMPropertyVault interface
- IWMPropertyVault
ms.topic: article
ms.date: 05/31/2018
---

# Configuring VBR Streams

You can use variable bit rate (VBR) encoding to produce high quality streams for local files or for downloading and playing. There are three options for VBR: quality-based (one-pass), unconstrained (two-pass), and constrained (two-pass). For more information about the types of VBR encoding, see [Variable Bit Rate (VBR) Encoding](variable-bit-rate--vbr--encoding.md).

You can configure VBR encoding in a profile by setting properties with the [**IWMPropertyVault**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmpropertyvault) interface. The following table describes the properties used to configure VBR encoding.



| Property                     | Description                                                                                       |
|------------------------------|---------------------------------------------------------------------------------------------------|
| **g\_wszVBREnabled**         | Boolean value. Set to True to use VBR encoding.                                                   |
| **g\_wszVBRQuality**         | **DWORD** value. Set to the desired quality level (1 to 100) for quality-based VBR encoding.      |
| **g\_wszVBRBitrateMax**      | **DWORD** value. Set to the maximum bit rate, in bits per second, for constrained VBR encoding.   |
| **g\_wszVBRBufferWindowMax** | **DWORD** value. Set to the maximum buffer window, in milliseconds, for constrained VBR encoding. |



 

The following sections describe how to use the different types of variable bit rate encoding.



| Section                                                              | Description                                                                                                        |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [To Configure Quality-Based VBR](to-configure-quality-based-vbr.md) | Describes how to use variable bit rate encoding based on a static quality level.                                   |
| [To Configure Unconstrained VBR](to-configure-unconstrained-vbr.md) | Describes how to use variable bit rate encoding based on a target average bit rate without an explicit peak value. |
| [To Configure Constrained VBR](to-configure-constrained-vbr.md)     | Describes how to use variable bit rate encoding based on a target average bit rate and an explicit peak value.     |



 

## Related topics

<dl> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> </dl>

 

 




