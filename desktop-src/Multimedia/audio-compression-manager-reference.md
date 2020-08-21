---
title: Audio Compression Manager Reference
description: Audio Compression Manager Reference
ms.assetid: a4e234c7-4dd3-4269-90a5-5de2c8837c0f
keywords:
- Windows multimedia,ACM reference
- multimedia,ACM reference
- multimedia audio,ACM reference
- audio,ACM reference)
- audio compression manager (ACM),reference
- ACM (audio compression manager),reference
- ACM reference,about
- reference for ACM,about
ms.topic: article
ms.date: 05/31/2018
---

# Audio Compression Manager Reference

This section describes the functions, structures, and messages associated with the ACM. These elements are grouped as follows.

## Drivers

-   [**acmDriverAdd**](/windows/desktop/api/Msacm/nf-msacm-acmdriveradd)
-   [**acmDriverClose**](/windows/desktop/api/Msacm/nf-msacm-acmdriverclose)
-   [**ACMDRIVERDETAILS**](/windows/win32/api/msacm/ns-msacm-acmdriverdetails)
-   [**acmDriverEnum**](/windows/desktop/api/Msacm/nf-msacm-acmdriverenum)
-   [**acmDriverEnumCallback**](/windows/win32/api/msacm/nc-msacm-acmdriverenumcb)
-   [**acmDriverID**](/windows/desktop/api/Msacm/nf-msacm-acmdriverid)
-   [**acmDriverMessage**](/windows/desktop/api/Msacm/nf-msacm-acmdrivermessage)
-   [**acmDriverOpen**](/windows/desktop/api/Msacm/nf-msacm-acmdriveropen)
-   [**acmDriverPriority**](/windows/desktop/api/Msacm/nf-msacm-acmdriverpriority)
-   [**acmDriverProc**](/windows/desktop/api/Msacm/nc-msacm-acmdriverproc)
-   [**acmDriverRemove**](/windows/desktop/api/Msacm/nf-msacm-acmdriverremove)

## Filters

-   [**ACMFILTERCHOOSE**](/windows/win32/api/msacm/ns-msacm-acmfilterchoose)
-   [**acmFilterChooseHookProc**](/windows/desktop/api/Msacm/nc-msacm-acmfilterchoosehookproc)
-   [**ACMFILTERDETAILS**](/windows/win32/api/msacm/ns-msacm-acmfilterdetails)
-   [**acmFilterEnum**](/windows/desktop/api/Msacm/nf-msacm-acmfilterenum)
-   [**acmFilterEnumCallback**](/windows/desktop/api/Msacm/nc-msacm-acmfilterenumcb)
-   [**ACMFILTERTAGDETAILS**](/windows/win32/api/msacm/ns-msacm-acmfiltertagdetails)
-   [**acmFilterTagEnum**](/windows/desktop/api/Msacm/nf-msacm-acmfiltertagenum)
-   [**acmFilterTagEnumCallback**](/windows/desktop/api/Msacm/nc-msacm-acmfiltertagenumcb)

## Formats

-   [**ACMFORMATCHOOSE**](/windows/win32/api/msacm/ns-msacm-acmformatchoose)
-   [**acmFormatChooseHookProc**](/windows/desktop/api/Msacm/nc-msacm-acmformatchoosehookproc)
-   [**ACMFORMATDETAILS**](/windows/win32/api/msacm/ns-msacm-acmformatdetails)
-   [**acmFormatEnum**](/windows/desktop/api/Msacm/nf-msacm-acmformatenum)
-   [**acmFormatEnumCallback**](/windows/desktop/api/Msacm/nc-msacm-acmformatenumcb)
-   [**acmFormatSuggest**](/windows/desktop/api/Msacm/nf-msacm-acmformatsuggest)
-   [**ACMFORMATTAGDETAILS**](/windows/win32/api/msacm/ns-msacm-acmformattagdetails)
-   [**acmFormatTagEnum**](/windows/desktop/api/Msacm/nf-msacm-acmformattagenum)
-   [**acmFormatTagEnumCallback**](/windows/desktop/api/Msacm/nc-msacm-acmformattagenumcb)

## Messages

-   [**MM\_ACM\_FILTERCHOOSE**](mm-acm-filterchoose.md)
-   [**MM\_ACM\_FORMATCHOOSE**](mm-acm-formatchoose.md)

## Streams

-   [**acmStreamClose**](/windows/desktop/api/Msacm/nf-msacm-acmstreamclose)
-   [**acmStreamConvert**](/windows/desktop/api/Msacm/nf-msacm-acmstreamconvert)
-   [**acmStreamConvertCallback**](/previous-versions//dd742925(v=vs.85))
-   [**ACMSTREAMHEADER**](/windows/win32/api/msacm/ns-msacm-acmstreamheader)
-   [**acmStreamMessage**](/windows/desktop/api/Msacm/nf-msacm-acmstreammessage)
-   [**acmStreamOpen**](/windows/desktop/api/Msacm/nf-msacm-acmstreamopen)
-   [**acmStreamPrepareHeader**](/windows/desktop/api/Msacm/nf-msacm-acmstreamprepareheader)
-   [**acmStreamReset**](/windows/desktop/api/Msacm/nf-msacm-acmstreamreset)
-   [**acmStreamSize**](/windows/desktop/api/Msacm/nf-msacm-acmstreamsize)
-   [**acmStreamUnprepareHeader**](/windows/desktop/api/Msacm/nf-msacm-acmstreamunprepareheader)

## Miscellaneous

-   [**acmGetVersion**](/windows/desktop/api/Msacm/nf-msacm-acmgetversion)
-   [**acmMetrics**](/windows/desktop/api/Msacm/nf-msacm-acmmetrics)

## Related topics

<dl> <dt>

[Audio Compression Manager](audio-compression-manager.md)
</dt> </dl>

 

 