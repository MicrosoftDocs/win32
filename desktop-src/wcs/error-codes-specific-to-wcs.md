---
title: Error Codes Specific To WCS
description: The following is a list of error codes that are specifically related to the use of WCS 1.0.
ms.assetid: c6a0cacc-f83e-4f5c-9002-7718bb2ffb6c


ms.topic: article
ms.date: 05/31/2018
---

# Error Codes Specific To WCS

The following is a list of error codes that are specifically related to the use of WCS 1.0. This does not mean that WCS functions will return only these error codes. It means that the codes in the table below are returned only by WCS functions. They may also return other Win32 error codes that are documented elsewhere in the Win32 API of the Platform SDK.

<dl> <dt>

<span id="ERROR_DELETING_ICM_XFORM"></span><span id="error_deleting_icm_xform"></span>ERROR\_DELETING\_ICM\_XFORM
</dt> <dd>

The specified color transform could not be deleted.

</dd> <dt>

<span id="ERROR_DUPLICATE_TAG"></span><span id="error_duplicate_tag"></span>ERROR\_DUPLICATE\_TAG
</dt> <dd>

The specified color profile element tag is already present in the color profile.

</dd> <dt>

<span id="ERROR_ICM_NOT_ENABLED"></span><span id="error_icm_not_enabled"></span>ERROR\_ICM\_NOT\_ENABLED
</dt> <dd>

Image Color Management is not currently enabled.

</dd> <dt>

<span id="ERROR_INVALID_CMM"></span><span id="error_invalid_cmm"></span>ERROR\_INVALID\_CMM
</dt> <dd>

The specified file name does not refer to a valid color management module.

</dd> <dt>

<span id="ERROR_INVALID_COLORSPACE"></span><span id="error_invalid_colorspace"></span>ERROR\_INVALID\_COLORSPACE
</dt> <dd>

The specified color space is invalid.

</dd> <dt>

<span id="ERROR_INVALID_PROFILE"></span><span id="error_invalid_profile"></span>ERROR\_INVALID\_PROFILE
</dt> <dd>

The specified file name does not refer to a valid color profile.

</dd> <dt>

<span id="ERROR_INVALID_TRANSFORM_"></span><span id="error_invalid_transform_"></span>ERROR\_INVALID\_TRANSFORM 
</dt> <dd>

The color transform that was specified is not a valid color transform.

</dd> <dt>

<span id="ERROR_PROFILE_NOT_ASSOCIATED_WITH_DEVICE"></span><span id="error_profile_not_associated_with_device"></span>ERROR\_PROFILE\_NOT\_ASSOCIATED\_WITH\_DEVICE
</dt> <dd>

The specified color profile is not associated with any device.

</dd> <dt>

<span id="ERROR_PROFILE_NOT_FOUND_"></span><span id="error_profile_not_found_"></span>ERROR\_PROFILE\_NOT\_FOUND 
</dt> <dd>

The specified color profile file name was not found. The file name or path is incorrect.

</dd> <dt>

<span id="ERROR_TAG_NOT_FOUND"></span><span id="error_tag_not_found"></span>ERROR\_TAG\_NOT\_FOUND
</dt> <dd>

The specified color profile element tag was not found in the color profile.

</dd> <dt>

<span id="ERROR_TAG_NOT_PRESENT"></span><span id="error_tag_not_present"></span>ERROR\_TAG\_NOT\_PRESENT
</dt> <dd>

A color profile element tag that is required for the function to succeed was not passed to the function.

</dd> </dl>

## Related topics

<dl> <dt>

[Basic color management concepts](basic-color-management-concepts.md)
</dt> <dt>

[WCS Constants](wcs-constants.md)
</dt> </dl>

 

 




