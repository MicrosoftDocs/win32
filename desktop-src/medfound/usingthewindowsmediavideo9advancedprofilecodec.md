---
description: Using the Windows Media Video 9 Advanced Profile
ms.assetid: 2abc0efc-dd11-4921-897c-209a26f8ba1d
title: Using the Windows Media Video 9 Advanced Profile
ms.topic: article
ms.date: 05/31/2018
---

# Using the Windows Media Video 9 Advanced Profile

The basic video procedures described in the [Working with Video](workingwithvideo.md) section also apply directly to the Windows Media Video 9 Advanced Profile. No special procedures are required.

The Windows Media Video 9 Advanced Profile is associated with the class identifiers CLSID\_CWMV9EncMediaObject and CLSID\_CWMVDecMediaObject. The FOURCC value for media types using this codec is "WVC1".

The Windows Media Video 9 Advanced Profile supports all common encoding modes as well interlaced encoding, mixed interlaced and progressive encoding, resolutions that are different than the display, and range reduction features. Another feature is the ability to store sequence and frame metadata in the bit-stream itself; previously this had required use of the ASF and Data Unit Extensions API.

The following properties of the Windows Media Video 9 Advanced Profile, which can be controlled using registry settings, do not have corresponding **IPropertyBag** or **IPropertyStore** strings:

-   Dquant Option.
-   Dquant Strength.
-   Force Overlap.
-   Motion Vector Cost Method.

## Achieving Optimal Visual Quality

For most video data, to achieve optimal visual quality using the Windows Media Video 9 Advanced Profile, you can set the [MFPKEY\_COMPRESSIONOPTIMIZATIONTYPE](mfpkey-compressionoptimizationtypeproperty.md) property to 1.

## About the Previous Windows Media Video 9 Advanced Profile Codecs

The current version of the Windows Media Video 9 Advanced Profile codec is based on the Society of Motion Picture and Television Engineers (SMPTE) standard for VC-1 (SMPTE 421M) Advanced Profile. This codec replaces the earlier codec from Windows also called the Windows Media Video 9 Advanced Profile codec which was identified by the FOURCC code "WMVA". The previous version of the VC-1 codec was implemented before the VC-1 advanced profile standard was finalized, and is no longer supported.

## Related topics

<dl> <dt>

[Working with Video](workingwithvideo.md)
</dt> 
 </dl>

 

 



