---
description: Parameter Information
ms.assetid: 2600b200-f57a-46cd-8740-89b7f7aba540
title: Parameter Information
ms.topic: article
ms.date: 05/31/2018
---

# Parameter Information

The [**IMediaParamInfo::GetParamInfo**](/previous-versions/windows/desktop/api/Medparam/nf-medparam-imediaparaminfo-getparaminfo) method returns an [**MP\_PARAMINFO**](/previous-versions/windows/desktop/api/Medparam/ns-medparam-mp_paraminfo) structure that describes a parameter. This structure contains the following information:

-   The **mpType** member indicates the data type of the parameter value. For efficiency, all parameters are implemented as 32-bit floating-point values. The [**MP\_TYPE**](/previous-versions/windows/desktop/api/Medparam/ne-medparam-mp_type) enumeration defines whether to interpret the value as an integer, floating-point value, Boolean, or enumeration (integer series).
-   The **mopCaps** member indicates which curves this parameter supports. If the data type is Boolean or enumeration, the only curve that the parameter can support is "Jump."
-   The **mpdMinValue** and **mpdMaxValue** members define the minimum and maximum values for this parameter. Any curves for this parameter must fall within this range.
-   The **mpdNeutralValue** member is the default value of the parameter.
-   The **szLabel** member is the name of the parameter, and the **szUnitText** member is the name for the unit of measure for the parameter. Examples might include "Volume" and "Decibels," or "Frequency" and "kHz." Both strings are English and are never localized. The DMO can provide localized versions through the [**IMediaParamInfo::GetParamText**](/previous-versions/windows/desktop/api/Medparam/nf-medparam-imediaparaminfo-getparamtext) method.

The information for each parameter remains fixed throughout the lifetime of the DMO. Therefore, the client can query for this information once and then cache it.

**Time Formats**

The client must time stamp the input data, so that the DMO can calculate the corresponding parameter values. By default, time stamps represent units of 100 nanoseconds, also called *reference time*. This time unit is not convenient for every application, however, so a DMO has an option to support other time formats. Time formats are identified by GUID.



| **GUID**              | Description                   |
|-----------------------|-------------------------------|
| GUID\_TIME\_REFERENCE | Reference time                |
| GUID\_TIME\_MUSIC     | Parts per quarter note (PPQN) |
| GUID\_TIME\_SAMPLES   | Samples per second            |



 

Third parties are encouraged to define their own time formats as needed. However, all DMOs must support reference time. This provides a standard baseline that everyone can use. To determine how many time formats a DMO supports, call the [**IMediaParamInfo::GetNumTimeFormats**](/previous-versions/windows/desktop/api/Medparam/nf-medparam-imediaparaminfo-getnumtimeformats) method. To enumerate the supported formats, call the [**IMediaParamInfo::GetSupportedTimeFormat**](/previous-versions/windows/desktop/api/Medparam/nf-medparam-imediaparaminfo-getsupportedtimeformat) method.

To set the time format, call [**IMediaParams::SetTimeFormat**](/previous-versions/windows/desktop/api/Medparam/nf-medparam-imediaparams-settimeformat). This method specifies the time format GUID and the *time data*, which is the number of units per clock tick. For example, if the time format is samples per second, and the time data is 32, then a time stamp value of 10 corresponds to 320 samples.

## Related topics

<dl> <dt>

[Media Parameters](media-parameters.md)
</dt> </dl>

 

 



