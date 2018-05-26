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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Audio Compression Manager Reference

This section describes the functions, structures, and messages associated with the ACM. These elements are grouped as follows.

## Drivers

-   [**acmDriverAdd**](/windows/win32/Msacm/nf-msacm-acmdriveradd?branch=master)
-   [**acmDriverClose**](/windows/win32/Msacm/nf-msacm-acmdriverclose?branch=master)
-   [**ACMDRIVERDETAILS**](/windows/win32/Msacm/ns-msacm-tacmdriverdetails?branch=master)
-   [**acmDriverEnum**](/windows/win32/Msacm/nf-msacm-acmdriverenum?branch=master)
-   [**acmDriverEnumCallback**](/windows/win32/Msacm/nc-msacm-acmdriverenumcb?branch=master)
-   [**acmDriverID**](/windows/win32/Msacm/nf-msacm-acmdriverid?branch=master)
-   [**acmDriverMessage**](/windows/win32/Msacm/nf-msacm-acmdrivermessage?branch=master)
-   [**acmDriverOpen**](/windows/win32/Msacm/nf-msacm-acmdriveropen?branch=master)
-   [**acmDriverPriority**](/windows/win32/Msacm/nf-msacm-acmdriverpriority?branch=master)
-   [**acmDriverProc**](/windows/win32/Msacm/nc-msacm-acmdriverproc?branch=master)
-   [**acmDriverRemove**](/windows/win32/Msacm/nf-msacm-acmdriverremove?branch=master)

## Filters

-   [**ACMFILTERCHOOSE**](/windows/win32/Msacm/ns-msacm-tacmfilterchoose?branch=master)
-   [**acmFilterChooseHookProc**](/windows/win32/Msacm/nc-msacm-acmfilterchoosehookproc?branch=master)
-   [**ACMFILTERDETAILS**](/windows/win32/Msacm/ns-msacm-tacmfilterdetails?branch=master)
-   [**acmFilterEnum**](/windows/win32/Msacm/nf-msacm-acmfilterenum?branch=master)
-   [**acmFilterEnumCallback**](/windows/win32/Msacm/nc-msacm-acmfilterenumcb?branch=master)
-   [**ACMFILTERTAGDETAILS**](/windows/win32/Msacm/ns-msacm-tacmfiltertagdetails?branch=master)
-   [**acmFilterTagEnum**](/windows/win32/Msacm/nf-msacm-acmfiltertagenum?branch=master)
-   [**acmFilterTagEnumCallback**](/windows/win32/Msacm/nc-msacm-acmfiltertagenumcb?branch=master)

## Formats

-   [**ACMFORMATCHOOSE**](/windows/win32/Msacm/ns-msacm-tacmformatchoose?branch=master)
-   [**acmFormatChooseHookProc**](/windows/win32/Msacm/nc-msacm-acmformatchoosehookproc?branch=master)
-   [**ACMFORMATDETAILS**](/windows/win32/Msacm/ns-msacm-tacmformatdetails?branch=master)
-   [**acmFormatEnum**](/windows/win32/Msacm/nf-msacm-acmformatenum?branch=master)
-   [**acmFormatEnumCallback**](/windows/win32/Msacm/nc-msacm-acmformatenumcb?branch=master)
-   [**acmFormatSuggest**](/windows/win32/Msacm/nf-msacm-acmformatsuggest?branch=master)
-   [**ACMFORMATTAGDETAILS**](/windows/win32/Msacm/ns-msacm-tacmformattagdetails?branch=master)
-   [**acmFormatTagEnum**](/windows/win32/Msacm/nf-msacm-acmformattagenum?branch=master)
-   [**acmFormatTagEnumCallback**](/windows/win32/Msacm/nc-msacm-acmformattagenumcb?branch=master)

## Messages

-   [**MM\_ACM\_FILTERCHOOSE**](mm-acm-filterchoose.md)
-   [**MM\_ACM\_FORMATCHOOSE**](mm-acm-formatchoose.md)

## Streams

-   [**acmStreamClose**](/windows/win32/Msacm/nf-msacm-acmstreamclose?branch=master)
-   [**acmStreamConvert**](/windows/win32/Msacm/nf-msacm-acmstreamconvert?branch=master)
-   [**acmStreamConvertCallback**](https://msdn.microsoft.com/library/windows/desktop/dd742925)
-   [**ACMSTREAMHEADER**](/windows/win32/Msacm/ns-msacm-tacmstreamheader?branch=master)
-   [**acmStreamMessage**](/windows/win32/Msacm/nf-msacm-acmstreammessage?branch=master)
-   [**acmStreamOpen**](/windows/win32/Msacm/nf-msacm-acmstreamopen?branch=master)
-   [**acmStreamPrepareHeader**](/windows/win32/Msacm/nf-msacm-acmstreamprepareheader?branch=master)
-   [**acmStreamReset**](/windows/win32/Msacm/nf-msacm-acmstreamreset?branch=master)
-   [**acmStreamSize**](/windows/win32/Msacm/nf-msacm-acmstreamsize?branch=master)
-   [**acmStreamUnprepareHeader**](/windows/win32/Msacm/nf-msacm-acmstreamunprepareheader?branch=master)

## Miscellaneous

-   [**acmGetVersion**](/windows/win32/Msacm/nf-msacm-acmgetversion?branch=master)
-   [**acmMetrics**](/windows/win32/Msacm/nf-msacm-acmmetrics?branch=master)

## Related topics

<dl> <dt>

[Audio Compression Manager](audio-compression-manager.md)
</dt> </dl>

 

 




