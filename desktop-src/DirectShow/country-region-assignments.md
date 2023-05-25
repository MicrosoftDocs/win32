---
description: Country/Region Assignments
ms.assetid: a71784eb-e6b4-4dab-91fc-103c39dd1591
title: Country/Region Assignments
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Country/Region Assignments

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

International Telecommunication Union (ITU) standard country calling codes are passed to the [**IAMTuner::put\_CountryCode**](/windows/desktop/api/Strmif/nf-strmif-iamtuner-put_countrycode) method to select default television frequency mappings.

For example, passing 20, the ITU-T calling code for Egypt, would select default television frequencies for Egypt.

For a list of country calling codes, refer to the current ITU-T recommendation of assigned country codes.

## Related topics

<dl> <dt>

[Tables and Assignments](tables-and-assignments.md)
</dt> </dl>

 

 



