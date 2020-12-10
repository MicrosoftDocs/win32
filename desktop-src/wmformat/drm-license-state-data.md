---
title: DRM_LICENSE_STATE_DATA structure (Drmexternals.h)
description: The DRM\_LICENSE\_STATE\_DATA structure contains license information about a specified DRM right.
ms.assetid: '5ca577b5-d28b-4e36-8af7-6fae4300d464'
keywords:
- DRM_LICENSE_STATE_DATA structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- DRM_LICENSE_STATE_DATA
api_location:
- Drmexternals.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRM_LICENSE_STATE_DATA structure (Drmexternals.h)

The **DRM\_LICENSE\_STATE\_DATA** structure contains [*license*](wmformat-glossary.md) information about a specified [*DRM*](wmformat-glossary.md) right.

## Syntax


```C++
typedef struct DRM_LICENSE_STATE_DATA {
  DWORD                      dwStreamId;
  DRM_LICENSE_STATE_CATEGORY dwCategory;
  DWORD                      dwNumCounts;
  DWORD                      dwCount[4];
  DWORD                      dwNumDates;
  FILETIME                   datetime[4];
  DWORD                      dwVague;
} ;
```



## Members

<dl> <dt>

**dwStreamId**
</dt> <dd>

Stream number to which the license applies. Must be 0, which indicates that the license applies to all streams in the file.

</dd> <dt>

**dwCategory**
</dt> <dd>

Category of string to be displayed. See [**DRM\_LICENSE\_STATE\_CATEGORY**](drm-license-state-category.md) for possible values and their meaning.

</dd> <dt>

**dwNumCounts**
</dt> <dd>

Number of items supplied in **dwCount**. This value is typically 0 or 1.

</dd> <dt>

**dwCount\[4\]**
</dt> <dd>

An array of 0 or 1 or more **DWORD**s that represent the number of times the action specified in **dwCategory** may be performed. See remarks.

</dd> <dt>

**dwNumDates**
</dt> <dd>

Number of items supplied in **datetime**. Typically no more than two dates are used, for example, with a license that is valid from one date until another date.

</dd> <dt>

**datetime\[4\]**
</dt> <dd>

An array of one or more FILETIME structures representing one or more dates in the license. The meaning of a particular date depends on the value of **dwCategory**.

</dd> <dt>

**dwVague**
</dt> <dd>

Zero or more of the following flags combined with a bitwise **OR**:



| Flag                                    | Description                                                                                                                                           |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| DRM\_LICENSE\_STATE\_DATA\_VAGUE        | If set, there may be more licenses that apply to the content.                                                                                         |
| DRM\_LICENSE\_STATE\_DATA\_OPL\_PRESENT | If set, the license includes output protection levels (OPLs) that must be retrieved and checked against the destination of your application's output. |
| DRM\_LICENSE\_STATE\_DATA\_SAP\_PRESENT | If set, the content must be delivered using secure audio path (SAP).                                                                                  |



 

</dd> </dl>

## Remarks

This structure is returned (encapsulated in a [**WM\_LICENSE\_STATE\_DATA**](/previous-versions/windows/desktop/legacy/dd757942(v=vs.85)) structure) from a call to [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty) when you specify one of the DRM license state properties. These properties are:

-   [**DRM\_LicenseState\_Playback**](drm-licensestate-playback.md)
-   [**DRM\_LicenseState\_CopyToCD**](drm-licensestate-copytocd.md)
-   [**DRM\_LicenseState\_CopyToSDMIDevice**](drm-licensestate-copytosdmidevice.md)
-   [**DRM\_LicenseState\_CopyToNonSDMIDevice**](drm-licensestate-copytononsdmidevice.md)
-   [**DRM\_LicenseState\_CollaborativePlay**](drm-licensestate-collaborativeplay.md)
-   [**DRM\_LicenseState\_Copy**](drm-licensestate-copy.md)
-   [**DRM\_LicenseState\_PlaylistBurn**](drm-licensestate-playlistburn.md)

If **dwCategory** is **WM\_DRM\_LICENSE\_STATE\_COUNT\_FROM\_UNTIL,** then the **datetime** array will typically contain two dates, a "from" date and an "until" date. Two date pairs may also be specified to create more complex licenses.

The elements of the **dwCount** array correspond to the dates or date ranges specified in the **datetime** array. If **dwCategory** is **WM\_DRM\_LICENSE\_STATE\_COUNT\_FROM\_UNTIL** and **datetime** contains one pair of dates, then **dwCount** will contain one element. If **datetime** contains two date pairs (four elements), then **dwCount** should contain two elements, one for each date pair.

In some cases, users may have been issued more than one license for a file. For example, they might have acquired a license that allowed five plays until the end of the month, and later acquired a second license for unlimited rights. In such a case, the DRM\_LICENSE\_STATE\_DATA\_VAGUE flag is set in **dwVague** (`dwVague & DRM_LICENSE_STATE_DATA_VAGUE != 0`) and the DRM component will use an algorithm to determine the most likely set of rights that have been applied. When one license expires, the DRM component will examine the remaining license(s), and so on until all licenses have expired.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                      |
| Version<br/>                  | Windows Media Format 7 SDK, or later versions of the SDK<br/>                       |
| Header<br/>                   | <dl> <dt>Drmexternals.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

